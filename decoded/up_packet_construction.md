# Client-to-server UP packet construction guide

Báo cáo này mô tả cấu tạo các gói `UP` trong capture để bạn có thể tái hiện lại flow trên môi trường bạn được phép kiểm thử. Không nên replay vào server thật nếu không có quyền, vì session/key/trạng thái server có thể thay đổi.

## Cấu trúc chung của application frame

Mỗi application frame trong TCP stream có dạng:

```text
[16-byte header][payload]
```

Header 16 byte quan sát được trong capture:

| Offset | Size | Ý nghĩa suy luận từ capture |
| --- | ---: | --- |
| `0..3` | 4 | message id/checksum-like bytes; giữ nguyên nếu replay raw capture |
| `4..6` | 3 | tổng độ dài frame, big-endian 24-bit, bao gồm cả 16 byte header |
| `7` | 1 | flag/opcode; gói control dùng `0x0a`, `0x14`; request JSON thường là `0x00` |
| `8..14` | 7 | route/session-like bytes; trong request thường là `00 00 00 00 00 00 00` |
| `15` | 1 | sequence byte trong header; thường khớp `seq` URL query với request thường |

Payload UP thường là URL-encoded query string UTF-8:

```text
bv=7%2E0%2E2&request=<urlencoded-json-array>&seq=<n>&session=<session_key>&sptype=spv2jodo&version=7%2E0%2E2
```

Pseudo-code tạo một frame UP mới từ payload:

```python
payload = query_string.encode('utf-8')
total_len = 16 + len(payload)
header = bytearray(16)
header[4:7] = total_len.to_bytes(3, 'big')
header[7] = 0x00
header[15] = seq & 0xff
packet = bytes(header) + payload
```

Lưu ý: 4 byte đầu header và một số byte flag/route có thể là checksum/message-id do client sinh. Với replay chính xác capture, cách an toàn nhất là dùng raw bytes trong các file `*.bin`; với request mới, cần reverse thêm thuật toán tạo 4 byte đầu nếu server kiểm tra.

## Các UP frame trong capture

### UP frame 000 — Func: `control/empty`

- **Raw segment(s)**: `[0]`
- **Header hex**: `61da39960000100a0000000000000005`
- **Total length**: `16` bytes
- **Header length bytes `4..6`**: `000010` = `16`
- **Flag/opcode byte `7`**: `10`
- **Header sequence byte `15`**: `5`
- **Decoded request/control payload**:
  ```json
  ""
  ```

### UP frame 003 — Func: `Login`

- **Raw segment(s)**: `[2]`
- **Header hex**: `e51e7d370002e0000000000000000000`
- **Total length**: `736` bytes
- **Header length bytes `4..6`**: `0002e0` = `736`
- **Flag/opcode byte `7`**: `0`
- **Header sequence byte `15`**: `0`
- **URL query fields**: `{"bv": "7.0.2", "seq": "1", "session": "", "sptype": "spv2jodo", "version": "7.0.2"}`
- **Decoded request/control payload**:
  ```json
  [{"deviceType": 2, "func": "Login", "info": "{\"appVersion\":\"7.0.2\",\"appBaseVersion\":\"7.0.2\",\"deviceId\":\"DEVICE#mac00dbda57f973\",\"combinedDeviceId\":\"00db11d44a68_010138020814576\",\"deviceCheckChannel\":\"\",\"deviceType\":17,\"model\":\"SM-S9210\",\"os\":\"Android\",\"osversion\":\"9\",\"mac\":\"00:db:11:d4:4a:68\"}", "serverid": 1195, "userid": "v2jodo#2835376"}]
  ```

### UP frame 005 — Func: `control/empty`

- **Raw segment(s)**: `[4]`
- **Header hex**: `b853646c000010140000000000000001`
- **Total length**: `16` bytes
- **Header length bytes `4..6`**: `000010` = `16`
- **Flag/opcode byte `7`**: `20`
- **Header sequence byte `15`**: `1`
- **Decoded request/control payload**:
  ```json
  ""
  ```

### UP frame 007 — Func: `QueryAvatarAttribute`

- **Raw segment(s)**: `[6]`
- **Header hex**: `6ca96b6c000099000000000000000002`
- **Total length**: `153` bytes
- **Header length bytes `4..6`**: `000099` = `153`
- **Flag/opcode byte `7`**: `0`
- **Header sequence byte `15`**: `2`
- **URL query fields**: `{"bv": "7.0.2", "seq": "2", "session": "02D1B0135ABCDC0D", "sptype": "spv2jodo", "version": "7.0.2"}`
- **Decoded request/control payload**:
  ```json
  [{"func": "QueryAvatarAttribute"}]
  ```

### UP frame 009 — Func: `QueryChargeInfo`

- **Raw segment(s)**: `[8]`
- **Header hex**: `b2167f02000094000000000000000003`
- **Total length**: `148` bytes
- **Header length bytes `4..6`**: `000094` = `148`
- **Flag/opcode byte `7`**: `0`
- **Header sequence byte `15`**: `3`
- **URL query fields**: `{"bv": "7.0.2", "seq": "3", "session": "02D1B0135ABCDC0D", "sptype": "spv2jodo", "version": "7.0.2"}`
- **Decoded request/control payload**:
  ```json
  [{"func": "QueryChargeInfo"}]
  ```

### UP frame 010 — Func: `CreateAvatar`

- **Raw segment(s)**: `[9]`
- **Header hex**: `24c39b190000e2000000000000000004`
- **Total length**: `226` bytes
- **Header length bytes `4..6`**: `0000e2` = `226`
- **Flag/opcode byte `7`**: `0`
- **Header sequence byte `15`**: `4`
- **URL query fields**: `{"bv": "7.0.2", "seq": "4", "session": "02D1B0135ABCDC0D", "sptype": "spv2jodo", "version": "7.0.2"}`
- **Decoded request/control payload**:
  ```json
  [{"avatarName": "BeetBoij", "chiefBuddy": 1002, "func": "CreateAvatar", "gender": 0}]
  ```

### UP frame 014 — Func: `QueryAvatarAttribute`

- **Raw segment(s)**: `[12]`
- **Header hex**: `27e2d294000099000000000000000005`
- **Total length**: `153` bytes
- **Header length bytes `4..6`**: `000099` = `153`
- **Flag/opcode byte `7`**: `0`
- **Header sequence byte `15`**: `5`
- **URL query fields**: `{"bv": "7.0.2", "seq": "5", "session": "02D1B0135ABCDC0D", "sptype": "spv2jodo", "version": "7.0.2"}`
- **Decoded request/control payload**:
  ```json
  [{"func": "QueryAvatarAttribute"}]
  ```

### UP frame 019 — Func: `UpdateGuide`

- **Raw segment(s)**: `[14]`
- **Header hex**: `b0b4c25e0000b0000000000000000006`
- **Total length**: `176` bytes
- **Header length bytes `4..6`**: `0000b0` = `176`
- **Flag/opcode byte `7`**: `0`
- **Header sequence byte `15`**: `6`
- **URL query fields**: `{"bv": "7.0.2", "seq": "6", "session": "02D1B0135ABCDC0D", "sptype": "spv2jodo", "version": "7.0.2"}`
- **Decoded request/control payload**:
  ```json
  [{"func": "UpdateGuide", "id": 1, "step": 0}]
  ```

### UP frame 021 — Func: `HeartBeat`

- **Raw segment(s)**: `[16]`
- **Header hex**: `ac854aa10000a2000000000000000007`
- **Total length**: `162` bytes
- **Header length bytes `4..6`**: `0000a2` = `162`
- **Flag/opcode byte `7`**: `0`
- **Header sequence byte `15`**: `7`
- **URL query fields**: `{"bv": "7.0.2", "seq": "7", "session": "02D1B0135ABCDC0D", "sptype": "spv2jodo", "version": "7.0.2"}`
- **Decoded request/control payload**:
  ```json
  [{"func": "HeartBeat", "time": 0}]
  ```

### UP frame 024 — Func: `QueryAllChargeConfig`

- **Raw segment(s)**: `[18]`
- **Header hex**: `8ceaee37000099000000000000000008`
- **Total length**: `153` bytes
- **Header length bytes `4..6`**: `000099` = `153`
- **Flag/opcode byte `7`**: `0`
- **Header sequence byte `15`**: `8`
- **URL query fields**: `{"bv": "7.0.2", "seq": "8", "session": "02D1B0135ABCDC0D", "sptype": "spv2jodo", "version": "7.0.2"}`
- **Decoded request/control payload**:
  ```json
  [{"func": "QueryAllChargeConfig"}]
  ```

### UP frame 027 — Func: `GetChengHaoList`

- **Raw segment(s)**: `[21]`
- **Header hex**: `9e638116000094000000000000000009`
- **Total length**: `148` bytes
- **Header length bytes `4..6`**: `000094` = `148`
- **Flag/opcode byte `7`**: `0`
- **Header sequence byte `15`**: `9`
- **URL query fields**: `{"bv": "7.0.2", "seq": "9", "session": "02D1B0135ABCDC0D", "sptype": "spv2jodo", "version": "7.0.2"}`
- **Decoded request/control payload**:
  ```json
  [{"func": "GetChengHaoList"}]
  ```

### UP frame 029 — Func: `GetHuiZhangList`

- **Raw segment(s)**: `[23]`
- **Header hex**: `77ae0bed00009500000000000000000a`
- **Total length**: `149` bytes
- **Header length bytes `4..6`**: `000095` = `149`
- **Flag/opcode byte `7`**: `0`
- **Header sequence byte `15`**: `10`
- **URL query fields**: `{"bv": "7.0.2", "seq": "10", "session": "02D1B0135ABCDC0D", "sptype": "spv2jodo", "version": "7.0.2"}`
- **Decoded request/control payload**:
  ```json
  [{"func": "GetHuiZhangList"}]
  ```

### UP frame 031 — Func: `QueryJingLingInfo`

- **Raw segment(s)**: `[25]`
- **Header hex**: `ca8d06c700009700000000000000000b`
- **Total length**: `151` bytes
- **Header length bytes `4..6`**: `000097` = `151`
- **Flag/opcode byte `7`**: `0`
- **Header sequence byte `15`**: `11`
- **URL query fields**: `{"bv": "7.0.2", "seq": "11", "session": "02D1B0135ABCDC0D", "sptype": "spv2jodo", "version": "7.0.2"}`
- **Decoded request/control payload**:
  ```json
  [{"func": "QueryJingLingInfo"}]
  ```

### UP frame 033 — Func: `QueryZuoQiList`

- **Raw segment(s)**: `[27]`
- **Header hex**: `1898146300009400000000000000000c`
- **Total length**: `148` bytes
- **Header length bytes `4..6`**: `000094` = `148`
- **Flag/opcode byte `7`**: `0`
- **Header sequence byte `15`**: `12`
- **URL query fields**: `{"bv": "7.0.2", "seq": "12", "session": "02D1B0135ABCDC0D", "sptype": "spv2jodo", "version": "7.0.2"}`
- **Decoded request/control payload**:
  ```json
  [{"func": "QueryZuoQiList"}]
  ```

### UP frame 035 — Func: `ZuoQiEquipQuery`

- **Raw segment(s)**: `[29]`
- **Header hex**: `01a023870000a600000000000000000d`
- **Total length**: `166` bytes
- **Header length bytes `4..6`**: `0000a6` = `166`
- **Flag/opcode byte `7`**: `0`
- **Header sequence byte `15`**: `13`
- **URL query fields**: `{"bv": "7.0.2", "seq": "13", "session": "02D1B0135ABCDC0D", "sptype": "spv2jodo", "version": "7.0.2"}`
- **Decoded request/control payload**:
  ```json
  [{"func": "ZuoQiEquipQuery", "zqId": 0}]
  ```

### UP frame 037 — Func: `ZuoQiSkinQuery`

- **Raw segment(s)**: `[31]`
- **Header hex**: `3d0ab55500009400000000000000000e`
- **Total length**: `148` bytes
- **Header length bytes `4..6`**: `000094` = `148`
- **Flag/opcode byte `7`**: `0`
- **Header sequence byte `15`**: `14`
- **URL query fields**: `{"bv": "7.0.2", "seq": "14", "session": "02D1B0135ABCDC0D", "sptype": "spv2jodo", "version": "7.0.2"}`
- **Decoded request/control payload**:
  ```json
  [{"func": "ZuoQiSkinQuery"}]
  ```

### UP frame 039 — Func: `QueryAllTalentInfo`

- **Raw segment(s)**: `[33]`
- **Header hex**: `a92dab7f00009800000000000000000f`
- **Total length**: `152` bytes
- **Header length bytes `4..6`**: `000098` = `152`
- **Flag/opcode byte `7`**: `0`
- **Header sequence byte `15`**: `15`
- **URL query fields**: `{"bv": "7.0.2", "seq": "15", "session": "02D1B0135ABCDC0D", "sptype": "spv2jodo", "version": "7.0.2"}`
- **Decoded request/control payload**:
  ```json
  [{"func": "QueryAllTalentInfo"}]
  ```

### UP frame 041 — Func: `DollQuery`

- **Raw segment(s)**: `[35]`
- **Header hex**: `f8fd7e8000008f000000000000000010`
- **Total length**: `143` bytes
- **Header length bytes `4..6`**: `00008f` = `143`
- **Flag/opcode byte `7`**: `0`
- **Header sequence byte `15`**: `16`
- **URL query fields**: `{"bv": "7.0.2", "seq": "16", "session": "02D1B0135ABCDC0D", "sptype": "spv2jodo", "version": "7.0.2"}`
- **Decoded request/control payload**:
  ```json
  [{"func": "DollQuery"}]
  ```

### UP frame 043 — Func: `QueryPetList`

- **Raw segment(s)**: `[37]`
- **Header hex**: `21cfd21a000092000000000000000011`
- **Total length**: `146` bytes
- **Header length bytes `4..6`**: `000092` = `146`
- **Flag/opcode byte `7`**: `0`
- **Header sequence byte `15`**: `17`
- **URL query fields**: `{"bv": "7.0.2", "seq": "17", "session": "02D1B0135ABCDC0D", "sptype": "spv2jodo", "version": "7.0.2"}`
- **Decoded request/control payload**:
  ```json
  [{"func": "QueryPetList"}]
  ```

### UP frame 045 — Func: `QueryDailyProgress`

- **Raw segment(s)**: `[39]`
- **Header hex**: `378c7a2f000098000000000000000012`
- **Total length**: `152` bytes
- **Header length bytes `4..6`**: `000098` = `152`
- **Flag/opcode byte `7`**: `0`
- **Header sequence byte `15`**: `18`
- **URL query fields**: `{"bv": "7.0.2", "seq": "18", "session": "02D1B0135ABCDC0D", "sptype": "spv2jodo", "version": "7.0.2"}`
- **Decoded request/control payload**:
  ```json
  [{"func": "QueryDailyProgress"}]
  ```

### UP frame 047 — Func: `ObjRecordQuery`

- **Raw segment(s)**: `[41]`
- **Header hex**: `b080b6eb000094000000000000000013`
- **Total length**: `148` bytes
- **Header length bytes `4..6`**: `000094` = `148`
- **Flag/opcode byte `7`**: `0`
- **Header sequence byte `15`**: `19`
- **URL query fields**: `{"bv": "7.0.2", "seq": "19", "session": "02D1B0135ABCDC0D", "sptype": "spv2jodo", "version": "7.0.2"}`
- **Decoded request/control payload**:
  ```json
  [{"func": "ObjRecordQuery"}]
  ```

### UP frame 049 — Func: `QueryQianDao`

- **Raw segment(s)**: `[43]`
- **Header hex**: `e8b16c61000092000000000000000014`
- **Total length**: `146` bytes
- **Header length bytes `4..6`**: `000092` = `146`
- **Flag/opcode byte `7`**: `0`
- **Header sequence byte `15`**: `20`
- **URL query fields**: `{"bv": "7.0.2", "seq": "20", "session": "02D1B0135ABCDC0D", "sptype": "spv2jodo", "version": "7.0.2"}`
- **Decoded request/control payload**:
  ```json
  [{"func": "QueryQianDao"}]
  ```

### UP frame 051 — Func: `LotteryQuery`

- **Raw segment(s)**: `[45]`
- **Header hex**: `905c84f3000092000000000000000015`
- **Total length**: `146` bytes
- **Header length bytes `4..6`**: `000092` = `146`
- **Flag/opcode byte `7`**: `0`
- **Header sequence byte `15`**: `21`
- **URL query fields**: `{"bv": "7.0.2", "seq": "21", "session": "02D1B0135ABCDC0D", "sptype": "spv2jodo", "version": "7.0.2"}`
- **Decoded request/control payload**:
  ```json
  [{"func": "LotteryQuery"}]
  ```

### UP frame 053 — Func: `QueryBattleRecord`

- **Raw segment(s)**: `[47]`
- **Header hex**: `d5d230b7000097000000000000000016`
- **Total length**: `151` bytes
- **Header length bytes `4..6`**: `000097` = `151`
- **Flag/opcode byte `7`**: `0`
- **Header sequence byte `15`**: `22`
- **URL query fields**: `{"bv": "7.0.2", "seq": "22", "session": "02D1B0135ABCDC0D", "sptype": "spv2jodo", "version": "7.0.2"}`
- **Decoded request/control payload**:
  ```json
  [{"func": "QueryBattleRecord"}]
  ```

### UP frame 055 — Func: `TaskQuery`

- **Raw segment(s)**: `[49]`
- **Header hex**: `f22c435c00008f000000000000000017`
- **Total length**: `143` bytes
- **Header length bytes `4..6`**: `00008f` = `143`
- **Flag/opcode byte `7`**: `0`
- **Header sequence byte `15`**: `23`
- **URL query fields**: `{"bv": "7.0.2", "seq": "23", "session": "02D1B0135ABCDC0D", "sptype": "spv2jodo", "version": "7.0.2"}`
- **Decoded request/control payload**:
  ```json
  [{"func": "TaskQuery"}]
  ```

### UP frame 057 — Func: `QueryGuideRecord`

- **Raw segment(s)**: `[51]`
- **Header hex**: `4bf18e56000096000000000000000018`
- **Total length**: `150` bytes
- **Header length bytes `4..6`**: `000096` = `150`
- **Flag/opcode byte `7`**: `0`
- **Header sequence byte `15`**: `24`
- **URL query fields**: `{"bv": "7.0.2", "seq": "24", "session": "02D1B0135ABCDC0D", "sptype": "spv2jodo", "version": "7.0.2"}`
- **Decoded request/control payload**:
  ```json
  [{"func": "QueryGuideRecord"}]
  ```

### UP frame 059 — Func: `RibbonQuery`

- **Raw segment(s)**: `[53]`
- **Header hex**: `452e9cf3000091000000000000000019`
- **Total length**: `145` bytes
- **Header length bytes `4..6`**: `000091` = `145`
- **Flag/opcode byte `7`**: `0`
- **Header sequence byte `15`**: `25`
- **URL query fields**: `{"bv": "7.0.2", "seq": "25", "session": "02D1B0135ABCDC0D", "sptype": "spv2jodo", "version": "7.0.2"}`
- **Decoded request/control payload**:
  ```json
  [{"func": "RibbonQuery"}]
  ```

### UP frame 061 — Func: `UpdateCity`

- **Raw segment(s)**: `[55]`
- **Header hex**: `f4e9d4a00000a300000000000000001a`
- **Total length**: `163` bytes
- **Header length bytes `4..6`**: `0000a3` = `163`
- **Flag/opcode byte `7`**: `0`
- **Header sequence byte `15`**: `26`
- **URL query fields**: `{"bv": "7.0.2", "seq": "26", "session": "02D1B0135ABCDC0D", "sptype": "spv2jodo", "version": "7.0.2"}`
- **Decoded request/control payload**:
  ```json
  [{"city": 201, "func": "UpdateCity"}]
  ```

### UP frame 062 — Func: `QueryStatus`

- **Raw segment(s)**: `[56]`
- **Header hex**: `c0f1a68400009100000000000000001b`
- **Total length**: `145` bytes
- **Header length bytes `4..6`**: `000091` = `145`
- **Flag/opcode byte `7`**: `0`
- **Header sequence byte `15`**: `27`
- **URL query fields**: `{"bv": "7.0.2", "seq": "27", "session": "02D1B0135ABCDC0D", "sptype": "spv2jodo", "version": "7.0.2"}`
- **Decoded request/control payload**:
  ```json
  [{"func": "QueryStatus"}]
  ```

### UP frame 063 — Func: `GetTeamList`

- **Raw segment(s)**: `[57]`
- **Header hex**: `35ff421a00009100000000000000001c`
- **Total length**: `145` bytes
- **Header length bytes `4..6`**: `000091` = `145`
- **Flag/opcode byte `7`**: `0`
- **Header sequence byte `15`**: `28`
- **URL query fields**: `{"bv": "7.0.2", "seq": "28", "session": "02D1B0135ABCDC0D", "sptype": "spv2jodo", "version": "7.0.2"}`
- **Decoded request/control payload**:
  ```json
  [{"func": "GetTeamList"}]
  ```

### UP frame 064 — Func: `QueryMailBox`

- **Raw segment(s)**: `[58]`
- **Header hex**: `5a3fd55400009200000000000000001d`
- **Total length**: `146` bytes
- **Header length bytes `4..6`**: `000092` = `146`
- **Flag/opcode byte `7`**: `0`
- **Header sequence byte `15`**: `29`
- **URL query fields**: `{"bv": "7.0.2", "seq": "29", "session": "02D1B0135ABCDC0D", "sptype": "spv2jodo", "version": "7.0.2"}`
- **Decoded request/control payload**:
  ```json
  [{"func": "QueryMailBox"}]
  ```

### UP frame 065 — Func: `QueryChargeInfo`

- **Raw segment(s)**: `[59]`
- **Header hex**: `a44e6f2800009500000000000000001e`
- **Total length**: `149` bytes
- **Header length bytes `4..6`**: `000095` = `149`
- **Flag/opcode byte `7`**: `0`
- **Header sequence byte `15`**: `30`
- **URL query fields**: `{"bv": "7.0.2", "seq": "30", "session": "02D1B0135ABCDC0D", "sptype": "spv2jodo", "version": "7.0.2"}`
- **Decoded request/control payload**:
  ```json
  [{"func": "QueryChargeInfo"}]
  ```

### UP frame 070 — Func: `FriendQuery`

- **Raw segment(s)**: `[62]`
- **Header hex**: `5362324f00009100000000000000001f`
- **Total length**: `145` bytes
- **Header length bytes `4..6`**: `000091` = `145`
- **Flag/opcode byte `7`**: `0`
- **Header sequence byte `15`**: `31`
- **URL query fields**: `{"bv": "7.0.2", "seq": "31", "session": "02D1B0135ABCDC0D", "sptype": "spv2jodo", "version": "7.0.2"}`
- **Decoded request/control payload**:
  ```json
  [{"func": "FriendQuery"}]
  ```

### UP frame 072 — Func: `QueryAvatarItems`

- **Raw segment(s)**: `[64]`
- **Header hex**: `93aad4ea000096000000000000000020`
- **Total length**: `150` bytes
- **Header length bytes `4..6`**: `000096` = `150`
- **Flag/opcode byte `7`**: `0`
- **Header sequence byte `15`**: `32`
- **URL query fields**: `{"bv": "7.0.2", "seq": "32", "session": "02D1B0135ABCDC0D", "sptype": "spv2jodo", "version": "7.0.2"}`
- **Decoded request/control payload**:
  ```json
  [{"func": "QueryAvatarItems"}]
  ```

### UP frame 074 — Func: `PVPStatusQuery`

- **Raw segment(s)**: `[66]`
- **Header hex**: `d534eed5000094000000000000000021`
- **Total length**: `148` bytes
- **Header length bytes `4..6`**: `000094` = `148`
- **Flag/opcode byte `7`**: `0`
- **Header sequence byte `15`**: `33`
- **URL query fields**: `{"bv": "7.0.2", "seq": "33", "session": "02D1B0135ABCDC0D", "sptype": "spv2jodo", "version": "7.0.2"}`
- **Decoded request/control payload**:
  ```json
  [{"func": "PVPStatusQuery"}]
  ```

### UP frame 076 — Func: `GetSoliderList`

- **Raw segment(s)**: `[68]`
- **Header hex**: `0628a613000094000000000000000022`
- **Total length**: `148` bytes
- **Header length bytes `4..6`**: `000094` = `148`
- **Flag/opcode byte `7`**: `0`
- **Header sequence byte `15`**: `34`
- **URL query fields**: `{"bv": "7.0.2", "seq": "34", "session": "02D1B0135ABCDC0D", "sptype": "spv2jodo", "version": "7.0.2"}`
- **Decoded request/control payload**:
  ```json
  [{"func": "GetSoliderList"}]
  ```

### UP frame 077 — Func: `QueryEmploySoliderHistory`

- **Raw segment(s)**: `[69]`
- **Header hex**: `ce5f2dbf00009f000000000000000023`
- **Total length**: `159` bytes
- **Header length bytes `4..6`**: `00009f` = `159`
- **Flag/opcode byte `7`**: `0`
- **Header sequence byte `15`**: `35`
- **URL query fields**: `{"bv": "7.0.2", "seq": "35", "session": "02D1B0135ABCDC0D", "sptype": "spv2jodo", "version": "7.0.2"}`
- **Decoded request/control payload**:
  ```json
  [{"func": "QueryEmploySoliderHistory"}]
  ```

### UP frame 079 — Func: `QueryTreasureCave`

- **Raw segment(s)**: `[71]`
- **Header hex**: `c4a3fcc5000097000000000000000024`
- **Total length**: `151` bytes
- **Header length bytes `4..6`**: `000097` = `151`
- **Flag/opcode byte `7`**: `0`
- **Header sequence byte `15`**: `36`
- **URL query fields**: `{"bv": "7.0.2", "seq": "36", "session": "02D1B0135ABCDC0D", "sptype": "spv2jodo", "version": "7.0.2"}`
- **Decoded request/control payload**:
  ```json
  [{"func": "QueryTreasureCave"}]
  ```

### UP frame 081 — Func: `QueryTreasureCaveAward`

- **Raw segment(s)**: `[73]`
- **Header hex**: `b0b2185d00009c000000000000000025`
- **Total length**: `156` bytes
- **Header length bytes `4..6`**: `00009c` = `156`
- **Flag/opcode byte `7`**: `0`
- **Header sequence byte `15`**: `37`
- **URL query fields**: `{"bv": "7.0.2", "seq": "37", "session": "02D1B0135ABCDC0D", "sptype": "spv2jodo", "version": "7.0.2"}`
- **Decoded request/control payload**:
  ```json
  [{"func": "QueryTreasureCaveAward"}]
  ```

### UP frame 083 — Func: `QueryVipLiBaoDraw`

- **Raw segment(s)**: `[75]`
- **Header hex**: `34fe11f6000097000000000000000026`
- **Total length**: `151` bytes
- **Header length bytes `4..6`**: `000097` = `151`
- **Flag/opcode byte `7`**: `0`
- **Header sequence byte `15`**: `38`
- **URL query fields**: `{"bv": "7.0.2", "seq": "38", "session": "02D1B0135ABCDC0D", "sptype": "spv2jodo", "version": "7.0.2"}`
- **Decoded request/control payload**:
  ```json
  [{"func": "QueryVipLiBaoDraw"}]
  ```

### UP frame 085 — Func: `GlobalBossQuery`

- **Raw segment(s)**: `[77]`
- **Header hex**: `54e3872f000095000000000000000027`
- **Total length**: `149` bytes
- **Header length bytes `4..6`**: `000095` = `149`
- **Flag/opcode byte `7`**: `0`
- **Header sequence byte `15`**: `39`
- **URL query fields**: `{"bv": "7.0.2", "seq": "39", "session": "02D1B0135ABCDC0D", "sptype": "spv2jodo", "version": "7.0.2"}`
- **Decoded request/control payload**:
  ```json
  [{"func": "GlobalBossQuery"}]
  ```

### UP frame 086 — Func: `GlobalPetQuery`

- **Raw segment(s)**: `[79]`
- **Header hex**: `4c1645e8000094000000000000000028`
- **Total length**: `148` bytes
- **Header length bytes `4..6`**: `000094` = `148`
- **Flag/opcode byte `7`**: `0`
- **Header sequence byte `15`**: `40`
- **URL query fields**: `{"bv": "7.0.2", "seq": "40", "session": "02D1B0135ABCDC0D", "sptype": "spv2jodo", "version": "7.0.2"}`
- **Decoded request/control payload**:
  ```json
  [{"func": "GlobalPetQuery"}]
  ```

### UP frame 089 — Func: `MiJingStatusQuery`

- **Raw segment(s)**: `[83]`
- **Header hex**: `5104eaea000097000000000000000029`
- **Total length**: `151` bytes
- **Header length bytes `4..6`**: `000097` = `151`
- **Flag/opcode byte `7`**: `0`
- **Header sequence byte `15`**: `41`
- **URL query fields**: `{"bv": "7.0.2", "seq": "41", "session": "02D1B0135ABCDC0D", "sptype": "spv2jodo", "version": "7.0.2"}`
- **Decoded request/control payload**:
  ```json
  [{"func": "MiJingStatusQuery"}]
  ```

### UP frame 091 — Func: `PetExploreQuery`

- **Raw segment(s)**: `[85]`
- **Header hex**: `42ddf10e00009500000000000000002a`
- **Total length**: `149` bytes
- **Header length bytes `4..6`**: `000095` = `149`
- **Flag/opcode byte `7`**: `0`
- **Header sequence byte `15`**: `42`
- **URL query fields**: `{"bv": "7.0.2", "seq": "42", "session": "02D1B0135ABCDC0D", "sptype": "spv2jodo", "version": "7.0.2"}`
- **Decoded request/control payload**:
  ```json
  [{"func": "PetExploreQuery"}]
  ```

### UP frame 093 — Func: `QueryDecorationBag`

- **Raw segment(s)**: `[87]`
- **Header hex**: `fa63f74f00009800000000000000002b`
- **Total length**: `152` bytes
- **Header length bytes `4..6`**: `000098` = `152`
- **Flag/opcode byte `7`**: `0`
- **Header sequence byte `15`**: `43`
- **URL query fields**: `{"bv": "7.0.2", "seq": "43", "session": "02D1B0135ABCDC0D", "sptype": "spv2jodo", "version": "7.0.2"}`
- **Decoded request/control payload**:
  ```json
  [{"func": "QueryDecorationBag"}]
  ```

### UP frame 095 — Func: `ZBraceletQuery`

- **Raw segment(s)**: `[89]`
- **Header hex**: `759eb31d00009400000000000000002c`
- **Total length**: `148` bytes
- **Header length bytes `4..6`**: `000094` = `148`
- **Flag/opcode byte `7`**: `0`
- **Header sequence byte `15`**: `44`
- **URL query fields**: `{"bv": "7.0.2", "seq": "44", "session": "02D1B0135ABCDC0D", "sptype": "spv2jodo", "version": "7.0.2"}`
- **Decoded request/control payload**:
  ```json
  [{"func": "ZBraceletQuery"}]
  ```

### UP frame 097 — Func: `QueryPetBag`

- **Raw segment(s)**: `[91]`
- **Header hex**: `5178b22500009100000000000000002d`
- **Total length**: `145` bytes
- **Header length bytes `4..6`**: `000091` = `145`
- **Flag/opcode byte `7`**: `0`
- **Header sequence byte `15`**: `45`
- **URL query fields**: `{"bv": "7.0.2", "seq": "45", "session": "02D1B0135ABCDC0D", "sptype": "spv2jodo", "version": "7.0.2"}`
- **Decoded request/control payload**:
  ```json
  [{"func": "QueryPetBag"}]
  ```

### UP frame 099 — Func: `LivenessQuery`

- **Raw segment(s)**: `[93]`
- **Header hex**: `797aed4b00009300000000000000002e`
- **Total length**: `147` bytes
- **Header length bytes `4..6`**: `000093` = `147`
- **Flag/opcode byte `7`**: `0`
- **Header sequence byte `15`**: `46`
- **URL query fields**: `{"bv": "7.0.2", "seq": "46", "session": "02D1B0135ABCDC0D", "sptype": "spv2jodo", "version": "7.0.2"}`
- **Decoded request/control payload**:
  ```json
  [{"func": "LivenessQuery"}]
  ```

### UP frame 101 — Func: `RichnessForestQuery`

- **Raw segment(s)**: `[95]`
- **Header hex**: `c9b4880600009900000000000000002f`
- **Total length**: `153` bytes
- **Header length bytes `4..6`**: `000099` = `153`
- **Flag/opcode byte `7`**: `0`
- **Header sequence byte `15`**: `47`
- **URL query fields**: `{"bv": "7.0.2", "seq": "47", "session": "02D1B0135ABCDC0D", "sptype": "spv2jodo", "version": "7.0.2"}`
- **Decoded request/control payload**:
  ```json
  [{"func": "RichnessForestQuery"}]
  ```

### UP frame 103 — Func: `CampTechQuery`

- **Raw segment(s)**: `[97]`
- **Header hex**: `c990109e000093000000000000000030`
- **Total length**: `147` bytes
- **Header length bytes `4..6`**: `000093` = `147`
- **Flag/opcode byte `7`**: `0`
- **Header sequence byte `15`**: `48`
- **URL query fields**: `{"bv": "7.0.2", "seq": "48", "session": "02D1B0135ABCDC0D", "sptype": "spv2jodo", "version": "7.0.2"}`
- **Decoded request/control payload**:
  ```json
  [{"func": "CampTechQuery"}]
  ```

### UP frame 105 — Func: `CampStatueQuery`

- **Raw segment(s)**: `[99]`
- **Header hex**: `2dbd811b000095000000000000000031`
- **Total length**: `149` bytes
- **Header length bytes `4..6`**: `000095` = `149`
- **Flag/opcode byte `7`**: `0`
- **Header sequence byte `15`**: `49`
- **URL query fields**: `{"bv": "7.0.2", "seq": "49", "session": "02D1B0135ABCDC0D", "sptype": "spv2jodo", "version": "7.0.2"}`
- **Decoded request/control payload**:
  ```json
  [{"func": "CampStatueQuery"}]
  ```

### UP frame 107 — Func: `InviteReturnQuery`

- **Raw segment(s)**: `[101]`
- **Header hex**: `ebfa15a3000097000000000000000032`
- **Total length**: `151` bytes
- **Header length bytes `4..6`**: `000097` = `151`
- **Flag/opcode byte `7`**: `0`
- **Header sequence byte `15`**: `50`
- **URL query fields**: `{"bv": "7.0.2", "seq": "50", "session": "02D1B0135ABCDC0D", "sptype": "spv2jodo", "version": "7.0.2"}`
- **Decoded request/control payload**:
  ```json
  [{"func": "InviteReturnQuery"}]
  ```

### UP frame 109 — Func: `TopMatchQuery`

- **Raw segment(s)**: `[103]`
- **Header hex**: `f829d894000093000000000000000033`
- **Total length**: `147` bytes
- **Header length bytes `4..6`**: `000093` = `147`
- **Flag/opcode byte `7`**: `0`
- **Header sequence byte `15`**: `51`
- **URL query fields**: `{"bv": "7.0.2", "seq": "51", "session": "02D1B0135ABCDC0D", "sptype": "spv2jodo", "version": "7.0.2"}`
- **Decoded request/control payload**:
  ```json
  [{"func": "TopMatchQuery"}]
  ```

### UP frame 111 — Func: `DecorationGemQuery`

- **Raw segment(s)**: `[105]`
- **Header hex**: `202cf91d000098000000000000000034`
- **Total length**: `152` bytes
- **Header length bytes `4..6`**: `000098` = `152`
- **Flag/opcode byte `7`**: `0`
- **Header sequence byte `15`**: `52`
- **URL query fields**: `{"bv": "7.0.2", "seq": "52", "session": "02D1B0135ABCDC0D", "sptype": "spv2jodo", "version": "7.0.2"}`
- **Decoded request/control payload**:
  ```json
  [{"func": "DecorationGemQuery"}]
  ```

### UP frame 113 — Func: `ExchangeShopQuery`

- **Raw segment(s)**: `[107]`
- **Header hex**: `339189cc000097000000000000000035`
- **Total length**: `151` bytes
- **Header length bytes `4..6`**: `000097` = `151`
- **Flag/opcode byte `7`**: `0`
- **Header sequence byte `15`**: `53`
- **URL query fields**: `{"bv": "7.0.2", "seq": "53", "session": "02D1B0135ABCDC0D", "sptype": "spv2jodo", "version": "7.0.2"}`
- **Decoded request/control payload**:
  ```json
  [{"func": "ExchangeShopQuery"}]
  ```

### UP frame 115 — Func: `PetResearchQuery`

- **Raw segment(s)**: `[109]`
- **Header hex**: `34ada0a1000096000000000000000036`
- **Total length**: `150` bytes
- **Header length bytes `4..6`**: `000096` = `150`
- **Flag/opcode byte `7`**: `0`
- **Header sequence byte `15`**: `54`
- **URL query fields**: `{"bv": "7.0.2", "seq": "54", "session": "02D1B0135ABCDC0D", "sptype": "spv2jodo", "version": "7.0.2"}`
- **Decoded request/control payload**:
  ```json
  [{"func": "PetResearchQuery"}]
  ```

### UP frame 117 — Func: `RecoverQuery`

- **Raw segment(s)**: `[111]`
- **Header hex**: `8ed4a170000092000000000000000037`
- **Total length**: `146` bytes
- **Header length bytes `4..6`**: `000092` = `146`
- **Flag/opcode byte `7`**: `0`
- **Header sequence byte `15`**: `55`
- **URL query fields**: `{"bv": "7.0.2", "seq": "55", "session": "02D1B0135ABCDC0D", "sptype": "spv2jodo", "version": "7.0.2"}`
- **Decoded request/control payload**:
  ```json
  [{"func": "RecoverQuery"}]
  ```

### UP frame 119 — Func: `TreasureScrambleInfoQuery`

- **Raw segment(s)**: `[113]`
- **Header hex**: `7d08a11b00009f000000000000000038`
- **Total length**: `159` bytes
- **Header length bytes `4..6`**: `00009f` = `159`
- **Flag/opcode byte `7`**: `0`
- **Header sequence byte `15`**: `56`
- **URL query fields**: `{"bv": "7.0.2", "seq": "56", "session": "02D1B0135ABCDC0D", "sptype": "spv2jodo", "version": "7.0.2"}`
- **Decoded request/control payload**:
  ```json
  [{"func": "TreasureScrambleInfoQuery"}]
  ```

### UP frame 121 — Func: `CampQuery`

- **Raw segment(s)**: `[115]`
- **Header hex**: `7e40cd0200008f000000000000000039`
- **Total length**: `143` bytes
- **Header length bytes `4..6`**: `00008f` = `143`
- **Flag/opcode byte `7`**: `0`
- **Header sequence byte `15`**: `57`
- **URL query fields**: `{"bv": "7.0.2", "seq": "57", "session": "02D1B0135ABCDC0D", "sptype": "spv2jodo", "version": "7.0.2"}`
- **Decoded request/control payload**:
  ```json
  [{"func": "CampQuery"}]
  ```

### UP frame 123 — Func: `PetOwnedQuery`

- **Raw segment(s)**: `[117]`
- **Header hex**: `43ed824400009300000000000000003a`
- **Total length**: `147` bytes
- **Header length bytes `4..6`**: `000093` = `147`
- **Flag/opcode byte `7`**: `0`
- **Header sequence byte `15`**: `58`
- **URL query fields**: `{"bv": "7.0.2", "seq": "58", "session": "02D1B0135ABCDC0D", "sptype": "spv2jodo", "version": "7.0.2"}`
- **Decoded request/control payload**:
  ```json
  [{"func": "PetOwnedQuery"}]
  ```

### UP frame 125 — Func: `StatisticsQuery`

- **Raw segment(s)**: `[119]`
- **Header hex**: `67d1396f00009500000000000000003b`
- **Total length**: `149` bytes
- **Header length bytes `4..6`**: `000095` = `149`
- **Flag/opcode byte `7`**: `0`
- **Header sequence byte `15`**: `59`
- **URL query fields**: `{"bv": "7.0.2", "seq": "59", "session": "02D1B0135ABCDC0D", "sptype": "spv2jodo", "version": "7.0.2"}`
- **Decoded request/control payload**:
  ```json
  [{"func": "StatisticsQuery"}]
  ```

### UP frame 127 — Func: `FriendHuntQuery`

- **Raw segment(s)**: `[121]`
- **Header hex**: `f3da11770000af00000000000000003c`
- **Total length**: `175` bytes
- **Header length bytes `4..6`**: `0000af` = `175`
- **Flag/opcode byte `7`**: `0`
- **Header sequence byte `15`**: `60`
- **URL query fields**: `{"bv": "7.0.2", "seq": "60", "session": "02D1B0135ABCDC0D", "sptype": "spv2jodo", "version": "7.0.2"}`
- **Decoded request/control payload**:
  ```json
  [{"avatarID": "", "func": "FriendHuntQuery"}]
  ```

### UP frame 129 — Func: `CampHuntQuery`

- **Raw segment(s)**: `[123]`
- **Header hex**: `9ae183260000ab00000000000000003d`
- **Total length**: `171` bytes
- **Header length bytes `4..6`**: `0000ab` = `171`
- **Flag/opcode byte `7`**: `0`
- **Header sequence byte `15`**: `61`
- **URL query fields**: `{"bv": "7.0.2", "seq": "61", "session": "02D1B0135ABCDC0D", "sptype": "spv2jodo", "version": "7.0.2"}`
- **Decoded request/control payload**:
  ```json
  [{"func": "CampHuntQuery", "huntId": ""}]
  ```

### UP frame 131 — Func: `QueryAvatarTechnologyTree`

- **Raw segment(s)**: `[125]`
- **Header hex**: `8440bc6800009f00000000000000003e`
- **Total length**: `159` bytes
- **Header length bytes `4..6`**: `00009f` = `159`
- **Flag/opcode byte `7`**: `0`
- **Header sequence byte `15`**: `62`
- **URL query fields**: `{"bv": "7.0.2", "seq": "62", "session": "02D1B0135ABCDC0D", "sptype": "spv2jodo", "version": "7.0.2"}`
- **Decoded request/control payload**:
  ```json
  [{"func": "QueryAvatarTechnologyTree"}]
  ```

### UP frame 133 — Func: `PVPRankingTopQuery`

- **Raw segment(s)**: `[127]`
- **Header hex**: `34f49ec10000b000000000000000003f`
- **Total length**: `176` bytes
- **Header length bytes `4..6`**: `0000b0` = `176`
- **Flag/opcode byte `7`**: `0`
- **Header sequence byte `15`**: `63`
- **URL query fields**: `{"bv": "7.0.2", "seq": "63", "session": "02D1B0135ABCDC0D", "sptype": "spv2jodo", "version": "7.0.2"}`
- **Decoded request/control payload**:
  ```json
  [{"func": "PVPRankingTopQuery", "sectionType": 1}]
  ```

### UP frame 135 — Func: `PetSummonQuery`

- **Raw segment(s)**: `[132]`
- **Header hex**: `df1887f8000094000000000000000040`
- **Total length**: `148` bytes
- **Header length bytes `4..6`**: `000094` = `148`
- **Flag/opcode byte `7`**: `0`
- **Header sequence byte `15`**: `64`
- **URL query fields**: `{"bv": "7.0.2", "seq": "64", "session": "02D1B0135ABCDC0D", "sptype": "spv2jodo", "version": "7.0.2"}`
- **Decoded request/control payload**:
  ```json
  [{"func": "PetSummonQuery"}]
  ```

### UP frame 137 — Func: `OnceRewardQuery`

- **Raw segment(s)**: `[137]`
- **Header hex**: `30c80515000095000000000000000041`
- **Total length**: `149` bytes
- **Header length bytes `4..6`**: `000095` = `149`
- **Flag/opcode byte `7`**: `0`
- **Header sequence byte `15`**: `65`
- **URL query fields**: `{"bv": "7.0.2", "seq": "65", "session": "02D1B0135ABCDC0D", "sptype": "spv2jodo", "version": "7.0.2"}`
- **Decoded request/control payload**:
  ```json
  [{"func": "OnceRewardQuery"}]
  ```

### UP frame 139 — Func: `PetCoordinationQuery`

- **Raw segment(s)**: `[139]`
- **Header hex**: `58b551f400009a000000000000000042`
- **Total length**: `154` bytes
- **Header length bytes `4..6`**: `00009a` = `154`
- **Flag/opcode byte `7`**: `0`
- **Header sequence byte `15`**: `66`
- **URL query fields**: `{"bv": "7.0.2", "seq": "66", "session": "02D1B0135ABCDC0D", "sptype": "spv2jodo", "version": "7.0.2"}`
- **Decoded request/control payload**:
  ```json
  [{"func": "PetCoordinationQuery"}]
  ```

### UP frame 141 — Func: `PetExpeditionQuery`

- **Raw segment(s)**: `[141]`
- **Header hex**: `02eb8e1b000098000000000000000043`
- **Total length**: `152` bytes
- **Header length bytes `4..6`**: `000098` = `152`
- **Flag/opcode byte `7`**: `0`
- **Header sequence byte `15`**: `67`
- **URL query fields**: `{"bv": "7.0.2", "seq": "67", "session": "02D1B0135ABCDC0D", "sptype": "spv2jodo", "version": "7.0.2"}`
- **Decoded request/control payload**:
  ```json
  [{"func": "PetExpeditionQuery"}]
  ```

### UP frame 143 — Func: `DaoguanInfoQuery`

- **Raw segment(s)**: `[143]`
- **Header hex**: `be6bacc40000aa000000000000000044`
- **Total length**: `170` bytes
- **Header length bytes `4..6`**: `0000aa` = `170`
- **Flag/opcode byte `7`**: `0`
- **Header sequence byte `15`**: `68`
- **URL query fields**: `{"bv": "7.0.2", "seq": "68", "session": "02D1B0135ABCDC0D", "sptype": "spv2jodo", "version": "7.0.2"}`
- **Decoded request/control payload**:
  ```json
  [{"func": "DaoguanInfoQuery", "skillId": 0}]
  ```

### UP frame 145 — Func: `WaiguanQuery`

- **Raw segment(s)**: `[145]`
- **Header hex**: `adfee7ee000092000000000000000045`
- **Total length**: `146` bytes
- **Header length bytes `4..6`**: `000092` = `146`
- **Flag/opcode byte `7`**: `0`
- **Header sequence byte `15`**: `69`
- **URL query fields**: `{"bv": "7.0.2", "seq": "69", "session": "02D1B0135ABCDC0D", "sptype": "spv2jodo", "version": "7.0.2"}`
- **Decoded request/control payload**:
  ```json
  [{"func": "WaiguanQuery"}]
  ```

### UP frame 147 — Func: `BattleTowerQuery`

- **Raw segment(s)**: `[147]`
- **Header hex**: `eec9aa1d000096000000000000000046`
- **Total length**: `150` bytes
- **Header length bytes `4..6`**: `000096` = `150`
- **Flag/opcode byte `7`**: `0`
- **Header sequence byte `15`**: `70`
- **URL query fields**: `{"bv": "7.0.2", "seq": "70", "session": "02D1B0135ABCDC0D", "sptype": "spv2jodo", "version": "7.0.2"}`
- **Decoded request/control payload**:
  ```json
  [{"func": "BattleTowerQuery"}]
  ```

### UP frame 149 — Func: `ChampionLeagueQueryTime`

- **Raw segment(s)**: `[149]`
- **Header hex**: `3ad4c37f00009d000000000000000047`
- **Total length**: `157` bytes
- **Header length bytes `4..6`**: `00009d` = `157`
- **Flag/opcode byte `7`**: `0`
- **Header sequence byte `15`**: `71`
- **URL query fields**: `{"bv": "7.0.2", "seq": "71", "session": "02D1B0135ABCDC0D", "sptype": "spv2jodo", "version": "7.0.2"}`
- **Decoded request/control payload**:
  ```json
  [{"func": "ChampionLeagueQueryTime"}]
  ```

### UP frame 151 — Func: `ReturnGiftQuery`

- **Raw segment(s)**: `[151]`
- **Header hex**: `1bdb716d000095000000000000000048`
- **Total length**: `149` bytes
- **Header length bytes `4..6`**: `000095` = `149`
- **Flag/opcode byte `7`**: `0`
- **Header sequence byte `15`**: `72`
- **URL query fields**: `{"bv": "7.0.2", "seq": "72", "session": "02D1B0135ABCDC0D", "sptype": "spv2jodo", "version": "7.0.2"}`
- **Decoded request/control payload**:
  ```json
  [{"func": "ReturnGiftQuery"}]
  ```

### UP frame 153 — Func: `GlobalGuildWarQuery`

- **Raw segment(s)**: `[153]`
- **Header hex**: `fe5ed839000099000000000000000049`
- **Total length**: `153` bytes
- **Header length bytes `4..6`**: `000099` = `153`
- **Flag/opcode byte `7`**: `0`
- **Header sequence byte `15`**: `73`
- **URL query fields**: `{"bv": "7.0.2", "seq": "73", "session": "02D1B0135ABCDC0D", "sptype": "spv2jodo", "version": "7.0.2"}`
- **Decoded request/control payload**:
  ```json
  [{"func": "GlobalGuildWarQuery"}]
  ```

### UP frame 155 — Func: `DaoguanSkillAwakenQuery`

- **Raw segment(s)**: `[155]`
- **Header hex**: `a0d6c62400009d00000000000000004a`
- **Total length**: `157` bytes
- **Header length bytes `4..6`**: `00009d` = `157`
- **Flag/opcode byte `7`**: `0`
- **Header sequence byte `15`**: `74`
- **URL query fields**: `{"bv": "7.0.2", "seq": "74", "session": "02D1B0135ABCDC0D", "sptype": "spv2jodo", "version": "7.0.2"}`
- **Decoded request/control payload**:
  ```json
  [{"func": "DaoguanSkillAwakenQuery"}]
  ```

### UP frame 157 — Func: `LeagueTripQuery`

- **Raw segment(s)**: `[157]`
- **Header hex**: `23d46a300000a600000000000000004b`
- **Total length**: `166` bytes
- **Header length bytes `4..6`**: `0000a6` = `166`
- **Flag/opcode byte `7`**: `0`
- **Header sequence byte `15`**: `75`
- **URL query fields**: `{"bv": "7.0.2", "seq": "75", "session": "02D1B0135ABCDC0D", "sptype": "spv2jodo", "version": "7.0.2"}`
- **Decoded request/control payload**:
  ```json
  [{"func": "LeagueTripQuery", "ltId": 0}]
  ```

### UP frame 159 — Func: `WishStarQuery`

- **Raw segment(s)**: `[159]`
- **Header hex**: `facd576700009300000000000000004c`
- **Total length**: `147` bytes
- **Header length bytes `4..6`**: `000093` = `147`
- **Flag/opcode byte `7`**: `0`
- **Header sequence byte `15`**: `76`
- **URL query fields**: `{"bv": "7.0.2", "seq": "76", "session": "02D1B0135ABCDC0D", "sptype": "spv2jodo", "version": "7.0.2"}`
- **Decoded request/control payload**:
  ```json
  [{"func": "WishStarQuery"}]
  ```

### UP frame 161 — Func: `AtlasInfoQuery`

- **Raw segment(s)**: `[161]`
- **Header hex**: `1d4f7e4700009400000000000000004d`
- **Total length**: `148` bytes
- **Header length bytes `4..6`**: `000094` = `148`
- **Flag/opcode byte `7`**: `0`
- **Header sequence byte `15`**: `77`
- **URL query fields**: `{"bv": "7.0.2", "seq": "77", "session": "02D1B0135ABCDC0D", "sptype": "spv2jodo", "version": "7.0.2"}`
- **Decoded request/control payload**:
  ```json
  [{"func": "AtlasInfoQuery"}]
  ```

### UP frame 163 — Func: `DaoguanOwnerQuery`

- **Raw segment(s)**: `[163]`
- **Header hex**: `ae051be10000aa00000000000000004e`
- **Total length**: `170` bytes
- **Header length bytes `4..6`**: `0000aa` = `170`
- **Flag/opcode byte `7`**: `0`
- **Header sequence byte `15`**: `78`
- **URL query fields**: `{"bv": "7.0.2", "seq": "78", "session": "02D1B0135ABCDC0D", "sptype": "spv2jodo", "version": "7.0.2"}`
- **Decoded request/control payload**:
  ```json
  [{"dgId": 501, "func": "DaoguanOwnerQuery"}]
  ```

### UP frame 165 — Func: `DaoguanOwnerQuery`

- **Raw segment(s)**: `[165]`
- **Header hex**: `8962e53f0000aa00000000000000004f`
- **Total length**: `170` bytes
- **Header length bytes `4..6`**: `0000aa` = `170`
- **Flag/opcode byte `7`**: `0`
- **Header sequence byte `15`**: `79`
- **URL query fields**: `{"bv": "7.0.2", "seq": "79", "session": "02D1B0135ABCDC0D", "sptype": "spv2jodo", "version": "7.0.2"}`
- **Decoded request/control payload**:
  ```json
  [{"dgId": 502, "func": "DaoguanOwnerQuery"}]
  ```

### UP frame 167 — Func: `DaoguanOwnerQuery`

- **Raw segment(s)**: `[167]`
- **Header hex**: `becd700b0000aa000000000000000050`
- **Total length**: `170` bytes
- **Header length bytes `4..6`**: `0000aa` = `170`
- **Flag/opcode byte `7`**: `0`
- **Header sequence byte `15`**: `80`
- **URL query fields**: `{"bv": "7.0.2", "seq": "80", "session": "02D1B0135ABCDC0D", "sptype": "spv2jodo", "version": "7.0.2"}`
- **Decoded request/control payload**:
  ```json
  [{"dgId": 503, "func": "DaoguanOwnerQuery"}]
  ```

### UP frame 169 — Func: `DaoguanOwnerQuery`

- **Raw segment(s)**: `[169]`
- **Header hex**: `61d14e290000aa000000000000000051`
- **Total length**: `170` bytes
- **Header length bytes `4..6`**: `0000aa` = `170`
- **Flag/opcode byte `7`**: `0`
- **Header sequence byte `15`**: `81`
- **URL query fields**: `{"bv": "7.0.2", "seq": "81", "session": "02D1B0135ABCDC0D", "sptype": "spv2jodo", "version": "7.0.2"}`
- **Decoded request/control payload**:
  ```json
  [{"dgId": 504, "func": "DaoguanOwnerQuery"}]
  ```

### UP frame 171 — Func: `DaoguanOwnerQuery`

- **Raw segment(s)**: `[171]`
- **Header hex**: `82de8db70000aa000000000000000052`
- **Total length**: `170` bytes
- **Header length bytes `4..6`**: `0000aa` = `170`
- **Flag/opcode byte `7`**: `0`
- **Header sequence byte `15`**: `82`
- **URL query fields**: `{"bv": "7.0.2", "seq": "82", "session": "02D1B0135ABCDC0D", "sptype": "spv2jodo", "version": "7.0.2"}`
- **Decoded request/control payload**:
  ```json
  [{"dgId": 505, "func": "DaoguanOwnerQuery"}]
  ```

### UP frame 173 — Func: `DaoguanOwnerQuery`

- **Raw segment(s)**: `[173]`
- **Header hex**: `a5b973690000aa000000000000000053`
- **Total length**: `170` bytes
- **Header length bytes `4..6`**: `0000aa` = `170`
- **Flag/opcode byte `7`**: `0`
- **Header sequence byte `15`**: `83`
- **URL query fields**: `{"bv": "7.0.2", "seq": "83", "session": "02D1B0135ABCDC0D", "sptype": "spv2jodo", "version": "7.0.2"}`
- **Decoded request/control payload**:
  ```json
  [{"dgId": 506, "func": "DaoguanOwnerQuery"}]
  ```

### UP frame 175 — Func: `DaoguanOwnerQuery`

- **Raw segment(s)**: `[175]`
- **Header hex**: `361d0a8b0000aa000000000000000054`
- **Total length**: `170` bytes
- **Header length bytes `4..6`**: `0000aa` = `170`
- **Flag/opcode byte `7`**: `0`
- **Header sequence byte `15`**: `84`
- **URL query fields**: `{"bv": "7.0.2", "seq": "84", "session": "02D1B0135ABCDC0D", "sptype": "spv2jodo", "version": "7.0.2"}`
- **Decoded request/control payload**:
  ```json
  [{"dgId": 507, "func": "DaoguanOwnerQuery"}]
  ```

### UP frame 177 — Func: `DaoguanOwnerQuery`

- **Raw segment(s)**: `[177]`
- **Header hex**: `6ef3b3100000aa000000000000000055`
- **Total length**: `170` bytes
- **Header length bytes `4..6`**: `0000aa` = `170`
- **Flag/opcode byte `7`**: `0`
- **Header sequence byte `15`**: `85`
- **URL query fields**: `{"bv": "7.0.2", "seq": "85", "session": "02D1B0135ABCDC0D", "sptype": "spv2jodo", "version": "7.0.2"}`
- **Decoded request/control payload**:
  ```json
  [{"dgId": 508, "func": "DaoguanOwnerQuery"}]
  ```

### UP frame 179 — Func: `ChampionLeagueQueryStatus`

- **Raw segment(s)**: `[179]`
- **Header hex**: `d3ceff6b00009f000000000000000056`
- **Total length**: `159` bytes
- **Header length bytes `4..6`**: `00009f` = `159`
- **Flag/opcode byte `7`**: `0`
- **Header sequence byte `15`**: `86`
- **URL query fields**: `{"bv": "7.0.2", "seq": "86", "session": "02D1B0135ABCDC0D", "sptype": "spv2jodo", "version": "7.0.2"}`
- **Decoded request/control payload**:
  ```json
  [{"func": "ChampionLeagueQueryStatus"}]
  ```

### UP frame 181 — Func: `FightRealtimeQuery`

- **Raw segment(s)**: `[181]`
- **Header hex**: `bda78ab40000f7000000000000000057`
- **Total length**: `247` bytes
- **Header length bytes `4..6`**: `0000f7` = `247`
- **Flag/opcode byte `7`**: `0`
- **Header sequence byte `15`**: `87`
- **URL query fields**: `{"bv": "7.0.2", "seq": "87", "session": "02D1B0135ABCDC0D", "sptype": "spv2jodo", "version": "7.0.2"}`
- **Decoded request/control payload**:
  ```json
  [{"avatarId": "f25f2e5d-5ff3-4a83-89d5-4d259303f4bd", "fightId": "", "func": "FightRealtimeQuery"}]
  ```

### UP frame 183 — Func: `DaoguanGlobalQuery`

- **Raw segment(s)**: `[183]`
- **Header hex**: `8be9cc900000a9000000000000000058`
- **Total length**: `169` bytes
- **Header length bytes `4..6`**: `0000a9` = `169`
- **Flag/opcode byte `7`**: `0`
- **Header sequence byte `15`**: `88`
- **URL query fields**: `{"bv": "7.0.2", "seq": "88", "session": "02D1B0135ABCDC0D", "sptype": "spv2jodo", "version": "7.0.2"}`
- **Decoded request/control payload**:
  ```json
  [{"dgId": 0, "func": "DaoguanGlobalQuery"}]
  ```

### UP frame 185 — Func: `DecorationHandbookQuery`

- **Raw segment(s)**: `[186]`
- **Header hex**: `c264ff0c00009d000000000000000059`
- **Total length**: `157` bytes
- **Header length bytes `4..6`**: `00009d` = `157`
- **Flag/opcode byte `7`**: `0`
- **Header sequence byte `15`**: `89`
- **URL query fields**: `{"bv": "7.0.2", "seq": "89", "session": "02D1B0135ABCDC0D", "sptype": "spv2jodo", "version": "7.0.2"}`
- **Decoded request/control payload**:
  ```json
  [{"func": "DecorationHandbookQuery"}]
  ```

### UP frame 187 — Func: `SecretBaseQueryPrivate`

- **Raw segment(s)**: `[188]`
- **Header hex**: `be5377ad00009c00000000000000005a`
- **Total length**: `156` bytes
- **Header length bytes `4..6`**: `00009c` = `156`
- **Flag/opcode byte `7`**: `0`
- **Header sequence byte `15`**: `90`
- **URL query fields**: `{"bv": "7.0.2", "seq": "90", "session": "02D1B0135ABCDC0D", "sptype": "spv2jodo", "version": "7.0.2"}`
- **Decoded request/control payload**:
  ```json
  [{"func": "SecretBaseQueryPrivate"}]
  ```

### UP frame 189 — Func: `MirrorChallengeQuery`

- **Raw segment(s)**: `[190]`
- **Header hex**: `f1f3331600009a00000000000000005b`
- **Total length**: `154` bytes
- **Header length bytes `4..6`**: `00009a` = `154`
- **Flag/opcode byte `7`**: `0`
- **Header sequence byte `15`**: `91`
- **URL query fields**: `{"bv": "7.0.2", "seq": "91", "session": "02D1B0135ABCDC0D", "sptype": "spv2jodo", "version": "7.0.2"}`
- **Decoded request/control payload**:
  ```json
  [{"func": "MirrorChallengeQuery"}]
  ```
