#!/usr/bin/env python3
"""Decode HttpCanary TCP .bin records into application frames.

The capture stores each TCP data chunk as N.bin and repeats the same chunks inside
``tcp.hcy`` with a tiny metadata prefix: direction, millisecond timestamp, and
chunk length.  The game protocol itself uses a 16-byte frame header whose bytes
4..6 are a big-endian 24-bit total frame length.  Payloads are usually URL
encoded client requests or JSON-like server responses; some large server frames
are zlib-compressed.
"""
from __future__ import annotations

import argparse
import json
import re
import urllib.parse
import zlib
from dataclasses import dataclass
from pathlib import Path
from typing import Any


META_RE = re.compile(rb"\x04([\x01\x02])\x0d(\d{13})(....)$", re.S)


@dataclass
class Segment:
    index: int
    path: str
    direction_code: int
    direction: str
    timestamp_ms: int
    length: int
    data: bytes


def load_segments(root: Path) -> list[Segment]:
    hcy = (root / "tcp.hcy").read_bytes()
    pos = 0
    segments: list[Segment] = []
    bin_paths = sorted(root.glob("*.bin"), key=lambda p: int(p.stem))
    for path in bin_paths:
        index = int(path.stem)
        data = path.read_bytes()
        off = hcy.find(data, pos)
        if off < 0:
            raise ValueError(f"{path.name} was not found in tcp.hcy after offset {pos}")
        prelude = hcy[max(0, off - 40):off]
        match = META_RE.search(prelude)
        if not match:
            raise ValueError(f"Could not parse HttpCanary metadata before {path.name}")
        direction_code = match.group(1)[0]
        timestamp_ms = int(match.group(2).decode("ascii"))
        recorded_len = int.from_bytes(match.group(3), "big")
        if recorded_len != len(data):
            raise ValueError(
                f"Length mismatch for {path.name}: metadata={recorded_len}, file={len(data)}"
            )
        segments.append(
            Segment(
                index=index,
                path=path.name,
                direction_code=direction_code,
                direction="up/client_to_server" if direction_code == 1 else "down/server_to_client",
                timestamp_ms=timestamp_ms,
                length=len(data),
                data=data,
            )
        )
        pos = off + len(data)
    return segments


def decode_payload(payload: bytes) -> dict[str, Any]:
    result: dict[str, Any] = {
        "payload_length": len(payload),
        "payload_hex_prefix": payload[:32].hex(),
    }
    decoded_bytes = payload
    if payload.startswith(b"x\x9c"):
        try:
            decoded_bytes = zlib.decompress(payload)
            result["payload_codec"] = "zlib"
            result["decompressed_length"] = len(decoded_bytes)
        except zlib.error as exc:
            result["payload_codec"] = "zlib_error"
            result["zlib_error"] = str(exc)
    else:
        result["payload_codec"] = "plain"

    try:
        text = decoded_bytes.decode("utf-8")
    except UnicodeDecodeError:
        text = decoded_bytes.decode("utf-8", errors="replace")
        result["text_decode_errors"] = True
    result["text"] = text

    normalized = text
    if normalized.startswith("0;"):
        result["server_status_prefix"] = "0;"
        normalized = normalized[2:]

    parsed: Any | None = None
    if normalized.startswith("bv=") or "&request=" in normalized:
        result["message_format"] = "urlencoded_request"
        query = urllib.parse.parse_qs(normalized, keep_blank_values=True)
        flat_query: dict[str, Any] = {
            key: values[0] if len(values) == 1 else values for key, values in query.items()
        }
        result["query"] = flat_query
        request_text = flat_query.get("request")
        if isinstance(request_text, str):
            try:
                parsed = json.loads(request_text)
                result["request"] = parsed
            except json.JSONDecodeError as exc:
                result["request_parse_error"] = str(exc)
    elif normalized.startswith("[") or normalized.startswith("{"):
        result["message_format"] = "json_response"
        try:
            parsed = json.loads(normalized)
            result["response"] = parsed
        except json.JSONDecodeError as exc:
            result["json_parse_error"] = str(exc)
    elif normalized == "":
        result["message_format"] = "empty_control"
    else:
        result["message_format"] = "text_or_binary"

    funcs: list[str] = []
    def collect(obj: Any) -> None:
        if isinstance(obj, dict):
            if isinstance(obj.get("func"), str):
                funcs.append(obj["func"])
            for value in obj.values():
                collect(value)
        elif isinstance(obj, list):
            for item in obj:
                collect(item)
    if parsed is not None:
        collect(parsed)
    result["functions"] = funcs
    return result


def parse_frames(segments: list[Segment]) -> list[dict[str, Any]]:
    buffers: dict[int, bytearray] = {1: bytearray(), 2: bytearray()}
    origins: dict[int, list[dict[str, int]]] = {1: [], 2: []}
    frames: list[dict[str, Any]] = []

    for segment in segments:
        buffers[segment.direction_code].extend(segment.data)
        origins[segment.direction_code].append(
            {
                "segment": segment.index,
                "timestamp_ms": segment.timestamp_ms,
                "remaining": len(segment.data),
            }
        )
        direction_code = segment.direction_code
        buf = buffers[direction_code]
        origin = origins[direction_code]

        while len(buf) >= 16:
            total_length = int.from_bytes(buf[4:7], "big")
            if total_length < 16:
                raise ValueError(
                    f"Invalid frame length {total_length} after segment {segment.index} "
                    f"in direction {direction_code}; header={bytes(buf[:16]).hex()}"
                )
            if len(buf) < total_length:
                break

            raw = bytes(buf[:total_length])
            need = total_length
            used_segments: list[int] = []
            used_timestamps: list[int] = []
            while need:
                current = origin[0]
                take = min(need, current["remaining"])
                if current["segment"] not in used_segments:
                    used_segments.append(current["segment"])
                    used_timestamps.append(current["timestamp_ms"])
                current["remaining"] -= take
                need -= take
                if current["remaining"] == 0:
                    origin.pop(0)

            payload = raw[16:]
            decoded = decode_payload(payload)
            frames.append(
                {
                    "frame_index": len(frames),
                    "direction": segment.direction if direction_code == segment.direction_code else "",
                    "direction_code": direction_code,
                    "segments": used_segments,
                    "timestamp_start_ms": min(used_timestamps),
                    "timestamp_end_ms": max(used_timestamps),
                    "total_length": total_length,
                    "header": {
                        "hex": raw[:16].hex(),
                        "message_id_or_checksum": raw[:4].hex(),
                        "total_length_24bit_be": total_length,
                        "flag_or_opcode": raw[7],
                        "route_or_session_hex": raw[8:15].hex(),
                        "sequence_byte": raw[15],
                    },
                    "decoded": decoded,
                }
            )
            del buf[:total_length]
    for code, buf in buffers.items():
        if buf:
            raise ValueError(f"Unparsed trailing bytes in direction {code}: {len(buf)}")
    return frames


def summarize_frames(frames: list[dict[str, Any]]) -> dict[str, Any]:
    function_counts: dict[str, int] = {}
    for frame in frames:
        for func in frame["decoded"].get("functions", []):
            function_counts[func] = function_counts.get(func, 0) + 1
    return {
        "frame_count": len(frames),
        "up_frames": sum(1 for f in frames if f["direction_code"] == 1),
        "down_frames": sum(1 for f in frames if f["direction_code"] == 2),
        "zlib_frames": sum(1 for f in frames if f["decoded"].get("payload_codec") == "zlib"),
        "function_counts": dict(sorted(function_counts.items())),
    }


def write_markdown(path: Path, metadata: dict[str, Any], segments: list[Segment], frames: list[dict[str, Any]], summary: dict[str, Any]) -> None:
    lines: list[str] = []
    lines.append("# Decoded TCP capture report")
    lines.append("")
    lines.append("## Capture metadata")
    lines.append("")
    for key, value in metadata.items():
        lines.append(f"- **{key}**: `{value}`")
    lines.append(f"- **TCP chunk files**: `{len(segments)}` (`0.bin` .. `{segments[-1].path}`)")
    lines.append(f"- **Decoded application frames**: `{summary['frame_count']}`")
    lines.append(f"- **Client → server frames**: `{summary['up_frames']}`")
    lines.append(f"- **Server → client frames**: `{summary['down_frames']}`")
    lines.append(f"- **zlib-compressed frames**: `{summary['zlib_frames']}`")
    lines.append("")
    lines.append("## Protocol notes")
    lines.append("")
    lines.append("- `tcp.hcy` metadata marks each TCP chunk as direction `1` (client → server) or `2` (server → client), with a millisecond timestamp and raw chunk length.")
    lines.append("- Each game application frame starts with a 16-byte header. Header bytes `4..6` are the big-endian 24-bit total frame length, so TCP chunks can contain multiple frames or only part of a larger frame.")
    lines.append("- Client payloads are normally URL-encoded query strings with a JSON `request` parameter. Server payloads normally start with `0;` followed by JSON. Large server responses may be zlib-compressed before that `0;` JSON text.")
    lines.append("")
    lines.append("## High-level flow")
    lines.append("")
    notable = [
        "Login",
        "LoginResult",
        "QueryAvatarAttribute",
        "CreateAvatar",
        "CreateAvatarResult",
        "UpdateGuide",
        "HeartBeat",
    ]
    for name in notable:
        count = summary["function_counts"].get(name, 0)
        if count:
            lines.append(f"- `{name}` appears `{count}` time(s).")
    lines.append("")
    lines.append("## Frame-by-frame decoded payloads")
    lines.append("")
    for frame in frames:
        decoded = frame["decoded"]
        funcs = ", ".join(decoded.get("functions", [])) or "—"
        lines.append(f"### Frame {frame['frame_index']:03d}: {frame['direction']}")
        lines.append("")
        lines.append(f"- **Segments**: `{frame['segments']}`")
        lines.append(f"- **Timestamp ms**: `{frame['timestamp_start_ms']}` .. `{frame['timestamp_end_ms']}`")
        lines.append(f"- **Header**: `{frame['header']['hex']}`")
        lines.append(f"- **Total length**: `{frame['total_length']}` bytes; **payload codec**: `{decoded.get('payload_codec')}`; **format**: `{decoded.get('message_format')}`")
        lines.append(f"- **Functions**: `{funcs}`")
        if "query" in decoded:
            query = {k: v for k, v in decoded["query"].items() if k != "request"}
            lines.append(f"- **Query fields**: `{json.dumps(query, ensure_ascii=False, sort_keys=True)}`")
        payload_obj = decoded.get("request", decoded.get("response", decoded.get("text", "")))
        payload_json = json.dumps(payload_obj, ensure_ascii=False, sort_keys=True)
        if len(payload_json) > 3000:
            payload_json = payload_json[:3000] + "... <truncated in markdown; see decoded_packets.json>"
        lines.append("- **Decoded payload**:")
        lines.append("  ```json")
        lines.append("  " + payload_json.replace("\n", "\n  "))
        lines.append("  ```")
        lines.append("")
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", default=".", help="Repository/capture root containing tcp.json, tcp.hcy, and *.bin")
    parser.add_argument("--out-json", default="decoded/decoded_packets.json")
    parser.add_argument("--out-md", default="decoded/decoded_packets.md")
    args = parser.parse_args()

    root = Path(args.root)
    metadata = json.loads((root / "tcp.json").read_text(encoding="utf-8"))
    segments = load_segments(root)
    frames = parse_frames(segments)
    summary = summarize_frames(frames)
    output = {
        "metadata": metadata,
        "summary": summary,
        "segments": [
            {
                "index": s.index,
                "path": s.path,
                "direction_code": s.direction_code,
                "direction": s.direction,
                "timestamp_ms": s.timestamp_ms,
                "length": s.length,
            }
            for s in segments
        ],
        "frames": frames,
    }
    out_json = root / args.out_json
    out_md = root / args.out_md
    out_json.parent.mkdir(parents=True, exist_ok=True)
    out_md.parent.mkdir(parents=True, exist_ok=True)
    out_json.write_text(json.dumps(output, ensure_ascii=False, indent=2, sort_keys=True), encoding="utf-8")
    write_markdown(out_md, metadata, segments, frames, summary)
    print(json.dumps(summary, ensure_ascii=False, indent=2, sort_keys=True))
    print(f"Wrote {out_json}")
    print(f"Wrote {out_md}")


if __name__ == "__main__":
    main()
