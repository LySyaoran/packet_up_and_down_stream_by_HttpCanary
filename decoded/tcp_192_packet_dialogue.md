# TCP dialogue replay by `.bin` packet

Báo cáo này tái hiện lại đúng thứ tự 192 chunk TCP trong capture. `UP` là client gửi lên server; `DOWN` là server trả về client.

## Tóm tắt

- App: `com.nnal.bb3ds`
- Server: `47.236.127.186:21195`
- Capture time: `2026-06-05 02:31:58`
- TCP chunks: `192`
- Application frames sau khi ghép TCP stream: `191` (`93` UP, `98` DOWN)

## Cách đọc

- Một `.bin` là một TCP data chunk do HttpCanary tách ra, không nhất thiết bằng đúng một application message.
- Nếu một chunk chứa nhiều application frame, phần `Frame(s)` sẽ liệt kê nhiều frame.
- Nếu một application frame bị TCP chia nhỏ qua nhiều `.bin`, báo cáo sẽ ghi `spans segments` để biết frame đó nằm ở các chunk nào.
- Payload dài được rút gọn trong báo cáo này; bản đầy đủ nằm ở `decoded/decoded_packets.json`.

## Các bước chính của flow tạo avatar

- **Login**: Client đăng nhập và gửi thông tin thiết bị/user/server. Xuất hiện tại frame `003` / packet(s) `[2]`.
- **LoginResult**: Server trả session key dùng cho các request sau. Xuất hiện tại frame `004` / packet(s) `[3]`.
- **QueryAvatarAttribute**: Client kiểm tra trạng thái avatar trước/sau khi tạo. Xuất hiện tại frame `007` / packet(s) `[6]`, frame `014` / packet(s) `[12]`.
- **CreateAvatar**: Client gửi yêu cầu tạo avatar. Xuất hiện tại frame `010` / packet(s) `[9]`.
- **CreateAvatarResult**: Server xác nhận kết quả tạo avatar. Xuất hiện tại frame `013` / packet(s) `[11]`.

Điểm quan trọng nhất trong capture: packet `9.bin` gửi `CreateAvatar` với `avatarName = BeetBoij`, `chiefBuddy = 1002`, `gender = 0`; server trả `CreateAvatarResult` thành công ở packet `11.bin` với `error_code = 0`.

## Replay 192 TCP chunks

### Packet 000 — `0.bin` — UP client → server

- **Timestamp ms**: `1780601518164`
- **TCP chunk length**: `16` bytes
- **Frame(s)**: `000`
  - **Frame 000**
    - Header: `61da39960000100a0000000000000005`
    - Total length: `16` bytes; codec: `plain`; format: `empty_control`
    - Func: `—`
    - Nội dung decoded:
      ```json
      ""
      ```

### Packet 001 — `1.bin` — DOWN server → client

- **Timestamp ms**: `1780601518196`
- **TCP chunk length**: `212` bytes
- **Frame(s)**: `001, 002`
  - **Frame 001**
    - Header: `b891bac10000c41e0e4010000000340d`
    - Total length: `196` bytes; codec: `plain`; format: `json_response`
    - Func: `—`
    - Nội dung decoded:
      ```json
      {"innerAddr": "/0.0.0.0:21195", "innerCount": 13, "launchInfo": "[\"-config\",\"/data/game1195/config.prop\"]", "number": 0, "para": "[1195]", "sid": 1195, "status": 1780601514, "type": "HTGame"}
      ```
  - **Frame 002**
    - Header: `59bb33c00000100b0e4010000000340d`
    - Total length: `16` bytes; codec: `plain`; format: `empty_control`
    - Func: `—`
    - Nội dung decoded:
      ```json
      ""
      ```

### Packet 002 — `2.bin` — UP client → server

- **Timestamp ms**: `1780601518271`
- **TCP chunk length**: `736` bytes
- **Frame(s)**: `003`
  - **Frame 003**
    - Header: `e51e7d370002e0000000000000000000`
    - Total length: `736` bytes; codec: `plain`; format: `urlencoded_request`
    - Func: `Login`
    - Query fields: `{"bv": "7.0.2", "seq": "1", "session": "", "sptype": "spv2jodo", "version": "7.0.2"}`
    - Nội dung decoded:
      ```json
      [{"deviceType": 2, "func": "Login", "info": "{\"appVersion\":\"7.0.2\",\"appBaseVersion\":\"7.0.2\",\"deviceId\":\"DEVICE#mac00dbda57f973\",\"combinedDeviceId\":\"00db11d44a68_010138020814576\",\"deviceCheckChannel\":\"\",\"deviceType\":17,\"model\":\"SM-S9210\",\"os\":\"Android\",\"osversion\":\"9\",\"mac\":\"00:db:11:d4:4a:68\"}", "serverid": 1195, "userid": "v2jodo#2835376"}]
      ```

### Packet 003 — `3.bin` — DOWN server → client

- **Timestamp ms**: `1780601518303`
- **TCP chunk length**: `75` bytes
- **Frame(s)**: `004`
  - **Frame 004**
    - Header: `a5b7588200004b000e40100000000000`
    - Total length: `75` bytes; codec: `plain`; format: `json_response`
    - Func: `LoginResult`
    - Nội dung decoded:
      ```json
      [{"func": "LoginResult", "session_key": "02D1B0135ABCDC0D"}]
      ```

### Packet 004 — `4.bin` — UP client → server

- **Timestamp ms**: `1780601518332`
- **TCP chunk length**: `16` bytes
- **Frame(s)**: `005`
  - **Frame 005**
    - Header: `b853646c000010140000000000000001`
    - Total length: `16` bytes; codec: `plain`; format: `empty_control`
    - Func: `—`
    - Nội dung decoded:
      ```json
      ""
      ```

### Packet 005 — `5.bin` — DOWN server → client

- **Timestamp ms**: `1780601518358`
- **TCP chunk length**: `16` bytes
- **Frame(s)**: `006`
  - **Frame 006**
    - Header: `7f11aa23000010150e4010000000340d`
    - Total length: `16` bytes; codec: `plain`; format: `empty_control`
    - Func: `—`
    - Nội dung decoded:
      ```json
      ""
      ```

### Packet 006 — `6.bin` — UP client → server

- **Timestamp ms**: `1780601518391`
- **TCP chunk length**: `153` bytes
- **Frame(s)**: `007`
  - **Frame 007**
    - Header: `6ca96b6c000099000000000000000002`
    - Total length: `153` bytes; codec: `plain`; format: `urlencoded_request`
    - Func: `QueryAvatarAttribute`
    - Query fields: `{"bv": "7.0.2", "seq": "2", "session": "02D1B0135ABCDC0D", "sptype": "spv2jodo", "version": "7.0.2"}`
    - Nội dung decoded:
      ```json
      [{"func": "QueryAvatarAttribute"}]
      ```

### Packet 007 — `7.bin` — DOWN server → client

- **Timestamp ms**: `1780601518420`
- **TCP chunk length**: `430` bytes
- **Frame(s)**: `008`
  - **Frame 008**
    - Header: `881aa0340001ae000e40100000000002`
    - Total length: `430` bytes; codec: `plain`; format: `json_response`
    - Func: `QueryAvatarAttributeResult`
    - Nội dung decoded:
      ```json
      [{"attribute": {"ChengHao_ID": 0, "JingLing_ID": 0, "TuXiang_ID": 0, "avatarName": "", "city": 0, "coins": [], "createTime": 0, "desc": "", "exp": 0, "fighting": 0, "figureID": 0, "gender": 0, "guildID": 0, "guildName": "", "guildRank": 0, "headFrame": 0, "level": 0, "masterExp": 0, "masterLevel": 0, "mountEquip": [], "mount_ID": 0, "pet_ID": 0, "pos": 0, "rid": 0, "rotom_ID": 0, "vipLevel": 0}, "avatarid": "", "error_code": 1, "func": "QueryAvatarAttributeResult"}]
      ```

### Packet 008 — `8.bin` — UP client → server

- **Timestamp ms**: `1780601518652`
- **TCP chunk length**: `148` bytes
- **Frame(s)**: `009`
  - **Frame 009**
    - Header: `b2167f02000094000000000000000003`
    - Total length: `148` bytes; codec: `plain`; format: `urlencoded_request`
    - Func: `QueryChargeInfo`
    - Query fields: `{"bv": "7.0.2", "seq": "3", "session": "02D1B0135ABCDC0D", "sptype": "spv2jodo", "version": "7.0.2"}`
    - Nội dung decoded:
      ```json
      [{"func": "QueryChargeInfo"}]
      ```

### Packet 009 — `9.bin` — UP client → server

- **Timestamp ms**: `1780601524147`
- **TCP chunk length**: `226` bytes
- **Frame(s)**: `010`
  - **Frame 010**
    - Header: `24c39b190000e2000000000000000004`
    - Total length: `226` bytes; codec: `plain`; format: `urlencoded_request`
    - Func: `CreateAvatar`
    - Query fields: `{"bv": "7.0.2", "seq": "4", "session": "02D1B0135ABCDC0D", "sptype": "spv2jodo", "version": "7.0.2"}`
    - Nội dung decoded:
      ```json
      [{"avatarName": "BeetBoij", "chiefBuddy": 1002, "func": "CreateAvatar", "gender": 0}]
      ```

### Packet 010 — `10.bin` — DOWN server → client

- **Timestamp ms**: `1780601524190`
- **TCP chunk length**: `350` bytes
- **Frame(s)**: `011, 012`
  - **Frame 011**
    - Header: `5671274c000066000e40100000000004`
    - Total length: `102` bytes; codec: `plain`; format: `json_response`
    - Func: `QueryOAProgressResult`
    - Nội dung decoded:
      ```json
      [{"func": "QueryOAProgressResult", "ids": [{"id": 66, "progress": 0, "progressList": [0]}]}]
      ```
  - **Frame 012**
    - Header: `40835f2d0000f8000e40100000000004`
    - Total length: `248` bytes; codec: `plain`; format: `json_response`
    - Func: `BattleTowerQueryResult`
    - Nội dung decoded:
      ```json
      [{"func": "BattleTowerQueryResult", "mode": 0, "petList": [], "status": {"awardPickId": 0, "buffList": [], "coin": 0, "curLevel": 0, "finishAwardList": [], "lootBuffBox": [], "maxLevel": 0, "opponentIndex": 0, "opponentList": [], "point": 0, "pointSum": 0}}]
      ```

### Packet 011 — `11.bin` — DOWN server → client

- **Timestamp ms**: `1780601524194`
- **TCP chunk length**: `64` bytes
- **Frame(s)**: `013`
  - **Frame 013**
    - Header: `0cd25da7000040000e40100000000004`
    - Total length: `64` bytes; codec: `plain`; format: `json_response`
    - Func: `CreateAvatarResult`
    - Nội dung decoded:
      ```json
      [{"error_code": 0, "func": "CreateAvatarResult"}]
      ```

### Packet 012 — `12.bin` — UP client → server

- **Timestamp ms**: `1780601524224`
- **TCP chunk length**: `153` bytes
- **Frame(s)**: `014`
  - **Frame 014**
    - Header: `27e2d294000099000000000000000005`
    - Total length: `153` bytes; codec: `plain`; format: `urlencoded_request`
    - Func: `QueryAvatarAttribute`
    - Query fields: `{"bv": "7.0.2", "seq": "5", "session": "02D1B0135ABCDC0D", "sptype": "spv2jodo", "version": "7.0.2"}`
    - Nội dung decoded:
      ```json
      [{"func": "QueryAvatarAttribute"}]
      ```

### Packet 013 — `13.bin` — DOWN server → client

- **Timestamp ms**: `1780601524251`
- **TCP chunk length**: `757` bytes
- **Frame(s)**: `015, 016, 017, 018`
  - **Frame 015**
    - Header: `eb1c28bb00003a000e40100000000005`
    - Total length: `58` bytes; codec: `plain`; format: `json_response`
    - Func: `UpdateHuiZhang`
    - Nội dung decoded:
      ```json
      [{"func": "UpdateHuiZhang", "huiZhang": 0}]
      ```
  - **Frame 016**
    - Header: `2bd029a7000049000e40100000000005`
    - Total length: `73` bytes; codec: `plain`; format: `json_response`
    - Func: `InitLastStartTime`
    - Nội dung decoded:
      ```json
      [{"func": "InitLastStartTime", "times": [0], "types": [12]}]
      ```
  - **Frame 017**
    - Header: `034865b2000046000e40100000000005`
    - Total length: `70` bytes; codec: `plain`; format: `json_response`
    - Func: `UpdatePetLinkInfo`
    - Nội dung decoded:
      ```json
      [{"func": "UpdatePetLinkInfo", "info": [], "mix": false}]
      ```
  - **Frame 018**
    - Header: `a8d8c87d00022c000e40100000000005`
    - Total length: `556` bytes; codec: `plain`; format: `json_response`
    - Func: `QueryAvatarAttributeResult`
    - Nội dung decoded:
      ```json
      [{"attribute": {"ChengHao_ID": 0, "JingLing_ID": 0, "TuXiang_ID": 1002, "avatarName": "BeetBoij", "city": 0, "coins": [0, 0, 0, 0, 0, 0, 60, 0, 0, 0, 10, 0, 20, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10, 0], "createTime": 1780601520, "desc": "", "exp": 0, "fighting": 0, "figureID": 1002, "gender": 0, "guildID": 0, "guildName": "", "guildRank": 0, "headFrame": 0, "level": 1, "masterExp": 0, "masterLevel": 0, "mountEquip": [], "mount_ID": 0, "pet_ID": 0, "pos": 0, "rid": 195132877, "rotom_ID": 0, "vipLevel": 0}, "avatarid": "f25f2e5d-5ff3-4a83-89d5-4d259303f4bd", "error_code": 0, "func": "QueryAvatarAttributeResult"}]
      ```

### Packet 014 — `14.bin` — UP client → server

- **Timestamp ms**: `1780601524282`
- **TCP chunk length**: `176` bytes
- **Frame(s)**: `019`
  - **Frame 019**
    - Header: `b0b4c25e0000b0000000000000000006`
    - Total length: `176` bytes; codec: `plain`; format: `urlencoded_request`
    - Func: `UpdateGuide`
    - Query fields: `{"bv": "7.0.2", "seq": "6", "session": "02D1B0135ABCDC0D", "sptype": "spv2jodo", "version": "7.0.2"}`
    - Nội dung decoded:
      ```json
      [{"func": "UpdateGuide", "id": 1, "step": 0}]
      ```

### Packet 015 — `15.bin` — DOWN server → client

- **Timestamp ms**: `1780601524308`
- **TCP chunk length**: `63` bytes
- **Frame(s)**: `020`
  - **Frame 020**
    - Header: `fb65cbce00003f000e40100000000006`
    - Total length: `63` bytes; codec: `plain`; format: `json_response`
    - Func: `UpdateGuideResult`
    - Nội dung decoded:
      ```json
      [{"error_code": 0, "func": "UpdateGuideResult"}]
      ```

### Packet 016 — `16.bin` — UP client → server

- **Timestamp ms**: `1780601524338`
- **TCP chunk length**: `162` bytes
- **Frame(s)**: `021`
  - **Frame 021**
    - Header: `ac854aa10000a2000000000000000007`
    - Total length: `162` bytes; codec: `plain`; format: `urlencoded_request`
    - Func: `HeartBeat`
    - Query fields: `{"bv": "7.0.2", "seq": "7", "session": "02D1B0135ABCDC0D", "sptype": "spv2jodo", "version": "7.0.2"}`
    - Nội dung decoded:
      ```json
      [{"func": "HeartBeat", "time": 0}]
      ```

### Packet 017 — `17.bin` — DOWN server → client

- **Timestamp ms**: `1780601524365`
- **TCP chunk length**: `694` bytes
- **Frame(s)**: `022, 023`
  - **Frame 022**
    - Header: `54d43c3c00004f000e40100000000007`
    - Total length: `79` bytes; codec: `plain`; format: `json_response`
    - Func: `HeartBeatResult`
    - Nội dung decoded:
      ```json
      [{"error_code": 0, "func": "HeartBeatResult", "time": 1780601520}]
      ```
  - **Frame 023**
    - Header: `41c17945000267000e40100000000007`
    - Total length: `615` bytes; codec: `plain`; format: `json_response`
    - Func: `NotifyChatUpdate`
    - Nội dung decoded:
      ```json
      [{"func": "NotifyChatUpdate", "isPrivateUpdate": 0, "msgs": [{"channel": 1, "content": "<I:UI_HT_chongwutujian.chongwutujian:bq11.png:31:28>", "keepTime": 0, "receiver": "", "receiverName": "", "receiverRid": 0, "sender": "f2b8b789-3f46-448c-b281-556aa6e98c93", "senderName": "Kun⚘kẩu", "senderRid": 0, "senderVIP": 12, "seq": 1380, "time": 1780575116}, {"channel": 1, "content": "<I:UI_HT_chongwutujian.chongwutujian:bq03.png:31:28>", "keepTime": 0, "receiver": "", "receiverName": "", "receiverRid": 0, "sender": "fb7681ca-82c0-4107-a6b5-7718825f9528", "senderName": "Clawn", "senderRid": 0, "senderVIP": 2, "seq": 1379, "time": 1780575018}]}]
      ```

### Packet 018 — `18.bin` — UP client → server

- **Timestamp ms**: `1780601524389`
- **TCP chunk length**: `153` bytes
- **Frame(s)**: `024`
  - **Frame 024**
    - Header: `8ceaee37000099000000000000000008`
    - Total length: `153` bytes; codec: `plain`; format: `urlencoded_request`
    - Func: `QueryAllChargeConfig`
    - Query fields: `{"bv": "7.0.2", "seq": "8", "session": "02D1B0135ABCDC0D", "sptype": "spv2jodo", "version": "7.0.2"}`
    - Nội dung decoded:
      ```json
      [{"func": "QueryAllChargeConfig"}]
      ```

### Packet 019 — `19.bin` — DOWN server → client

- **Timestamp ms**: `1780601524389`
- **TCP chunk length**: `192` bytes
- **Frame(s)**: `025`
  - **Frame 025**
    - Header: `4d4cbc8f0000c0000e40100000000007`
    - Total length: `192` bytes; codec: `plain`; format: `json_response`
    - Func: `Broadcast`
    - Nội dung decoded:
      ```json
      [{"broadChannel": 10, "func": "Broadcast", "msg": "<C:FFC080FF>Fanoking</C> monster [<C:66FFFBFF>Marill</C>] successfully evolve to [<C:66FFFBFF>Azumarill</C>],congratulation!!"}]
      ```

### Packet 020 — `20.bin` — DOWN server → client

- **Timestamp ms**: `1780601524427`
- **TCP chunk length**: `908` bytes
- **Frame(s)**: `026`
  - **Frame 026**
    - Header: `77a5617400038c010e40100000000008`
    - Total length: `908` bytes; codec: `zlib`; format: `json_response`
    - Func: `QueryAllChargeConfigResult`
    - Nội dung decoded:
      ```json
      [{"chargeList": [{"AdditionalDesc": "120 diamonds daily（30days）", "AdditionalYuanbao": 0, "BuyPrice": 499, "ChargeRank": 2, "ChargeType": 1, "CurrencyType": "RMB", "Desc": "300 Diamonds M-Giftpack", "DoubleDesc": "", "DoubleFirst": false, "DoubleRate": 1.0, "FirstDesc": "", "GainYuanbao": 300, "Icon": "UI_HT_VIP1.VIP1/icon_yueka.png", "MonthCardBenefit": 120, "MonthCardTime": 30, "PriceDesc": "4.99", "PriceID": 1, "RechargeDayTime": 0, "RechargeWeekTime": 0, "ShowYuanbao": 300, "VipAstrict": 0, "itemID": 1}, {"AdditionalDesc": "", "AdditionalYuanbao": 0, "BuyPrice": 99, "ChargeRank": 3, "ChargeType": 2, "CurrencyType": "RMB", "Desc": "60 Diamonds", "DoubleDesc": "无", "DoubleFirst": true, "DoubleRate": 2.0, "FirstDesc": "", "GainYuanbao": 60, "Icon": "UI_HT_VIP1.VIP1/icon_zuanshi.png", "MonthCardBenefit": 0, "MonthCardTime": 0, "PriceDesc": "0.99", "PriceID": 2, "RechargeDayTime": 3, "RechargeWeekTime": 0, "ShowYuanbao": 60, "VipAstrict": 0, "itemID": 2}, {"AdditionalDesc": "Additional 1,200 free diamonds", "AdditionalYuanbao": 1200, "BuyPrice": 9999, "ChargeRank": 8, "ChargeType": 2, "CurrencyType": "RMB", "Desc": "6,480 Diamonds", "DoubleDesc": "无", "DoubleFirst": true, "DoubleRate": 2.0, "FirstDesc": "", "GainYuanbao": 6480, "Icon": "UI_HT_VIP1.VIP1/icon_zuanshimuxiang.png", "MonthCardBenefit": 0, "MonthCardTime": 0, "PriceDesc": "99.99", "PriceID": 3, "RechargeDayTime": 0, "RechargeWeekTime": 1, "ShowYuanbao": 6480, "VipAstrict": 0, "itemID": 3}, {"AdditionalDesc": "Additional 500 free diamonds", "AdditionalYuanbao": 500, "BuyPrice": 4999, "ChargeRank": 7, "ChargeType": 2, "CurrencyType": "RMB", "Desc": "3,280 Diamonds", "DoubleDesc": "无", "DoubleFirst": true, "DoubleRate": 2.0, "FirstDesc": "", "GainYuanbao": 3280, "Icon": "UI_HT_VIP1.VIP1/icon_zuanshibao.png", "Mon... <truncated; see decoded/decoded_packets.json for full payload>
      ```

### Packet 021 — `21.bin` — UP client → server

- **Timestamp ms**: `1780601524460`
- **TCP chunk length**: `148` bytes
- **Frame(s)**: `027`
  - **Frame 027**
    - Header: `9e638116000094000000000000000009`
    - Total length: `148` bytes; codec: `plain`; format: `urlencoded_request`
    - Func: `GetChengHaoList`
    - Query fields: `{"bv": "7.0.2", "seq": "9", "session": "02D1B0135ABCDC0D", "sptype": "spv2jodo", "version": "7.0.2"}`
    - Nội dung decoded:
      ```json
      [{"func": "GetChengHaoList"}]
      ```

### Packet 022 — `22.bin` — DOWN server → client

- **Timestamp ms**: `1780601524485`
- **TCP chunk length**: `64` bytes
- **Frame(s)**: `028`
  - **Frame 028**
    - Header: `8a417e75000040000e40100000000009`
    - Total length: `64` bytes; codec: `plain`; format: `json_response`
    - Func: `GetChengHaoListResult`
    - Nội dung decoded:
      ```json
      [{"chList": [], "func": "GetChengHaoListResult"}]
      ```

### Packet 023 — `23.bin` — UP client → server

- **Timestamp ms**: `1780601524513`
- **TCP chunk length**: `149` bytes
- **Frame(s)**: `029`
  - **Frame 029**
    - Header: `77ae0bed00009500000000000000000a`
    - Total length: `149` bytes; codec: `plain`; format: `urlencoded_request`
    - Func: `GetHuiZhangList`
    - Query fields: `{"bv": "7.0.2", "seq": "10", "session": "02D1B0135ABCDC0D", "sptype": "spv2jodo", "version": "7.0.2"}`
    - Nội dung decoded:
      ```json
      [{"func": "GetHuiZhangList"}]
      ```

### Packet 024 — `24.bin` — DOWN server → client

- **Timestamp ms**: `1780601524538`
- **TCP chunk length**: `70` bytes
- **Frame(s)**: `030`
  - **Frame 030**
    - Header: `9d1675b9000046000e4010000000000a`
    - Total length: `70` bytes; codec: `plain`; format: `json_response`
    - Func: `GetHuiZhangListResult`
    - Nội dung decoded:
      ```json
      [{"func": "GetHuiZhangListResult", "huiZhangList": []}]
      ```

### Packet 025 — `25.bin` — UP client → server

- **Timestamp ms**: `1780601524568`
- **TCP chunk length**: `151` bytes
- **Frame(s)**: `031`
  - **Frame 031**
    - Header: `ca8d06c700009700000000000000000b`
    - Total length: `151` bytes; codec: `plain`; format: `urlencoded_request`
    - Func: `QueryJingLingInfo`
    - Query fields: `{"bv": "7.0.2", "seq": "11", "session": "02D1B0135ABCDC0D", "sptype": "spv2jodo", "version": "7.0.2"}`
    - Nội dung decoded:
      ```json
      [{"func": "QueryJingLingInfo"}]
      ```

### Packet 026 — `26.bin` — DOWN server → client

- **Timestamp ms**: `1780601524595`
- **TCP chunk length**: `120` bytes
- **Frame(s)**: `032`
  - **Frame 032**
    - Header: `18189c91000078000e4010000000000b`
    - Total length: `120` bytes; codec: `plain`; format: `json_response`
    - Func: `QueryJingLingInfoResult`
    - Nội dung decoded:
      ```json
      [{"CoinJingLingNum": 0, "Exp": 0, "JingLingID": 0, "LastTime": 0, "Level": 0, "func": "QueryJingLingInfoResult"}]
      ```

### Packet 027 — `27.bin` — UP client → server

- **Timestamp ms**: `1780601524621`
- **TCP chunk length**: `148` bytes
- **Frame(s)**: `033`
  - **Frame 033**
    - Header: `1898146300009400000000000000000c`
    - Total length: `148` bytes; codec: `plain`; format: `urlencoded_request`
    - Func: `QueryZuoQiList`
    - Query fields: `{"bv": "7.0.2", "seq": "12", "session": "02D1B0135ABCDC0D", "sptype": "spv2jodo", "version": "7.0.2"}`
    - Nội dung decoded:
      ```json
      [{"func": "QueryZuoQiList"}]
      ```

### Packet 028 — `28.bin` — DOWN server → client

- **Timestamp ms**: `1780601524647`
- **TCP chunk length**: `66` bytes
- **Frame(s)**: `034`
  - **Frame 034**
    - Header: `2c09d780000042000e4010000000000c`
    - Total length: `66` bytes; codec: `plain`; format: `json_response`
    - Func: `QueryZuoQiListResult`
    - Nội dung decoded:
      ```json
      [{"ZuoQiList": [], "func": "QueryZuoQiListResult"}]
      ```

### Packet 029 — `29.bin` — UP client → server

- **Timestamp ms**: `1780601524672`
- **TCP chunk length**: `166` bytes
- **Frame(s)**: `035`
  - **Frame 035**
    - Header: `01a023870000a600000000000000000d`
    - Total length: `166` bytes; codec: `plain`; format: `urlencoded_request`
    - Func: `ZuoQiEquipQuery`
    - Query fields: `{"bv": "7.0.2", "seq": "13", "session": "02D1B0135ABCDC0D", "sptype": "spv2jodo", "version": "7.0.2"}`
    - Nội dung decoded:
      ```json
      [{"func": "ZuoQiEquipQuery", "zqId": 0}]
      ```

### Packet 030 — `30.bin` — DOWN server → client

- **Timestamp ms**: `1780601524698`
- **TCP chunk length**: `63` bytes
- **Frame(s)**: `036`
  - **Frame 036**
    - Header: `9150e75f00003f000e4010000000000d`
    - Total length: `63` bytes; codec: `plain`; format: `json_response`
    - Func: `ZuoQiEquipQueryResult`
    - Nội dung decoded:
      ```json
      [{"equip": [], "func": "ZuoQiEquipQueryResult"}]
      ```

### Packet 031 — `31.bin` — UP client → server

- **Timestamp ms**: `1780601524725`
- **TCP chunk length**: `148` bytes
- **Frame(s)**: `037`
  - **Frame 037**
    - Header: `3d0ab55500009400000000000000000e`
    - Total length: `148` bytes; codec: `plain`; format: `urlencoded_request`
    - Func: `ZuoQiSkinQuery`
    - Query fields: `{"bv": "7.0.2", "seq": "14", "session": "02D1B0135ABCDC0D", "sptype": "spv2jodo", "version": "7.0.2"}`
    - Nội dung decoded:
      ```json
      [{"func": "ZuoQiSkinQuery"}]
      ```

### Packet 032 — `32.bin` — DOWN server → client

- **Timestamp ms**: `1780601524759`
- **TCP chunk length**: `65` bytes
- **Frame(s)**: `038`
  - **Frame 038**
    - Header: `bf2e230b000041000e4010000000000e`
    - Total length: `65` bytes; codec: `plain`; format: `json_response`
    - Func: `ZuoQiSkinQueryResult`
    - Nội dung decoded:
      ```json
      [{"func": "ZuoQiSkinQueryResult", "skinList": []}]
      ```

### Packet 033 — `33.bin` — UP client → server

- **Timestamp ms**: `1780601524787`
- **TCP chunk length**: `152` bytes
- **Frame(s)**: `039`
  - **Frame 039**
    - Header: `a92dab7f00009800000000000000000f`
    - Total length: `152` bytes; codec: `plain`; format: `urlencoded_request`
    - Func: `QueryAllTalentInfo`
    - Query fields: `{"bv": "7.0.2", "seq": "15", "session": "02D1B0135ABCDC0D", "sptype": "spv2jodo", "version": "7.0.2"}`
    - Nội dung decoded:
      ```json
      [{"func": "QueryAllTalentInfo"}]
      ```

### Packet 034 — `34.bin` — DOWN server → client

- **Timestamp ms**: `1780601524813`
- **TCP chunk length**: `95` bytes
- **Frame(s)**: `040`
  - **Frame 040**
    - Header: `67598b6200005f000e4010000000000f`
    - Total length: `95` bytes; codec: `plain`; format: `json_response`
    - Func: `QueryAllTalentInfoResult`
    - Nội dung decoded:
      ```json
      [{"TalentList": [], "TreePutedPointList": [], "func": "QueryAllTalentInfoResult"}]
      ```

### Packet 035 — `35.bin` — UP client → server

- **Timestamp ms**: `1780601524837`
- **TCP chunk length**: `143` bytes
- **Frame(s)**: `041`
  - **Frame 041**
    - Header: `f8fd7e8000008f000000000000000010`
    - Total length: `143` bytes; codec: `plain`; format: `urlencoded_request`
    - Func: `DollQuery`
    - Query fields: `{"bv": "7.0.2", "seq": "16", "session": "02D1B0135ABCDC0D", "sptype": "spv2jodo", "version": "7.0.2"}`
    - Nội dung decoded:
      ```json
      [{"func": "DollQuery"}]
      ```

### Packet 036 — `36.bin` — DOWN server → client

- **Timestamp ms**: `1780601524864`
- **TCP chunk length**: `82` bytes
- **Frame(s)**: `042`
  - **Frame 042**
    - Header: `8538900e000052000e40100000000010`
    - Total length: `82` bytes; codec: `plain`; format: `json_response`
    - Func: `DollQueryResult`
    - Nội dung decoded:
      ```json
      [{"cur": {"cId": 0, "name": ""}, "func": "DollQueryResult", "list": []}]
      ```

### Packet 037 — `37.bin` — UP client → server

- **Timestamp ms**: `1780601524893`
- **TCP chunk length**: `146` bytes
- **Frame(s)**: `043`
  - **Frame 043**
    - Header: `21cfd21a000092000000000000000011`
    - Total length: `146` bytes; codec: `plain`; format: `urlencoded_request`
    - Func: `QueryPetList`
    - Query fields: `{"bv": "7.0.2", "seq": "17", "session": "02D1B0135ABCDC0D", "sptype": "spv2jodo", "version": "7.0.2"}`
    - Nội dung decoded:
      ```json
      [{"func": "QueryPetList"}]
      ```

### Packet 038 — `38.bin` — DOWN server → client

- **Timestamp ms**: `1780601524922`
- **TCP chunk length**: `62` bytes
- **Frame(s)**: `044`
  - **Frame 044**
    - Header: `2fb4a40c00003e000e40100000000011`
    - Total length: `62` bytes; codec: `plain`; format: `json_response`
    - Func: `QueryPetListResult`
    - Nội dung decoded:
      ```json
      [{"PetList": [], "func": "QueryPetListResult"}]
      ```

### Packet 039 — `39.bin` — UP client → server

- **Timestamp ms**: `1780601524945`
- **TCP chunk length**: `152` bytes
- **Frame(s)**: `045`
  - **Frame 045**
    - Header: `378c7a2f000098000000000000000012`
    - Total length: `152` bytes; codec: `plain`; format: `urlencoded_request`
    - Func: `QueryDailyProgress`
    - Query fields: `{"bv": "7.0.2", "seq": "18", "session": "02D1B0135ABCDC0D", "sptype": "spv2jodo", "version": "7.0.2"}`
    - Nội dung decoded:
      ```json
      [{"func": "QueryDailyProgress"}]
      ```

### Packet 040 — `40.bin` — DOWN server → client

- **Timestamp ms**: `1780601524976`
- **TCP chunk length**: `74` bytes
- **Frame(s)**: `046`
  - **Frame 046**
    - Header: `5baa01eb00004a000e40100000000012`
    - Total length: `74` bytes; codec: `plain`; format: `json_response`
    - Func: `QueryDailyProgressResult`
    - Nội dung decoded:
      ```json
      [{"dailyProgress": [], "func": "QueryDailyProgressResult"}]
      ```

### Packet 041 — `41.bin` — UP client → server

- **Timestamp ms**: `1780601524998`
- **TCP chunk length**: `148` bytes
- **Frame(s)**: `047`
  - **Frame 047**
    - Header: `b080b6eb000094000000000000000013`
    - Total length: `148` bytes; codec: `plain`; format: `urlencoded_request`
    - Func: `ObjRecordQuery`
    - Query fields: `{"bv": "7.0.2", "seq": "19", "session": "02D1B0135ABCDC0D", "sptype": "spv2jodo", "version": "7.0.2"}`
    - Nội dung decoded:
      ```json
      [{"func": "ObjRecordQuery"}]
      ```

### Packet 042 — `42.bin` — DOWN server → client

- **Timestamp ms**: `1780601525024`
- **TCP chunk length**: `64` bytes
- **Frame(s)**: `048`
  - **Frame 048**
    - Header: `fa12d4cb000040000e40100000000013`
    - Total length: `64` bytes; codec: `plain`; format: `json_response`
    - Func: `ObjRecordQueryResult`
    - Nội dung decoded:
      ```json
      [{"func": "ObjRecordQueryResult", "objList": []}]
      ```

### Packet 043 — `43.bin` — UP client → server

- **Timestamp ms**: `1780601525053`
- **TCP chunk length**: `146` bytes
- **Frame(s)**: `049`
  - **Frame 049**
    - Header: `e8b16c61000092000000000000000014`
    - Total length: `146` bytes; codec: `plain`; format: `urlencoded_request`
    - Func: `QueryQianDao`
    - Query fields: `{"bv": "7.0.2", "seq": "20", "session": "02D1B0135ABCDC0D", "sptype": "spv2jodo", "version": "7.0.2"}`
    - Nội dung decoded:
      ```json
      [{"func": "QueryQianDao"}]
      ```

### Packet 044 — `44.bin` — DOWN server → client

- **Timestamp ms**: `1780601525083`
- **TCP chunk length**: `405` bytes
- **Frame(s)**: `050`
  - **Frame 050**
    - Header: `4555f24e000195010e40100000000014`
    - Total length: `405` bytes; codec: `zlib`; format: `json_response`
    - Func: `QueryQianDaoResult`
    - Nội dung decoded:
      ```json
      [{"accum": 0, "data": [{"ItemID": 1, "RewardType": 1, "VipDouble": 4, "count": 150, "id": 610}, {"ItemID": 70025, "RewardType": 0, "VipDouble": 0, "count": 3, "id": 611}, {"ItemID": 79001, "RewardType": 0, "VipDouble": 3, "count": 3, "id": 608}, {"ItemID": 70005, "RewardType": 0, "VipDouble": 0, "count": 2, "id": 609}, {"ItemID": 80262, "RewardType": 0, "VipDouble": 4, "count": 5, "id": 614}, {"ItemID": 14001, "RewardType": 0, "VipDouble": 0, "count": 10, "id": 615}, {"ItemID": 79001, "RewardType": 0, "VipDouble": 3, "count": 6, "id": 612}, {"ItemID": 70027, "RewardType": 0, "VipDouble": 0, "count": 5, "id": 613}, {"ItemID": 1, "RewardType": 1, "VipDouble": 5, "count": 150, "id": 618}, {"ItemID": 12004, "RewardType": 0, "VipDouble": 0, "count": 2, "id": 619}, {"ItemID": 80116, "RewardType": 0, "VipDouble": 3, "count": 3, "id": 616}, {"ItemID": 80198, "RewardType": 0, "VipDouble": 0, "count": 5, "id": 617}, {"ItemID": 1, "RewardType": 1, "VipDouble": 6, "count": 200, "id": 622}, {"ItemID": 70027, "RewardType": 0, "VipDouble": 0, "count": 5, "id": 623}, {"ItemID": 70010, "RewardType": 0, "VipDouble": 4, "count": 5, "id": 620}, {"ItemID": 70005, "RewardType": 0, "VipDouble": 0, "count": 2, "id": 621}, {"ItemID": 70026, "RewardType": 0, "VipDouble": 0, "count": 10, "id": 627}, {"ItemID": 1, "RewardType": 1, "VipDouble": 7, "count": 300, "id": 626}, {"ItemID": 70005, "RewardType": 0, "VipDouble": 0, "count": 2, "id": 625}, {"ItemID": 79001, "RewardType": 0, "VipDouble": 8, "count": 8, "id": 624}, {"ItemID": 12005, "RewardType": 0, "VipDouble": 0, "count": 1, "id": 631}, {"ItemID": 79001, "RewardType": 0, "VipDouble": 8, "count": 10, "id": 630}, {"ItemID": 70032, "RewardType": 0, "VipDouble": 0, "count": 1, "id": 629}, {"ItemID": 80262, "RewardType": 0, "VipDouble": 5, "count... <truncated; see decoded/decoded_packets.json for full payload>
      ```

### Packet 045 — `45.bin` — UP client → server

- **Timestamp ms**: `1780601525106`
- **TCP chunk length**: `146` bytes
- **Frame(s)**: `051`
  - **Frame 051**
    - Header: `905c84f3000092000000000000000015`
    - Total length: `146` bytes; codec: `plain`; format: `urlencoded_request`
    - Func: `LotteryQuery`
    - Query fields: `{"bv": "7.0.2", "seq": "21", "session": "02D1B0135ABCDC0D", "sptype": "spv2jodo", "version": "7.0.2"}`
    - Nội dung decoded:
      ```json
      [{"func": "LotteryQuery"}]
      ```

### Packet 046 — `46.bin` — DOWN server → client

- **Timestamp ms**: `1780601525132`
- **TCP chunk length**: `113` bytes
- **Frame(s)**: `052`
  - **Frame 052**
    - Header: `ca47ccfe000071000e40100000000015`
    - Total length: `113` bytes; codec: `plain`; format: `json_response`
    - Func: `LotteryQueryResult`
    - Nội dung decoded:
      ```json
      [{"func": "LotteryQueryResult", "lotteryList": [], "point": 0, "pointAwardList": [], "totalConsume": 0}]
      ```

### Packet 047 — `47.bin` — UP client → server

- **Timestamp ms**: `1780601525160`
- **TCP chunk length**: `151` bytes
- **Frame(s)**: `053`
  - **Frame 053**
    - Header: `d5d230b7000097000000000000000016`
    - Total length: `151` bytes; codec: `plain`; format: `urlencoded_request`
    - Func: `QueryBattleRecord`
    - Query fields: `{"bv": "7.0.2", "seq": "22", "session": "02D1B0135ABCDC0D", "sptype": "spv2jodo", "version": "7.0.2"}`
    - Nội dung decoded:
      ```json
      [{"func": "QueryBattleRecord"}]
      ```

### Packet 048 — `48.bin` — DOWN server → client

- **Timestamp ms**: `1780601525186`
- **TCP chunk length**: `128` bytes
- **Frame(s)**: `054`
  - **Frame 054**
    - Header: `d8036894000080000e40100000000016`
    - Total length: `128` bytes; codec: `plain`; format: `json_response`
    - Func: `QueryBattleRecordResult`
    - Nội dung decoded:
      ```json
      [{"battleRecord": {"chapterAward": [], "levelDailyStats": {}, "levelRecords": {}}, "func": "QueryBattleRecordResult"}]
      ```

### Packet 049 — `49.bin` — UP client → server

- **Timestamp ms**: `1780601525208`
- **TCP chunk length**: `143` bytes
- **Frame(s)**: `055`
  - **Frame 055**
    - Header: `f22c435c00008f000000000000000017`
    - Total length: `143` bytes; codec: `plain`; format: `urlencoded_request`
    - Func: `TaskQuery`
    - Query fields: `{"bv": "7.0.2", "seq": "23", "session": "02D1B0135ABCDC0D", "sptype": "spv2jodo", "version": "7.0.2"}`
    - Nội dung decoded:
      ```json
      [{"func": "TaskQuery"}]
      ```

### Packet 050 — `50.bin` — DOWN server → client

- **Timestamp ms**: `1780601525234`
- **TCP chunk length**: `146` bytes
- **Frame(s)**: `056`
  - **Frame 056**
    - Header: `a70a20de000092000e40100000000017`
    - Total length: `146` bytes; codec: `plain`; format: `json_response`
    - Func: `TaskQueryResult`
    - Nội dung decoded:
      ```json
      [{"func": "TaskQueryResult", "taskInfo": {"acceptedList": [], "finishedDailyList": [], "finishedList": [], "loopCount": 0, "loopIndex": 1}}]
      ```

### Packet 051 — `51.bin` — UP client → server

- **Timestamp ms**: `1780601525258`
- **TCP chunk length**: `150` bytes
- **Frame(s)**: `057`
  - **Frame 057**
    - Header: `4bf18e56000096000000000000000018`
    - Total length: `150` bytes; codec: `plain`; format: `urlencoded_request`
    - Func: `QueryGuideRecord`
    - Query fields: `{"bv": "7.0.2", "seq": "24", "session": "02D1B0135ABCDC0D", "sptype": "spv2jodo", "version": "7.0.2"}`
    - Nội dung decoded:
      ```json
      [{"func": "QueryGuideRecord"}]
      ```

### Packet 052 — `52.bin` — DOWN server → client

- **Timestamp ms**: `1780601525286`
- **TCP chunk length**: `109` bytes
- **Frame(s)**: `058`
  - **Frame 058**
    - Header: `b6ef803b00006d000e40100000000018`
    - Total length: `109` bytes; codec: `plain`; format: `json_response`
    - Func: `QueryGuideRecordResult`
    - Nội dung decoded:
      ```json
      [{"func": "QueryGuideRecordResult", "record": {"finished": [], "progress": [{"id": 1, "step": 0}]}}]
      ```

### Packet 053 — `53.bin` — UP client → server

- **Timestamp ms**: `1780601525309`
- **TCP chunk length**: `145` bytes
- **Frame(s)**: `059`
  - **Frame 059**
    - Header: `452e9cf3000091000000000000000019`
    - Total length: `145` bytes; codec: `plain`; format: `urlencoded_request`
    - Func: `RibbonQuery`
    - Query fields: `{"bv": "7.0.2", "seq": "25", "session": "02D1B0135ABCDC0D", "sptype": "spv2jodo", "version": "7.0.2"}`
    - Nội dung decoded:
      ```json
      [{"func": "RibbonQuery"}]
      ```

### Packet 054 — `54.bin` — DOWN server → client

- **Timestamp ms**: `1780601525336`
- **TCP chunk length**: `95` bytes
- **Frame(s)**: `060`
  - **Frame 060**
    - Header: `6414167700005f000e40100000000019`
    - Total length: `95` bytes; codec: `plain`; format: `json_response`
    - Func: `RibbonQueryResult`
    - Nội dung decoded:
      ```json
      [{"func": "RibbonQueryResult", "objectInfo": {"bagBuyCount": 0}, "ribbonList": []}]
      ```

### Packet 055 — `55.bin` — UP client → server

- **Timestamp ms**: `1780601525365`
- **TCP chunk length**: `163` bytes
- **Frame(s)**: `061`
  - **Frame 061**
    - Header: `f4e9d4a00000a300000000000000001a`
    - Total length: `163` bytes; codec: `plain`; format: `urlencoded_request`
    - Func: `UpdateCity`
    - Query fields: `{"bv": "7.0.2", "seq": "26", "session": "02D1B0135ABCDC0D", "sptype": "spv2jodo", "version": "7.0.2"}`
    - Nội dung decoded:
      ```json
      [{"city": 201, "func": "UpdateCity"}]
      ```

### Packet 056 — `56.bin` — UP client → server

- **Timestamp ms**: `1780601525418`
- **TCP chunk length**: `145` bytes
- **Frame(s)**: `062`
  - **Frame 062**
    - Header: `c0f1a68400009100000000000000001b`
    - Total length: `145` bytes; codec: `plain`; format: `urlencoded_request`
    - Func: `QueryStatus`
    - Query fields: `{"bv": "7.0.2", "seq": "27", "session": "02D1B0135ABCDC0D", "sptype": "spv2jodo", "version": "7.0.2"}`
    - Nội dung decoded:
      ```json
      [{"func": "QueryStatus"}]
      ```

### Packet 057 — `57.bin` — UP client → server

- **Timestamp ms**: `1780601525470`
- **TCP chunk length**: `145` bytes
- **Frame(s)**: `063`
  - **Frame 063**
    - Header: `35ff421a00009100000000000000001c`
    - Total length: `145` bytes; codec: `plain`; format: `urlencoded_request`
    - Func: `GetTeamList`
    - Query fields: `{"bv": "7.0.2", "seq": "28", "session": "02D1B0135ABCDC0D", "sptype": "spv2jodo", "version": "7.0.2"}`
    - Nội dung decoded:
      ```json
      [{"func": "GetTeamList"}]
      ```

### Packet 058 — `58.bin` — UP client → server

- **Timestamp ms**: `1780601525531`
- **TCP chunk length**: `146` bytes
- **Frame(s)**: `064`
  - **Frame 064**
    - Header: `5a3fd55400009200000000000000001d`
    - Total length: `146` bytes; codec: `plain`; format: `urlencoded_request`
    - Func: `QueryMailBox`
    - Query fields: `{"bv": "7.0.2", "seq": "29", "session": "02D1B0135ABCDC0D", "sptype": "spv2jodo", "version": "7.0.2"}`
    - Nội dung decoded:
      ```json
      [{"func": "QueryMailBox"}]
      ```

### Packet 059 — `59.bin` — UP client → server

- **Timestamp ms**: `1780601525567`
- **TCP chunk length**: `149` bytes
- **Frame(s)**: `065`
  - **Frame 065**
    - Header: `a44e6f2800009500000000000000001e`
    - Total length: `149` bytes; codec: `plain`; format: `urlencoded_request`
    - Func: `QueryChargeInfo`
    - Query fields: `{"bv": "7.0.2", "seq": "30", "session": "02D1B0135ABCDC0D", "sptype": "spv2jodo", "version": "7.0.2"}`
    - Nội dung decoded:
      ```json
      [{"func": "QueryChargeInfo"}]
      ```

### Packet 060 — `60.bin` — DOWN server → client

- **Timestamp ms**: `1780601525589`
- **TCP chunk length**: `246` bytes
- **Frame(s)**: `066, 067, 068`
  - **Frame 066**
    - Header: `06d2af5c00007b000e4010000000001b`
    - Total length: `123` bytes; codec: `plain`; format: `json_response`
    - Func: `QueryStatusResult`
    - Nội dung decoded:
      ```json
      [{"awardList": [], "cd": 0, "func": "QueryStatusResult", "inspireInfoa": [], "petCurInfos": [], "score": 0, "win": 0}]
      ```
  - **Frame 067**
    - Header: `f3f58de900003f000e4010000000001c`
    - Total length: `63` bytes; codec: `plain`; format: `json_response`
    - Func: `GetTeamListResult`
    - Nội dung decoded:
      ```json
      [{"TeamInfos": [], "func": "GetTeamListResult"}]
      ```
  - **Frame 068**
    - Header: `402ac6c200003c000e4010000000001d`
    - Total length: `60` bytes; codec: `plain`; format: `json_response`
    - Func: `QueryMailBoxResult`
    - Nội dung decoded:
      ```json
      [{"func": "QueryMailBoxResult", "mails": []}]
      ```

### Packet 061 — `61.bin` — DOWN server → client

- **Timestamp ms**: `1780601525615`
- **TCP chunk length**: `150` bytes
- **Frame(s)**: `069`
  - **Frame 069**
    - Header: `d5ae8223000096000e4010000000001e`
    - Total length: `150` bytes; codec: `plain`; format: `json_response`
    - Func: `QueryChargeInfoResult`
    - Nội dung decoded:
      ```json
      [{"func": "QueryChargeInfoResult", "info": {"charge": 0, "dailyCount": [], "history": [], "monthCardEnd": 0, "weeklyCount": [], "zhiZunCard": 0}}]
      ```

### Packet 062 — `62.bin` — UP client → server

- **Timestamp ms**: `1780601525617`
- **TCP chunk length**: `145` bytes
- **Frame(s)**: `070`
  - **Frame 070**
    - Header: `5362324f00009100000000000000001f`
    - Total length: `145` bytes; codec: `plain`; format: `urlencoded_request`
    - Func: `FriendQuery`
    - Query fields: `{"bv": "7.0.2", "seq": "31", "session": "02D1B0135ABCDC0D", "sptype": "spv2jodo", "version": "7.0.2"}`
    - Nội dung decoded:
      ```json
      [{"func": "FriendQuery"}]
      ```

### Packet 063 — `63.bin` — DOWN server → client

- **Timestamp ms**: `1780601525643`
- **TCP chunk length**: `79` bytes
- **Frame(s)**: `071`
  - **Frame 071**
    - Header: `beb21c3500004f000e4010000000001f`
    - Total length: `79` bytes; codec: `plain`; format: `json_response`
    - Func: `FriendQueryResult`
    - Nội dung decoded:
      ```json
      [{"applyList": [], "avatarList": [], "func": "FriendQueryResult"}]
      ```

### Packet 064 — `64.bin` — UP client → server

- **Timestamp ms**: `1780601525688`
- **TCP chunk length**: `150` bytes
- **Frame(s)**: `072`
  - **Frame 072**
    - Header: `93aad4ea000096000000000000000020`
    - Total length: `150` bytes; codec: `plain`; format: `urlencoded_request`
    - Func: `QueryAvatarItems`
    - Query fields: `{"bv": "7.0.2", "seq": "32", "session": "02D1B0135ABCDC0D", "sptype": "spv2jodo", "version": "7.0.2"}`
    - Nội dung decoded:
      ```json
      [{"func": "QueryAvatarItems"}]
      ```

### Packet 065 — `65.bin` — DOWN server → client

- **Timestamp ms**: `1780601525717`
- **TCP chunk length**: `63` bytes
- **Frame(s)**: `073`
  - **Frame 073**
    - Header: `81272d0300003f000e40100000000020`
    - Total length: `63` bytes; codec: `plain`; format: `json_response`
    - Func: `QueryAvatarItemResult`
    - Nội dung decoded:
      ```json
      [{"func": "QueryAvatarItemResult", "items": []}]
      ```

### Packet 066 — `66.bin` — UP client → server

- **Timestamp ms**: `1780601525740`
- **TCP chunk length**: `148` bytes
- **Frame(s)**: `074`
  - **Frame 074**
    - Header: `d534eed5000094000000000000000021`
    - Total length: `148` bytes; codec: `plain`; format: `urlencoded_request`
    - Func: `PVPStatusQuery`
    - Query fields: `{"bv": "7.0.2", "seq": "33", "session": "02D1B0135ABCDC0D", "sptype": "spv2jodo", "version": "7.0.2"}`
    - Nội dung decoded:
      ```json
      [{"func": "PVPStatusQuery"}]
      ```

### Packet 067 — `67.bin` — DOWN server → client

- **Timestamp ms**: `1780601525767`
- **TCP chunk length**: `712` bytes
- **Frame(s)**: `075`
  - **Frame 075**
    - Header: `49ecdf450002c8000e40100000000021`
    - Total length: `712` bytes; codec: `plain`; format: `json_response`
    - Func: `PVPStatusUpdate`
    - Nội dung decoded:
      ```json
      [{"func": "PVPStatusUpdate", "pvpStatus": {"defenderPet": {"paraList": [], "petIdList": [], "petList": []}, "pvpRanking": {"buyCount": 0, "comboWinMaxToday": 0, "fightCountLimit": 0, "fightTimeCommon": 0, "fightTimeMatch": 0, "rankingMax": 0}, "pvpShow": {"prestige": 0, "show": {"avatarID": "", "avatarName": "", "battlePoint": 0, "campId": 0, "chengHaoID": 0, "comboWin": 0, "comboWinMax": 0, "contentID": 0, "dollId": 0, "dollName": "", "fightCountTotal": 0, "fightCountWin": 0, "guild": "", "guildId": 0, "headFrame": 0, "lastActive": 0, "level": 0, "masterLevel": 0, "mountEquip": [], "mount_ID": 0, "petCount": 0, "petShowList": [], "pet_ID": 0, "ranking": 0, "rid": 0, "rotom_ID": 0, "spriteLevel": 0, "talk": "", "tuxiaongID": 0, "vip": 0}, "title": 0}, "worshipTarget": []}}]
      ```

### Packet 068 — `68.bin` — UP client → server

- **Timestamp ms**: `1780601525792`
- **TCP chunk length**: `148` bytes
- **Frame(s)**: `076`
  - **Frame 076**
    - Header: `0628a613000094000000000000000022`
    - Total length: `148` bytes; codec: `plain`; format: `urlencoded_request`
    - Func: `GetSoliderList`
    - Query fields: `{"bv": "7.0.2", "seq": "34", "session": "02D1B0135ABCDC0D", "sptype": "spv2jodo", "version": "7.0.2"}`
    - Nội dung decoded:
      ```json
      [{"func": "GetSoliderList"}]
      ```

### Packet 069 — `69.bin` — UP client → server

- **Timestamp ms**: `1780601525846`
- **TCP chunk length**: `159` bytes
- **Frame(s)**: `077`
  - **Frame 077**
    - Header: `ce5f2dbf00009f000000000000000023`
    - Total length: `159` bytes; codec: `plain`; format: `urlencoded_request`
    - Func: `QueryEmploySoliderHistory`
    - Query fields: `{"bv": "7.0.2", "seq": "35", "session": "02D1B0135ABCDC0D", "sptype": "spv2jodo", "version": "7.0.2"}`
    - Nội dung decoded:
      ```json
      [{"func": "QueryEmploySoliderHistory"}]
      ```

### Packet 070 — `70.bin` — DOWN server → client

- **Timestamp ms**: `1780601525873`
- **TCP chunk length**: `75` bytes
- **Frame(s)**: `078`
  - **Frame 078**
    - Header: `a6c0afd700004b000e40100000000023`
    - Total length: `75` bytes; codec: `plain`; format: `json_response`
    - Func: `QueryEmploySoliderHistoryResult`
    - Nội dung decoded:
      ```json
      [{"func": "QueryEmploySoliderHistoryResult", "history": []}]
      ```

### Packet 071 — `71.bin` — UP client → server

- **Timestamp ms**: `1780601525894`
- **TCP chunk length**: `151` bytes
- **Frame(s)**: `079`
  - **Frame 079**
    - Header: `c4a3fcc5000097000000000000000024`
    - Total length: `151` bytes; codec: `plain`; format: `urlencoded_request`
    - Func: `QueryTreasureCave`
    - Query fields: `{"bv": "7.0.2", "seq": "36", "session": "02D1B0135ABCDC0D", "sptype": "spv2jodo", "version": "7.0.2"}`
    - Nội dung decoded:
      ```json
      [{"func": "QueryTreasureCave"}]
      ```

### Packet 072 — `72.bin` — DOWN server → client

- **Timestamp ms**: `1780601525923`
- **TCP chunk length**: `122` bytes
- **Frame(s)**: `080`
  - **Frame 080**
    - Header: `17bf18c300007a000e40100000000024`
    - Total length: `122` bytes; codec: `plain`; format: `json_response`
    - Func: `QueryTreasureCaveResult`
    - Nội dung decoded:
      ```json
      [{"bossRank": 0, "bossTop": 0, "func": "QueryTreasureCaveResult", "lastChallengeTime": 0, "leftChallengeCnt": 2}]
      ```

### Packet 073 — `73.bin` — UP client → server

- **Timestamp ms**: `1780601525948`
- **TCP chunk length**: `156` bytes
- **Frame(s)**: `081`
  - **Frame 081**
    - Header: `b0b2185d00009c000000000000000025`
    - Total length: `156` bytes; codec: `plain`; format: `urlencoded_request`
    - Func: `QueryTreasureCaveAward`
    - Query fields: `{"bv": "7.0.2", "seq": "37", "session": "02D1B0135ABCDC0D", "sptype": "spv2jodo", "version": "7.0.2"}`
    - Nội dung decoded:
      ```json
      [{"func": "QueryTreasureCaveAward"}]
      ```

### Packet 074 — `74.bin` — DOWN server → client

- **Timestamp ms**: `1780601525975`
- **TCP chunk length**: `95` bytes
- **Frame(s)**: `082`
  - **Frame 082**
    - Header: `16f55ad000005f000e40100000000025`
    - Total length: `95` bytes; codec: `plain`; format: `json_response`
    - Func: `QueryTreasureCaveAwardResult`
    - Nội dung decoded:
      ```json
      [{"func": "QueryTreasureCaveAwardResult", "receivedAwards": [], "totalDamage": 0}]
      ```

### Packet 075 — `75.bin` — UP client → server

- **Timestamp ms**: `1780601526001`
- **TCP chunk length**: `151` bytes
- **Frame(s)**: `083`
  - **Frame 083**
    - Header: `34fe11f6000097000000000000000026`
    - Total length: `151` bytes; codec: `plain`; format: `urlencoded_request`
    - Func: `QueryVipLiBaoDraw`
    - Query fields: `{"bv": "7.0.2", "seq": "38", "session": "02D1B0135ABCDC0D", "sptype": "spv2jodo", "version": "7.0.2"}`
    - Nội dung decoded:
      ```json
      [{"func": "QueryVipLiBaoDraw"}]
      ```

### Packet 076 — `76.bin` — DOWN server → client

- **Timestamp ms**: `1780601526028`
- **TCP chunk length**: `65` bytes
- **Frame(s)**: `084`
  - **Frame 084**
    - Header: `7f16486c000041000e40100000000026`
    - Total length: `65` bytes; codec: `plain`; format: `json_response`
    - Func: `QueryVipLiBaoDrawResult`
    - Nội dung decoded:
      ```json
      [{"func": "QueryVipLiBaoDrawResult", "infos": []}]
      ```

### Packet 077 — `77.bin` — UP client → server

- **Timestamp ms**: `1780601526050`
- **TCP chunk length**: `149` bytes
- **Frame(s)**: `085`
  - **Frame 085**
    - Header: `54e3872f000095000000000000000027`
    - Total length: `149` bytes; codec: `plain`; format: `urlencoded_request`
    - Func: `GlobalBossQuery`
    - Query fields: `{"bv": "7.0.2", "seq": "39", "session": "02D1B0135ABCDC0D", "sptype": "spv2jodo", "version": "7.0.2"}`
    - Nội dung decoded:
      ```json
      [{"func": "GlobalBossQuery"}]
      ```

### Packet 078 — `78.bin` — DOWN server → client

- **Timestamp ms**: `1780601526077`
- **TCP chunk length**: `1460` bytes
- **Frame(s)**: `087`
  - **Frame 087**; spans segments `[78, 80]`
    - Header: `9a6321160005bc010e40100000000027`
    - Total length: `1468` bytes; codec: `zlib`; format: `json_response`
    - Func: `GlobalBossQueryResult`
    - Nội dung decoded:
      ```json
      [{"bossStatus": {"bossId": 990072, "damageList": [{"avatarID": "b19d03f0-6f6b-4fe8-a07a-e5cd70d60b33", "avatarName": "Isko", "battlePoint": 7999192, "campId": 1, "chengHaoID": 1023, "contentID": 2046, "damageTotal": 33755035, "dollId": 0, "dollName": "", "fightCount": 37, "fightTimeNext": 1780575849, "guild": "Stars", "guildId": 195125658, "headFrame": 4, "inspireCount": 10, "level": 84, "masterLevel": 0, "mountEquip": [], "mount_ID": 0, "petCount": 184, "petKilled": 0, "pet_ID": 21082, "ranking": 1, "rid": 195125409, "rotom_ID": 1001, "spriteLevel": 35, "talk": "", "tuxiaongID": 21572, "vip": 15}, {"avatarID": "07a68e7a-21ce-4387-a447-4ed2fb97f147", "avatarName": "Recycler", "battlePoint": 4579292, "campId": 1, "chengHaoID": 0, "contentID": 2045, "damageTotal": 15203154, "dollId": 0, "dollName": "", "fightCount": 20, "fightTimeNext": 1780575850, "guild": "SG⚘GĐ", "guildId": 195123642, "headFrame": 0, "inspireCount": 0, "level": 83, "masterLevel": 0, "mountEquip": [], "mount_ID": 7004, "petCount": 178, "petKilled": 0, "pet_ID": 1023522, "ranking": 2, "rid": 195123693, "rotom_ID": 1002, "spriteLevel": 34, "talk": "", "tuxiaongID": 2045, "vip": 14}, {"avatarID": "14fa5938-a9a4-4e99-9cb4-9738723cfcbe", "avatarName": "哈基咪", "battlePoint": 5144237, "campId": 1, "chengHaoID": 1029, "contentID": 2014, "damageTotal": 7197986, "dollId": 0, "dollName": "", "fightCount": 22, "fightTimeNext": 1780575804, "guild": "SG⚘GĐ", "guildId": 195123642, "headFrame": 13, "inspireCount": 0, "level": 80, "masterLevel": 0, "mountEquip": [{"id": 4, "value": 3}], "mount_ID": 7004, "petCount": 212, "petKilled": 0, "pet_ID": 1020592, "ranking": 3, "rid": 195123521, "rotom_ID": 0, "spriteLevel": 34, "talk": "", "tuxiaongID": 2014, "vip": 13}, {"avatarID": "8d413ef0-b103-4b88-bf45-db611d16219b", "avat... <truncated; see decoded/decoded_packets.json for full payload>
      ```

### Packet 079 — `79.bin` — UP client → server

- **Timestamp ms**: `1780601526105`
- **TCP chunk length**: `148` bytes
- **Frame(s)**: `086`
  - **Frame 086**
    - Header: `4c1645e8000094000000000000000028`
    - Total length: `148` bytes; codec: `plain`; format: `urlencoded_request`
    - Func: `GlobalPetQuery`
    - Query fields: `{"bv": "7.0.2", "seq": "40", "session": "02D1B0135ABCDC0D", "sptype": "spv2jodo", "version": "7.0.2"}`
    - Nội dung decoded:
      ```json
      [{"func": "GlobalPetQuery"}]
      ```

### Packet 080 — `80.bin` — DOWN server → client

- **Timestamp ms**: `1780601526105`
- **TCP chunk length**: `8` bytes
- **Frame(s)**: `087`
  - **Frame 087**; spans segments `[78, 80]`
    - Header: `9a6321160005bc010e40100000000027`
    - Total length: `1468` bytes; codec: `zlib`; format: `json_response`
    - Func: `GlobalBossQueryResult`
    - Nội dung decoded:
      ```json
      [{"bossStatus": {"bossId": 990072, "damageList": [{"avatarID": "b19d03f0-6f6b-4fe8-a07a-e5cd70d60b33", "avatarName": "Isko", "battlePoint": 7999192, "campId": 1, "chengHaoID": 1023, "contentID": 2046, "damageTotal": 33755035, "dollId": 0, "dollName": "", "fightCount": 37, "fightTimeNext": 1780575849, "guild": "Stars", "guildId": 195125658, "headFrame": 4, "inspireCount": 10, "level": 84, "masterLevel": 0, "mountEquip": [], "mount_ID": 0, "petCount": 184, "petKilled": 0, "pet_ID": 21082, "ranking": 1, "rid": 195125409, "rotom_ID": 1001, "spriteLevel": 35, "talk": "", "tuxiaongID": 21572, "vip": 15}, {"avatarID": "07a68e7a-21ce-4387-a447-4ed2fb97f147", "avatarName": "Recycler", "battlePoint": 4579292, "campId": 1, "chengHaoID": 0, "contentID": 2045, "damageTotal": 15203154, "dollId": 0, "dollName": "", "fightCount": 20, "fightTimeNext": 1780575850, "guild": "SG⚘GĐ", "guildId": 195123642, "headFrame": 0, "inspireCount": 0, "level": 83, "masterLevel": 0, "mountEquip": [], "mount_ID": 7004, "petCount": 178, "petKilled": 0, "pet_ID": 1023522, "ranking": 2, "rid": 195123693, "rotom_ID": 1002, "spriteLevel": 34, "talk": "", "tuxiaongID": 2045, "vip": 14}, {"avatarID": "14fa5938-a9a4-4e99-9cb4-9738723cfcbe", "avatarName": "哈基咪", "battlePoint": 5144237, "campId": 1, "chengHaoID": 1029, "contentID": 2014, "damageTotal": 7197986, "dollId": 0, "dollName": "", "fightCount": 22, "fightTimeNext": 1780575804, "guild": "SG⚘GĐ", "guildId": 195123642, "headFrame": 13, "inspireCount": 0, "level": 80, "masterLevel": 0, "mountEquip": [{"id": 4, "value": 3}], "mount_ID": 7004, "petCount": 212, "petKilled": 0, "pet_ID": 1020592, "ranking": 3, "rid": 195123521, "rotom_ID": 0, "spriteLevel": 34, "talk": "", "tuxiaongID": 2014, "vip": 13}, {"avatarID": "8d413ef0-b103-4b88-bf45-db611d16219b", "avat... <truncated; see decoded/decoded_packets.json for full payload>
      ```

### Packet 081 — `81.bin` — DOWN server → client

- **Timestamp ms**: `1780601526132`
- **TCP chunk length**: `1460` bytes
- **Frame(s)**: `088`
  - **Frame 088**; spans segments `[81, 82]`
    - Header: `e0ffb1120005c3010e40100000000028`
    - Total length: `1475` bytes; codec: `zlib`; format: `json_response`
    - Func: `GlobalPetQueryResult`
    - Nội dung decoded:
      ```json
      [{"func": "GlobalPetQueryResult", "gpetStatus": {"damageList": [{"avatarID": "07a68e7a-21ce-4387-a447-4ed2fb97f147", "avatarName": "Recycler", "battlePoint": 4579292, "campId": 1, "chengHaoID": 0, "contentID": 2045, "damageTotal": 5174587, "dollId": 0, "dollName": "", "fightCount": 242, "fightTimeNext": 1780579841, "guild": "SG⚘GĐ", "guildId": 195123642, "headFrame": 0, "level": 83, "masterLevel": 0, "mountEquip": [], "mount_ID": 7004, "petCount": 178, "petKilled": 242, "pet_ID": 1023522, "ranking": 1, "rid": 195123693, "rotom_ID": 1002, "spriteLevel": 34, "talk": "", "tuxiaongID": 2045, "vip": 14}, {"avatarID": "d4df0223-ca5d-48f7-9a50-fb408ca21915", "avatarName": "Gió⚘MD", "battlePoint": 5984835, "campId": 1, "chengHaoID": 1009, "contentID": 2019, "damageTotal": 1988851, "dollId": 0, "dollName": "", "fightCount": 78, "fightTimeNext": 1780579854, "guild": "SG⚘GĐ", "guildId": 195123642, "headFrame": 38, "level": 81, "masterLevel": 0, "mountEquip": [], "mount_ID": 7004, "petCount": 125, "petKilled": 78, "pet_ID": 1023522, "ranking": 2, "rid": 195123571, "rotom_ID": 1002, "spriteLevel": 33, "talk": "", "tuxiaongID": 1022, "vip": 14}, {"avatarID": "14fa5938-a9a4-4e99-9cb4-9738723cfcbe", "avatarName": "哈基咪", "battlePoint": 5169886, "campId": 1, "chengHaoID": 1029, "contentID": 2014, "damageTotal": 1983465, "dollId": 0, "dollName": "", "fightCount": 131, "fightTimeNext": 1780579811, "guild": "SG⚘GĐ", "guildId": 195123642, "headFrame": 13, "level": 80, "masterLevel": 0, "mountEquip": [{"id": 4, "value": 3}], "mount_ID": 7004, "petCount": 205, "petKilled": 120, "pet_ID": 1020592, "ranking": 3, "rid": 195123521, "rotom_ID": 0, "spriteLevel": 34, "talk": "", "tuxiaongID": 2014, "vip": 13}, {"avatarID": "8d413ef0-b103-4b88-bf45-db611d16219b", "avatarName": "MiH4wk", "battlePoint"... <truncated; see decoded/decoded_packets.json for full payload>
      ```

### Packet 082 — `82.bin` — DOWN server → client

- **Timestamp ms**: `1780601526132`
- **TCP chunk length**: `15` bytes
- **Frame(s)**: `088`
  - **Frame 088**; spans segments `[81, 82]`
    - Header: `e0ffb1120005c3010e40100000000028`
    - Total length: `1475` bytes; codec: `zlib`; format: `json_response`
    - Func: `GlobalPetQueryResult`
    - Nội dung decoded:
      ```json
      [{"func": "GlobalPetQueryResult", "gpetStatus": {"damageList": [{"avatarID": "07a68e7a-21ce-4387-a447-4ed2fb97f147", "avatarName": "Recycler", "battlePoint": 4579292, "campId": 1, "chengHaoID": 0, "contentID": 2045, "damageTotal": 5174587, "dollId": 0, "dollName": "", "fightCount": 242, "fightTimeNext": 1780579841, "guild": "SG⚘GĐ", "guildId": 195123642, "headFrame": 0, "level": 83, "masterLevel": 0, "mountEquip": [], "mount_ID": 7004, "petCount": 178, "petKilled": 242, "pet_ID": 1023522, "ranking": 1, "rid": 195123693, "rotom_ID": 1002, "spriteLevel": 34, "talk": "", "tuxiaongID": 2045, "vip": 14}, {"avatarID": "d4df0223-ca5d-48f7-9a50-fb408ca21915", "avatarName": "Gió⚘MD", "battlePoint": 5984835, "campId": 1, "chengHaoID": 1009, "contentID": 2019, "damageTotal": 1988851, "dollId": 0, "dollName": "", "fightCount": 78, "fightTimeNext": 1780579854, "guild": "SG⚘GĐ", "guildId": 195123642, "headFrame": 38, "level": 81, "masterLevel": 0, "mountEquip": [], "mount_ID": 7004, "petCount": 125, "petKilled": 78, "pet_ID": 1023522, "ranking": 2, "rid": 195123571, "rotom_ID": 1002, "spriteLevel": 33, "talk": "", "tuxiaongID": 1022, "vip": 14}, {"avatarID": "14fa5938-a9a4-4e99-9cb4-9738723cfcbe", "avatarName": "哈基咪", "battlePoint": 5169886, "campId": 1, "chengHaoID": 1029, "contentID": 2014, "damageTotal": 1983465, "dollId": 0, "dollName": "", "fightCount": 131, "fightTimeNext": 1780579811, "guild": "SG⚘GĐ", "guildId": 195123642, "headFrame": 13, "level": 80, "masterLevel": 0, "mountEquip": [{"id": 4, "value": 3}], "mount_ID": 7004, "petCount": 205, "petKilled": 120, "pet_ID": 1020592, "ranking": 3, "rid": 195123521, "rotom_ID": 0, "spriteLevel": 34, "talk": "", "tuxiaongID": 2014, "vip": 13}, {"avatarID": "8d413ef0-b103-4b88-bf45-db611d16219b", "avatarName": "MiH4wk", "battlePoint"... <truncated; see decoded/decoded_packets.json for full payload>
      ```

### Packet 083 — `83.bin` — UP client → server

- **Timestamp ms**: `1780601526152`
- **TCP chunk length**: `151` bytes
- **Frame(s)**: `089`
  - **Frame 089**
    - Header: `5104eaea000097000000000000000029`
    - Total length: `151` bytes; codec: `plain`; format: `urlencoded_request`
    - Func: `MiJingStatusQuery`
    - Query fields: `{"bv": "7.0.2", "seq": "41", "session": "02D1B0135ABCDC0D", "sptype": "spv2jodo", "version": "7.0.2"}`
    - Nội dung decoded:
      ```json
      [{"func": "MiJingStatusQuery"}]
      ```

### Packet 084 — `84.bin` — DOWN server → client

- **Timestamp ms**: `1780601526181`
- **TCP chunk length**: `335` bytes
- **Frame(s)**: `090`
  - **Frame 090**
    - Header: `4ffa8e2c00014f000e40100000000029`
    - Total length: `335` bytes; codec: `plain`; format: `json_response`
    - Func: `MiJingStatusUpdate`
    - Nội dung decoded:
      ```json
      [{"func": "MiJingStatusUpdate", "mijingStatus": {"catchCount": 0, "catchSenior": 0, "freeTicket": 1, "petIdList": [20291, 20791, 20761, 20151, 20921, 22751, 20291, 20622, 20791, 20621], "petIdSenior": [23201, 20781, 20342, 21211, 21231, 20302, 20311, 20311, 20342, 21231], "target": {"cdList": [], "escape": 0, "flagSenior": 0, "hp": 0, "hpMax": 0, "id": 0}}}]
      ```

### Packet 085 — `85.bin` — UP client → server

- **Timestamp ms**: `1780601526204`
- **TCP chunk length**: `149` bytes
- **Frame(s)**: `091`
  - **Frame 091**
    - Header: `42ddf10e00009500000000000000002a`
    - Total length: `149` bytes; codec: `plain`; format: `urlencoded_request`
    - Func: `PetExploreQuery`
    - Query fields: `{"bv": "7.0.2", "seq": "42", "session": "02D1B0135ABCDC0D", "sptype": "spv2jodo", "version": "7.0.2"}`
    - Nội dung decoded:
      ```json
      [{"func": "PetExploreQuery"}]
      ```

### Packet 086 — `86.bin` — DOWN server → client

- **Timestamp ms**: `1780601526233`
- **TCP chunk length**: `123` bytes
- **Frame(s)**: `092`
  - **Frame 092**
    - Header: `ca57eaa200007b000e4010000000002a`
    - Total length: `123` bytes; codec: `plain`; format: `json_response`
    - Func: `PetExploreQueryResult`
    - Nội dung decoded:
      ```json
      [{"func": "PetExploreQueryResult", "info": {"evolutionPicked": [], "exp": 0, "fragment": 0, "level": 0, "point": 0}}]
      ```

### Packet 087 — `87.bin` — UP client → server

- **Timestamp ms**: `1780601526258`
- **TCP chunk length**: `152` bytes
- **Frame(s)**: `093`
  - **Frame 093**
    - Header: `fa63f74f00009800000000000000002b`
    - Total length: `152` bytes; codec: `plain`; format: `urlencoded_request`
    - Func: `QueryDecorationBag`
    - Query fields: `{"bv": "7.0.2", "seq": "43", "session": "02D1B0135ABCDC0D", "sptype": "spv2jodo", "version": "7.0.2"}`
    - Nội dung decoded:
      ```json
      [{"func": "QueryDecorationBag"}]
      ```

### Packet 088 — `88.bin` — DOWN server → client

- **Timestamp ms**: `1780601526286`
- **TCP chunk length**: `95` bytes
- **Frame(s)**: `094`
  - **Frame 094**
    - Header: `01d8258900005f000e4010000000002b`
    - Total length: `95` bytes; codec: `plain`; format: `json_response`
    - Func: `QueryDecorationBagResult`
    - Nội dung decoded:
      ```json
      [{"count": 1, "decorationInfos": [], "func": "QueryDecorationBagResult", "num": 50}]
      ```

### Packet 089 — `89.bin` — UP client → server

- **Timestamp ms**: `1780601526310`
- **TCP chunk length**: `148` bytes
- **Frame(s)**: `095`
  - **Frame 095**
    - Header: `759eb31d00009400000000000000002c`
    - Total length: `148` bytes; codec: `plain`; format: `urlencoded_request`
    - Func: `ZBraceletQuery`
    - Query fields: `{"bv": "7.0.2", "seq": "44", "session": "02D1B0135ABCDC0D", "sptype": "spv2jodo", "version": "7.0.2"}`
    - Nội dung decoded:
      ```json
      [{"func": "ZBraceletQuery"}]
      ```

### Packet 090 — `90.bin` — DOWN server → client

- **Timestamp ms**: `1780601526336`
- **TCP chunk length**: `62` bytes
- **Frame(s)**: `096`
  - **Frame 096**
    - Header: `53bf26b400003e000e4010000000002c`
    - Total length: `62` bytes; codec: `plain`; format: `json_response`
    - Func: `ZBraceletQueryResult`
    - Nội dung decoded:
      ```json
      [{"func": "ZBraceletQueryResult", "zbAll": []}]
      ```

### Packet 091 — `91.bin` — UP client → server

- **Timestamp ms**: `1780601526365`
- **TCP chunk length**: `145` bytes
- **Frame(s)**: `097`
  - **Frame 097**
    - Header: `5178b22500009100000000000000002d`
    - Total length: `145` bytes; codec: `plain`; format: `urlencoded_request`
    - Func: `QueryPetBag`
    - Query fields: `{"bv": "7.0.2", "seq": "45", "session": "02D1B0135ABCDC0D", "sptype": "spv2jodo", "version": "7.0.2"}`
    - Nội dung decoded:
      ```json
      [{"func": "QueryPetBag"}]
      ```

### Packet 092 — `92.bin` — DOWN server → client

- **Timestamp ms**: `1780601526391`
- **TCP chunk length**: `67` bytes
- **Frame(s)**: `098`
  - **Frame 098**
    - Header: `541eebee000043000e4010000000002d`
    - Total length: `67` bytes; codec: `plain`; format: `json_response`
    - Func: `QueryPetBagResult`
    - Nội dung decoded:
      ```json
      [{"count": 0, "func": "QueryPetBagResult", "num": 50}]
      ```

### Packet 093 — `93.bin` — UP client → server

- **Timestamp ms**: `1780601526420`
- **TCP chunk length**: `147` bytes
- **Frame(s)**: `099`
  - **Frame 099**
    - Header: `797aed4b00009300000000000000002e`
    - Total length: `147` bytes; codec: `plain`; format: `urlencoded_request`
    - Func: `LivenessQuery`
    - Query fields: `{"bv": "7.0.2", "seq": "46", "session": "02D1B0135ABCDC0D", "sptype": "spv2jodo", "version": "7.0.2"}`
    - Nội dung decoded:
      ```json
      [{"func": "LivenessQuery"}]
      ```

### Packet 094 — `94.bin` — DOWN server → client

- **Timestamp ms**: `1780601526448`
- **TCP chunk length**: `162` bytes
- **Frame(s)**: `100`
  - **Frame 100**
    - Header: `247abc0f0000a2000e4010000000002e`
    - Total length: `162` bytes; codec: `plain`; format: `json_response`
    - Func: `LivenessQueryResult`
    - Nội dung decoded:
      ```json
      [{"func": "LivenessQueryResult", "livenessInfo": {"dailyLevel": 1, "dailyReward": [], "dailyValue": 0, "weekReward": [], "weekValue": 0}, "livenessList": []}]
      ```

### Packet 095 — `95.bin` — UP client → server

- **Timestamp ms**: `1780601526474`
- **TCP chunk length**: `153` bytes
- **Frame(s)**: `101`
  - **Frame 101**
    - Header: `c9b4880600009900000000000000002f`
    - Total length: `153` bytes; codec: `plain`; format: `urlencoded_request`
    - Func: `RichnessForestQuery`
    - Query fields: `{"bv": "7.0.2", "seq": "47", "session": "02D1B0135ABCDC0D", "sptype": "spv2jodo", "version": "7.0.2"}`
    - Nội dung decoded:
      ```json
      [{"func": "RichnessForestQuery"}]
      ```

### Packet 096 — `96.bin` — DOWN server → client

- **Timestamp ms**: `1780601526500`
- **TCP chunk length**: `217` bytes
- **Frame(s)**: `102`
  - **Frame 102**
    - Header: `b1202d9b0000d9000e4010000000002f`
    - Total length: `217` bytes; codec: `plain`; format: `json_response`
    - Func: `RichnessForestQueryResult`
    - Nội dung decoded:
      ```json
      [{"func": "RichnessForestQueryResult", "info": {"battleResult": 0, "challengeCount": 0, "lastWinWave": 0, "maxWave": 0, "petFight": {"paraList": [], "petIdList": [], "petList": []}, "usedPetList": [], "waveReward": []}}]
      ```

### Packet 097 — `97.bin` — UP client → server

- **Timestamp ms**: `1780601526537`
- **TCP chunk length**: `147` bytes
- **Frame(s)**: `103`
  - **Frame 103**
    - Header: `c990109e000093000000000000000030`
    - Total length: `147` bytes; codec: `plain`; format: `urlencoded_request`
    - Func: `CampTechQuery`
    - Query fields: `{"bv": "7.0.2", "seq": "48", "session": "02D1B0135ABCDC0D", "sptype": "spv2jodo", "version": "7.0.2"}`
    - Nội dung decoded:
      ```json
      [{"func": "CampTechQuery"}]
      ```

### Packet 098 — `98.bin` — DOWN server → client

- **Timestamp ms**: `1780601526565`
- **TCP chunk length**: `83` bytes
- **Frame(s)**: `104`
  - **Frame 104**
    - Header: `6a63c2d2000053000e40100000000030`
    - Total length: `83` bytes; codec: `plain`; format: `json_response`
    - Func: `CampTechQueryResult`
    - Nội dung decoded:
      ```json
      [{"func": "CampTechQueryResult", "techList": [], "techPointList": []}]
      ```

### Packet 099 — `99.bin` — UP client → server

- **Timestamp ms**: `1780601526590`
- **TCP chunk length**: `149` bytes
- **Frame(s)**: `105`
  - **Frame 105**
    - Header: `2dbd811b000095000000000000000031`
    - Total length: `149` bytes; codec: `plain`; format: `urlencoded_request`
    - Func: `CampStatueQuery`
    - Query fields: `{"bv": "7.0.2", "seq": "49", "session": "02D1B0135ABCDC0D", "sptype": "spv2jodo", "version": "7.0.2"}`
    - Nội dung decoded:
      ```json
      [{"func": "CampStatueQuery"}]
      ```

### Packet 100 — `100.bin` — DOWN server → client

- **Timestamp ms**: `1780601526617`
- **TCP chunk length**: `98` bytes
- **Frame(s)**: `106`
  - **Frame 106**
    - Header: `0bdeeb28000062000e40100000000031`
    - Total length: `98` bytes; codec: `plain`; format: `json_response`
    - Func: `CampStatueQueryResult`
    - Nội dung decoded:
      ```json
      [{"func": "CampStatueQueryResult", "infos": [], "squareDreamBag": [], "statueBag": []}]
      ```

### Packet 101 — `101.bin` — UP client → server

- **Timestamp ms**: `1780601526644`
- **TCP chunk length**: `151` bytes
- **Frame(s)**: `107`
  - **Frame 107**
    - Header: `ebfa15a3000097000000000000000032`
    - Total length: `151` bytes; codec: `plain`; format: `urlencoded_request`
    - Func: `InviteReturnQuery`
    - Query fields: `{"bv": "7.0.2", "seq": "50", "session": "02D1B0135ABCDC0D", "sptype": "spv2jodo", "version": "7.0.2"}`
    - Nội dung decoded:
      ```json
      [{"func": "InviteReturnQuery"}]
      ```

### Packet 102 — `102.bin` — DOWN server → client

- **Timestamp ms**: `1780601526673`
- **TCP chunk length**: `516` bytes
- **Frame(s)**: `108`
  - **Frame 108**
    - Header: `7ea76e8f000204000e40100000000032`
    - Total length: `516` bytes; codec: `plain`; format: `json_response`
    - Func: `InviteReturnQueryResult`
    - Nội dung decoded:
      ```json
      [{"error_code": 0, "func": "InviteReturnQueryResult", "info": {"common": {"avatarID": "f25f2e5d-5ff3-4a83-89d5-4d259303f4bd", "avatarName": "BeetBoij", "battlePoint": 0, "campId": 0, "chengHaoID": 0, "contentID": 1002, "dollId": 0, "dollName": "", "guild": "", "guildId": 0, "headFrame": 0, "level": 1, "masterLevel": 0, "mountEquip": [], "mount_ID": 0, "petCount": 0, "pet_ID": 0, "rid": 195132877, "rotom_ID": 0, "spriteLevel": 0, "talk": "", "tuxiaongID": 1002, "vip": 0}, "invite": "v2R55YC3", "inviteBind": "", "statistics": [], "task": []}, "list": []}]
      ```

### Packet 103 — `103.bin` — UP client → server

- **Timestamp ms**: `1780601526701`
- **TCP chunk length**: `147` bytes
- **Frame(s)**: `109`
  - **Frame 109**
    - Header: `f829d894000093000000000000000033`
    - Total length: `147` bytes; codec: `plain`; format: `urlencoded_request`
    - Func: `TopMatchQuery`
    - Query fields: `{"bv": "7.0.2", "seq": "51", "session": "02D1B0135ABCDC0D", "sptype": "spv2jodo", "version": "7.0.2"}`
    - Nội dung decoded:
      ```json
      [{"func": "TopMatchQuery"}]
      ```

### Packet 104 — `104.bin` — DOWN server → client

- **Timestamp ms**: `1780601526730`
- **TCP chunk length**: `695` bytes
- **Frame(s)**: `110`
  - **Frame 110**
    - Header: `d1e26ef70002b7000e40100000000033`
    - Total length: `695` bytes; codec: `plain`; format: `json_response`
    - Func: `TopMatchQueryResult`
    - Nội dung decoded:
      ```json
      [{"avatar": {"bApply": 0, "common": {"avatarID": "f25f2e5d-5ff3-4a83-89d5-4d259303f4bd", "avatarName": "BeetBoij", "battlePoint": 0, "campId": 0, "chengHaoID": 0, "contentID": 1002, "dollId": 0, "dollName": "", "guild": "", "guildId": 0, "headFrame": 0, "level": 1, "masterLevel": 0, "mountEquip": [], "mount_ID": 0, "petCount": 0, "pet_ID": 0, "rid": 195132877, "rotom_ID": 0, "spriteLevel": 0, "talk": "", "tuxiaongID": 1002, "vip": 0}, "enemyList": [], "fightLog": [], "lastAddScore": 0, "petList": [], "petShowList": [], "record": 0, "rewardList": [], "score": 0, "support": []}, "error_code": 0, "func": "TopMatchQueryResult", "info": {"avatars": [], "fightLog": [], "gid": 16, "num": 11, "rank": [], "round": 6, "stage": 2, "status": 0, "weekResetDay": 20604}}]
      ```

### Packet 105 — `105.bin` — UP client → server

- **Timestamp ms**: `1780601526761`
- **TCP chunk length**: `152` bytes
- **Frame(s)**: `111`
  - **Frame 111**
    - Header: `202cf91d000098000000000000000034`
    - Total length: `152` bytes; codec: `plain`; format: `urlencoded_request`
    - Func: `DecorationGemQuery`
    - Query fields: `{"bv": "7.0.2", "seq": "52", "session": "02D1B0135ABCDC0D", "sptype": "spv2jodo", "version": "7.0.2"}`
    - Nội dung decoded:
      ```json
      [{"func": "DecorationGemQuery"}]
      ```

### Packet 106 — `106.bin` — DOWN server → client

- **Timestamp ms**: `1780601526787`
- **TCP chunk length**: `68` bytes
- **Frame(s)**: `112`
  - **Frame 112**
    - Header: `6492b7ef000044000e40100000000034`
    - Total length: `68` bytes; codec: `plain`; format: `json_response`
    - Func: `DecorationGemQueryResult`
    - Nội dung decoded:
      ```json
      [{"func": "DecorationGemQueryResult", "gamlist": []}]
      ```

### Packet 107 — `107.bin` — UP client → server

- **Timestamp ms**: `1780601526823`
- **TCP chunk length**: `151` bytes
- **Frame(s)**: `113`
  - **Frame 113**
    - Header: `339189cc000097000000000000000035`
    - Total length: `151` bytes; codec: `plain`; format: `urlencoded_request`
    - Func: `ExchangeShopQuery`
    - Query fields: `{"bv": "7.0.2", "seq": "53", "session": "02D1B0135ABCDC0D", "sptype": "spv2jodo", "version": "7.0.2"}`
    - Nội dung decoded:
      ```json
      [{"func": "ExchangeShopQuery"}]
      ```

### Packet 108 — `108.bin` — DOWN server → client

- **Timestamp ms**: `1780601526848`
- **TCP chunk length**: `390` bytes
- **Frame(s)**: `114`
  - **Frame 114**
    - Header: `2399cb04000186010e40100000000035`
    - Total length: `390` bytes; codec: `zlib`; format: `json_response`
    - Func: `ExchangeShopQueryResult`
    - Nội dung decoded:
      ```json
      [{"func": "ExchangeShopQueryResult", "shopList": [{"buyCount": 0, "count": 1, "lastTimeReset": 1780601520, "shopId": 2}, {"buyCount": 0, "count": 1, "lastTimeReset": 1780601520, "shopId": 3}, {"buyCount": 0, "count": 1, "lastTimeReset": 1780601520, "shopId": 4}, {"buyCount": 0, "count": 1, "lastTimeReset": 1780601520, "shopId": 5}, {"buyCount": 0, "count": 1, "lastTimeReset": 1780601520, "shopId": 6}, {"buyCount": 0, "count": 1, "lastTimeReset": 1780601520, "shopId": 7}, {"buyCount": 0, "count": 1, "lastTimeReset": 1780601520, "shopId": 8}, {"buyCount": 0, "count": 1, "lastTimeReset": 1780601520, "shopId": 9}, {"buyCount": 0, "count": 1, "lastTimeReset": 1780601520, "shopId": 10}, {"buyCount": 0, "count": 1, "lastTimeReset": 1780601520, "shopId": 11}, {"buyCount": 0, "count": 1, "lastTimeReset": 1780601520, "shopId": 12}, {"buyCount": 0, "count": 1, "lastTimeReset": 1780601520, "shopId": 13}, {"buyCount": 0, "count": 1, "lastTimeReset": 1780601520, "shopId": 14}, {"buyCount": 0, "count": 1, "lastTimeReset": 1780601520, "shopId": 15}, {"buyCount": 0, "count": 1, "lastTimeReset": 1780601520, "shopId": 17}, {"buyCount": 0, "count": 1, "lastTimeReset": 1780601520, "shopId": 16}, {"buyCount": 0, "count": 1, "lastTimeReset": 1780601520, "shopId": 19}, {"buyCount": 0, "count": 1, "lastTimeReset": 1780601520, "shopId": 18}, {"buyCount": 0, "count": 1, "lastTimeReset": 1780601520, "shopId": 21}, {"buyCount": 0, "count": 1, "lastTimeReset": 1780601520, "shopId": 20}, {"buyCount": 0, "count": 1, "lastTimeReset": 1780601520, "shopId": 23}, {"buyCount": 0, "count": 1, "lastTimeReset": 1780601520, "shopId": 22}, {"buyCount": 0, "count": 1, "lastTimeReset": 1780601520, "shopId": 25}, {"buyCount": 0, "count": 1, "lastTimeReset": 1780601520, "shopId": 24}, {"buyCount": 0, "count": 1, "l... <truncated; see decoded/decoded_packets.json for full payload>
      ```

### Packet 109 — `109.bin` — UP client → server

- **Timestamp ms**: `1780601526883`
- **TCP chunk length**: `150` bytes
- **Frame(s)**: `115`
  - **Frame 115**
    - Header: `34ada0a1000096000000000000000036`
    - Total length: `150` bytes; codec: `plain`; format: `urlencoded_request`
    - Func: `PetResearchQuery`
    - Query fields: `{"bv": "7.0.2", "seq": "54", "session": "02D1B0135ABCDC0D", "sptype": "spv2jodo", "version": "7.0.2"}`
    - Nội dung decoded:
      ```json
      [{"func": "PetResearchQuery"}]
      ```

### Packet 110 — `110.bin` — DOWN server → client

- **Timestamp ms**: `1780601526909`
- **TCP chunk length**: `91` bytes
- **Frame(s)**: `116`
  - **Frame 116**
    - Header: `c36c0b0e00005b000e40100000000036`
    - Total length: `91` bytes; codec: `plain`; format: `json_response`
    - Func: `PetResearchQueryResult`
    - Nội dung decoded:
      ```json
      [{"func": "PetResearchQueryResult", "info": {"levelInfo": [], "slotList": []}}]
      ```

### Packet 111 — `111.bin` — UP client → server

- **Timestamp ms**: `1780601526941`
- **TCP chunk length**: `146` bytes
- **Frame(s)**: `117`
  - **Frame 117**
    - Header: `8ed4a170000092000000000000000037`
    - Total length: `146` bytes; codec: `plain`; format: `urlencoded_request`
    - Func: `RecoverQuery`
    - Query fields: `{"bv": "7.0.2", "seq": "55", "session": "02D1B0135ABCDC0D", "sptype": "spv2jodo", "version": "7.0.2"}`
    - Nội dung decoded:
      ```json
      [{"func": "RecoverQuery"}]
      ```

### Packet 112 — `112.bin` — DOWN server → client

- **Timestamp ms**: `1780601526970`
- **TCP chunk length**: `165` bytes
- **Frame(s)**: `118`
  - **Frame 118**
    - Header: `419345170000a5000e40100000000037`
    - Total length: `165` bytes; codec: `plain`; format: `json_response`
    - Func: `RecoverQueryResult`
    - Nội dung decoded:
      ```json
      [{"func": "RecoverQueryResult", "recoverList": [{"isRecover": 1, "recoverCnt": 0, "recoverFunc": 0, "recoverId": 10101, "recoverTotal": 0, "recoveredPara": 0}]}]
      ```

### Packet 113 — `113.bin` — UP client → server

- **Timestamp ms**: `1780601526995`
- **TCP chunk length**: `159` bytes
- **Frame(s)**: `119`
  - **Frame 119**
    - Header: `7d08a11b00009f000000000000000038`
    - Total length: `159` bytes; codec: `plain`; format: `urlencoded_request`
    - Func: `TreasureScrambleInfoQuery`
    - Query fields: `{"bv": "7.0.2", "seq": "56", "session": "02D1B0135ABCDC0D", "sptype": "spv2jodo", "version": "7.0.2"}`
    - Nội dung decoded:
      ```json
      [{"func": "TreasureScrambleInfoQuery"}]
      ```

### Packet 114 — `114.bin` — DOWN server → client

- **Timestamp ms**: `1780601527022`
- **TCP chunk length**: `93` bytes
- **Frame(s)**: `120`
  - **Frame 120**
    - Header: `031a885300005d000e40100000000038`
    - Total length: `93` bytes; codec: `plain`; format: `json_response`
    - Func: `TreasureScrambleInfoQueryResult`
    - Nội dung decoded:
      ```json
      [{"func": "TreasureScrambleInfoQueryResult", "info": {"exp": 0, "joinCount": 0}}]
      ```

### Packet 115 — `115.bin` — UP client → server

- **Timestamp ms**: `1780601527046`
- **TCP chunk length**: `143` bytes
- **Frame(s)**: `121`
  - **Frame 121**
    - Header: `7e40cd0200008f000000000000000039`
    - Total length: `143` bytes; codec: `plain`; format: `urlencoded_request`
    - Func: `CampQuery`
    - Query fields: `{"bv": "7.0.2", "seq": "57", "session": "02D1B0135ABCDC0D", "sptype": "spv2jodo", "version": "7.0.2"}`
    - Nội dung decoded:
      ```json
      [{"func": "CampQuery"}]
      ```

### Packet 116 — `116.bin` — DOWN server → client

- **Timestamp ms**: `1780601527072`
- **TCP chunk length**: `485` bytes
- **Frame(s)**: `122`
  - **Frame 122**
    - Header: `9e4d4f980001e5000e40100000000039`
    - Total length: `485` bytes; codec: `plain`; format: `json_response`
    - Func: `CampQueryResult`
    - Nội dung decoded:
      ```json
      [{"camp": {"count": 0, "gid": 0, "id": 0, "jobs": [], "sid": 0, "statistics": [], "weekTask": []}, "func": "CampQueryResult", "info": {"challengeCount": 0, "exp": 0, "id": 0, "lastQuitTime": 0}, "task": [{"id": 500024, "option": 60, "type": 70, "value": 0}, {"id": 500020, "option": 2000, "type": 57, "value": 0}, {"id": 500021, "option": 50000000, "type": 58, "value": 0}, {"id": 500022, "option": 6, "type": 59, "value": 0}, {"id": 500023, "option": 50000, "type": 63, "value": 0}, {"id": 500019, "option": 1000, "type": 56, "value": 0}]}]
      ```

### Packet 117 — `117.bin` — UP client → server

- **Timestamp ms**: `1780601527100`
- **TCP chunk length**: `147` bytes
- **Frame(s)**: `123`
  - **Frame 123**
    - Header: `43ed824400009300000000000000003a`
    - Total length: `147` bytes; codec: `plain`; format: `urlencoded_request`
    - Func: `PetOwnedQuery`
    - Query fields: `{"bv": "7.0.2", "seq": "58", "session": "02D1B0135ABCDC0D", "sptype": "spv2jodo", "version": "7.0.2"}`
    - Nội dung decoded:
      ```json
      [{"func": "PetOwnedQuery"}]
      ```

### Packet 118 — `118.bin` — DOWN server → client

- **Timestamp ms**: `1780601527128`
- **TCP chunk length**: `111` bytes
- **Frame(s)**: `124`
  - **Frame 124**
    - Header: `c67fc75100006f000e4010000000003a`
    - Total length: `111` bytes; codec: `plain`; format: `json_response`
    - Func: `PetOwnedQueryResult`
    - Nội dung decoded:
      ```json
      [{"biggestNew": [], "biggestOwned": [0], "func": "PetOwnedQueryResult", "petNew": [], "petOwned": []}]
      ```

### Packet 119 — `119.bin` — UP client → server

- **Timestamp ms**: `1780601527153`
- **TCP chunk length**: `149` bytes
- **Frame(s)**: `125`
  - **Frame 125**
    - Header: `67d1396f00009500000000000000003b`
    - Total length: `149` bytes; codec: `plain`; format: `urlencoded_request`
    - Func: `StatisticsQuery`
    - Query fields: `{"bv": "7.0.2", "seq": "59", "session": "02D1B0135ABCDC0D", "sptype": "spv2jodo", "version": "7.0.2"}`
    - Nội dung decoded:
      ```json
      [{"func": "StatisticsQuery"}]
      ```

### Packet 120 — `120.bin` — DOWN server → client

- **Timestamp ms**: `1780601527179`
- **TCP chunk length**: `148` bytes
- **Frame(s)**: `126`
  - **Frame 126**
    - Header: `d3a463b3000094000e4010000000003b`
    - Total length: `148` bytes; codec: `plain`; format: `json_response`
    - Func: `StatisticsQueryResult`
    - Nội dung decoded:
      ```json
      [{"func": "StatisticsQueryResult", "statisticsValue": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}]
      ```

### Packet 121 — `121.bin` — UP client → server

- **Timestamp ms**: `1780601527202`
- **TCP chunk length**: `175` bytes
- **Frame(s)**: `127`
  - **Frame 127**
    - Header: `f3da11770000af00000000000000003c`
    - Total length: `175` bytes; codec: `plain`; format: `urlencoded_request`
    - Func: `FriendHuntQuery`
    - Query fields: `{"bv": "7.0.2", "seq": "60", "session": "02D1B0135ABCDC0D", "sptype": "spv2jodo", "version": "7.0.2"}`
    - Nội dung decoded:
      ```json
      [{"avatarID": "", "func": "FriendHuntQuery"}]
      ```

### Packet 122 — `122.bin` — DOWN server → client

- **Timestamp ms**: `1780601527227`
- **TCP chunk length**: `98` bytes
- **Frame(s)**: `128`
  - **Frame 128**
    - Header: `495299ab000062000e4010000000003c`
    - Total length: `98` bytes; codec: `plain`; format: `json_response`
    - Func: `FriendHuntQueryResult`
    - Nội dung decoded:
      ```json
      [{"avatarID": "", "func": "FriendHuntQueryResult", "huntBuyCount": -1, "huntList": []}]
      ```

### Packet 123 — `123.bin` — UP client → server

- **Timestamp ms**: `1780601527254`
- **TCP chunk length**: `171` bytes
- **Frame(s)**: `129`
  - **Frame 129**
    - Header: `9ae183260000ab00000000000000003d`
    - Total length: `171` bytes; codec: `plain`; format: `urlencoded_request`
    - Func: `CampHuntQuery`
    - Query fields: `{"bv": "7.0.2", "seq": "61", "session": "02D1B0135ABCDC0D", "sptype": "spv2jodo", "version": "7.0.2"}`
    - Nội dung decoded:
      ```json
      [{"func": "CampHuntQuery", "huntId": ""}]
      ```

### Packet 124 — `124.bin` — DOWN server → client

- **Timestamp ms**: `1780601527281`
- **TCP chunk length**: `134` bytes
- **Frame(s)**: `130`
  - **Frame 130**
    - Header: `9b09b485000086000e4010000000003d`
    - Total length: `134` bytes; codec: `plain`; format: `json_response`
    - Func: `CampHuntQueryResult`
    - Nội dung decoded:
      ```json
      [{"biggestBuyCnt": 0, "biggestList": [], "func": "CampHuntQueryResult", "huntId": "", "overLoadBuyCnt": 0, "overLoadList": []}]
      ```

### Packet 125 — `125.bin` — UP client → server

- **Timestamp ms**: `1780601527306`
- **TCP chunk length**: `159` bytes
- **Frame(s)**: `131`
  - **Frame 131**
    - Header: `8440bc6800009f00000000000000003e`
    - Total length: `159` bytes; codec: `plain`; format: `urlencoded_request`
    - Func: `QueryAvatarTechnologyTree`
    - Query fields: `{"bv": "7.0.2", "seq": "62", "session": "02D1B0135ABCDC0D", "sptype": "spv2jodo", "version": "7.0.2"}`
    - Nội dung decoded:
      ```json
      [{"func": "QueryAvatarTechnologyTree"}]
      ```

### Packet 126 — `126.bin` — DOWN server → client

- **Timestamp ms**: `1780601527333`
- **TCP chunk length**: `78` bytes
- **Frame(s)**: `132`
  - **Frame 132**
    - Header: `d183119c00004e000e4010000000003e`
    - Total length: `78` bytes; codec: `plain`; format: `json_response`
    - Func: `QueryAvatarTechnologyTreeResult`
    - Nội dung decoded:
      ```json
      [{"func": "QueryAvatarTechnologyTreeResult", "technology": []}]
      ```

### Packet 127 — `127.bin` — UP client → server

- **Timestamp ms**: `1780601527362`
- **TCP chunk length**: `176` bytes
- **Frame(s)**: `133`
  - **Frame 133**
    - Header: `34f49ec10000b000000000000000003f`
    - Total length: `176` bytes; codec: `plain`; format: `urlencoded_request`
    - Func: `PVPRankingTopQuery`
    - Query fields: `{"bv": "7.0.2", "seq": "63", "session": "02D1B0135ABCDC0D", "sptype": "spv2jodo", "version": "7.0.2"}`
    - Nội dung decoded:
      ```json
      [{"func": "PVPRankingTopQuery", "sectionType": 1}]
      ```

### Packet 128 — `128.bin` — DOWN server → client

- **Timestamp ms**: `1780601527390`
- **TCP chunk length**: `1452` bytes
- **Frame(s)**: `134`
  - **Frame 134**; spans segments `[128, 129, 130, 131]`
    - Header: `33050484001e33010e4010000000003f`
    - Total length: `7731` bytes; codec: `zlib`; format: `json_response`
    - Func: `PVPRankingTopQueryResult`
    - Nội dung decoded:
      ```json
      [{"func": "PVPRankingTopQueryResult", "pvpShowList": [{"prestige": 762, "show": {"avatarID": "716cc804-6090-48c8-9b0b-f8dec36be97b", "avatarName": "FabianTyt", "battlePoint": 7258037, "campId": 1, "chengHaoID": 1009, "comboWin": 26, "comboWinMax": 26, "contentID": 1009, "dollId": 0, "dollName": "", "fightCountTotal": 247, "fightCountWin": 181, "guild": "Warzone", "guildId": 195123738, "headFrame": 24, "lastActive": 1780600247, "level": 83, "masterLevel": 0, "mountEquip": [{"id": 4, "value": 3}, {"id": 5, "value": 1}], "mount_ID": 7004, "petCount": 195, "petShowList": [{"afinity": 66, "id": 20563, "level": 80}, {"afinity": 60, "id": 1022312, "level": 76}, {"afinity": 65, "id": 21451, "level": 72}, {"afinity": 75, "id": 1023522, "level": 83}, {"afinity": 0, "id": 1021511, "level": 1}, {"afinity": 9, "id": 20981, "level": 45}, {"afinity": 63, "id": 1020051, "level": 81}, {"afinity": 74, "id": 1023502, "level": 83}, {"afinity": 74, "id": 23601, "level": 82}], "pet_ID": 1023502, "ranking": 1000001, "rid": 195125267, "rotom_ID": 0, "spriteLevel": 35, "talk": "", "tuxiaongID": 20859, "vip": 14}, "title": 0}, {"prestige": 764, "show": {"avatarID": "b19d03f0-6f6b-4fe8-a07a-e5cd70d60b33", "avatarName": "Isko", "battlePoint": 7868532, "campId": 1, "chengHaoID": 1023, "comboWin": 3, "comboWinMax": 23, "contentID": 2046, "dollId": 0, "dollName": "", "fightCountTotal": 142, "fightCountWin": 90, "guild": "Stars", "guildId": 195125658, "headFrame": 4, "lastActive": 1780588325, "level": 84, "masterLevel": 0, "mountEquip": [], "mount_ID": 0, "petCount": 179, "petShowList": [{"afinity": 76, "id": 1023502, "level": 84}, {"afinity": 71, "id": 21461, "level": 77}, {"afinity": 65, "id": 1023601, "level": 83}, {"afinity": 78, "id": 1023522, "level": 84}, {"afinity": 67, "id": 20433, "level": 7... <truncated; see decoded/decoded_packets.json for full payload>
      ```

### Packet 129 — `129.bin` — DOWN server → client

- **Timestamp ms**: `1780601527391`
- **TCP chunk length**: `2560` bytes
- **Frame(s)**: `134`
  - **Frame 134**; spans segments `[128, 129, 130, 131]`
    - Header: `33050484001e33010e4010000000003f`
    - Total length: `7731` bytes; codec: `zlib`; format: `json_response`
    - Func: `PVPRankingTopQueryResult`
    - Nội dung decoded:
      ```json
      [{"func": "PVPRankingTopQueryResult", "pvpShowList": [{"prestige": 762, "show": {"avatarID": "716cc804-6090-48c8-9b0b-f8dec36be97b", "avatarName": "FabianTyt", "battlePoint": 7258037, "campId": 1, "chengHaoID": 1009, "comboWin": 26, "comboWinMax": 26, "contentID": 1009, "dollId": 0, "dollName": "", "fightCountTotal": 247, "fightCountWin": 181, "guild": "Warzone", "guildId": 195123738, "headFrame": 24, "lastActive": 1780600247, "level": 83, "masterLevel": 0, "mountEquip": [{"id": 4, "value": 3}, {"id": 5, "value": 1}], "mount_ID": 7004, "petCount": 195, "petShowList": [{"afinity": 66, "id": 20563, "level": 80}, {"afinity": 60, "id": 1022312, "level": 76}, {"afinity": 65, "id": 21451, "level": 72}, {"afinity": 75, "id": 1023522, "level": 83}, {"afinity": 0, "id": 1021511, "level": 1}, {"afinity": 9, "id": 20981, "level": 45}, {"afinity": 63, "id": 1020051, "level": 81}, {"afinity": 74, "id": 1023502, "level": 83}, {"afinity": 74, "id": 23601, "level": 82}], "pet_ID": 1023502, "ranking": 1000001, "rid": 195125267, "rotom_ID": 0, "spriteLevel": 35, "talk": "", "tuxiaongID": 20859, "vip": 14}, "title": 0}, {"prestige": 764, "show": {"avatarID": "b19d03f0-6f6b-4fe8-a07a-e5cd70d60b33", "avatarName": "Isko", "battlePoint": 7868532, "campId": 1, "chengHaoID": 1023, "comboWin": 3, "comboWinMax": 23, "contentID": 2046, "dollId": 0, "dollName": "", "fightCountTotal": 142, "fightCountWin": 90, "guild": "Stars", "guildId": 195125658, "headFrame": 4, "lastActive": 1780588325, "level": 84, "masterLevel": 0, "mountEquip": [], "mount_ID": 0, "petCount": 179, "petShowList": [{"afinity": 76, "id": 1023502, "level": 84}, {"afinity": 71, "id": 21461, "level": 77}, {"afinity": 65, "id": 1023601, "level": 83}, {"afinity": 78, "id": 1023522, "level": 84}, {"afinity": 67, "id": 20433, "level": 7... <truncated; see decoded/decoded_packets.json for full payload>
      ```

### Packet 130 — `130.bin` — DOWN server → client

- **Timestamp ms**: `1780601527391`
- **TCP chunk length**: `2560` bytes
- **Frame(s)**: `134`
  - **Frame 134**; spans segments `[128, 129, 130, 131]`
    - Header: `33050484001e33010e4010000000003f`
    - Total length: `7731` bytes; codec: `zlib`; format: `json_response`
    - Func: `PVPRankingTopQueryResult`
    - Nội dung decoded:
      ```json
      [{"func": "PVPRankingTopQueryResult", "pvpShowList": [{"prestige": 762, "show": {"avatarID": "716cc804-6090-48c8-9b0b-f8dec36be97b", "avatarName": "FabianTyt", "battlePoint": 7258037, "campId": 1, "chengHaoID": 1009, "comboWin": 26, "comboWinMax": 26, "contentID": 1009, "dollId": 0, "dollName": "", "fightCountTotal": 247, "fightCountWin": 181, "guild": "Warzone", "guildId": 195123738, "headFrame": 24, "lastActive": 1780600247, "level": 83, "masterLevel": 0, "mountEquip": [{"id": 4, "value": 3}, {"id": 5, "value": 1}], "mount_ID": 7004, "petCount": 195, "petShowList": [{"afinity": 66, "id": 20563, "level": 80}, {"afinity": 60, "id": 1022312, "level": 76}, {"afinity": 65, "id": 21451, "level": 72}, {"afinity": 75, "id": 1023522, "level": 83}, {"afinity": 0, "id": 1021511, "level": 1}, {"afinity": 9, "id": 20981, "level": 45}, {"afinity": 63, "id": 1020051, "level": 81}, {"afinity": 74, "id": 1023502, "level": 83}, {"afinity": 74, "id": 23601, "level": 82}], "pet_ID": 1023502, "ranking": 1000001, "rid": 195125267, "rotom_ID": 0, "spriteLevel": 35, "talk": "", "tuxiaongID": 20859, "vip": 14}, "title": 0}, {"prestige": 764, "show": {"avatarID": "b19d03f0-6f6b-4fe8-a07a-e5cd70d60b33", "avatarName": "Isko", "battlePoint": 7868532, "campId": 1, "chengHaoID": 1023, "comboWin": 3, "comboWinMax": 23, "contentID": 2046, "dollId": 0, "dollName": "", "fightCountTotal": 142, "fightCountWin": 90, "guild": "Stars", "guildId": 195125658, "headFrame": 4, "lastActive": 1780588325, "level": 84, "masterLevel": 0, "mountEquip": [], "mount_ID": 0, "petCount": 179, "petShowList": [{"afinity": 76, "id": 1023502, "level": 84}, {"afinity": 71, "id": 21461, "level": 77}, {"afinity": 65, "id": 1023601, "level": 83}, {"afinity": 78, "id": 1023522, "level": 84}, {"afinity": 67, "id": 20433, "level": 7... <truncated; see decoded/decoded_packets.json for full payload>
      ```

### Packet 131 — `131.bin` — DOWN server → client

- **Timestamp ms**: `1780601527391`
- **TCP chunk length**: `1159` bytes
- **Frame(s)**: `134`
  - **Frame 134**; spans segments `[128, 129, 130, 131]`
    - Header: `33050484001e33010e4010000000003f`
    - Total length: `7731` bytes; codec: `zlib`; format: `json_response`
    - Func: `PVPRankingTopQueryResult`
    - Nội dung decoded:
      ```json
      [{"func": "PVPRankingTopQueryResult", "pvpShowList": [{"prestige": 762, "show": {"avatarID": "716cc804-6090-48c8-9b0b-f8dec36be97b", "avatarName": "FabianTyt", "battlePoint": 7258037, "campId": 1, "chengHaoID": 1009, "comboWin": 26, "comboWinMax": 26, "contentID": 1009, "dollId": 0, "dollName": "", "fightCountTotal": 247, "fightCountWin": 181, "guild": "Warzone", "guildId": 195123738, "headFrame": 24, "lastActive": 1780600247, "level": 83, "masterLevel": 0, "mountEquip": [{"id": 4, "value": 3}, {"id": 5, "value": 1}], "mount_ID": 7004, "petCount": 195, "petShowList": [{"afinity": 66, "id": 20563, "level": 80}, {"afinity": 60, "id": 1022312, "level": 76}, {"afinity": 65, "id": 21451, "level": 72}, {"afinity": 75, "id": 1023522, "level": 83}, {"afinity": 0, "id": 1021511, "level": 1}, {"afinity": 9, "id": 20981, "level": 45}, {"afinity": 63, "id": 1020051, "level": 81}, {"afinity": 74, "id": 1023502, "level": 83}, {"afinity": 74, "id": 23601, "level": 82}], "pet_ID": 1023502, "ranking": 1000001, "rid": 195125267, "rotom_ID": 0, "spriteLevel": 35, "talk": "", "tuxiaongID": 20859, "vip": 14}, "title": 0}, {"prestige": 764, "show": {"avatarID": "b19d03f0-6f6b-4fe8-a07a-e5cd70d60b33", "avatarName": "Isko", "battlePoint": 7868532, "campId": 1, "chengHaoID": 1023, "comboWin": 3, "comboWinMax": 23, "contentID": 2046, "dollId": 0, "dollName": "", "fightCountTotal": 142, "fightCountWin": 90, "guild": "Stars", "guildId": 195125658, "headFrame": 4, "lastActive": 1780588325, "level": 84, "masterLevel": 0, "mountEquip": [], "mount_ID": 0, "petCount": 179, "petShowList": [{"afinity": 76, "id": 1023502, "level": 84}, {"afinity": 71, "id": 21461, "level": 77}, {"afinity": 65, "id": 1023601, "level": 83}, {"afinity": 78, "id": 1023522, "level": 84}, {"afinity": 67, "id": 20433, "level": 7... <truncated; see decoded/decoded_packets.json for full payload>
      ```

### Packet 132 — `132.bin` — UP client → server

- **Timestamp ms**: `1780601527422`
- **TCP chunk length**: `148` bytes
- **Frame(s)**: `135`
  - **Frame 135**
    - Header: `df1887f8000094000000000000000040`
    - Total length: `148` bytes; codec: `plain`; format: `urlencoded_request`
    - Func: `PetSummonQuery`
    - Query fields: `{"bv": "7.0.2", "seq": "64", "session": "02D1B0135ABCDC0D", "sptype": "spv2jodo", "version": "7.0.2"}`
    - Nội dung decoded:
      ```json
      [{"func": "PetSummonQuery"}]
      ```

### Packet 133 — `133.bin` — DOWN server → client

- **Timestamp ms**: `1780601527452`
- **TCP chunk length**: `1452` bytes
- **Frame(s)**: `136`
  - **Frame 136**; spans segments `[133, 134, 135, 136]`
    - Header: `5dfcba94001f43010e40100000000040`
    - Total length: `8003` bytes; codec: `zlib`; format: `json_response`
    - Func: `PetSummonQueryResult`
    - Nội dung decoded:
      ```json
      [{"func": "PetSummonQueryResult", "petList": [{"AfinityExp": 0, "AfinityLevel": 0, "FettersExp": 0, "FettersLevel": 0, "Fighting": 0, "HouYuanID": 0, "IsFollow": 0, "IsLock": 0, "MarkType": 0, "PetBaseZiZhi": [15, 31, 27, 18, 25, 57], "PetBreakZiZhi": [-1, -1, -1, -1, -1, -1], "PetConfigID": 22279, "PetParams": [], "QiangHuaExp": 0, "QiangHuaLevel": 0, "TeXingIdList": [20411], "XingGeID": 1015, "aidRune": [], "equipments": [-1, -1, -1], "exp": 0, "level": 1, "miSkill": [{"invalid": false, "isLock": 0, "skillId": 0}, {"invalid": false, "isLock": 0, "skillId": 0}, {"invalid": false, "isLock": 0, "skillId": 0}, {"invalid": false, "isLock": 0, "skillId": 0}, {"invalid": false, "isLock": 0, "skillId": 0}, {"invalid": false, "isLock": 0, "skillId": 0}, {"invalid": false, "isLock": 0, "skillId": 0}, {"invalid": false, "isLock": 0, "skillId": 0}], "name": "Lilie's Snowy", "petInfo": {"petAttr": [], "petId": 114, "skillId": [222790, 222791, 222792, 222793, 222794], "skillLevel": [0, 1, 0, 0, 0]}, "sex": 0, "skillLock": 0}, {"AfinityExp": 0, "AfinityLevel": 0, "FettersExp": 0, "FettersLevel": 0, "Fighting": 0, "HouYuanID": 0, "IsFollow": 0, "IsLock": 0, "MarkType": 0, "PetBaseZiZhi": [45, 25, 45, 20, 27, 53], "PetBreakZiZhi": [-1, -1, -1, -1, -1, -1], "PetConfigID": 23441, "PetParams": [], "QiangHuaExp": 0, "QiangHuaLevel": 0, "TeXingIdList": [20180], "XingGeID": 1018, "aidRune": [], "equipments": [-1, -1, -1], "exp": 0, "level": 1, "miSkill": [{"invalid": false, "isLock": 0, "skillId": 0}, {"invalid": false, "isLock": 0, "skillId": 0}, {"invalid": false, "isLock": 0, "skillId": 0}, {"invalid": false, "isLock": 0, "skillId": 0}, {"invalid": false, "isLock": 0, "skillId": 0}, {"invalid": false, "isLock": 0, "skillId": 0}, {"invalid": false, "isLock": 0, "skillId": 0}, {"invalid": ... <truncated; see decoded/decoded_packets.json for full payload>
      ```

### Packet 134 — `134.bin` — DOWN server → client

- **Timestamp ms**: `1780601527452`
- **TCP chunk length**: `2560` bytes
- **Frame(s)**: `136`
  - **Frame 136**; spans segments `[133, 134, 135, 136]`
    - Header: `5dfcba94001f43010e40100000000040`
    - Total length: `8003` bytes; codec: `zlib`; format: `json_response`
    - Func: `PetSummonQueryResult`
    - Nội dung decoded:
      ```json
      [{"func": "PetSummonQueryResult", "petList": [{"AfinityExp": 0, "AfinityLevel": 0, "FettersExp": 0, "FettersLevel": 0, "Fighting": 0, "HouYuanID": 0, "IsFollow": 0, "IsLock": 0, "MarkType": 0, "PetBaseZiZhi": [15, 31, 27, 18, 25, 57], "PetBreakZiZhi": [-1, -1, -1, -1, -1, -1], "PetConfigID": 22279, "PetParams": [], "QiangHuaExp": 0, "QiangHuaLevel": 0, "TeXingIdList": [20411], "XingGeID": 1015, "aidRune": [], "equipments": [-1, -1, -1], "exp": 0, "level": 1, "miSkill": [{"invalid": false, "isLock": 0, "skillId": 0}, {"invalid": false, "isLock": 0, "skillId": 0}, {"invalid": false, "isLock": 0, "skillId": 0}, {"invalid": false, "isLock": 0, "skillId": 0}, {"invalid": false, "isLock": 0, "skillId": 0}, {"invalid": false, "isLock": 0, "skillId": 0}, {"invalid": false, "isLock": 0, "skillId": 0}, {"invalid": false, "isLock": 0, "skillId": 0}], "name": "Lilie's Snowy", "petInfo": {"petAttr": [], "petId": 114, "skillId": [222790, 222791, 222792, 222793, 222794], "skillLevel": [0, 1, 0, 0, 0]}, "sex": 0, "skillLock": 0}, {"AfinityExp": 0, "AfinityLevel": 0, "FettersExp": 0, "FettersLevel": 0, "Fighting": 0, "HouYuanID": 0, "IsFollow": 0, "IsLock": 0, "MarkType": 0, "PetBaseZiZhi": [45, 25, 45, 20, 27, 53], "PetBreakZiZhi": [-1, -1, -1, -1, -1, -1], "PetConfigID": 23441, "PetParams": [], "QiangHuaExp": 0, "QiangHuaLevel": 0, "TeXingIdList": [20180], "XingGeID": 1018, "aidRune": [], "equipments": [-1, -1, -1], "exp": 0, "level": 1, "miSkill": [{"invalid": false, "isLock": 0, "skillId": 0}, {"invalid": false, "isLock": 0, "skillId": 0}, {"invalid": false, "isLock": 0, "skillId": 0}, {"invalid": false, "isLock": 0, "skillId": 0}, {"invalid": false, "isLock": 0, "skillId": 0}, {"invalid": false, "isLock": 0, "skillId": 0}, {"invalid": false, "isLock": 0, "skillId": 0}, {"invalid": ... <truncated; see decoded/decoded_packets.json for full payload>
      ```

### Packet 135 — `135.bin` — DOWN server → client

- **Timestamp ms**: `1780601527453`
- **TCP chunk length**: `2560` bytes
- **Frame(s)**: `136`
  - **Frame 136**; spans segments `[133, 134, 135, 136]`
    - Header: `5dfcba94001f43010e40100000000040`
    - Total length: `8003` bytes; codec: `zlib`; format: `json_response`
    - Func: `PetSummonQueryResult`
    - Nội dung decoded:
      ```json
      [{"func": "PetSummonQueryResult", "petList": [{"AfinityExp": 0, "AfinityLevel": 0, "FettersExp": 0, "FettersLevel": 0, "Fighting": 0, "HouYuanID": 0, "IsFollow": 0, "IsLock": 0, "MarkType": 0, "PetBaseZiZhi": [15, 31, 27, 18, 25, 57], "PetBreakZiZhi": [-1, -1, -1, -1, -1, -1], "PetConfigID": 22279, "PetParams": [], "QiangHuaExp": 0, "QiangHuaLevel": 0, "TeXingIdList": [20411], "XingGeID": 1015, "aidRune": [], "equipments": [-1, -1, -1], "exp": 0, "level": 1, "miSkill": [{"invalid": false, "isLock": 0, "skillId": 0}, {"invalid": false, "isLock": 0, "skillId": 0}, {"invalid": false, "isLock": 0, "skillId": 0}, {"invalid": false, "isLock": 0, "skillId": 0}, {"invalid": false, "isLock": 0, "skillId": 0}, {"invalid": false, "isLock": 0, "skillId": 0}, {"invalid": false, "isLock": 0, "skillId": 0}, {"invalid": false, "isLock": 0, "skillId": 0}], "name": "Lilie's Snowy", "petInfo": {"petAttr": [], "petId": 114, "skillId": [222790, 222791, 222792, 222793, 222794], "skillLevel": [0, 1, 0, 0, 0]}, "sex": 0, "skillLock": 0}, {"AfinityExp": 0, "AfinityLevel": 0, "FettersExp": 0, "FettersLevel": 0, "Fighting": 0, "HouYuanID": 0, "IsFollow": 0, "IsLock": 0, "MarkType": 0, "PetBaseZiZhi": [45, 25, 45, 20, 27, 53], "PetBreakZiZhi": [-1, -1, -1, -1, -1, -1], "PetConfigID": 23441, "PetParams": [], "QiangHuaExp": 0, "QiangHuaLevel": 0, "TeXingIdList": [20180], "XingGeID": 1018, "aidRune": [], "equipments": [-1, -1, -1], "exp": 0, "level": 1, "miSkill": [{"invalid": false, "isLock": 0, "skillId": 0}, {"invalid": false, "isLock": 0, "skillId": 0}, {"invalid": false, "isLock": 0, "skillId": 0}, {"invalid": false, "isLock": 0, "skillId": 0}, {"invalid": false, "isLock": 0, "skillId": 0}, {"invalid": false, "isLock": 0, "skillId": 0}, {"invalid": false, "isLock": 0, "skillId": 0}, {"invalid": ... <truncated; see decoded/decoded_packets.json for full payload>
      ```

### Packet 136 — `136.bin` — DOWN server → client

- **Timestamp ms**: `1780601527453`
- **TCP chunk length**: `1431` bytes
- **Frame(s)**: `136`
  - **Frame 136**; spans segments `[133, 134, 135, 136]`
    - Header: `5dfcba94001f43010e40100000000040`
    - Total length: `8003` bytes; codec: `zlib`; format: `json_response`
    - Func: `PetSummonQueryResult`
    - Nội dung decoded:
      ```json
      [{"func": "PetSummonQueryResult", "petList": [{"AfinityExp": 0, "AfinityLevel": 0, "FettersExp": 0, "FettersLevel": 0, "Fighting": 0, "HouYuanID": 0, "IsFollow": 0, "IsLock": 0, "MarkType": 0, "PetBaseZiZhi": [15, 31, 27, 18, 25, 57], "PetBreakZiZhi": [-1, -1, -1, -1, -1, -1], "PetConfigID": 22279, "PetParams": [], "QiangHuaExp": 0, "QiangHuaLevel": 0, "TeXingIdList": [20411], "XingGeID": 1015, "aidRune": [], "equipments": [-1, -1, -1], "exp": 0, "level": 1, "miSkill": [{"invalid": false, "isLock": 0, "skillId": 0}, {"invalid": false, "isLock": 0, "skillId": 0}, {"invalid": false, "isLock": 0, "skillId": 0}, {"invalid": false, "isLock": 0, "skillId": 0}, {"invalid": false, "isLock": 0, "skillId": 0}, {"invalid": false, "isLock": 0, "skillId": 0}, {"invalid": false, "isLock": 0, "skillId": 0}, {"invalid": false, "isLock": 0, "skillId": 0}], "name": "Lilie's Snowy", "petInfo": {"petAttr": [], "petId": 114, "skillId": [222790, 222791, 222792, 222793, 222794], "skillLevel": [0, 1, 0, 0, 0]}, "sex": 0, "skillLock": 0}, {"AfinityExp": 0, "AfinityLevel": 0, "FettersExp": 0, "FettersLevel": 0, "Fighting": 0, "HouYuanID": 0, "IsFollow": 0, "IsLock": 0, "MarkType": 0, "PetBaseZiZhi": [45, 25, 45, 20, 27, 53], "PetBreakZiZhi": [-1, -1, -1, -1, -1, -1], "PetConfigID": 23441, "PetParams": [], "QiangHuaExp": 0, "QiangHuaLevel": 0, "TeXingIdList": [20180], "XingGeID": 1018, "aidRune": [], "equipments": [-1, -1, -1], "exp": 0, "level": 1, "miSkill": [{"invalid": false, "isLock": 0, "skillId": 0}, {"invalid": false, "isLock": 0, "skillId": 0}, {"invalid": false, "isLock": 0, "skillId": 0}, {"invalid": false, "isLock": 0, "skillId": 0}, {"invalid": false, "isLock": 0, "skillId": 0}, {"invalid": false, "isLock": 0, "skillId": 0}, {"invalid": false, "isLock": 0, "skillId": 0}, {"invalid": ... <truncated; see decoded/decoded_packets.json for full payload>
      ```

### Packet 137 — `137.bin` — UP client → server

- **Timestamp ms**: `1780601527478`
- **TCP chunk length**: `149` bytes
- **Frame(s)**: `137`
  - **Frame 137**
    - Header: `30c80515000095000000000000000041`
    - Total length: `149` bytes; codec: `plain`; format: `urlencoded_request`
    - Func: `OnceRewardQuery`
    - Query fields: `{"bv": "7.0.2", "seq": "65", "session": "02D1B0135ABCDC0D", "sptype": "spv2jodo", "version": "7.0.2"}`
    - Nội dung decoded:
      ```json
      [{"func": "OnceRewardQuery"}]
      ```

### Packet 138 — `138.bin` — DOWN server → client

- **Timestamp ms**: `1780601527503`
- **TCP chunk length**: `67` bytes
- **Frame(s)**: `138`
  - **Frame 138**
    - Header: `5438e784000043000e40100000000041`
    - Total length: `67` bytes; codec: `plain`; format: `json_response`
    - Func: `OnceRewardQueryResult`
    - Nội dung decoded:
      ```json
      [{"func": "OnceRewardQueryResult", "valueList": []}]
      ```

### Packet 139 — `139.bin` — UP client → server

- **Timestamp ms**: `1780601527527`
- **TCP chunk length**: `154` bytes
- **Frame(s)**: `139`
  - **Frame 139**
    - Header: `58b551f400009a000000000000000042`
    - Total length: `154` bytes; codec: `plain`; format: `urlencoded_request`
    - Func: `PetCoordinationQuery`
    - Query fields: `{"bv": "7.0.2", "seq": "66", "session": "02D1B0135ABCDC0D", "sptype": "spv2jodo", "version": "7.0.2"}`
    - Nội dung decoded:
      ```json
      [{"func": "PetCoordinationQuery"}]
      ```

### Packet 140 — `140.bin` — DOWN server → client

- **Timestamp ms**: `1780601527553`
- **TCP chunk length**: `85` bytes
- **Frame(s)**: `140`
  - **Frame 140**
    - Header: `432d6bf6000055000e40100000000042`
    - Total length: `85` bytes; codec: `plain`; format: `json_response`
    - Func: `PetCoordinationQueryResult`
    - Nội dung decoded:
      ```json
      [{"func": "PetCoordinationQueryResult", "petFriend": [], "petSelf": []}]
      ```

### Packet 141 — `141.bin` — UP client → server

- **Timestamp ms**: `1780601527579`
- **TCP chunk length**: `152` bytes
- **Frame(s)**: `141`
  - **Frame 141**
    - Header: `02eb8e1b000098000000000000000043`
    - Total length: `152` bytes; codec: `plain`; format: `urlencoded_request`
    - Func: `PetExpeditionQuery`
    - Query fields: `{"bv": "7.0.2", "seq": "67", "session": "02D1B0135ABCDC0D", "sptype": "spv2jodo", "version": "7.0.2"}`
    - Nội dung decoded:
      ```json
      [{"func": "PetExpeditionQuery"}]
      ```

### Packet 142 — `142.bin` — DOWN server → client

- **Timestamp ms**: `1780601527604`
- **TCP chunk length**: `181` bytes
- **Frame(s)**: `142`
  - **Frame 142**
    - Header: `e989287b0000b5000e40100000000043`
    - Total length: `181` bytes; codec: `plain`; format: `json_response`
    - Func: `PetExpeditionQueryResult`
    - Nội dung decoded:
      ```json
      [{"func": "PetExpeditionQueryResult", "info": {"missionAccected": [], "missionList": [30007, 30012, 10001], "missionRunning": [], "pidUsedList": [], "refreshTime": 1780601400}}]
      ```

### Packet 143 — `143.bin` — UP client → server

- **Timestamp ms**: `1780601527636`
- **TCP chunk length**: `170` bytes
- **Frame(s)**: `143`
  - **Frame 143**
    - Header: `be6bacc40000aa000000000000000044`
    - Total length: `170` bytes; codec: `plain`; format: `urlencoded_request`
    - Func: `DaoguanInfoQuery`
    - Query fields: `{"bv": "7.0.2", "seq": "68", "session": "02D1B0135ABCDC0D", "sptype": "spv2jodo", "version": "7.0.2"}`
    - Nội dung decoded:
      ```json
      [{"func": "DaoguanInfoQuery", "skillId": 0}]
      ```

### Packet 144 — `144.bin` — DOWN server → client

- **Timestamp ms**: `1780601527662`
- **TCP chunk length**: `97` bytes
- **Frame(s)**: `144`
  - **Frame 144**
    - Header: `cb00974f000061000e40100000000044`
    - Total length: `97` bytes; codec: `plain`; format: `json_response`
    - Func: `DaoguanInfoQueryResult`
    - Nội dung decoded:
      ```json
      [{"coreList": [], "func": "DaoguanInfoQueryResult", "infoList": [], "numberList": []}]
      ```

### Packet 145 — `145.bin` — UP client → server

- **Timestamp ms**: `1780601527690`
- **TCP chunk length**: `146` bytes
- **Frame(s)**: `145`
  - **Frame 145**
    - Header: `adfee7ee000092000000000000000045`
    - Total length: `146` bytes; codec: `plain`; format: `urlencoded_request`
    - Func: `WaiguanQuery`
    - Query fields: `{"bv": "7.0.2", "seq": "69", "session": "02D1B0135ABCDC0D", "sptype": "spv2jodo", "version": "7.0.2"}`
    - Nội dung decoded:
      ```json
      [{"func": "WaiguanQuery"}]
      ```

### Packet 146 — `146.bin` — DOWN server → client

- **Timestamp ms**: `1780601527716`
- **TCP chunk length**: `66` bytes
- **Frame(s)**: `146`
  - **Frame 146**
    - Header: `9c943d6e000042000e40100000000045`
    - Total length: `66` bytes; codec: `plain`; format: `json_response`
    - Func: `WaiguanQueryResult`
    - Nội dung decoded:
      ```json
      [{"func": "WaiguanQueryResult", "waiguanList": []}]
      ```

### Packet 147 — `147.bin` — UP client → server

- **Timestamp ms**: `1780601527745`
- **TCP chunk length**: `150` bytes
- **Frame(s)**: `147`
  - **Frame 147**
    - Header: `eec9aa1d000096000000000000000046`
    - Total length: `150` bytes; codec: `plain`; format: `urlencoded_request`
    - Func: `BattleTowerQuery`
    - Query fields: `{"bv": "7.0.2", "seq": "70", "session": "02D1B0135ABCDC0D", "sptype": "spv2jodo", "version": "7.0.2"}`
    - Nội dung decoded:
      ```json
      [{"func": "BattleTowerQuery"}]
      ```

### Packet 148 — `148.bin` — DOWN server → client

- **Timestamp ms**: `1780601527771`
- **TCP chunk length**: `248` bytes
- **Frame(s)**: `148`
  - **Frame 148**
    - Header: `1dac57410000f8000e40100000000046`
    - Total length: `248` bytes; codec: `plain`; format: `json_response`
    - Func: `BattleTowerQueryResult`
    - Nội dung decoded:
      ```json
      [{"func": "BattleTowerQueryResult", "mode": 0, "petList": [], "status": {"awardPickId": 0, "buffList": [], "coin": 0, "curLevel": 0, "finishAwardList": [], "lootBuffBox": [], "maxLevel": 0, "opponentIndex": 0, "opponentList": [], "point": 0, "pointSum": 0}}]
      ```

### Packet 149 — `149.bin` — UP client → server

- **Timestamp ms**: `1780601527796`
- **TCP chunk length**: `157` bytes
- **Frame(s)**: `149`
  - **Frame 149**
    - Header: `3ad4c37f00009d000000000000000047`
    - Total length: `157` bytes; codec: `plain`; format: `urlencoded_request`
    - Func: `ChampionLeagueQueryTime`
    - Query fields: `{"bv": "7.0.2", "seq": "71", "session": "02D1B0135ABCDC0D", "sptype": "spv2jodo", "version": "7.0.2"}`
    - Nội dung decoded:
      ```json
      [{"func": "ChampionLeagueQueryTime"}]
      ```

### Packet 150 — `150.bin` — DOWN server → client

- **Timestamp ms**: `1780601527822`
- **TCP chunk length**: `189` bytes
- **Frame(s)**: `150`
  - **Frame 150**
    - Header: `f8eec04c0000bd000e40100000000047`
    - Total length: `189` bytes; codec: `plain`; format: `json_response`
    - Func: `ChampionLeagueQueryTimeResult`
    - Nội dung decoded:
      ```json
      [{"func": "ChampionLeagueQueryTimeResult", "setcion": [1, -1, 1, -1, 1, -1, 1, -1], "time": [1780542000, 1780552800, 1780563600, 1780570800, 1780628400, 1780639200, 1780650000, 1780657200]}]
      ```

### Packet 151 — `151.bin` — UP client → server

- **Timestamp ms**: `1780601527847`
- **TCP chunk length**: `149` bytes
- **Frame(s)**: `151`
  - **Frame 151**
    - Header: `1bdb716d000095000000000000000048`
    - Total length: `149` bytes; codec: `plain`; format: `urlencoded_request`
    - Func: `ReturnGiftQuery`
    - Query fields: `{"bv": "7.0.2", "seq": "72", "session": "02D1B0135ABCDC0D", "sptype": "spv2jodo", "version": "7.0.2"}`
    - Nội dung decoded:
      ```json
      [{"func": "ReturnGiftQuery"}]
      ```

### Packet 152 — `152.bin` — DOWN server → client

- **Timestamp ms**: `1780601527873`
- **TCP chunk length**: `141` bytes
- **Frame(s)**: `152`
  - **Frame 152**
    - Header: `2833be3300008d000e40100000000048`
    - Total length: `141` bytes; codec: `plain`; format: `json_response`
    - Func: `ReturnGiftQueryResult`
    - Nội dung decoded:
      ```json
      [{"func": "ReturnGiftQueryResult", "returnGift": {"buyCount": [], "giftCharge": [], "giftFree": [], "onlineDays": 0, "returnTime": 0}}]
      ```

### Packet 153 — `153.bin` — UP client → server

- **Timestamp ms**: `1780601527899`
- **TCP chunk length**: `153` bytes
- **Frame(s)**: `153`
  - **Frame 153**
    - Header: `fe5ed839000099000000000000000049`
    - Total length: `153` bytes; codec: `plain`; format: `urlencoded_request`
    - Func: `GlobalGuildWarQuery`
    - Query fields: `{"bv": "7.0.2", "seq": "73", "session": "02D1B0135ABCDC0D", "sptype": "spv2jodo", "version": "7.0.2"}`
    - Nội dung decoded:
      ```json
      [{"func": "GlobalGuildWarQuery"}]
      ```

### Packet 154 — `154.bin` — DOWN server → client

- **Timestamp ms**: `1780601527927`
- **TCP chunk length**: `177` bytes
- **Frame(s)**: `154`
  - **Frame 154**
    - Header: `8a1287130000b1000e40100000000049`
    - Total length: `177` bytes; codec: `plain`; format: `json_response`
    - Func: `GlobalGuildWarQueryResult`
    - Nội dung decoded:
      ```json
      [{"func": "GlobalGuildWarQueryResult", "status": {"awardList": [], "buyCount": 0, "fightCount": 0, "inspireCount": [], "point": 0, "winCombo": 0}, "timeEnd": 0, "timeStart": 0}]
      ```

### Packet 155 — `155.bin` — UP client → server

- **Timestamp ms**: `1780601527956`
- **TCP chunk length**: `157` bytes
- **Frame(s)**: `155`
  - **Frame 155**
    - Header: `a0d6c62400009d00000000000000004a`
    - Total length: `157` bytes; codec: `plain`; format: `urlencoded_request`
    - Func: `DaoguanSkillAwakenQuery`
    - Query fields: `{"bv": "7.0.2", "seq": "74", "session": "02D1B0135ABCDC0D", "sptype": "spv2jodo", "version": "7.0.2"}`
    - Nội dung decoded:
      ```json
      [{"func": "DaoguanSkillAwakenQuery"}]
      ```

### Packet 156 — `156.bin` — DOWN server → client

- **Timestamp ms**: `1780601527984`
- **TCP chunk length**: `74` bytes
- **Frame(s)**: `156`
  - **Frame 156**
    - Header: `338dc7b400004a000e4010000000004a`
    - Total length: `74` bytes; codec: `plain`; format: `json_response`
    - Func: `DaoguanSkillAwakenQueryResult`
    - Nội dung decoded:
      ```json
      [{"attrList": [], "func": "DaoguanSkillAwakenQueryResult"}]
      ```

### Packet 157 — `157.bin` — UP client → server

- **Timestamp ms**: `1780601528009`
- **TCP chunk length**: `166` bytes
- **Frame(s)**: `157`
  - **Frame 157**
    - Header: `23d46a300000a600000000000000004b`
    - Total length: `166` bytes; codec: `plain`; format: `urlencoded_request`
    - Func: `LeagueTripQuery`
    - Query fields: `{"bv": "7.0.2", "seq": "75", "session": "02D1B0135ABCDC0D", "sptype": "spv2jodo", "version": "7.0.2"}`
    - Nội dung decoded:
      ```json
      [{"func": "LeagueTripQuery", "ltId": 0}]
      ```

### Packet 158 — `158.bin` — DOWN server → client

- **Timestamp ms**: `1780601528035`
- **TCP chunk length**: `111` bytes
- **Frame(s)**: `158`
  - **Frame 158**
    - Header: `cf6e866400006f000e4010000000004b`
    - Total length: `111` bytes; codec: `plain`; format: `json_response`
    - Func: `LeagueTripQueryResult`
    - Nội dung decoded:
      ```json
      [{"func": "LeagueTripQueryResult", "ltDailyChallengeRestCnt": 0, "ltDailyRestCnt": 0, "ltList": []}]
      ```

### Packet 159 — `159.bin` — UP client → server

- **Timestamp ms**: `1780601528059`
- **TCP chunk length**: `147` bytes
- **Frame(s)**: `159`
  - **Frame 159**
    - Header: `facd576700009300000000000000004c`
    - Total length: `147` bytes; codec: `plain`; format: `urlencoded_request`
    - Func: `WishStarQuery`
    - Query fields: `{"bv": "7.0.2", "seq": "76", "session": "02D1B0135ABCDC0D", "sptype": "spv2jodo", "version": "7.0.2"}`
    - Nội dung decoded:
      ```json
      [{"func": "WishStarQuery"}]
      ```

### Packet 160 — `160.bin` — DOWN server → client

- **Timestamp ms**: `1780601528087`
- **TCP chunk length**: `92` bytes
- **Frame(s)**: `160`
  - **Frame 160**
    - Header: `e69bda6200005c000e4010000000004c`
    - Total length: `92` bytes; codec: `plain`; format: `json_response`
    - Func: `WishStarQueryResult`
    - Nội dung decoded:
      ```json
      [{"func": "WishStarQueryResult", "nextLottery": 1, "platList": [], "wslist": []}]
      ```

### Packet 161 — `161.bin` — UP client → server

- **Timestamp ms**: `1780601528114`
- **TCP chunk length**: `148` bytes
- **Frame(s)**: `161`
  - **Frame 161**
    - Header: `1d4f7e4700009400000000000000004d`
    - Total length: `148` bytes; codec: `plain`; format: `urlencoded_request`
    - Func: `AtlasInfoQuery`
    - Query fields: `{"bv": "7.0.2", "seq": "77", "session": "02D1B0135ABCDC0D", "sptype": "spv2jodo", "version": "7.0.2"}`
    - Nội dung decoded:
      ```json
      [{"func": "AtlasInfoQuery"}]
      ```

### Packet 162 — `162.bin` — DOWN server → client

- **Timestamp ms**: `1780601528140`
- **TCP chunk length**: `119` bytes
- **Frame(s)**: `162`
  - **Frame 162**
    - Header: `74f3b00d000077000e4010000000004d`
    - Total length: `119` bytes; codec: `plain`; format: `json_response`
    - Func: `AtlasInfoQueryResult`
    - Nội dung decoded:
      ```json
      [{"atlasArray": [], "cardArray": [], "friendPoint": 0, "friendProofLevel": 0, "func": "AtlasInfoQueryResult"}]
      ```

### Packet 163 — `163.bin` — UP client → server

- **Timestamp ms**: `1780601528170`
- **TCP chunk length**: `170` bytes
- **Frame(s)**: `163`
  - **Frame 163**
    - Header: `ae051be10000aa00000000000000004e`
    - Total length: `170` bytes; codec: `plain`; format: `urlencoded_request`
    - Func: `DaoguanOwnerQuery`
    - Query fields: `{"bv": "7.0.2", "seq": "78", "session": "02D1B0135ABCDC0D", "sptype": "spv2jodo", "version": "7.0.2"}`
    - Nội dung decoded:
      ```json
      [{"dgId": 501, "func": "DaoguanOwnerQuery"}]
      ```

### Packet 164 — `164.bin` — DOWN server → client

- **Timestamp ms**: `1780601528196`
- **TCP chunk length**: `1048` bytes
- **Frame(s)**: `164`
  - **Frame 164**
    - Header: `8da08e3e000418010e4010000000004e`
    - Total length: `1048` bytes; codec: `zlib`; format: `json_response`
    - Func: `DaoguanOwnerQueryResult`
    - Nội dung decoded:
      ```json
      [{"dgId": 501, "func": "DaoguanOwnerQueryResult", "ownerList": [{"comboWin": 53, "defenderPet": {"paraList": [6500534, 1001, 81, 45400, 0, 28, 0, 0, 0, 0, 0], "petIdList": [300, 30, 272, 0], "petList": [{"petAttr": [688113, 105678, 109242, 59187, 61769, 59108, 1052, 69, 411, 488, 121, 23522, 90358, 3799647, 0, 0, 0, 0], "petId": 1023522, "skillId": [31075, 31074, 2201, 1101, 2202, 935222, 31079, 2204, 935223, 2205, 935220, 2206, 935221, 31076, 31083, 4263, 31085, 31102, 31100, 235224, 235222, 235223, 235220, 31055, 235221, 31054, 31056, 31057, 31058, 40006, 4253, 31065, 31070, 4192, 4203, 20862, 30303, 30293, 20112, 31118, 72018, 72016, 31115, 31108, 31104, 50002, 50001, 400011, 31128, 400012, 30150, 400013, 31120, 31123], "skillLevel": [1, 1, 13, 2, 7, 84, 1, 7, 84, 7, 84, 8, 84, 1, 1, 1, 1, 1, 1, 84, 84, 84, 84, 9, 84, 12, 10, 10, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 10, 9, 1, 1, 1, 1, 1, 1, 1]}, {"petAttr": [509349, 47405, 51197, 37603, 42715, 5542, 1046, 69, 291, 488, 115, 21461, 0, 1554507, 0, 0, 0, 0], "petId": 21461, "skillId": [31075, 1101, 2201, 31074, 2202, 30132, 2204, 31079, 2205, 2206, 31076, 214614, 31083, 30142, 214612, 214613, 214610, 214611, 31085, 20411, 31102, 31100, 31118, 30162, 31115, 31108, 30240, 31104, 50002, 50001, 31055, 31054, 31056, 31057, 31058, 31128, 30150, 31065, 31120, 31070], "skillLevel": [1, 2, 13, 1, 7, 1, 7, 1, 7, 8, 1, 77, 1, 1, 77, 77, 77, 77, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 10, 9, 9, 12, 10, 10, 1, 1, 1, 1, 1, 1]}, {"petAttr": [425442, 34293, 41106, 21236, 25377, 5995, 1046, 69, 371, 488, 415, 20441, 0, 1048690, 0, 0, 0, 0], "petId": 20441, "skillId": [31075, 1101, 2201, 31074, 2202, 30132, 2204, 31079, 2205, 2206, 31076, 31083, 31085, 204411, 204410, 204413, 204412, 204414, 31102, 31100, 20302, 31118, 30162, 31115, ... <truncated; see decoded/decoded_packets.json for full payload>
      ```

### Packet 165 — `165.bin` — UP client → server

- **Timestamp ms**: `1780601528221`
- **TCP chunk length**: `170` bytes
- **Frame(s)**: `165`
  - **Frame 165**
    - Header: `8962e53f0000aa00000000000000004f`
    - Total length: `170` bytes; codec: `plain`; format: `urlencoded_request`
    - Func: `DaoguanOwnerQuery`
    - Query fields: `{"bv": "7.0.2", "seq": "79", "session": "02D1B0135ABCDC0D", "sptype": "spv2jodo", "version": "7.0.2"}`
    - Nội dung decoded:
      ```json
      [{"dgId": 502, "func": "DaoguanOwnerQuery"}]
      ```

### Packet 166 — `166.bin` — DOWN server → client

- **Timestamp ms**: `1780601528247`
- **TCP chunk length**: `958` bytes
- **Frame(s)**: `166`
  - **Frame 166**
    - Header: `70c7814a0003be010e4010000000004f`
    - Total length: `958` bytes; codec: `zlib`; format: `json_response`
    - Func: `DaoguanOwnerQueryResult`
    - Nội dung decoded:
      ```json
      [{"dgId": 502, "func": "DaoguanOwnerQueryResult", "ownerList": [{"comboWin": 11, "defenderPet": {"paraList": [2699806, 1004, 50, 17000, 0, 28, 0, 0, 0, 0, 0], "petIdList": [177, 260, 254], "petList": [{"petAttr": [277769, 62891, 29147, 22313, 19140, 12039, 1121, 132, 411, 304, 1019, 23502, 90351, 1484158, 0, 0, 0, 0], "petId": 1023502, "skillId": [30133, 23501, 4193, 46525, 935021, 31083, 935020, 935023, 935022, 24220, 20862, 4213, 80060, 4093, 235024, 72016, 31051, 31104, 50002, 400011, 40007, 30150, 400012, 4254, 235022, 235023, 31065, 235020, 235021, 31067, 31068, 31069, 31123, 31070, 21172], "skillLevel": [1, 1, 1, 1, 76, 1, 76, 76, 76, 1, 1, 1, 1, 1, 76, 1, 1, 1, 9, 1, 1, 1, 1, 1, 76, 76, 1, 76, 76, 1, 1, 1, 1, 1, 1]}, {"petAttr": [226840, 35931, 23816, 19520, 19523, 6059, 1121, 132, 411, 304, 1003, 23602, 90351, 891809, 0, 0, 0, 0], "petId": 1023602, "skillId": [30133, 31083, 23601, 236022, 236023, 236020, 236021, 46625, 936022, 936023, 936020, 31051, 936021, 20830, 31104, 50002, 236024, 40001, 4313, 4253, 30150, 31065, 31067, 31068, 31069, 31070, 31122], "skillLevel": [1, 1, 1, 76, 76, 76, 76, 1, 76, 76, 76, 1, 76, 1, 1, 9, 76, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]}, {"petAttr": [138074, 14278, 13057, 6105, 6303, 3297, 1121, 132, 291, 304, 1016, 22571, 0, 275839, 0, 0, 0, 0], "petId": 22571, "skillId": [225711, 20031, 31083, 31065, 31051, 31067, 31068, 31104, 31069, 50002, 31070], "skillLevel": [1, 1, 1, 1, 1, 1, 1, 1, 1, 9, 1]}]}, "show": {"avatarID": "d660c65e-c3d0-43ba-9e46-3eae52dce466", "avatarName": "⚘Civic", "battlePoint": 2788500, "campId": 2, "chengHaoID": 1022, "comboWin": 11, "comboWinMax": 15, "contentID": 1009, "dollId": 0, "dollName": "", "fightCountTotal": 154, "fightCountWin": 119, "guild": "SG⚘GĐ", "guildId": 195123642, "headFrame": 0, "lastActive": 1780... <truncated; see decoded/decoded_packets.json for full payload>
      ```

### Packet 167 — `167.bin` — UP client → server

- **Timestamp ms**: `1780601528273`
- **TCP chunk length**: `170` bytes
- **Frame(s)**: `167`
  - **Frame 167**
    - Header: `becd700b0000aa000000000000000050`
    - Total length: `170` bytes; codec: `plain`; format: `urlencoded_request`
    - Func: `DaoguanOwnerQuery`
    - Query fields: `{"bv": "7.0.2", "seq": "80", "session": "02D1B0135ABCDC0D", "sptype": "spv2jodo", "version": "7.0.2"}`
    - Nội dung decoded:
      ```json
      [{"dgId": 503, "func": "DaoguanOwnerQuery"}]
      ```

### Packet 168 — `168.bin` — DOWN server → client

- **Timestamp ms**: `1780601528306`
- **TCP chunk length**: `1014` bytes
- **Frame(s)**: `168`
  - **Frame 168**
    - Header: `4544495c0003f6010e40100000000050`
    - Total length: `1014` bytes; codec: `zlib`; format: `json_response`
    - Func: `DaoguanOwnerQueryResult`
    - Nội dung decoded:
      ```json
      [{"dgId": 503, "func": "DaoguanOwnerQueryResult", "ownerList": [{"comboWin": 4, "defenderPet": {"paraList": [4917809, 0, 0, 0, 0, 28, 0, 0, 0, 0, 0], "petIdList": [264, 73, 194], "petList": [{"petAttr": [602765, 77091, 71125, 40159, 36341, 12729, 1121, 176, 515, 566, 121, 23522, 90358, 2259371, 0, 0, 0, 0], "petId": 1023522, "skillId": [1101, 2201, 1102, 2202, 30133, 935222, 31079, 935223, 935220, 2206, 935221, 31083, 20862, 4213, 4284, 4998, 31097, 235224, 20182, 31118, 31112, 72018, 72016, 31115, 31108, 31051, 235222, 235223, 31105, 235220, 235221, 400011, 40006, 400014, 31128, 30150, 400012, 4254, 42707, 31065, 31120, 31123, 30262, 31070], "skillLevel": [2, 6, 2, 12, 1, 81, 1, 81, 81, 13, 81, 1, 1, 1, 1, 1, 1, 81, 1, 1, 1, 1, 1, 1, 1, 1, 81, 81, 1, 81, 81, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]}, {"petAttr": [549646, 59318, 33892, 36511, 31844, 9374, 1121, 176, 515, 566, 411, 20051, 0, 1498456, 0, 0, 0, 0], "petId": 1020051, "skillId": [1101, 2201, 1102, 2202, 30133, 31079, 43007, 2206, 31083, 200513, 200512, 200514, 31097, 20112, 200511, 31118, 31112, 40017, 31115, 31108, 31051, 31105, 2005104, 31128, 31065, 31120, 30262, 31070], "skillLevel": [2, 6, 2, 12, 1, 1, 1, 13, 1, 81, 81, 81, 1, 1, 81, 1, 1, 1, 1, 1, 1, 1, 81, 1, 1, 1, 1, 1]}, {"petAttr": [412650, 39460, 37658, 21642, 20120, 7520, 1121, 176, 515, 566, 104, 21511, 0, 1115762, 0, 0, 0, 0], "petId": 1021511, "skillId": [1101, 2201, 1102, 30133, 20212, 2202, 31079, 2206, 31083, 31097, 31118, 215111, 31112, 215110, 31115, 31108, 215113, 31051, 215112, 31105, 46707, 31128, 30150, 31065, 31120, 31070], "skillLevel": [2, 6, 2, 1, 1, 12, 1, 13, 1, 1, 1, 65, 1, 71, 1, 1, 65, 1, 71, 1, 1, 1, 1, 1, 1, 1]}]}, "show": {"avatarID": "d4df0223-ca5d-48f7-9a50-fb408ca21915", "avatarName": "Gió⚘MD", "battlePoint": 6120383, "ca... <truncated; see decoded/decoded_packets.json for full payload>
      ```

### Packet 169 — `169.bin` — UP client → server

- **Timestamp ms**: `1780601528336`
- **TCP chunk length**: `170` bytes
- **Frame(s)**: `169`
  - **Frame 169**
    - Header: `61d14e290000aa000000000000000051`
    - Total length: `170` bytes; codec: `plain`; format: `urlencoded_request`
    - Func: `DaoguanOwnerQuery`
    - Query fields: `{"bv": "7.0.2", "seq": "81", "session": "02D1B0135ABCDC0D", "sptype": "spv2jodo", "version": "7.0.2"}`
    - Nội dung decoded:
      ```json
      [{"dgId": 504, "func": "DaoguanOwnerQuery"}]
      ```

### Packet 170 — `170.bin` — DOWN server → client

- **Timestamp ms**: `1780601528369`
- **TCP chunk length**: `1033` bytes
- **Frame(s)**: `170`
  - **Frame 170**
    - Header: `20367e4a000409010e40100000000051`
    - Total length: `1033` bytes; codec: `zlib`; format: `json_response`
    - Func: `DaoguanOwnerQueryResult`
    - Nội dung decoded:
      ```json
      [{"dgId": 504, "func": "DaoguanOwnerQueryResult", "ownerList": [{"comboWin": 2, "defenderPet": {"paraList": [5279278, 1004, 80, 32000, 0, 28, 0, 0, 0, 0, 0], "petIdList": [234, 25, 258, 0], "petList": [{"petAttr": [517698, 82493, 53225, 36006, 31254, 13743, 1064, 44, 425, 380, 1019, 23502, 90351, 2167123, 0, 0, 0, 0], "petId": 1023502, "skillId": [31075, 2202, 30133, 23501, 2206, 4133, 46525, 31076, 935021, 31083, 935020, 935023, 935022, 20862, 31085, 30303, 4212, 80060, 31097, 31102, 4093, 31103, 31100, 31101, 72021, 30163, 235024, 4172, 30310, 400011, 40007, 4054, 400014, 30150, 400012, 235022, 235023, 31065, 235020, 235021, 31120, 31123, 31070], "skillLevel": [1, 20, 1, 1, 3, 1, 1, 1, 80, 1, 80, 80, 80, 1, 1, 1, 1, 3, 1, 1, 1, 1, 1, 1, 1, 1, 80, 1, 1, 1, 1, 1, 1, 1, 1, 80, 80, 1, 80, 80, 1, 1, 1]}, {"petAttr": [463060, 43951, 32763, 30196, 32206, 6104, 1062, 44, 425, 380, 411, 20051, 0, 1322200, 0, 0, 0, 0], "petId": 1020051, "skillId": [31075, 2005134, 30133, 2202, 2206, 31076, 31083, 31085, 200512, 200514, 31097, 31102, 31103, 31100, 31101, 20112, 200511, 40017, 2005106, 30150, 31065, 31120, 31070], "skillLevel": [1, 80, 1, 20, 3, 1, 1, 1, 80, 80, 1, 1, 1, 1, 1, 1, 80, 1, 80, 1, 1, 1, 1]}, {"petAttr": [459544, 55941, 39180, 37629, 38360, 6812, 1062, 44, 425, 380, 1003, 23602, 90351, 1717395, 0, 0, 0, 0], "petId": 1023602, "skillId": [31075, 2202, 30133, 2206, 31076, 31083, 4074, 31085, 23601, 20832, 4221, 31097, 31102, 31103, 31100, 31101, 236022, 236023, 236020, 4033, 30163, 236021, 46625, 936022, 40028, 936023, 936020, 936021, 236024, 30150, 31065, 72011, 31120, 31070, 31122], "skillLevel": [1, 20, 1, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 80, 80, 80, 1, 1, 80, 1, 80, 1, 80, 80, 80, 80, 1, 1, 1, 1, 1, 1]}]}, "show": {"avatarID": "8d413ef0-b103-4b88-bf45-db611d162... <truncated; see decoded/decoded_packets.json for full payload>
      ```

### Packet 171 — `171.bin` — UP client → server

- **Timestamp ms**: `1780601528401`
- **TCP chunk length**: `170` bytes
- **Frame(s)**: `171`
  - **Frame 171**
    - Header: `82de8db70000aa000000000000000052`
    - Total length: `170` bytes; codec: `plain`; format: `urlencoded_request`
    - Func: `DaoguanOwnerQuery`
    - Query fields: `{"bv": "7.0.2", "seq": "82", "session": "02D1B0135ABCDC0D", "sptype": "spv2jodo", "version": "7.0.2"}`
    - Nội dung decoded:
      ```json
      [{"dgId": 505, "func": "DaoguanOwnerQuery"}]
      ```

### Packet 172 — `172.bin` — DOWN server → client

- **Timestamp ms**: `1780601528429`
- **TCP chunk length**: `1167` bytes
- **Frame(s)**: `172`
  - **Frame 172**
    - Header: `cac720dc00048f010e40100000000052`
    - Total length: `1167` bytes; codec: `zlib`; format: `json_response`
    - Func: `DaoguanOwnerQueryResult`
    - Nội dung decoded:
      ```json
      [{"dgId": 505, "func": "DaoguanOwnerQueryResult", "ownerList": [{"comboWin": 7, "defenderPet": {"paraList": [7258037, 1001, 71, 29800, 0, 28, 0, 0, 0, 0, 0], "petIdList": [233, 138, 295, 0], "petList": [{"petAttr": [479393, 73773, 45817, 36139, 39172, 7280, 1213, 257, 605, 542, 1019, 23502, 90351, 1898862, 0, 0, 0, 0], "petId": 1023502, "skillId": [1101, 31074, 30133, 31073, 31072, 2206, 46524, 31083, 31086, 31085, 31102, 31100, 4224, 31051, 31055, 31054, 31056, 40005, 31057, 20742, 31058, 31065, 31066, 31067, 4124, 31068, 31069, 31070, 30263, 23501, 935021, 935020, 935023, 935022, 31116, 31117, 31118, 31112, 31113, 31114, 235024, 72016, 31115, 31108, 31109, 4294, 31110, 4174, 30310, 50002, 31105, 50001, 31106, 31128, 30150, 31131, 235022, 235023, 235020, 235021, 31120, 31122], "skillLevel": [2, 1, 1, 1, 1, 14, 1, 1, 1, 1, 1, 1, 1, 1, 4, 4, 3, 1, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 83, 83, 83, 83, 1, 1, 1, 1, 1, 1, 83, 1, 1, 1, 1, 1, 1, 1, 1, 6, 1, 10, 1, 1, 1, 1, 83, 83, 83, 83, 1, 1]}, {"petAttr": [574757, 99811, 105944, 51937, 56907, 56449, 1213, 257, 605, 542, 121, 23522, 90358, 3535914, 0, 0, 0, 0], "petId": 1023522, "skillId": [1101, 31074, 31073, 31072, 935222, 935223, 935220, 2206, 935221, 31083, 31086, 31085, 4283, 4998, 31102, 31100, 40040, 235224, 31051, 235222, 235223, 235220, 31055, 235221, 31054, 31056, 31057, 31058, 31065, 31066, 31067, 31068, 31069, 48802, 31070, 4192, 4203, 20862, 30303, 20112, 31116, 31117, 31118, 31112, 72018, 31113, 31114, 72016, 31115, 31108, 31109, 4294, 31110, 30310, 31105, 50002, 31106, 50001, 400011, 400014, 31128, 400012, 30150, 31131, 31120, 31123], "skillLevel": [2, 1, 1, 1, 83, 83, 83, 14, 83, 1, 1, 1, 1, 1, 1, 1, 1, 83, 1, 83, 83, 83, 4, 83, 4, 3, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,... <truncated; see decoded/decoded_packets.json for full payload>
      ```

### Packet 173 — `173.bin` — UP client → server

- **Timestamp ms**: `1780601528454`
- **TCP chunk length**: `170` bytes
- **Frame(s)**: `173`
  - **Frame 173**
    - Header: `a5b973690000aa000000000000000053`
    - Total length: `170` bytes; codec: `plain`; format: `urlencoded_request`
    - Func: `DaoguanOwnerQuery`
    - Query fields: `{"bv": "7.0.2", "seq": "83", "session": "02D1B0135ABCDC0D", "sptype": "spv2jodo", "version": "7.0.2"}`
    - Nội dung decoded:
      ```json
      [{"dgId": 506, "func": "DaoguanOwnerQuery"}]
      ```

### Packet 174 — `174.bin` — DOWN server → client

- **Timestamp ms**: `1780601528492`
- **TCP chunk length**: `972` bytes
- **Frame(s)**: `174`
  - **Frame 174**
    - Header: `f9cf770d0003cc010e40100000000053`
    - Total length: `972` bytes; codec: `zlib`; format: `json_response`
    - Func: `DaoguanOwnerQueryResult`
    - Nội dung decoded:
      ```json
      [{"dgId": 506, "func": "DaoguanOwnerQueryResult", "ownerList": [{"comboWin": 2, "defenderPet": {"paraList": [4466894, 1001, 83, 41300, 0, 28, 0, 0, 0, 0, 0], "petIdList": [154, 31, 24], "petList": [{"petAttr": [743764, 75715, 54449, 27202, 25699, 26793, 1064, 73, 285, 186, 121, 23522, 90358, 2645366, 0, 0, 0, 0], "petId": 1023522, "skillId": [31075, 1101, 2202, 30133, 2203, 935222, 935223, 935220, 2206, 935221, 31076, 4323, 20862, 31085, 4998, 4274, 235224, 30163, 20182, 235222, 235223, 235220, 31055, 235221, 31054, 31056, 400011, 40007, 31128, 30150, 400012, 400013, 4254, 31065, 72013, 72011, 31123], "skillLevel": [1, 2, 6, 1, 5, 84, 84, 84, 12, 84, 1, 1, 1, 1, 1, 1, 84, 1, 1, 84, 84, 84, 1, 84, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]}, {"petAttr": [379089, 33408, 30389, 19402, 18461, 6274, 1064, 73, 285, 186, 114, 20961, 0, 1285776, 0, 0, 0, 0], "petId": 20961, "skillId": [31075, 1101, 30133, 2202, 2203, 44007, 2206, 31076, 2096102, 31085, 20902, 2096119, 2096132, 30163, 20182, 31055, 31054, 31056, 40001, 209612, 31128, 30150, 31065], "skillLevel": [1, 2, 1, 6, 5, 1, 12, 1, 84, 1, 1, 84, 84, 1, 1, 1, 1, 1, 1, 84, 1, 1, 1]}, {"petAttr": [250393, 18141, 14697, 8570, 8009, 3056, 1064, 73, 165, 186, 708, 23572, 90359, 463452, 0, 0, 0, 0], "petId": 23572, "skillId": [31075, 1101, 2202, 2203, 2206, 31076, 20222, 235724, 235723, 235722, 235721, 31055, 31085, 235720, 31054, 31056, 31128, 31065], "skillLevel": [1, 2, 6, 5, 12, 1, 1, 75, 75, 75, 75, 1, 1, 75, 1, 1, 1, 1]}]}, "show": {"avatarID": "56350147-1a02-4a63-bf36-a01685fa4e72", "avatarName": "nohatno", "battlePoint": 5493458, "campId": 2, "chengHaoID": 1007, "comboWin": 0, "comboWinMax": 15, "contentID": 1034, "dollId": 0, "dollName": "", "fightCountTotal": 198, "fightCountWin": 97, "guild": "Warzone", "guildId": 19512373... <truncated; see decoded/decoded_packets.json for full payload>
      ```

### Packet 175 — `175.bin` — UP client → server

- **Timestamp ms**: `1780601528518`
- **TCP chunk length**: `170` bytes
- **Frame(s)**: `175`
  - **Frame 175**
    - Header: `361d0a8b0000aa000000000000000054`
    - Total length: `170` bytes; codec: `plain`; format: `urlencoded_request`
    - Func: `DaoguanOwnerQuery`
    - Query fields: `{"bv": "7.0.2", "seq": "84", "session": "02D1B0135ABCDC0D", "sptype": "spv2jodo", "version": "7.0.2"}`
    - Nội dung decoded:
      ```json
      [{"dgId": 507, "func": "DaoguanOwnerQuery"}]
      ```

### Packet 176 — `176.bin` — DOWN server → client

- **Timestamp ms**: `1780601528544`
- **TCP chunk length**: `983` bytes
- **Frame(s)**: `176`
  - **Frame 176**
    - Header: `4d46d1390003d7010e40100000000054`
    - Total length: `983` bytes; codec: `zlib`; format: `json_response`
    - Func: `DaoguanOwnerQueryResult`
    - Nội dung decoded:
      ```json
      [{"dgId": 507, "func": "DaoguanOwnerQueryResult", "ownerList": [{"comboWin": 0, "defenderPet": {"paraList": [4156423, 1004, 2, 24100, 0, 28, 0, 0, 0, 15003038, 3], "petIdList": [34, 156, 312, 53], "petList": [{"petAttr": [621707, 55406, 93836, 26814, 34639, 46490, 1104, 121, 600, 589, 121, 23522, 90358, 2635516, 0, 0, 0, 0], "petId": 1023522, "skillId": [1101, 2201, 30133, 935222, 935223, 935220, 935221, 4321, 30303, 4213, 72033, 4274, 31102, 31103, 31116, 31117, 235224, 20182, 31118, 4303, 31112, 31114, 31115, 72031, 31108, 31110, 31051, 30310, 235222, 235223, 31105, 50002, 235220, 50001, 235221, 31107, 400011, 40007, 31128, 30150, 400012, 400013, 4241, 31065, 31123, 48802, 31070, 30263, 12013], "skillLevel": [2, 5, 1, 81, 81, 81, 81, 1, 1, 1, 1, 1, 1, 1, 1, 1, 81, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 81, 81, 1, 8, 81, 10, 81, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]}, {"petAttr": [382543, 29337, 33243, 13163, 13039, 4993, 1104, 121, 480, 589, 1517, 21022, 90351, 737512, 0, 0, 0, 0], "petId": 21022, "skillId": [1101, 2201, 20221, 4222, 4998, 31102, 31103, 31116, 31117, 31118, 210220, 31112, 210221, 210222, 31114, 210223, 31115, 31108, 31051, 31110, 50002, 31105, 50001, 31107, 46706, 40001, 31128, 4241, 210224, 31065, 31070, 31122, 12013], "skillLevel": [2, 5, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 8, 1, 10, 1, 1, 1, 1, 1, 31, 1, 1, 1, 1]}, {"petAttr": [379848, 28146, 31437, 12367, 12199, 4890, 1104, 121, 480, 589, 1517, 21011, 0, 664437, 0, 0, 0, 0], "petId": 21011, "skillId": [2201, 1101, 40039, 210113, 210112, 210114, 31102, 31103, 31116, 31117, 31118, 20300, 31112, 31114, 31115, 31108, 31051, 31110, 210110, 210111, 50002, 31105, 50001, 31107, 31128, 31065, 31070, 12013], "skillLevel": [5, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 8, 1, 10,... <truncated; see decoded/decoded_packets.json for full payload>
      ```

### Packet 177 — `177.bin` — UP client → server

- **Timestamp ms**: `1780601528651`
- **TCP chunk length**: `170` bytes
- **Frame(s)**: `177`
  - **Frame 177**
    - Header: `6ef3b3100000aa000000000000000055`
    - Total length: `170` bytes; codec: `plain`; format: `urlencoded_request`
    - Func: `DaoguanOwnerQuery`
    - Query fields: `{"bv": "7.0.2", "seq": "85", "session": "02D1B0135ABCDC0D", "sptype": "spv2jodo", "version": "7.0.2"}`
    - Nội dung decoded:
      ```json
      [{"dgId": 508, "func": "DaoguanOwnerQuery"}]
      ```

### Packet 178 — `178.bin` — DOWN server → client

- **Timestamp ms**: `1780601528680`
- **TCP chunk length**: `1066` bytes
- **Frame(s)**: `178`
  - **Frame 178**
    - Header: `a709560400042a010e40100000000055`
    - Total length: `1066` bytes; codec: `zlib`; format: `json_response`
    - Func: `DaoguanOwnerQueryResult`
    - Nội dung decoded:
      ```json
      [{"dgId": 508, "func": "DaoguanOwnerQueryResult", "ownerList": [{"comboWin": 0, "defenderPet": {"paraList": [4694305, 1004, 79, 31600, 0, 28, 0, 0, 0, 0, 0], "petIdList": [193, 5, 103], "petList": [{"petAttr": [568366, 73259, 63865, 34193, 33110, 36833, 1153, 161, 470, 583, 121, 23522, 90358, 2510231, 0, 0, 0, 0], "petId": 1023522, "skillId": [1101, 2201, 2202, 30133, 20212, 2203, 935222, 935223, 2205, 935220, 2206, 935221, 31085, 30303, 4998, 235224, 20952, 31115, 31108, 30310, 235222, 235223, 235220, 31055, 235221, 31054, 31056, 31057, 400011, 40007, 4253, 31128, 30150, 400012, 400013, 31065, 4243, 72013, 72011, 31069, 31123, 31070, 30263], "skillLevel": [2, 7, 7, 1, 1, 7, 79, 79, 7, 79, 7, 79, 1, 1, 1, 79, 1, 1, 1, 1, 79, 79, 79, 5, 79, 5, 4, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]}, {"petAttr": [364205, 25933, 26988, 15297, 15661, 5953, 1153, 161, 550, 583, 114, 20961, 0, 907239, 0, 0, 0, 0], "petId": 20961, "skillId": [1101, 2201, 30133, 2202, 2203, 2205, 2206, 2096101, 31085, 2096118, 20112, 30163, 31115, 31108, 31055, 31054, 31056, 31057, 209613, 209612, 31128, 30150, 31065, 31069, 31070], "skillLevel": [2, 7, 1, 7, 7, 7, 7, 64, 1, 64, 1, 1, 1, 1, 5, 5, 4, 3, 64, 64, 1, 1, 1, 1, 1]}, {"petAttr": [429659, 46122, 37694, 24733, 22867, 5007, 1153, 161, 550, 583, 708, 23572, 90359, 1197085, 0, 0, 0, 0], "petId": 23572, "skillId": [1101, 2201, 30133, 2202, 2203, 2205, 2206, 20222, 30142, 235724, 235723, 235722, 235721, 31085, 235720, 30302, 40039, 30163, 31115, 31108, 31055, 31054, 31056, 31057, 31128, 30150, 31065, 42705, 31069, 31070], "skillLevel": [2, 7, 1, 7, 7, 7, 7, 1, 1, 72, 72, 72, 72, 1, 72, 1, 1, 1, 1, 1, 5, 5, 4, 3, 1, 1, 1, 1, 1, 1]}]}, "show": {"avatarID": "14fa5938-a9a4-4e99-9cb4-9738723cfcbe", "avatarName": "哈基咪", "battlePoint": 4609727, "campId... <truncated; see decoded/decoded_packets.json for full payload>
      ```

### Packet 179 — `179.bin` — UP client → server

- **Timestamp ms**: `1780601528778`
- **TCP chunk length**: `159` bytes
- **Frame(s)**: `179`
  - **Frame 179**
    - Header: `d3ceff6b00009f000000000000000056`
    - Total length: `159` bytes; codec: `plain`; format: `urlencoded_request`
    - Func: `ChampionLeagueQueryStatus`
    - Query fields: `{"bv": "7.0.2", "seq": "86", "session": "02D1B0135ABCDC0D", "sptype": "spv2jodo", "version": "7.0.2"}`
    - Nội dung decoded:
      ```json
      [{"func": "ChampionLeagueQueryStatus"}]
      ```

### Packet 180 — `180.bin` — DOWN server → client

- **Timestamp ms**: `1780601528804`
- **TCP chunk length**: `622` bytes
- **Frame(s)**: `180`
  - **Frame 180**
    - Header: `671a18e600026e000e40100000000056`
    - Total length: `622` bytes; codec: `plain`; format: `json_response`
    - Func: `ChampionLeagueQueryStatusResult`
    - Nội dung decoded:
      ```json
      [{"func": "ChampionLeagueQueryStatusResult", "status": {"areaSupportList": [], "awardList": [], "fightCount": [0, 0, 0, 0, 0], "fightStatus": 0, "petList": [], "point": 0, "show": {"avatarID": "", "avatarName": "", "battlePoint": 0, "campId": 0, "chengHaoID": 0, "comboWin": 0, "comboWinMax": 0, "contentID": 0, "dollId": 0, "dollName": "", "fightCountTotal": 0, "fightCountWin": 0, "guild": "", "guildId": 0, "headFrame": 0, "lastActive": 0, "level": 0, "masterLevel": 0, "mountEquip": [], "mount_ID": 0, "petCount": 0, "petShowList": [], "pet_ID": 0, "ranking": 0, "rid": 0, "rotom_ID": 0, "spriteLevel": 0, "talk": "", "tuxiaongID": 0, "vip": 0}, "supportGet": 0, "supportList": []}}]
      ```

### Packet 181 — `181.bin` — UP client → server

- **Timestamp ms**: `1780601528910`
- **TCP chunk length**: `247` bytes
- **Frame(s)**: `181`
  - **Frame 181**
    - Header: `bda78ab40000f7000000000000000057`
    - Total length: `247` bytes; codec: `plain`; format: `urlencoded_request`
    - Func: `FightRealtimeQuery`
    - Query fields: `{"bv": "7.0.2", "seq": "87", "session": "02D1B0135ABCDC0D", "sptype": "spv2jodo", "version": "7.0.2"}`
    - Nội dung decoded:
      ```json
      [{"avatarId": "f25f2e5d-5ff3-4a83-89d5-4d259303f4bd", "fightId": "", "func": "FightRealtimeQuery"}]
      ```

### Packet 182 — `182.bin` — DOWN server → client

- **Timestamp ms**: `1780601528944`
- **TCP chunk length**: `70` bytes
- **Frame(s)**: `182`
  - **Frame 182**
    - Header: `ee47ff7f000046000e40100000000057`
    - Total length: `70` bytes; codec: `plain`; format: `json_response`
    - Func: `FightRealtimeQueryResult`
    - Nội dung decoded:
      ```json
      [{"fightList": [], "func": "FightRealtimeQueryResult"}]
      ```

### Packet 183 — `183.bin` — UP client → server

- **Timestamp ms**: `1780601529043`
- **TCP chunk length**: `169` bytes
- **Frame(s)**: `183`
  - **Frame 183**
    - Header: `8be9cc900000a9000000000000000058`
    - Total length: `169` bytes; codec: `plain`; format: `urlencoded_request`
    - Func: `DaoguanGlobalQuery`
    - Query fields: `{"bv": "7.0.2", "seq": "88", "session": "02D1B0135ABCDC0D", "sptype": "spv2jodo", "version": "7.0.2"}`
    - Nội dung decoded:
      ```json
      [{"dgId": 0, "func": "DaoguanGlobalQuery"}]
      ```

### Packet 184 — `184.bin` — DOWN server → client

- **Timestamp ms**: `1780601529077`
- **TCP chunk length**: `1460` bytes
- **Frame(s)**: `184`
  - **Frame 184**; spans segments `[184, 185]`
    - Header: `824d4055000c3e010e40100000000058`
    - Total length: `3134` bytes; codec: `zlib`; format: `json_response`
    - Func: `DaoguanGlobalQueryResult`
    - Nội dung decoded:
      ```json
      [{"func": "DaoguanGlobalQueryResult", "list": [{"awardList": [], "dgid": 102, "ownerList": [{"defenderPet": {"paraList": [1222140], "petIdList": [], "petList": [{"petAttr": [201905, 47592, 29744, 20581, 22867, 5306, 1000, 0, 136, 136, 1914, 22071, 0, 0, 0, 0, 0, 0], "petId": 401311, "skillId": [220712, 220713, 20190, 220710, 220711, 220714], "skillLevel": [85, 85, 1, 85, 85, 85]}, {"petAttr": [143470, 26195, 35342, 24561, 27632, 3579, 1000, 0, 130, 130, 414, 21521, 0, 0, 0, 0, 0, 0], "petId": 401312, "skillId": [215210, 215211, 20211, 215213, 215214, 215212], "skillLevel": [85, 85, 1, 85, 85, 85]}, {"petAttr": [151910, 54051, 33263, 22105, 21492, 3150, 1000, 0, 130, 130, 1417, 20571, 0, 0, 0, 0, 0, 0], "petId": 401313, "skillId": [205711, 205712, 20190, 205714, 205710, 205713], "skillLevel": [85, 85, 1, 85, 85, 85]}]}, "dgTitleId": 1013001, "maxWaveWin": 0, "show": {"avatarID": "", "avatarName": "Elesa", "battlePoint": 1222140, "campId": 0, "chengHaoID": 0, "comboWin": 0, "comboWinMax": 0, "contentID": 387, "dollId": 0, "dollName": "", "fightCountTotal": 0, "fightCountWin": 0, "guild": "", "guildId": 0, "headFrame": 0, "lastActive": 1780497692, "level": 85, "masterLevel": 0, "mountEquip": [], "mount_ID": 0, "petCount": 0, "petShowList": [{"afinity": 0, "id": 401311, "level": 0}, {"afinity": 0, "id": 401312, "level": 0}, {"afinity": 0, "id": 401313, "level": 0}], "pet_ID": 0, "ranking": 0, "rid": -1, "rotom_ID": 0, "spriteLevel": 0, "talk": "I will resign myself to your guidance!", "tuxiaongID": 387, "vip": 0}, "timeWin": 1780497692, "waveWin": 0}], "record": [], "timeReset": 1780261201}, {"awardList": [], "dgid": 103, "ownerList": [{"defenderPet": {"paraList": [9873836, 1004, 50, 35200, 0, 28, 0, 0, 0, 0, 0], "petIdList": [58, 282, 33], "petList": [{"petAttr": [1168407,... <truncated; see decoded/decoded_packets.json for full payload>
      ```

### Packet 185 — `185.bin` — DOWN server → client

- **Timestamp ms**: `1780601529078`
- **TCP chunk length**: `1674` bytes
- **Frame(s)**: `184`
  - **Frame 184**; spans segments `[184, 185]`
    - Header: `824d4055000c3e010e40100000000058`
    - Total length: `3134` bytes; codec: `zlib`; format: `json_response`
    - Func: `DaoguanGlobalQueryResult`
    - Nội dung decoded:
      ```json
      [{"func": "DaoguanGlobalQueryResult", "list": [{"awardList": [], "dgid": 102, "ownerList": [{"defenderPet": {"paraList": [1222140], "petIdList": [], "petList": [{"petAttr": [201905, 47592, 29744, 20581, 22867, 5306, 1000, 0, 136, 136, 1914, 22071, 0, 0, 0, 0, 0, 0], "petId": 401311, "skillId": [220712, 220713, 20190, 220710, 220711, 220714], "skillLevel": [85, 85, 1, 85, 85, 85]}, {"petAttr": [143470, 26195, 35342, 24561, 27632, 3579, 1000, 0, 130, 130, 414, 21521, 0, 0, 0, 0, 0, 0], "petId": 401312, "skillId": [215210, 215211, 20211, 215213, 215214, 215212], "skillLevel": [85, 85, 1, 85, 85, 85]}, {"petAttr": [151910, 54051, 33263, 22105, 21492, 3150, 1000, 0, 130, 130, 1417, 20571, 0, 0, 0, 0, 0, 0], "petId": 401313, "skillId": [205711, 205712, 20190, 205714, 205710, 205713], "skillLevel": [85, 85, 1, 85, 85, 85]}]}, "dgTitleId": 1013001, "maxWaveWin": 0, "show": {"avatarID": "", "avatarName": "Elesa", "battlePoint": 1222140, "campId": 0, "chengHaoID": 0, "comboWin": 0, "comboWinMax": 0, "contentID": 387, "dollId": 0, "dollName": "", "fightCountTotal": 0, "fightCountWin": 0, "guild": "", "guildId": 0, "headFrame": 0, "lastActive": 1780497692, "level": 85, "masterLevel": 0, "mountEquip": [], "mount_ID": 0, "petCount": 0, "petShowList": [{"afinity": 0, "id": 401311, "level": 0}, {"afinity": 0, "id": 401312, "level": 0}, {"afinity": 0, "id": 401313, "level": 0}], "pet_ID": 0, "ranking": 0, "rid": -1, "rotom_ID": 0, "spriteLevel": 0, "talk": "I will resign myself to your guidance!", "tuxiaongID": 387, "vip": 0}, "timeWin": 1780497692, "waveWin": 0}], "record": [], "timeReset": 1780261201}, {"awardList": [], "dgid": 103, "ownerList": [{"defenderPet": {"paraList": [9873836, 1004, 50, 35200, 0, 28, 0, 0, 0, 0, 0], "petIdList": [58, 282, 33], "petList": [{"petAttr": [1168407,... <truncated; see decoded/decoded_packets.json for full payload>
      ```

### Packet 186 — `186.bin` — UP client → server

- **Timestamp ms**: `1780601529118`
- **TCP chunk length**: `157` bytes
- **Frame(s)**: `185`
  - **Frame 185**
    - Header: `c264ff0c00009d000000000000000059`
    - Total length: `157` bytes; codec: `plain`; format: `urlencoded_request`
    - Func: `DecorationHandbookQuery`
    - Query fields: `{"bv": "7.0.2", "seq": "89", "session": "02D1B0135ABCDC0D", "sptype": "spv2jodo", "version": "7.0.2"}`
    - Nội dung decoded:
      ```json
      [{"func": "DecorationHandbookQuery"}]
      ```

### Packet 187 — `187.bin` — DOWN server → client

- **Timestamp ms**: `1780601529144`
- **TCP chunk length**: `90` bytes
- **Frame(s)**: `186`
  - **Frame 186**
    - Header: `99d8b94b00005a000e40100000000059`
    - Total length: `90` bytes; codec: `plain`; format: `json_response`
    - Func: `DecorationHandbookQueryResult`
    - Nội dung decoded:
      ```json
      [{"awardList": [], "func": "DecorationHandbookQueryResult", "ownedList": []}]
      ```

### Packet 188 — `188.bin` — UP client → server

- **Timestamp ms**: `1780601529229`
- **TCP chunk length**: `156` bytes
- **Frame(s)**: `187`
  - **Frame 187**
    - Header: `be5377ad00009c00000000000000005a`
    - Total length: `156` bytes; codec: `plain`; format: `urlencoded_request`
    - Func: `SecretBaseQueryPrivate`
    - Query fields: `{"bv": "7.0.2", "seq": "90", "session": "02D1B0135ABCDC0D", "sptype": "spv2jodo", "version": "7.0.2"}`
    - Nội dung decoded:
      ```json
      [{"func": "SecretBaseQueryPrivate"}]
      ```

### Packet 189 — `189.bin` — DOWN server → client

- **Timestamp ms**: `1780601529255`
- **TCP chunk length**: `174` bytes
- **Frame(s)**: `188`
  - **Frame 188**
    - Header: `758a2f230000ae000e4010000000005a`
    - Total length: `174` bytes; codec: `plain`; format: `json_response`
    - Func: `SecretBaseQueryPrivateResult`
    - Nội dung decoded:
      ```json
      [{"func": "SecretBaseQueryPrivateResult", "sbPrivate": {"actionList": [], "furnitureList": [], "optionTime": [], "petSlotList": [], "themePosAll": [], "themeValid": []}}]
      ```

### Packet 190 — `190.bin` — UP client → server

- **Timestamp ms**: `1780601529362`
- **TCP chunk length**: `154` bytes
- **Frame(s)**: `189`
  - **Frame 189**
    - Header: `f1f3331600009a00000000000000005b`
    - Total length: `154` bytes; codec: `plain`; format: `urlencoded_request`
    - Func: `MirrorChallengeQuery`
    - Query fields: `{"bv": "7.0.2", "seq": "91", "session": "02D1B0135ABCDC0D", "sptype": "spv2jodo", "version": "7.0.2"}`
    - Nội dung decoded:
      ```json
      [{"func": "MirrorChallengeQuery"}]
      ```

### Packet 191 — `191.bin` — DOWN server → client

- **Timestamp ms**: `1780601529388`
- **TCP chunk length**: `328` bytes
- **Frame(s)**: `190`
  - **Frame 190**
    - Header: `b75d4905000148000e4010000000005b`
    - Total length: `328` bytes; codec: `plain`; format: `json_response`
    - Func: `MirrorChallengeQueryResult`
    - Nội dung decoded:
      ```json
      [{"func": "MirrorChallengeQueryResult", "mcStatus": {"awardList": [], "buyCount": 0, "mirrorList": [130401, 130301], "point": 0, "progress": [{"id": 1, "value": 1}, {"id": 2, "value": 1}, {"id": 3, "value": 1}, {"id": 4, "value": 1}, {"id": 5, "value": 1}, {"id": 6, "value": 1}, {"id": 7, "value": 1}], "recoverCount": 0, "resetCount": 0, "winCount": 0}}]
      ```
