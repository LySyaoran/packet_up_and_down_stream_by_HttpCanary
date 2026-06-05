# Decoded TCP capture report

## Capture metadata

- **app**: `com.nnal.bb3ds`
- **host**: `None`
- **protocol**: `TCP`
- **remoteIp**: `47.236.127.186`
- **remotePort**: `21195`
- **security**: `False`
- **sessionId**: `7bc6d518-aa17-48f6-8cad-d9a7a521a7bb`
- **time**: `2026-06-05 02:31:58`
- **TCP chunk files**: `192` (`0.bin` .. `191.bin`)
- **Decoded application frames**: `191`
- **Client → server frames**: `93`
- **Server → client frames**: `98`
- **zlib-compressed frames**: `16`

## Protocol notes

- `tcp.hcy` metadata marks each TCP chunk as direction `1` (client → server) or `2` (server → client), with a millisecond timestamp and raw chunk length.
- Each game application frame starts with a 16-byte header. Header bytes `4..6` are the big-endian 24-bit total frame length, so TCP chunks can contain multiple frames or only part of a larger frame.
- Client payloads are normally URL-encoded query strings with a JSON `request` parameter. Server payloads normally start with `0;` followed by JSON. Large server responses may be zlib-compressed before that `0;` JSON text.

## High-level flow

- `Login` appears `1` time(s).
- `LoginResult` appears `1` time(s).
- `QueryAvatarAttribute` appears `2` time(s).
- `CreateAvatar` appears `1` time(s).
- `CreateAvatarResult` appears `1` time(s).
- `UpdateGuide` appears `1` time(s).
- `HeartBeat` appears `1` time(s).

## Frame-by-frame decoded payloads

### Frame 000: up/client_to_server

- **Segments**: `[0]`
- **Timestamp ms**: `1780601518164` .. `1780601518164`
- **Header**: `61da39960000100a0000000000000005`
- **Total length**: `16` bytes; **payload codec**: `plain`; **format**: `empty_control`
- **Functions**: `—`
- **Decoded payload**:
  ```json
  ""
  ```

### Frame 001: down/server_to_client

- **Segments**: `[1]`
- **Timestamp ms**: `1780601518196` .. `1780601518196`
- **Header**: `b891bac10000c41e0e4010000000340d`
- **Total length**: `196` bytes; **payload codec**: `plain`; **format**: `json_response`
- **Functions**: `—`
- **Decoded payload**:
  ```json
  {"innerAddr": "/0.0.0.0:21195", "innerCount": 13, "launchInfo": "[\"-config\",\"/data/game1195/config.prop\"]", "number": 0, "para": "[1195]", "sid": 1195, "status": 1780601514, "type": "HTGame"}
  ```

### Frame 002: down/server_to_client

- **Segments**: `[1]`
- **Timestamp ms**: `1780601518196` .. `1780601518196`
- **Header**: `59bb33c00000100b0e4010000000340d`
- **Total length**: `16` bytes; **payload codec**: `plain`; **format**: `empty_control`
- **Functions**: `—`
- **Decoded payload**:
  ```json
  ""
  ```

### Frame 003: up/client_to_server

- **Segments**: `[2]`
- **Timestamp ms**: `1780601518271` .. `1780601518271`
- **Header**: `e51e7d370002e0000000000000000000`
- **Total length**: `736` bytes; **payload codec**: `plain`; **format**: `urlencoded_request`
- **Functions**: `Login`
- **Query fields**: `{"bv": "7.0.2", "seq": "1", "session": "", "sptype": "spv2jodo", "version": "7.0.2"}`
- **Decoded payload**:
  ```json
  [{"deviceType": 2, "func": "Login", "info": "{\"appVersion\":\"7.0.2\",\"appBaseVersion\":\"7.0.2\",\"deviceId\":\"DEVICE#mac00dbda57f973\",\"combinedDeviceId\":\"00db11d44a68_010138020814576\",\"deviceCheckChannel\":\"\",\"deviceType\":17,\"model\":\"SM-S9210\",\"os\":\"Android\",\"osversion\":\"9\",\"mac\":\"00:db:11:d4:4a:68\"}", "serverid": 1195, "userid": "v2jodo#2835376"}]
  ```

### Frame 004: down/server_to_client

- **Segments**: `[3]`
- **Timestamp ms**: `1780601518303` .. `1780601518303`
- **Header**: `a5b7588200004b000e40100000000000`
- **Total length**: `75` bytes; **payload codec**: `plain`; **format**: `json_response`
- **Functions**: `LoginResult`
- **Decoded payload**:
  ```json
  [{"func": "LoginResult", "session_key": "02D1B0135ABCDC0D"}]
  ```

### Frame 005: up/client_to_server

- **Segments**: `[4]`
- **Timestamp ms**: `1780601518332` .. `1780601518332`
- **Header**: `b853646c000010140000000000000001`
- **Total length**: `16` bytes; **payload codec**: `plain`; **format**: `empty_control`
- **Functions**: `—`
- **Decoded payload**:
  ```json
  ""
  ```

### Frame 006: down/server_to_client

- **Segments**: `[5]`
- **Timestamp ms**: `1780601518358` .. `1780601518358`
- **Header**: `7f11aa23000010150e4010000000340d`
- **Total length**: `16` bytes; **payload codec**: `plain`; **format**: `empty_control`
- **Functions**: `—`
- **Decoded payload**:
  ```json
  ""
  ```

### Frame 007: up/client_to_server

- **Segments**: `[6]`
- **Timestamp ms**: `1780601518391` .. `1780601518391`
- **Header**: `6ca96b6c000099000000000000000002`
- **Total length**: `153` bytes; **payload codec**: `plain`; **format**: `urlencoded_request`
- **Functions**: `QueryAvatarAttribute`
- **Query fields**: `{"bv": "7.0.2", "seq": "2", "session": "02D1B0135ABCDC0D", "sptype": "spv2jodo", "version": "7.0.2"}`
- **Decoded payload**:
  ```json
  [{"func": "QueryAvatarAttribute"}]
  ```

### Frame 008: down/server_to_client

- **Segments**: `[7]`
- **Timestamp ms**: `1780601518420` .. `1780601518420`
- **Header**: `881aa0340001ae000e40100000000002`
- **Total length**: `430` bytes; **payload codec**: `plain`; **format**: `json_response`
- **Functions**: `QueryAvatarAttributeResult`
- **Decoded payload**:
  ```json
  [{"attribute": {"ChengHao_ID": 0, "JingLing_ID": 0, "TuXiang_ID": 0, "avatarName": "", "city": 0, "coins": [], "createTime": 0, "desc": "", "exp": 0, "fighting": 0, "figureID": 0, "gender": 0, "guildID": 0, "guildName": "", "guildRank": 0, "headFrame": 0, "level": 0, "masterExp": 0, "masterLevel": 0, "mountEquip": [], "mount_ID": 0, "pet_ID": 0, "pos": 0, "rid": 0, "rotom_ID": 0, "vipLevel": 0}, "avatarid": "", "error_code": 1, "func": "QueryAvatarAttributeResult"}]
  ```

### Frame 009: up/client_to_server

- **Segments**: `[8]`
- **Timestamp ms**: `1780601518652` .. `1780601518652`
- **Header**: `b2167f02000094000000000000000003`
- **Total length**: `148` bytes; **payload codec**: `plain`; **format**: `urlencoded_request`
- **Functions**: `QueryChargeInfo`
- **Query fields**: `{"bv": "7.0.2", "seq": "3", "session": "02D1B0135ABCDC0D", "sptype": "spv2jodo", "version": "7.0.2"}`
- **Decoded payload**:
  ```json
  [{"func": "QueryChargeInfo"}]
  ```

### Frame 010: up/client_to_server

- **Segments**: `[9]`
- **Timestamp ms**: `1780601524147` .. `1780601524147`
- **Header**: `24c39b190000e2000000000000000004`
- **Total length**: `226` bytes; **payload codec**: `plain`; **format**: `urlencoded_request`
- **Functions**: `CreateAvatar`
- **Query fields**: `{"bv": "7.0.2", "seq": "4", "session": "02D1B0135ABCDC0D", "sptype": "spv2jodo", "version": "7.0.2"}`
- **Decoded payload**:
  ```json
  [{"avatarName": "BeetBoij", "chiefBuddy": 1002, "func": "CreateAvatar", "gender": 0}]
  ```

### Frame 011: down/server_to_client

- **Segments**: `[10]`
- **Timestamp ms**: `1780601524190` .. `1780601524190`
- **Header**: `5671274c000066000e40100000000004`
- **Total length**: `102` bytes; **payload codec**: `plain`; **format**: `json_response`
- **Functions**: `QueryOAProgressResult`
- **Decoded payload**:
  ```json
  [{"func": "QueryOAProgressResult", "ids": [{"id": 66, "progress": 0, "progressList": [0]}]}]
  ```

### Frame 012: down/server_to_client

- **Segments**: `[10]`
- **Timestamp ms**: `1780601524190` .. `1780601524190`
- **Header**: `40835f2d0000f8000e40100000000004`
- **Total length**: `248` bytes; **payload codec**: `plain`; **format**: `json_response`
- **Functions**: `BattleTowerQueryResult`
- **Decoded payload**:
  ```json
  [{"func": "BattleTowerQueryResult", "mode": 0, "petList": [], "status": {"awardPickId": 0, "buffList": [], "coin": 0, "curLevel": 0, "finishAwardList": [], "lootBuffBox": [], "maxLevel": 0, "opponentIndex": 0, "opponentList": [], "point": 0, "pointSum": 0}}]
  ```

### Frame 013: down/server_to_client

- **Segments**: `[11]`
- **Timestamp ms**: `1780601524194` .. `1780601524194`
- **Header**: `0cd25da7000040000e40100000000004`
- **Total length**: `64` bytes; **payload codec**: `plain`; **format**: `json_response`
- **Functions**: `CreateAvatarResult`
- **Decoded payload**:
  ```json
  [{"error_code": 0, "func": "CreateAvatarResult"}]
  ```

### Frame 014: up/client_to_server

- **Segments**: `[12]`
- **Timestamp ms**: `1780601524224` .. `1780601524224`
- **Header**: `27e2d294000099000000000000000005`
- **Total length**: `153` bytes; **payload codec**: `plain`; **format**: `urlencoded_request`
- **Functions**: `QueryAvatarAttribute`
- **Query fields**: `{"bv": "7.0.2", "seq": "5", "session": "02D1B0135ABCDC0D", "sptype": "spv2jodo", "version": "7.0.2"}`
- **Decoded payload**:
  ```json
  [{"func": "QueryAvatarAttribute"}]
  ```

### Frame 015: down/server_to_client

- **Segments**: `[13]`
- **Timestamp ms**: `1780601524251` .. `1780601524251`
- **Header**: `eb1c28bb00003a000e40100000000005`
- **Total length**: `58` bytes; **payload codec**: `plain`; **format**: `json_response`
- **Functions**: `UpdateHuiZhang`
- **Decoded payload**:
  ```json
  [{"func": "UpdateHuiZhang", "huiZhang": 0}]
  ```

### Frame 016: down/server_to_client

- **Segments**: `[13]`
- **Timestamp ms**: `1780601524251` .. `1780601524251`
- **Header**: `2bd029a7000049000e40100000000005`
- **Total length**: `73` bytes; **payload codec**: `plain`; **format**: `json_response`
- **Functions**: `InitLastStartTime`
- **Decoded payload**:
  ```json
  [{"func": "InitLastStartTime", "times": [0], "types": [12]}]
  ```

### Frame 017: down/server_to_client

- **Segments**: `[13]`
- **Timestamp ms**: `1780601524251` .. `1780601524251`
- **Header**: `034865b2000046000e40100000000005`
- **Total length**: `70` bytes; **payload codec**: `plain`; **format**: `json_response`
- **Functions**: `UpdatePetLinkInfo`
- **Decoded payload**:
  ```json
  [{"func": "UpdatePetLinkInfo", "info": [], "mix": false}]
  ```

### Frame 018: down/server_to_client

- **Segments**: `[13]`
- **Timestamp ms**: `1780601524251` .. `1780601524251`
- **Header**: `a8d8c87d00022c000e40100000000005`
- **Total length**: `556` bytes; **payload codec**: `plain`; **format**: `json_response`
- **Functions**: `QueryAvatarAttributeResult`
- **Decoded payload**:
  ```json
  [{"attribute": {"ChengHao_ID": 0, "JingLing_ID": 0, "TuXiang_ID": 1002, "avatarName": "BeetBoij", "city": 0, "coins": [0, 0, 0, 0, 0, 0, 60, 0, 0, 0, 10, 0, 20, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10, 0], "createTime": 1780601520, "desc": "", "exp": 0, "fighting": 0, "figureID": 1002, "gender": 0, "guildID": 0, "guildName": "", "guildRank": 0, "headFrame": 0, "level": 1, "masterExp": 0, "masterLevel": 0, "mountEquip": [], "mount_ID": 0, "pet_ID": 0, "pos": 0, "rid": 195132877, "rotom_ID": 0, "vipLevel": 0}, "avatarid": "f25f2e5d-5ff3-4a83-89d5-4d259303f4bd", "error_code": 0, "func": "QueryAvatarAttributeResult"}]
  ```

### Frame 019: up/client_to_server

- **Segments**: `[14]`
- **Timestamp ms**: `1780601524282` .. `1780601524282`
- **Header**: `b0b4c25e0000b0000000000000000006`
- **Total length**: `176` bytes; **payload codec**: `plain`; **format**: `urlencoded_request`
- **Functions**: `UpdateGuide`
- **Query fields**: `{"bv": "7.0.2", "seq": "6", "session": "02D1B0135ABCDC0D", "sptype": "spv2jodo", "version": "7.0.2"}`
- **Decoded payload**:
  ```json
  [{"func": "UpdateGuide", "id": 1, "step": 0}]
  ```

### Frame 020: down/server_to_client

- **Segments**: `[15]`
- **Timestamp ms**: `1780601524308` .. `1780601524308`
- **Header**: `fb65cbce00003f000e40100000000006`
- **Total length**: `63` bytes; **payload codec**: `plain`; **format**: `json_response`
- **Functions**: `UpdateGuideResult`
- **Decoded payload**:
  ```json
  [{"error_code": 0, "func": "UpdateGuideResult"}]
  ```

### Frame 021: up/client_to_server

- **Segments**: `[16]`
- **Timestamp ms**: `1780601524338` .. `1780601524338`
- **Header**: `ac854aa10000a2000000000000000007`
- **Total length**: `162` bytes; **payload codec**: `plain`; **format**: `urlencoded_request`
- **Functions**: `HeartBeat`
- **Query fields**: `{"bv": "7.0.2", "seq": "7", "session": "02D1B0135ABCDC0D", "sptype": "spv2jodo", "version": "7.0.2"}`
- **Decoded payload**:
  ```json
  [{"func": "HeartBeat", "time": 0}]
  ```

### Frame 022: down/server_to_client

- **Segments**: `[17]`
- **Timestamp ms**: `1780601524365` .. `1780601524365`
- **Header**: `54d43c3c00004f000e40100000000007`
- **Total length**: `79` bytes; **payload codec**: `plain`; **format**: `json_response`
- **Functions**: `HeartBeatResult`
- **Decoded payload**:
  ```json
  [{"error_code": 0, "func": "HeartBeatResult", "time": 1780601520}]
  ```

### Frame 023: down/server_to_client

- **Segments**: `[17]`
- **Timestamp ms**: `1780601524365` .. `1780601524365`
- **Header**: `41c17945000267000e40100000000007`
- **Total length**: `615` bytes; **payload codec**: `plain`; **format**: `json_response`
- **Functions**: `NotifyChatUpdate`
- **Decoded payload**:
  ```json
  [{"func": "NotifyChatUpdate", "isPrivateUpdate": 0, "msgs": [{"channel": 1, "content": "<I:UI_HT_chongwutujian.chongwutujian:bq11.png:31:28>", "keepTime": 0, "receiver": "", "receiverName": "", "receiverRid": 0, "sender": "f2b8b789-3f46-448c-b281-556aa6e98c93", "senderName": "Kun⚘kẩu", "senderRid": 0, "senderVIP": 12, "seq": 1380, "time": 1780575116}, {"channel": 1, "content": "<I:UI_HT_chongwutujian.chongwutujian:bq03.png:31:28>", "keepTime": 0, "receiver": "", "receiverName": "", "receiverRid": 0, "sender": "fb7681ca-82c0-4107-a6b5-7718825f9528", "senderName": "Clawn", "senderRid": 0, "senderVIP": 2, "seq": 1379, "time": 1780575018}]}]
  ```

### Frame 024: up/client_to_server

- **Segments**: `[18]`
- **Timestamp ms**: `1780601524389` .. `1780601524389`
- **Header**: `8ceaee37000099000000000000000008`
- **Total length**: `153` bytes; **payload codec**: `plain`; **format**: `urlencoded_request`
- **Functions**: `QueryAllChargeConfig`
- **Query fields**: `{"bv": "7.0.2", "seq": "8", "session": "02D1B0135ABCDC0D", "sptype": "spv2jodo", "version": "7.0.2"}`
- **Decoded payload**:
  ```json
  [{"func": "QueryAllChargeConfig"}]
  ```

### Frame 025: down/server_to_client

- **Segments**: `[19]`
- **Timestamp ms**: `1780601524389` .. `1780601524389`
- **Header**: `4d4cbc8f0000c0000e40100000000007`
- **Total length**: `192` bytes; **payload codec**: `plain`; **format**: `json_response`
- **Functions**: `Broadcast`
- **Decoded payload**:
  ```json
  [{"broadChannel": 10, "func": "Broadcast", "msg": "<C:FFC080FF>Fanoking</C> monster [<C:66FFFBFF>Marill</C>] successfully evolve to [<C:66FFFBFF>Azumarill</C>],congratulation!!"}]
  ```

### Frame 026: down/server_to_client

- **Segments**: `[20]`
- **Timestamp ms**: `1780601524427` .. `1780601524427`
- **Header**: `77a5617400038c010e40100000000008`
- **Total length**: `908` bytes; **payload codec**: `zlib`; **format**: `json_response`
- **Functions**: `QueryAllChargeConfigResult`
- **Decoded payload**:
  ```json
  [{"chargeList": [{"AdditionalDesc": "120 diamonds daily（30days）", "AdditionalYuanbao": 0, "BuyPrice": 499, "ChargeRank": 2, "ChargeType": 1, "CurrencyType": "RMB", "Desc": "300 Diamonds M-Giftpack", "DoubleDesc": "", "DoubleFirst": false, "DoubleRate": 1.0, "FirstDesc": "", "GainYuanbao": 300, "Icon": "UI_HT_VIP1.VIP1/icon_yueka.png", "MonthCardBenefit": 120, "MonthCardTime": 30, "PriceDesc": "4.99", "PriceID": 1, "RechargeDayTime": 0, "RechargeWeekTime": 0, "ShowYuanbao": 300, "VipAstrict": 0, "itemID": 1}, {"AdditionalDesc": "", "AdditionalYuanbao": 0, "BuyPrice": 99, "ChargeRank": 3, "ChargeType": 2, "CurrencyType": "RMB", "Desc": "60 Diamonds", "DoubleDesc": "无", "DoubleFirst": true, "DoubleRate": 2.0, "FirstDesc": "", "GainYuanbao": 60, "Icon": "UI_HT_VIP1.VIP1/icon_zuanshi.png", "MonthCardBenefit": 0, "MonthCardTime": 0, "PriceDesc": "0.99", "PriceID": 2, "RechargeDayTime": 3, "RechargeWeekTime": 0, "ShowYuanbao": 60, "VipAstrict": 0, "itemID": 2}, {"AdditionalDesc": "Additional 1,200 free diamonds", "AdditionalYuanbao": 1200, "BuyPrice": 9999, "ChargeRank": 8, "ChargeType": 2, "CurrencyType": "RMB", "Desc": "6,480 Diamonds", "DoubleDesc": "无", "DoubleFirst": true, "DoubleRate": 2.0, "FirstDesc": "", "GainYuanbao": 6480, "Icon": "UI_HT_VIP1.VIP1/icon_zuanshimuxiang.png", "MonthCardBenefit": 0, "MonthCardTime": 0, "PriceDesc": "99.99", "PriceID": 3, "RechargeDayTime": 0, "RechargeWeekTime": 1, "ShowYuanbao": 6480, "VipAstrict": 0, "itemID": 3}, {"AdditionalDesc": "Additional 500 free diamonds", "AdditionalYuanbao": 500, "BuyPrice": 4999, "ChargeRank": 7, "ChargeType": 2, "CurrencyType": "RMB", "Desc": "3,280 Diamonds", "DoubleDesc": "无", "DoubleFirst": true, "DoubleRate": 2.0, "FirstDesc": "", "GainYuanbao": 3280, "Icon": "UI_HT_VIP1.VIP1/icon_zuanshibao.png", "MonthCardBenefit": 0, "MonthCardTime": 0, "PriceDesc": "49.99", "PriceID": 4, "RechargeDayTime": 0, "RechargeWeekTime": 1, "ShowYuanbao": 3280, "VipAstrict": 0, "itemID": 4}, {"AdditionalDesc": "Additional 200 free diamonds", "AdditionalYuanbao": 200, "BuyPrice": 2999, "ChargeRank": 6, "ChargeType": 2, "CurrencyType": "RMB", "Desc": "1,980 Diamonds", "DoubleDesc": "无", "DoubleFirst": true, "DoubleRate": 2.0, "FirstDesc": "", "GainYuanbao": 1980, "Icon": "UI_HT_VIP1.VIP1/icon_zuanshidui.png", "MonthCardBenefit": 0, "MonthCardTime": 0, "PriceDesc": "29.99", "PriceID": 5, "RechargeDayTime": 0, "RechargeWeekTime": 1, "ShowYuanbao": 1980, "VipAstrict": 0, "itemID": 5}, {"AdditionalDesc": "Additional 80 free diamonds", "AdditionalYuanbao": 80, "BuyPrice": 1499, "ChargeRank": 5, "ChargeType": 2, "CurrencyType": "RMB", "Desc": "980 Diamonds", "DoubleDesc": "无", "DoubleFirst": true, "DoubleRate": 2.0, "FirstDesc": "", "GainYuanbao": 980, "Icon": "UI_HT_VIP1.VIP1/icon_zuanshi2.png", "MonthCardBenefit": 0, "MonthCardTime": 0, "PriceDesc": "14.99", "PriceID": 6, "RechargeDayTime": 0, "RechargeWeekTime": 1, "ShowYuanbao": 980, "VipAstrict": 0, "itemID": 6}, {"AdditionalDesc": "Additional 15 free d... <truncated in markdown; see decoded_packets.json>
  ```

### Frame 027: up/client_to_server

- **Segments**: `[21]`
- **Timestamp ms**: `1780601524460` .. `1780601524460`
- **Header**: `9e638116000094000000000000000009`
- **Total length**: `148` bytes; **payload codec**: `plain`; **format**: `urlencoded_request`
- **Functions**: `GetChengHaoList`
- **Query fields**: `{"bv": "7.0.2", "seq": "9", "session": "02D1B0135ABCDC0D", "sptype": "spv2jodo", "version": "7.0.2"}`
- **Decoded payload**:
  ```json
  [{"func": "GetChengHaoList"}]
  ```

### Frame 028: down/server_to_client

- **Segments**: `[22]`
- **Timestamp ms**: `1780601524485` .. `1780601524485`
- **Header**: `8a417e75000040000e40100000000009`
- **Total length**: `64` bytes; **payload codec**: `plain`; **format**: `json_response`
- **Functions**: `GetChengHaoListResult`
- **Decoded payload**:
  ```json
  [{"chList": [], "func": "GetChengHaoListResult"}]
  ```

### Frame 029: up/client_to_server

- **Segments**: `[23]`
- **Timestamp ms**: `1780601524513` .. `1780601524513`
- **Header**: `77ae0bed00009500000000000000000a`
- **Total length**: `149` bytes; **payload codec**: `plain`; **format**: `urlencoded_request`
- **Functions**: `GetHuiZhangList`
- **Query fields**: `{"bv": "7.0.2", "seq": "10", "session": "02D1B0135ABCDC0D", "sptype": "spv2jodo", "version": "7.0.2"}`
- **Decoded payload**:
  ```json
  [{"func": "GetHuiZhangList"}]
  ```

### Frame 030: down/server_to_client

- **Segments**: `[24]`
- **Timestamp ms**: `1780601524538` .. `1780601524538`
- **Header**: `9d1675b9000046000e4010000000000a`
- **Total length**: `70` bytes; **payload codec**: `plain`; **format**: `json_response`
- **Functions**: `GetHuiZhangListResult`
- **Decoded payload**:
  ```json
  [{"func": "GetHuiZhangListResult", "huiZhangList": []}]
  ```

### Frame 031: up/client_to_server

- **Segments**: `[25]`
- **Timestamp ms**: `1780601524568` .. `1780601524568`
- **Header**: `ca8d06c700009700000000000000000b`
- **Total length**: `151` bytes; **payload codec**: `plain`; **format**: `urlencoded_request`
- **Functions**: `QueryJingLingInfo`
- **Query fields**: `{"bv": "7.0.2", "seq": "11", "session": "02D1B0135ABCDC0D", "sptype": "spv2jodo", "version": "7.0.2"}`
- **Decoded payload**:
  ```json
  [{"func": "QueryJingLingInfo"}]
  ```

### Frame 032: down/server_to_client

- **Segments**: `[26]`
- **Timestamp ms**: `1780601524595` .. `1780601524595`
- **Header**: `18189c91000078000e4010000000000b`
- **Total length**: `120` bytes; **payload codec**: `plain`; **format**: `json_response`
- **Functions**: `QueryJingLingInfoResult`
- **Decoded payload**:
  ```json
  [{"CoinJingLingNum": 0, "Exp": 0, "JingLingID": 0, "LastTime": 0, "Level": 0, "func": "QueryJingLingInfoResult"}]
  ```

### Frame 033: up/client_to_server

- **Segments**: `[27]`
- **Timestamp ms**: `1780601524621` .. `1780601524621`
- **Header**: `1898146300009400000000000000000c`
- **Total length**: `148` bytes; **payload codec**: `plain`; **format**: `urlencoded_request`
- **Functions**: `QueryZuoQiList`
- **Query fields**: `{"bv": "7.0.2", "seq": "12", "session": "02D1B0135ABCDC0D", "sptype": "spv2jodo", "version": "7.0.2"}`
- **Decoded payload**:
  ```json
  [{"func": "QueryZuoQiList"}]
  ```

### Frame 034: down/server_to_client

- **Segments**: `[28]`
- **Timestamp ms**: `1780601524647` .. `1780601524647`
- **Header**: `2c09d780000042000e4010000000000c`
- **Total length**: `66` bytes; **payload codec**: `plain`; **format**: `json_response`
- **Functions**: `QueryZuoQiListResult`
- **Decoded payload**:
  ```json
  [{"ZuoQiList": [], "func": "QueryZuoQiListResult"}]
  ```

### Frame 035: up/client_to_server

- **Segments**: `[29]`
- **Timestamp ms**: `1780601524672` .. `1780601524672`
- **Header**: `01a023870000a600000000000000000d`
- **Total length**: `166` bytes; **payload codec**: `plain`; **format**: `urlencoded_request`
- **Functions**: `ZuoQiEquipQuery`
- **Query fields**: `{"bv": "7.0.2", "seq": "13", "session": "02D1B0135ABCDC0D", "sptype": "spv2jodo", "version": "7.0.2"}`
- **Decoded payload**:
  ```json
  [{"func": "ZuoQiEquipQuery", "zqId": 0}]
  ```

### Frame 036: down/server_to_client

- **Segments**: `[30]`
- **Timestamp ms**: `1780601524698` .. `1780601524698`
- **Header**: `9150e75f00003f000e4010000000000d`
- **Total length**: `63` bytes; **payload codec**: `plain`; **format**: `json_response`
- **Functions**: `ZuoQiEquipQueryResult`
- **Decoded payload**:
  ```json
  [{"equip": [], "func": "ZuoQiEquipQueryResult"}]
  ```

### Frame 037: up/client_to_server

- **Segments**: `[31]`
- **Timestamp ms**: `1780601524725` .. `1780601524725`
- **Header**: `3d0ab55500009400000000000000000e`
- **Total length**: `148` bytes; **payload codec**: `plain`; **format**: `urlencoded_request`
- **Functions**: `ZuoQiSkinQuery`
- **Query fields**: `{"bv": "7.0.2", "seq": "14", "session": "02D1B0135ABCDC0D", "sptype": "spv2jodo", "version": "7.0.2"}`
- **Decoded payload**:
  ```json
  [{"func": "ZuoQiSkinQuery"}]
  ```

### Frame 038: down/server_to_client

- **Segments**: `[32]`
- **Timestamp ms**: `1780601524759` .. `1780601524759`
- **Header**: `bf2e230b000041000e4010000000000e`
- **Total length**: `65` bytes; **payload codec**: `plain`; **format**: `json_response`
- **Functions**: `ZuoQiSkinQueryResult`
- **Decoded payload**:
  ```json
  [{"func": "ZuoQiSkinQueryResult", "skinList": []}]
  ```

### Frame 039: up/client_to_server

- **Segments**: `[33]`
- **Timestamp ms**: `1780601524787` .. `1780601524787`
- **Header**: `a92dab7f00009800000000000000000f`
- **Total length**: `152` bytes; **payload codec**: `plain`; **format**: `urlencoded_request`
- **Functions**: `QueryAllTalentInfo`
- **Query fields**: `{"bv": "7.0.2", "seq": "15", "session": "02D1B0135ABCDC0D", "sptype": "spv2jodo", "version": "7.0.2"}`
- **Decoded payload**:
  ```json
  [{"func": "QueryAllTalentInfo"}]
  ```

### Frame 040: down/server_to_client

- **Segments**: `[34]`
- **Timestamp ms**: `1780601524813` .. `1780601524813`
- **Header**: `67598b6200005f000e4010000000000f`
- **Total length**: `95` bytes; **payload codec**: `plain`; **format**: `json_response`
- **Functions**: `QueryAllTalentInfoResult`
- **Decoded payload**:
  ```json
  [{"TalentList": [], "TreePutedPointList": [], "func": "QueryAllTalentInfoResult"}]
  ```

### Frame 041: up/client_to_server

- **Segments**: `[35]`
- **Timestamp ms**: `1780601524837` .. `1780601524837`
- **Header**: `f8fd7e8000008f000000000000000010`
- **Total length**: `143` bytes; **payload codec**: `plain`; **format**: `urlencoded_request`
- **Functions**: `DollQuery`
- **Query fields**: `{"bv": "7.0.2", "seq": "16", "session": "02D1B0135ABCDC0D", "sptype": "spv2jodo", "version": "7.0.2"}`
- **Decoded payload**:
  ```json
  [{"func": "DollQuery"}]
  ```

### Frame 042: down/server_to_client

- **Segments**: `[36]`
- **Timestamp ms**: `1780601524864` .. `1780601524864`
- **Header**: `8538900e000052000e40100000000010`
- **Total length**: `82` bytes; **payload codec**: `plain`; **format**: `json_response`
- **Functions**: `DollQueryResult`
- **Decoded payload**:
  ```json
  [{"cur": {"cId": 0, "name": ""}, "func": "DollQueryResult", "list": []}]
  ```

### Frame 043: up/client_to_server

- **Segments**: `[37]`
- **Timestamp ms**: `1780601524893` .. `1780601524893`
- **Header**: `21cfd21a000092000000000000000011`
- **Total length**: `146` bytes; **payload codec**: `plain`; **format**: `urlencoded_request`
- **Functions**: `QueryPetList`
- **Query fields**: `{"bv": "7.0.2", "seq": "17", "session": "02D1B0135ABCDC0D", "sptype": "spv2jodo", "version": "7.0.2"}`
- **Decoded payload**:
  ```json
  [{"func": "QueryPetList"}]
  ```

### Frame 044: down/server_to_client

- **Segments**: `[38]`
- **Timestamp ms**: `1780601524922` .. `1780601524922`
- **Header**: `2fb4a40c00003e000e40100000000011`
- **Total length**: `62` bytes; **payload codec**: `plain`; **format**: `json_response`
- **Functions**: `QueryPetListResult`
- **Decoded payload**:
  ```json
  [{"PetList": [], "func": "QueryPetListResult"}]
  ```

### Frame 045: up/client_to_server

- **Segments**: `[39]`
- **Timestamp ms**: `1780601524945` .. `1780601524945`
- **Header**: `378c7a2f000098000000000000000012`
- **Total length**: `152` bytes; **payload codec**: `plain`; **format**: `urlencoded_request`
- **Functions**: `QueryDailyProgress`
- **Query fields**: `{"bv": "7.0.2", "seq": "18", "session": "02D1B0135ABCDC0D", "sptype": "spv2jodo", "version": "7.0.2"}`
- **Decoded payload**:
  ```json
  [{"func": "QueryDailyProgress"}]
  ```

### Frame 046: down/server_to_client

- **Segments**: `[40]`
- **Timestamp ms**: `1780601524976` .. `1780601524976`
- **Header**: `5baa01eb00004a000e40100000000012`
- **Total length**: `74` bytes; **payload codec**: `plain`; **format**: `json_response`
- **Functions**: `QueryDailyProgressResult`
- **Decoded payload**:
  ```json
  [{"dailyProgress": [], "func": "QueryDailyProgressResult"}]
  ```

### Frame 047: up/client_to_server

- **Segments**: `[41]`
- **Timestamp ms**: `1780601524998` .. `1780601524998`
- **Header**: `b080b6eb000094000000000000000013`
- **Total length**: `148` bytes; **payload codec**: `plain`; **format**: `urlencoded_request`
- **Functions**: `ObjRecordQuery`
- **Query fields**: `{"bv": "7.0.2", "seq": "19", "session": "02D1B0135ABCDC0D", "sptype": "spv2jodo", "version": "7.0.2"}`
- **Decoded payload**:
  ```json
  [{"func": "ObjRecordQuery"}]
  ```

### Frame 048: down/server_to_client

- **Segments**: `[42]`
- **Timestamp ms**: `1780601525024` .. `1780601525024`
- **Header**: `fa12d4cb000040000e40100000000013`
- **Total length**: `64` bytes; **payload codec**: `plain`; **format**: `json_response`
- **Functions**: `ObjRecordQueryResult`
- **Decoded payload**:
  ```json
  [{"func": "ObjRecordQueryResult", "objList": []}]
  ```

### Frame 049: up/client_to_server

- **Segments**: `[43]`
- **Timestamp ms**: `1780601525053` .. `1780601525053`
- **Header**: `e8b16c61000092000000000000000014`
- **Total length**: `146` bytes; **payload codec**: `plain`; **format**: `urlencoded_request`
- **Functions**: `QueryQianDao`
- **Query fields**: `{"bv": "7.0.2", "seq": "20", "session": "02D1B0135ABCDC0D", "sptype": "spv2jodo", "version": "7.0.2"}`
- **Decoded payload**:
  ```json
  [{"func": "QueryQianDao"}]
  ```

### Frame 050: down/server_to_client

- **Segments**: `[44]`
- **Timestamp ms**: `1780601525083` .. `1780601525083`
- **Header**: `4555f24e000195010e40100000000014`
- **Total length**: `405` bytes; **payload codec**: `zlib`; **format**: `json_response`
- **Functions**: `QueryQianDaoResult`
- **Decoded payload**:
  ```json
  [{"accum": 0, "data": [{"ItemID": 1, "RewardType": 1, "VipDouble": 4, "count": 150, "id": 610}, {"ItemID": 70025, "RewardType": 0, "VipDouble": 0, "count": 3, "id": 611}, {"ItemID": 79001, "RewardType": 0, "VipDouble": 3, "count": 3, "id": 608}, {"ItemID": 70005, "RewardType": 0, "VipDouble": 0, "count": 2, "id": 609}, {"ItemID": 80262, "RewardType": 0, "VipDouble": 4, "count": 5, "id": 614}, {"ItemID": 14001, "RewardType": 0, "VipDouble": 0, "count": 10, "id": 615}, {"ItemID": 79001, "RewardType": 0, "VipDouble": 3, "count": 6, "id": 612}, {"ItemID": 70027, "RewardType": 0, "VipDouble": 0, "count": 5, "id": 613}, {"ItemID": 1, "RewardType": 1, "VipDouble": 5, "count": 150, "id": 618}, {"ItemID": 12004, "RewardType": 0, "VipDouble": 0, "count": 2, "id": 619}, {"ItemID": 80116, "RewardType": 0, "VipDouble": 3, "count": 3, "id": 616}, {"ItemID": 80198, "RewardType": 0, "VipDouble": 0, "count": 5, "id": 617}, {"ItemID": 1, "RewardType": 1, "VipDouble": 6, "count": 200, "id": 622}, {"ItemID": 70027, "RewardType": 0, "VipDouble": 0, "count": 5, "id": 623}, {"ItemID": 70010, "RewardType": 0, "VipDouble": 4, "count": 5, "id": 620}, {"ItemID": 70005, "RewardType": 0, "VipDouble": 0, "count": 2, "id": 621}, {"ItemID": 70026, "RewardType": 0, "VipDouble": 0, "count": 10, "id": 627}, {"ItemID": 1, "RewardType": 1, "VipDouble": 7, "count": 300, "id": 626}, {"ItemID": 70005, "RewardType": 0, "VipDouble": 0, "count": 2, "id": 625}, {"ItemID": 79001, "RewardType": 0, "VipDouble": 8, "count": 8, "id": 624}, {"ItemID": 12005, "RewardType": 0, "VipDouble": 0, "count": 1, "id": 631}, {"ItemID": 79001, "RewardType": 0, "VipDouble": 8, "count": 10, "id": 630}, {"ItemID": 70032, "RewardType": 0, "VipDouble": 0, "count": 1, "id": 629}, {"ItemID": 80262, "RewardType": 0, "VipDouble": 5, "count": 5, "id": 628}, {"ItemID": 12003, "RewardType": 0, "VipDouble": 0, "count": 2, "id": 601}, {"ItemID": 70026, "RewardType": 0, "VipDouble": 0, "count": 10, "id": 603}, {"ItemID": 1, "RewardType": 1, "VipDouble": 1, "count": 50, "id": 602}, {"ItemID": 70027, "RewardType": 0, "VipDouble": 0, "count": 5, "id": 605}, {"ItemID": 70010, "RewardType": 0, "VipDouble": 2, "count": 5, "id": 604}, {"ItemID": 23302, "RewardType": 2, "VipDouble": 0, "count": 1, "id": 607}, {"ItemID": 1, "RewardType": 1, "VipDouble": 2, "count": 100, "id": 606}], "func": "QueryQianDaoResult", "month": 6, "status": 0}]
  ```

### Frame 051: up/client_to_server

- **Segments**: `[45]`
- **Timestamp ms**: `1780601525106` .. `1780601525106`
- **Header**: `905c84f3000092000000000000000015`
- **Total length**: `146` bytes; **payload codec**: `plain`; **format**: `urlencoded_request`
- **Functions**: `LotteryQuery`
- **Query fields**: `{"bv": "7.0.2", "seq": "21", "session": "02D1B0135ABCDC0D", "sptype": "spv2jodo", "version": "7.0.2"}`
- **Decoded payload**:
  ```json
  [{"func": "LotteryQuery"}]
  ```

### Frame 052: down/server_to_client

- **Segments**: `[46]`
- **Timestamp ms**: `1780601525132` .. `1780601525132`
- **Header**: `ca47ccfe000071000e40100000000015`
- **Total length**: `113` bytes; **payload codec**: `plain`; **format**: `json_response`
- **Functions**: `LotteryQueryResult`
- **Decoded payload**:
  ```json
  [{"func": "LotteryQueryResult", "lotteryList": [], "point": 0, "pointAwardList": [], "totalConsume": 0}]
  ```

### Frame 053: up/client_to_server

- **Segments**: `[47]`
- **Timestamp ms**: `1780601525160` .. `1780601525160`
- **Header**: `d5d230b7000097000000000000000016`
- **Total length**: `151` bytes; **payload codec**: `plain`; **format**: `urlencoded_request`
- **Functions**: `QueryBattleRecord`
- **Query fields**: `{"bv": "7.0.2", "seq": "22", "session": "02D1B0135ABCDC0D", "sptype": "spv2jodo", "version": "7.0.2"}`
- **Decoded payload**:
  ```json
  [{"func": "QueryBattleRecord"}]
  ```

### Frame 054: down/server_to_client

- **Segments**: `[48]`
- **Timestamp ms**: `1780601525186` .. `1780601525186`
- **Header**: `d8036894000080000e40100000000016`
- **Total length**: `128` bytes; **payload codec**: `plain`; **format**: `json_response`
- **Functions**: `QueryBattleRecordResult`
- **Decoded payload**:
  ```json
  [{"battleRecord": {"chapterAward": [], "levelDailyStats": {}, "levelRecords": {}}, "func": "QueryBattleRecordResult"}]
  ```

### Frame 055: up/client_to_server

- **Segments**: `[49]`
- **Timestamp ms**: `1780601525208` .. `1780601525208`
- **Header**: `f22c435c00008f000000000000000017`
- **Total length**: `143` bytes; **payload codec**: `plain`; **format**: `urlencoded_request`
- **Functions**: `TaskQuery`
- **Query fields**: `{"bv": "7.0.2", "seq": "23", "session": "02D1B0135ABCDC0D", "sptype": "spv2jodo", "version": "7.0.2"}`
- **Decoded payload**:
  ```json
  [{"func": "TaskQuery"}]
  ```

### Frame 056: down/server_to_client

- **Segments**: `[50]`
- **Timestamp ms**: `1780601525234` .. `1780601525234`
- **Header**: `a70a20de000092000e40100000000017`
- **Total length**: `146` bytes; **payload codec**: `plain`; **format**: `json_response`
- **Functions**: `TaskQueryResult`
- **Decoded payload**:
  ```json
  [{"func": "TaskQueryResult", "taskInfo": {"acceptedList": [], "finishedDailyList": [], "finishedList": [], "loopCount": 0, "loopIndex": 1}}]
  ```

### Frame 057: up/client_to_server

- **Segments**: `[51]`
- **Timestamp ms**: `1780601525258` .. `1780601525258`
- **Header**: `4bf18e56000096000000000000000018`
- **Total length**: `150` bytes; **payload codec**: `plain`; **format**: `urlencoded_request`
- **Functions**: `QueryGuideRecord`
- **Query fields**: `{"bv": "7.0.2", "seq": "24", "session": "02D1B0135ABCDC0D", "sptype": "spv2jodo", "version": "7.0.2"}`
- **Decoded payload**:
  ```json
  [{"func": "QueryGuideRecord"}]
  ```

### Frame 058: down/server_to_client

- **Segments**: `[52]`
- **Timestamp ms**: `1780601525286` .. `1780601525286`
- **Header**: `b6ef803b00006d000e40100000000018`
- **Total length**: `109` bytes; **payload codec**: `plain`; **format**: `json_response`
- **Functions**: `QueryGuideRecordResult`
- **Decoded payload**:
  ```json
  [{"func": "QueryGuideRecordResult", "record": {"finished": [], "progress": [{"id": 1, "step": 0}]}}]
  ```

### Frame 059: up/client_to_server

- **Segments**: `[53]`
- **Timestamp ms**: `1780601525309` .. `1780601525309`
- **Header**: `452e9cf3000091000000000000000019`
- **Total length**: `145` bytes; **payload codec**: `plain`; **format**: `urlencoded_request`
- **Functions**: `RibbonQuery`
- **Query fields**: `{"bv": "7.0.2", "seq": "25", "session": "02D1B0135ABCDC0D", "sptype": "spv2jodo", "version": "7.0.2"}`
- **Decoded payload**:
  ```json
  [{"func": "RibbonQuery"}]
  ```

### Frame 060: down/server_to_client

- **Segments**: `[54]`
- **Timestamp ms**: `1780601525336` .. `1780601525336`
- **Header**: `6414167700005f000e40100000000019`
- **Total length**: `95` bytes; **payload codec**: `plain`; **format**: `json_response`
- **Functions**: `RibbonQueryResult`
- **Decoded payload**:
  ```json
  [{"func": "RibbonQueryResult", "objectInfo": {"bagBuyCount": 0}, "ribbonList": []}]
  ```

### Frame 061: up/client_to_server

- **Segments**: `[55]`
- **Timestamp ms**: `1780601525365` .. `1780601525365`
- **Header**: `f4e9d4a00000a300000000000000001a`
- **Total length**: `163` bytes; **payload codec**: `plain`; **format**: `urlencoded_request`
- **Functions**: `UpdateCity`
- **Query fields**: `{"bv": "7.0.2", "seq": "26", "session": "02D1B0135ABCDC0D", "sptype": "spv2jodo", "version": "7.0.2"}`
- **Decoded payload**:
  ```json
  [{"city": 201, "func": "UpdateCity"}]
  ```

### Frame 062: up/client_to_server

- **Segments**: `[56]`
- **Timestamp ms**: `1780601525418` .. `1780601525418`
- **Header**: `c0f1a68400009100000000000000001b`
- **Total length**: `145` bytes; **payload codec**: `plain`; **format**: `urlencoded_request`
- **Functions**: `QueryStatus`
- **Query fields**: `{"bv": "7.0.2", "seq": "27", "session": "02D1B0135ABCDC0D", "sptype": "spv2jodo", "version": "7.0.2"}`
- **Decoded payload**:
  ```json
  [{"func": "QueryStatus"}]
  ```

### Frame 063: up/client_to_server

- **Segments**: `[57]`
- **Timestamp ms**: `1780601525470` .. `1780601525470`
- **Header**: `35ff421a00009100000000000000001c`
- **Total length**: `145` bytes; **payload codec**: `plain`; **format**: `urlencoded_request`
- **Functions**: `GetTeamList`
- **Query fields**: `{"bv": "7.0.2", "seq": "28", "session": "02D1B0135ABCDC0D", "sptype": "spv2jodo", "version": "7.0.2"}`
- **Decoded payload**:
  ```json
  [{"func": "GetTeamList"}]
  ```

### Frame 064: up/client_to_server

- **Segments**: `[58]`
- **Timestamp ms**: `1780601525531` .. `1780601525531`
- **Header**: `5a3fd55400009200000000000000001d`
- **Total length**: `146` bytes; **payload codec**: `plain`; **format**: `urlencoded_request`
- **Functions**: `QueryMailBox`
- **Query fields**: `{"bv": "7.0.2", "seq": "29", "session": "02D1B0135ABCDC0D", "sptype": "spv2jodo", "version": "7.0.2"}`
- **Decoded payload**:
  ```json
  [{"func": "QueryMailBox"}]
  ```

### Frame 065: up/client_to_server

- **Segments**: `[59]`
- **Timestamp ms**: `1780601525567` .. `1780601525567`
- **Header**: `a44e6f2800009500000000000000001e`
- **Total length**: `149` bytes; **payload codec**: `plain`; **format**: `urlencoded_request`
- **Functions**: `QueryChargeInfo`
- **Query fields**: `{"bv": "7.0.2", "seq": "30", "session": "02D1B0135ABCDC0D", "sptype": "spv2jodo", "version": "7.0.2"}`
- **Decoded payload**:
  ```json
  [{"func": "QueryChargeInfo"}]
  ```

### Frame 066: down/server_to_client

- **Segments**: `[60]`
- **Timestamp ms**: `1780601525589` .. `1780601525589`
- **Header**: `06d2af5c00007b000e4010000000001b`
- **Total length**: `123` bytes; **payload codec**: `plain`; **format**: `json_response`
- **Functions**: `QueryStatusResult`
- **Decoded payload**:
  ```json
  [{"awardList": [], "cd": 0, "func": "QueryStatusResult", "inspireInfoa": [], "petCurInfos": [], "score": 0, "win": 0}]
  ```

### Frame 067: down/server_to_client

- **Segments**: `[60]`
- **Timestamp ms**: `1780601525589` .. `1780601525589`
- **Header**: `f3f58de900003f000e4010000000001c`
- **Total length**: `63` bytes; **payload codec**: `plain`; **format**: `json_response`
- **Functions**: `GetTeamListResult`
- **Decoded payload**:
  ```json
  [{"TeamInfos": [], "func": "GetTeamListResult"}]
  ```

### Frame 068: down/server_to_client

- **Segments**: `[60]`
- **Timestamp ms**: `1780601525589` .. `1780601525589`
- **Header**: `402ac6c200003c000e4010000000001d`
- **Total length**: `60` bytes; **payload codec**: `plain`; **format**: `json_response`
- **Functions**: `QueryMailBoxResult`
- **Decoded payload**:
  ```json
  [{"func": "QueryMailBoxResult", "mails": []}]
  ```

### Frame 069: down/server_to_client

- **Segments**: `[61]`
- **Timestamp ms**: `1780601525615` .. `1780601525615`
- **Header**: `d5ae8223000096000e4010000000001e`
- **Total length**: `150` bytes; **payload codec**: `plain`; **format**: `json_response`
- **Functions**: `QueryChargeInfoResult`
- **Decoded payload**:
  ```json
  [{"func": "QueryChargeInfoResult", "info": {"charge": 0, "dailyCount": [], "history": [], "monthCardEnd": 0, "weeklyCount": [], "zhiZunCard": 0}}]
  ```

### Frame 070: up/client_to_server

- **Segments**: `[62]`
- **Timestamp ms**: `1780601525617` .. `1780601525617`
- **Header**: `5362324f00009100000000000000001f`
- **Total length**: `145` bytes; **payload codec**: `plain`; **format**: `urlencoded_request`
- **Functions**: `FriendQuery`
- **Query fields**: `{"bv": "7.0.2", "seq": "31", "session": "02D1B0135ABCDC0D", "sptype": "spv2jodo", "version": "7.0.2"}`
- **Decoded payload**:
  ```json
  [{"func": "FriendQuery"}]
  ```

### Frame 071: down/server_to_client

- **Segments**: `[63]`
- **Timestamp ms**: `1780601525643` .. `1780601525643`
- **Header**: `beb21c3500004f000e4010000000001f`
- **Total length**: `79` bytes; **payload codec**: `plain`; **format**: `json_response`
- **Functions**: `FriendQueryResult`
- **Decoded payload**:
  ```json
  [{"applyList": [], "avatarList": [], "func": "FriendQueryResult"}]
  ```

### Frame 072: up/client_to_server

- **Segments**: `[64]`
- **Timestamp ms**: `1780601525688` .. `1780601525688`
- **Header**: `93aad4ea000096000000000000000020`
- **Total length**: `150` bytes; **payload codec**: `plain`; **format**: `urlencoded_request`
- **Functions**: `QueryAvatarItems`
- **Query fields**: `{"bv": "7.0.2", "seq": "32", "session": "02D1B0135ABCDC0D", "sptype": "spv2jodo", "version": "7.0.2"}`
- **Decoded payload**:
  ```json
  [{"func": "QueryAvatarItems"}]
  ```

### Frame 073: down/server_to_client

- **Segments**: `[65]`
- **Timestamp ms**: `1780601525717` .. `1780601525717`
- **Header**: `81272d0300003f000e40100000000020`
- **Total length**: `63` bytes; **payload codec**: `plain`; **format**: `json_response`
- **Functions**: `QueryAvatarItemResult`
- **Decoded payload**:
  ```json
  [{"func": "QueryAvatarItemResult", "items": []}]
  ```

### Frame 074: up/client_to_server

- **Segments**: `[66]`
- **Timestamp ms**: `1780601525740` .. `1780601525740`
- **Header**: `d534eed5000094000000000000000021`
- **Total length**: `148` bytes; **payload codec**: `plain`; **format**: `urlencoded_request`
- **Functions**: `PVPStatusQuery`
- **Query fields**: `{"bv": "7.0.2", "seq": "33", "session": "02D1B0135ABCDC0D", "sptype": "spv2jodo", "version": "7.0.2"}`
- **Decoded payload**:
  ```json
  [{"func": "PVPStatusQuery"}]
  ```

### Frame 075: down/server_to_client

- **Segments**: `[67]`
- **Timestamp ms**: `1780601525767` .. `1780601525767`
- **Header**: `49ecdf450002c8000e40100000000021`
- **Total length**: `712` bytes; **payload codec**: `plain`; **format**: `json_response`
- **Functions**: `PVPStatusUpdate`
- **Decoded payload**:
  ```json
  [{"func": "PVPStatusUpdate", "pvpStatus": {"defenderPet": {"paraList": [], "petIdList": [], "petList": []}, "pvpRanking": {"buyCount": 0, "comboWinMaxToday": 0, "fightCountLimit": 0, "fightTimeCommon": 0, "fightTimeMatch": 0, "rankingMax": 0}, "pvpShow": {"prestige": 0, "show": {"avatarID": "", "avatarName": "", "battlePoint": 0, "campId": 0, "chengHaoID": 0, "comboWin": 0, "comboWinMax": 0, "contentID": 0, "dollId": 0, "dollName": "", "fightCountTotal": 0, "fightCountWin": 0, "guild": "", "guildId": 0, "headFrame": 0, "lastActive": 0, "level": 0, "masterLevel": 0, "mountEquip": [], "mount_ID": 0, "petCount": 0, "petShowList": [], "pet_ID": 0, "ranking": 0, "rid": 0, "rotom_ID": 0, "spriteLevel": 0, "talk": "", "tuxiaongID": 0, "vip": 0}, "title": 0}, "worshipTarget": []}}]
  ```

### Frame 076: up/client_to_server

- **Segments**: `[68]`
- **Timestamp ms**: `1780601525792` .. `1780601525792`
- **Header**: `0628a613000094000000000000000022`
- **Total length**: `148` bytes; **payload codec**: `plain`; **format**: `urlencoded_request`
- **Functions**: `GetSoliderList`
- **Query fields**: `{"bv": "7.0.2", "seq": "34", "session": "02D1B0135ABCDC0D", "sptype": "spv2jodo", "version": "7.0.2"}`
- **Decoded payload**:
  ```json
  [{"func": "GetSoliderList"}]
  ```

### Frame 077: up/client_to_server

- **Segments**: `[69]`
- **Timestamp ms**: `1780601525846` .. `1780601525846`
- **Header**: `ce5f2dbf00009f000000000000000023`
- **Total length**: `159` bytes; **payload codec**: `plain`; **format**: `urlencoded_request`
- **Functions**: `QueryEmploySoliderHistory`
- **Query fields**: `{"bv": "7.0.2", "seq": "35", "session": "02D1B0135ABCDC0D", "sptype": "spv2jodo", "version": "7.0.2"}`
- **Decoded payload**:
  ```json
  [{"func": "QueryEmploySoliderHistory"}]
  ```

### Frame 078: down/server_to_client

- **Segments**: `[70]`
- **Timestamp ms**: `1780601525873` .. `1780601525873`
- **Header**: `a6c0afd700004b000e40100000000023`
- **Total length**: `75` bytes; **payload codec**: `plain`; **format**: `json_response`
- **Functions**: `QueryEmploySoliderHistoryResult`
- **Decoded payload**:
  ```json
  [{"func": "QueryEmploySoliderHistoryResult", "history": []}]
  ```

### Frame 079: up/client_to_server

- **Segments**: `[71]`
- **Timestamp ms**: `1780601525894` .. `1780601525894`
- **Header**: `c4a3fcc5000097000000000000000024`
- **Total length**: `151` bytes; **payload codec**: `plain`; **format**: `urlencoded_request`
- **Functions**: `QueryTreasureCave`
- **Query fields**: `{"bv": "7.0.2", "seq": "36", "session": "02D1B0135ABCDC0D", "sptype": "spv2jodo", "version": "7.0.2"}`
- **Decoded payload**:
  ```json
  [{"func": "QueryTreasureCave"}]
  ```

### Frame 080: down/server_to_client

- **Segments**: `[72]`
- **Timestamp ms**: `1780601525923` .. `1780601525923`
- **Header**: `17bf18c300007a000e40100000000024`
- **Total length**: `122` bytes; **payload codec**: `plain`; **format**: `json_response`
- **Functions**: `QueryTreasureCaveResult`
- **Decoded payload**:
  ```json
  [{"bossRank": 0, "bossTop": 0, "func": "QueryTreasureCaveResult", "lastChallengeTime": 0, "leftChallengeCnt": 2}]
  ```

### Frame 081: up/client_to_server

- **Segments**: `[73]`
- **Timestamp ms**: `1780601525948` .. `1780601525948`
- **Header**: `b0b2185d00009c000000000000000025`
- **Total length**: `156` bytes; **payload codec**: `plain`; **format**: `urlencoded_request`
- **Functions**: `QueryTreasureCaveAward`
- **Query fields**: `{"bv": "7.0.2", "seq": "37", "session": "02D1B0135ABCDC0D", "sptype": "spv2jodo", "version": "7.0.2"}`
- **Decoded payload**:
  ```json
  [{"func": "QueryTreasureCaveAward"}]
  ```

### Frame 082: down/server_to_client

- **Segments**: `[74]`
- **Timestamp ms**: `1780601525975` .. `1780601525975`
- **Header**: `16f55ad000005f000e40100000000025`
- **Total length**: `95` bytes; **payload codec**: `plain`; **format**: `json_response`
- **Functions**: `QueryTreasureCaveAwardResult`
- **Decoded payload**:
  ```json
  [{"func": "QueryTreasureCaveAwardResult", "receivedAwards": [], "totalDamage": 0}]
  ```

### Frame 083: up/client_to_server

- **Segments**: `[75]`
- **Timestamp ms**: `1780601526001` .. `1780601526001`
- **Header**: `34fe11f6000097000000000000000026`
- **Total length**: `151` bytes; **payload codec**: `plain`; **format**: `urlencoded_request`
- **Functions**: `QueryVipLiBaoDraw`
- **Query fields**: `{"bv": "7.0.2", "seq": "38", "session": "02D1B0135ABCDC0D", "sptype": "spv2jodo", "version": "7.0.2"}`
- **Decoded payload**:
  ```json
  [{"func": "QueryVipLiBaoDraw"}]
  ```

### Frame 084: down/server_to_client

- **Segments**: `[76]`
- **Timestamp ms**: `1780601526028` .. `1780601526028`
- **Header**: `7f16486c000041000e40100000000026`
- **Total length**: `65` bytes; **payload codec**: `plain`; **format**: `json_response`
- **Functions**: `QueryVipLiBaoDrawResult`
- **Decoded payload**:
  ```json
  [{"func": "QueryVipLiBaoDrawResult", "infos": []}]
  ```

### Frame 085: up/client_to_server

- **Segments**: `[77]`
- **Timestamp ms**: `1780601526050` .. `1780601526050`
- **Header**: `54e3872f000095000000000000000027`
- **Total length**: `149` bytes; **payload codec**: `plain`; **format**: `urlencoded_request`
- **Functions**: `GlobalBossQuery`
- **Query fields**: `{"bv": "7.0.2", "seq": "39", "session": "02D1B0135ABCDC0D", "sptype": "spv2jodo", "version": "7.0.2"}`
- **Decoded payload**:
  ```json
  [{"func": "GlobalBossQuery"}]
  ```

### Frame 086: up/client_to_server

- **Segments**: `[79]`
- **Timestamp ms**: `1780601526105` .. `1780601526105`
- **Header**: `4c1645e8000094000000000000000028`
- **Total length**: `148` bytes; **payload codec**: `plain`; **format**: `urlencoded_request`
- **Functions**: `GlobalPetQuery`
- **Query fields**: `{"bv": "7.0.2", "seq": "40", "session": "02D1B0135ABCDC0D", "sptype": "spv2jodo", "version": "7.0.2"}`
- **Decoded payload**:
  ```json
  [{"func": "GlobalPetQuery"}]
  ```

### Frame 087: down/server_to_client

- **Segments**: `[78, 80]`
- **Timestamp ms**: `1780601526077` .. `1780601526105`
- **Header**: `9a6321160005bc010e40100000000027`
- **Total length**: `1468` bytes; **payload codec**: `zlib`; **format**: `json_response`
- **Functions**: `GlobalBossQueryResult`
- **Decoded payload**:
  ```json
  [{"bossStatus": {"bossId": 990072, "damageList": [{"avatarID": "b19d03f0-6f6b-4fe8-a07a-e5cd70d60b33", "avatarName": "Isko", "battlePoint": 7999192, "campId": 1, "chengHaoID": 1023, "contentID": 2046, "damageTotal": 33755035, "dollId": 0, "dollName": "", "fightCount": 37, "fightTimeNext": 1780575849, "guild": "Stars", "guildId": 195125658, "headFrame": 4, "inspireCount": 10, "level": 84, "masterLevel": 0, "mountEquip": [], "mount_ID": 0, "petCount": 184, "petKilled": 0, "pet_ID": 21082, "ranking": 1, "rid": 195125409, "rotom_ID": 1001, "spriteLevel": 35, "talk": "", "tuxiaongID": 21572, "vip": 15}, {"avatarID": "07a68e7a-21ce-4387-a447-4ed2fb97f147", "avatarName": "Recycler", "battlePoint": 4579292, "campId": 1, "chengHaoID": 0, "contentID": 2045, "damageTotal": 15203154, "dollId": 0, "dollName": "", "fightCount": 20, "fightTimeNext": 1780575850, "guild": "SG⚘GĐ", "guildId": 195123642, "headFrame": 0, "inspireCount": 0, "level": 83, "masterLevel": 0, "mountEquip": [], "mount_ID": 7004, "petCount": 178, "petKilled": 0, "pet_ID": 1023522, "ranking": 2, "rid": 195123693, "rotom_ID": 1002, "spriteLevel": 34, "talk": "", "tuxiaongID": 2045, "vip": 14}, {"avatarID": "14fa5938-a9a4-4e99-9cb4-9738723cfcbe", "avatarName": "哈基咪", "battlePoint": 5144237, "campId": 1, "chengHaoID": 1029, "contentID": 2014, "damageTotal": 7197986, "dollId": 0, "dollName": "", "fightCount": 22, "fightTimeNext": 1780575804, "guild": "SG⚘GĐ", "guildId": 195123642, "headFrame": 13, "inspireCount": 0, "level": 80, "masterLevel": 0, "mountEquip": [{"id": 4, "value": 3}], "mount_ID": 7004, "petCount": 212, "petKilled": 0, "pet_ID": 1020592, "ranking": 3, "rid": 195123521, "rotom_ID": 0, "spriteLevel": 34, "talk": "", "tuxiaongID": 2014, "vip": 13}, {"avatarID": "8d413ef0-b103-4b88-bf45-db611d16219b", "avatarName": "MiH4wk", "battlePoint": 5210991, "campId": 1, "chengHaoID": 1022, "contentID": 2037, "damageTotal": 5853144, "dollId": 0, "dollName": "", "fightCount": 24, "fightTimeNext": 1780575843, "guild": "SG⚘GĐ", "guildId": 195123642, "headFrame": 0, "inspireCount": 0, "level": 80, "masterLevel": 0, "mountEquip": [], "mount_ID": 7004, "petCount": 184, "petKilled": 0, "pet_ID": 1023502, "ranking": 4, "rid": 195123794, "rotom_ID": 1002, "spriteLevel": 32, "talk": "", "tuxiaongID": 2037, "vip": 13}, {"avatarID": "716cc804-6090-48c8-9b0b-f8dec36be97b", "avatarName": "FabianTyt", "battlePoint": 7249864, "campId": 1, "chengHaoID": 1009, "contentID": 1009, "damageTotal": 5278128, "dollId": 0, "dollName": "", "fightCount": 10, "fightTimeNext": 1780575801, "guild": "Warzone", "guildId": 195123738, "headFrame": 24, "inspireCount": 0, "level": 83, "masterLevel": 0, "mountEquip": [{"id": 4, "value": 3}, {"id": 5, "value": 1}], "mount_ID": 7004, "petCount": 195, "petKilled": 0, "pet_ID": 1023502, "ranking": 5, "rid": 195125267, "rotom_ID": 0, "spriteLevel": 35, "talk": "", "tuxiaongID": 20859, "vip": 14}, {"avatarID": "d660c65e-c3d0-43ba-9e46-3eae52dce466", "avatarName": "⚘Civic", "battlePoint"... <truncated in markdown; see decoded_packets.json>
  ```

### Frame 088: down/server_to_client

- **Segments**: `[81, 82]`
- **Timestamp ms**: `1780601526132` .. `1780601526132`
- **Header**: `e0ffb1120005c3010e40100000000028`
- **Total length**: `1475` bytes; **payload codec**: `zlib`; **format**: `json_response`
- **Functions**: `GlobalPetQueryResult`
- **Decoded payload**:
  ```json
  [{"func": "GlobalPetQueryResult", "gpetStatus": {"damageList": [{"avatarID": "07a68e7a-21ce-4387-a447-4ed2fb97f147", "avatarName": "Recycler", "battlePoint": 4579292, "campId": 1, "chengHaoID": 0, "contentID": 2045, "damageTotal": 5174587, "dollId": 0, "dollName": "", "fightCount": 242, "fightTimeNext": 1780579841, "guild": "SG⚘GĐ", "guildId": 195123642, "headFrame": 0, "level": 83, "masterLevel": 0, "mountEquip": [], "mount_ID": 7004, "petCount": 178, "petKilled": 242, "pet_ID": 1023522, "ranking": 1, "rid": 195123693, "rotom_ID": 1002, "spriteLevel": 34, "talk": "", "tuxiaongID": 2045, "vip": 14}, {"avatarID": "d4df0223-ca5d-48f7-9a50-fb408ca21915", "avatarName": "Gió⚘MD", "battlePoint": 5984835, "campId": 1, "chengHaoID": 1009, "contentID": 2019, "damageTotal": 1988851, "dollId": 0, "dollName": "", "fightCount": 78, "fightTimeNext": 1780579854, "guild": "SG⚘GĐ", "guildId": 195123642, "headFrame": 38, "level": 81, "masterLevel": 0, "mountEquip": [], "mount_ID": 7004, "petCount": 125, "petKilled": 78, "pet_ID": 1023522, "ranking": 2, "rid": 195123571, "rotom_ID": 1002, "spriteLevel": 33, "talk": "", "tuxiaongID": 1022, "vip": 14}, {"avatarID": "14fa5938-a9a4-4e99-9cb4-9738723cfcbe", "avatarName": "哈基咪", "battlePoint": 5169886, "campId": 1, "chengHaoID": 1029, "contentID": 2014, "damageTotal": 1983465, "dollId": 0, "dollName": "", "fightCount": 131, "fightTimeNext": 1780579811, "guild": "SG⚘GĐ", "guildId": 195123642, "headFrame": 13, "level": 80, "masterLevel": 0, "mountEquip": [{"id": 4, "value": 3}], "mount_ID": 7004, "petCount": 205, "petKilled": 120, "pet_ID": 1020592, "ranking": 3, "rid": 195123521, "rotom_ID": 0, "spriteLevel": 34, "talk": "", "tuxiaongID": 2014, "vip": 13}, {"avatarID": "8d413ef0-b103-4b88-bf45-db611d16219b", "avatarName": "MiH4wk", "battlePoint": 5233968, "campId": 1, "chengHaoID": 1022, "contentID": 2037, "damageTotal": 549937, "dollId": 0, "dollName": "", "fightCount": 24, "fightTimeNext": 1780579852, "guild": "SG⚘GĐ", "guildId": 195123642, "headFrame": 0, "level": 80, "masterLevel": 0, "mountEquip": [], "mount_ID": 7004, "petCount": 184, "petKilled": 20, "pet_ID": 1023502, "ranking": 4, "rid": 195123794, "rotom_ID": 1002, "spriteLevel": 32, "talk": "", "tuxiaongID": 2037, "vip": 13}, {"avatarID": "c6f7c86c-fa41-40c4-b980-93016401760c", "avatarName": "BassBale", "battlePoint": 2925552, "campId": 2, "chengHaoID": 11049, "contentID": 2014, "damageTotal": 394305, "dollId": 0, "dollName": "", "fightCount": 25, "fightTimeNext": 1780579592, "guild": "SG⚘GĐ", "guildId": 195123642, "headFrame": 13, "level": 75, "masterLevel": 0, "mountEquip": [{"id": 4, "value": 1}], "mount_ID": 7004, "petCount": 148, "petKilled": 18, "pet_ID": 20744, "ranking": 5, "rid": 195123518, "rotom_ID": 0, "spriteLevel": 32, "talk": "", "tuxiaongID": 2014, "vip": 13}, {"avatarID": "56350147-1a02-4a63-bf36-a01685fa4e72", "avatarName": "nohatno", "battlePoint": 5493321, "campId": 2, "chengHaoID": 1007, "contentID": 1034, "damageTotal": 352204, "dollId": 0... <truncated in markdown; see decoded_packets.json>
  ```

### Frame 089: up/client_to_server

- **Segments**: `[83]`
- **Timestamp ms**: `1780601526152` .. `1780601526152`
- **Header**: `5104eaea000097000000000000000029`
- **Total length**: `151` bytes; **payload codec**: `plain`; **format**: `urlencoded_request`
- **Functions**: `MiJingStatusQuery`
- **Query fields**: `{"bv": "7.0.2", "seq": "41", "session": "02D1B0135ABCDC0D", "sptype": "spv2jodo", "version": "7.0.2"}`
- **Decoded payload**:
  ```json
  [{"func": "MiJingStatusQuery"}]
  ```

### Frame 090: down/server_to_client

- **Segments**: `[84]`
- **Timestamp ms**: `1780601526181` .. `1780601526181`
- **Header**: `4ffa8e2c00014f000e40100000000029`
- **Total length**: `335` bytes; **payload codec**: `plain`; **format**: `json_response`
- **Functions**: `MiJingStatusUpdate`
- **Decoded payload**:
  ```json
  [{"func": "MiJingStatusUpdate", "mijingStatus": {"catchCount": 0, "catchSenior": 0, "freeTicket": 1, "petIdList": [20291, 20791, 20761, 20151, 20921, 22751, 20291, 20622, 20791, 20621], "petIdSenior": [23201, 20781, 20342, 21211, 21231, 20302, 20311, 20311, 20342, 21231], "target": {"cdList": [], "escape": 0, "flagSenior": 0, "hp": 0, "hpMax": 0, "id": 0}}}]
  ```

### Frame 091: up/client_to_server

- **Segments**: `[85]`
- **Timestamp ms**: `1780601526204` .. `1780601526204`
- **Header**: `42ddf10e00009500000000000000002a`
- **Total length**: `149` bytes; **payload codec**: `plain`; **format**: `urlencoded_request`
- **Functions**: `PetExploreQuery`
- **Query fields**: `{"bv": "7.0.2", "seq": "42", "session": "02D1B0135ABCDC0D", "sptype": "spv2jodo", "version": "7.0.2"}`
- **Decoded payload**:
  ```json
  [{"func": "PetExploreQuery"}]
  ```

### Frame 092: down/server_to_client

- **Segments**: `[86]`
- **Timestamp ms**: `1780601526233` .. `1780601526233`
- **Header**: `ca57eaa200007b000e4010000000002a`
- **Total length**: `123` bytes; **payload codec**: `plain`; **format**: `json_response`
- **Functions**: `PetExploreQueryResult`
- **Decoded payload**:
  ```json
  [{"func": "PetExploreQueryResult", "info": {"evolutionPicked": [], "exp": 0, "fragment": 0, "level": 0, "point": 0}}]
  ```

### Frame 093: up/client_to_server

- **Segments**: `[87]`
- **Timestamp ms**: `1780601526258` .. `1780601526258`
- **Header**: `fa63f74f00009800000000000000002b`
- **Total length**: `152` bytes; **payload codec**: `plain`; **format**: `urlencoded_request`
- **Functions**: `QueryDecorationBag`
- **Query fields**: `{"bv": "7.0.2", "seq": "43", "session": "02D1B0135ABCDC0D", "sptype": "spv2jodo", "version": "7.0.2"}`
- **Decoded payload**:
  ```json
  [{"func": "QueryDecorationBag"}]
  ```

### Frame 094: down/server_to_client

- **Segments**: `[88]`
- **Timestamp ms**: `1780601526286` .. `1780601526286`
- **Header**: `01d8258900005f000e4010000000002b`
- **Total length**: `95` bytes; **payload codec**: `plain`; **format**: `json_response`
- **Functions**: `QueryDecorationBagResult`
- **Decoded payload**:
  ```json
  [{"count": 1, "decorationInfos": [], "func": "QueryDecorationBagResult", "num": 50}]
  ```

### Frame 095: up/client_to_server

- **Segments**: `[89]`
- **Timestamp ms**: `1780601526310` .. `1780601526310`
- **Header**: `759eb31d00009400000000000000002c`
- **Total length**: `148` bytes; **payload codec**: `plain`; **format**: `urlencoded_request`
- **Functions**: `ZBraceletQuery`
- **Query fields**: `{"bv": "7.0.2", "seq": "44", "session": "02D1B0135ABCDC0D", "sptype": "spv2jodo", "version": "7.0.2"}`
- **Decoded payload**:
  ```json
  [{"func": "ZBraceletQuery"}]
  ```

### Frame 096: down/server_to_client

- **Segments**: `[90]`
- **Timestamp ms**: `1780601526336` .. `1780601526336`
- **Header**: `53bf26b400003e000e4010000000002c`
- **Total length**: `62` bytes; **payload codec**: `plain`; **format**: `json_response`
- **Functions**: `ZBraceletQueryResult`
- **Decoded payload**:
  ```json
  [{"func": "ZBraceletQueryResult", "zbAll": []}]
  ```

### Frame 097: up/client_to_server

- **Segments**: `[91]`
- **Timestamp ms**: `1780601526365` .. `1780601526365`
- **Header**: `5178b22500009100000000000000002d`
- **Total length**: `145` bytes; **payload codec**: `plain`; **format**: `urlencoded_request`
- **Functions**: `QueryPetBag`
- **Query fields**: `{"bv": "7.0.2", "seq": "45", "session": "02D1B0135ABCDC0D", "sptype": "spv2jodo", "version": "7.0.2"}`
- **Decoded payload**:
  ```json
  [{"func": "QueryPetBag"}]
  ```

### Frame 098: down/server_to_client

- **Segments**: `[92]`
- **Timestamp ms**: `1780601526391` .. `1780601526391`
- **Header**: `541eebee000043000e4010000000002d`
- **Total length**: `67` bytes; **payload codec**: `plain`; **format**: `json_response`
- **Functions**: `QueryPetBagResult`
- **Decoded payload**:
  ```json
  [{"count": 0, "func": "QueryPetBagResult", "num": 50}]
  ```

### Frame 099: up/client_to_server

- **Segments**: `[93]`
- **Timestamp ms**: `1780601526420` .. `1780601526420`
- **Header**: `797aed4b00009300000000000000002e`
- **Total length**: `147` bytes; **payload codec**: `plain`; **format**: `urlencoded_request`
- **Functions**: `LivenessQuery`
- **Query fields**: `{"bv": "7.0.2", "seq": "46", "session": "02D1B0135ABCDC0D", "sptype": "spv2jodo", "version": "7.0.2"}`
- **Decoded payload**:
  ```json
  [{"func": "LivenessQuery"}]
  ```

### Frame 100: down/server_to_client

- **Segments**: `[94]`
- **Timestamp ms**: `1780601526448` .. `1780601526448`
- **Header**: `247abc0f0000a2000e4010000000002e`
- **Total length**: `162` bytes; **payload codec**: `plain`; **format**: `json_response`
- **Functions**: `LivenessQueryResult`
- **Decoded payload**:
  ```json
  [{"func": "LivenessQueryResult", "livenessInfo": {"dailyLevel": 1, "dailyReward": [], "dailyValue": 0, "weekReward": [], "weekValue": 0}, "livenessList": []}]
  ```

### Frame 101: up/client_to_server

- **Segments**: `[95]`
- **Timestamp ms**: `1780601526474` .. `1780601526474`
- **Header**: `c9b4880600009900000000000000002f`
- **Total length**: `153` bytes; **payload codec**: `plain`; **format**: `urlencoded_request`
- **Functions**: `RichnessForestQuery`
- **Query fields**: `{"bv": "7.0.2", "seq": "47", "session": "02D1B0135ABCDC0D", "sptype": "spv2jodo", "version": "7.0.2"}`
- **Decoded payload**:
  ```json
  [{"func": "RichnessForestQuery"}]
  ```

### Frame 102: down/server_to_client

- **Segments**: `[96]`
- **Timestamp ms**: `1780601526500` .. `1780601526500`
- **Header**: `b1202d9b0000d9000e4010000000002f`
- **Total length**: `217` bytes; **payload codec**: `plain`; **format**: `json_response`
- **Functions**: `RichnessForestQueryResult`
- **Decoded payload**:
  ```json
  [{"func": "RichnessForestQueryResult", "info": {"battleResult": 0, "challengeCount": 0, "lastWinWave": 0, "maxWave": 0, "petFight": {"paraList": [], "petIdList": [], "petList": []}, "usedPetList": [], "waveReward": []}}]
  ```

### Frame 103: up/client_to_server

- **Segments**: `[97]`
- **Timestamp ms**: `1780601526537` .. `1780601526537`
- **Header**: `c990109e000093000000000000000030`
- **Total length**: `147` bytes; **payload codec**: `plain`; **format**: `urlencoded_request`
- **Functions**: `CampTechQuery`
- **Query fields**: `{"bv": "7.0.2", "seq": "48", "session": "02D1B0135ABCDC0D", "sptype": "spv2jodo", "version": "7.0.2"}`
- **Decoded payload**:
  ```json
  [{"func": "CampTechQuery"}]
  ```

### Frame 104: down/server_to_client

- **Segments**: `[98]`
- **Timestamp ms**: `1780601526565` .. `1780601526565`
- **Header**: `6a63c2d2000053000e40100000000030`
- **Total length**: `83` bytes; **payload codec**: `plain`; **format**: `json_response`
- **Functions**: `CampTechQueryResult`
- **Decoded payload**:
  ```json
  [{"func": "CampTechQueryResult", "techList": [], "techPointList": []}]
  ```

### Frame 105: up/client_to_server

- **Segments**: `[99]`
- **Timestamp ms**: `1780601526590` .. `1780601526590`
- **Header**: `2dbd811b000095000000000000000031`
- **Total length**: `149` bytes; **payload codec**: `plain`; **format**: `urlencoded_request`
- **Functions**: `CampStatueQuery`
- **Query fields**: `{"bv": "7.0.2", "seq": "49", "session": "02D1B0135ABCDC0D", "sptype": "spv2jodo", "version": "7.0.2"}`
- **Decoded payload**:
  ```json
  [{"func": "CampStatueQuery"}]
  ```

### Frame 106: down/server_to_client

- **Segments**: `[100]`
- **Timestamp ms**: `1780601526617` .. `1780601526617`
- **Header**: `0bdeeb28000062000e40100000000031`
- **Total length**: `98` bytes; **payload codec**: `plain`; **format**: `json_response`
- **Functions**: `CampStatueQueryResult`
- **Decoded payload**:
  ```json
  [{"func": "CampStatueQueryResult", "infos": [], "squareDreamBag": [], "statueBag": []}]
  ```

### Frame 107: up/client_to_server

- **Segments**: `[101]`
- **Timestamp ms**: `1780601526644` .. `1780601526644`
- **Header**: `ebfa15a3000097000000000000000032`
- **Total length**: `151` bytes; **payload codec**: `plain`; **format**: `urlencoded_request`
- **Functions**: `InviteReturnQuery`
- **Query fields**: `{"bv": "7.0.2", "seq": "50", "session": "02D1B0135ABCDC0D", "sptype": "spv2jodo", "version": "7.0.2"}`
- **Decoded payload**:
  ```json
  [{"func": "InviteReturnQuery"}]
  ```

### Frame 108: down/server_to_client

- **Segments**: `[102]`
- **Timestamp ms**: `1780601526673` .. `1780601526673`
- **Header**: `7ea76e8f000204000e40100000000032`
- **Total length**: `516` bytes; **payload codec**: `plain`; **format**: `json_response`
- **Functions**: `InviteReturnQueryResult`
- **Decoded payload**:
  ```json
  [{"error_code": 0, "func": "InviteReturnQueryResult", "info": {"common": {"avatarID": "f25f2e5d-5ff3-4a83-89d5-4d259303f4bd", "avatarName": "BeetBoij", "battlePoint": 0, "campId": 0, "chengHaoID": 0, "contentID": 1002, "dollId": 0, "dollName": "", "guild": "", "guildId": 0, "headFrame": 0, "level": 1, "masterLevel": 0, "mountEquip": [], "mount_ID": 0, "petCount": 0, "pet_ID": 0, "rid": 195132877, "rotom_ID": 0, "spriteLevel": 0, "talk": "", "tuxiaongID": 1002, "vip": 0}, "invite": "v2R55YC3", "inviteBind": "", "statistics": [], "task": []}, "list": []}]
  ```

### Frame 109: up/client_to_server

- **Segments**: `[103]`
- **Timestamp ms**: `1780601526701` .. `1780601526701`
- **Header**: `f829d894000093000000000000000033`
- **Total length**: `147` bytes; **payload codec**: `plain`; **format**: `urlencoded_request`
- **Functions**: `TopMatchQuery`
- **Query fields**: `{"bv": "7.0.2", "seq": "51", "session": "02D1B0135ABCDC0D", "sptype": "spv2jodo", "version": "7.0.2"}`
- **Decoded payload**:
  ```json
  [{"func": "TopMatchQuery"}]
  ```

### Frame 110: down/server_to_client

- **Segments**: `[104]`
- **Timestamp ms**: `1780601526730` .. `1780601526730`
- **Header**: `d1e26ef70002b7000e40100000000033`
- **Total length**: `695` bytes; **payload codec**: `plain`; **format**: `json_response`
- **Functions**: `TopMatchQueryResult`
- **Decoded payload**:
  ```json
  [{"avatar": {"bApply": 0, "common": {"avatarID": "f25f2e5d-5ff3-4a83-89d5-4d259303f4bd", "avatarName": "BeetBoij", "battlePoint": 0, "campId": 0, "chengHaoID": 0, "contentID": 1002, "dollId": 0, "dollName": "", "guild": "", "guildId": 0, "headFrame": 0, "level": 1, "masterLevel": 0, "mountEquip": [], "mount_ID": 0, "petCount": 0, "pet_ID": 0, "rid": 195132877, "rotom_ID": 0, "spriteLevel": 0, "talk": "", "tuxiaongID": 1002, "vip": 0}, "enemyList": [], "fightLog": [], "lastAddScore": 0, "petList": [], "petShowList": [], "record": 0, "rewardList": [], "score": 0, "support": []}, "error_code": 0, "func": "TopMatchQueryResult", "info": {"avatars": [], "fightLog": [], "gid": 16, "num": 11, "rank": [], "round": 6, "stage": 2, "status": 0, "weekResetDay": 20604}}]
  ```

### Frame 111: up/client_to_server

- **Segments**: `[105]`
- **Timestamp ms**: `1780601526761` .. `1780601526761`
- **Header**: `202cf91d000098000000000000000034`
- **Total length**: `152` bytes; **payload codec**: `plain`; **format**: `urlencoded_request`
- **Functions**: `DecorationGemQuery`
- **Query fields**: `{"bv": "7.0.2", "seq": "52", "session": "02D1B0135ABCDC0D", "sptype": "spv2jodo", "version": "7.0.2"}`
- **Decoded payload**:
  ```json
  [{"func": "DecorationGemQuery"}]
  ```

### Frame 112: down/server_to_client

- **Segments**: `[106]`
- **Timestamp ms**: `1780601526787` .. `1780601526787`
- **Header**: `6492b7ef000044000e40100000000034`
- **Total length**: `68` bytes; **payload codec**: `plain`; **format**: `json_response`
- **Functions**: `DecorationGemQueryResult`
- **Decoded payload**:
  ```json
  [{"func": "DecorationGemQueryResult", "gamlist": []}]
  ```

### Frame 113: up/client_to_server

- **Segments**: `[107]`
- **Timestamp ms**: `1780601526823` .. `1780601526823`
- **Header**: `339189cc000097000000000000000035`
- **Total length**: `151` bytes; **payload codec**: `plain`; **format**: `urlencoded_request`
- **Functions**: `ExchangeShopQuery`
- **Query fields**: `{"bv": "7.0.2", "seq": "53", "session": "02D1B0135ABCDC0D", "sptype": "spv2jodo", "version": "7.0.2"}`
- **Decoded payload**:
  ```json
  [{"func": "ExchangeShopQuery"}]
  ```

### Frame 114: down/server_to_client

- **Segments**: `[108]`
- **Timestamp ms**: `1780601526848` .. `1780601526848`
- **Header**: `2399cb04000186010e40100000000035`
- **Total length**: `390` bytes; **payload codec**: `zlib`; **format**: `json_response`
- **Functions**: `ExchangeShopQueryResult`
- **Decoded payload**:
  ```json
  [{"func": "ExchangeShopQueryResult", "shopList": [{"buyCount": 0, "count": 1, "lastTimeReset": 1780601520, "shopId": 2}, {"buyCount": 0, "count": 1, "lastTimeReset": 1780601520, "shopId": 3}, {"buyCount": 0, "count": 1, "lastTimeReset": 1780601520, "shopId": 4}, {"buyCount": 0, "count": 1, "lastTimeReset": 1780601520, "shopId": 5}, {"buyCount": 0, "count": 1, "lastTimeReset": 1780601520, "shopId": 6}, {"buyCount": 0, "count": 1, "lastTimeReset": 1780601520, "shopId": 7}, {"buyCount": 0, "count": 1, "lastTimeReset": 1780601520, "shopId": 8}, {"buyCount": 0, "count": 1, "lastTimeReset": 1780601520, "shopId": 9}, {"buyCount": 0, "count": 1, "lastTimeReset": 1780601520, "shopId": 10}, {"buyCount": 0, "count": 1, "lastTimeReset": 1780601520, "shopId": 11}, {"buyCount": 0, "count": 1, "lastTimeReset": 1780601520, "shopId": 12}, {"buyCount": 0, "count": 1, "lastTimeReset": 1780601520, "shopId": 13}, {"buyCount": 0, "count": 1, "lastTimeReset": 1780601520, "shopId": 14}, {"buyCount": 0, "count": 1, "lastTimeReset": 1780601520, "shopId": 15}, {"buyCount": 0, "count": 1, "lastTimeReset": 1780601520, "shopId": 17}, {"buyCount": 0, "count": 1, "lastTimeReset": 1780601520, "shopId": 16}, {"buyCount": 0, "count": 1, "lastTimeReset": 1780601520, "shopId": 19}, {"buyCount": 0, "count": 1, "lastTimeReset": 1780601520, "shopId": 18}, {"buyCount": 0, "count": 1, "lastTimeReset": 1780601520, "shopId": 21}, {"buyCount": 0, "count": 1, "lastTimeReset": 1780601520, "shopId": 20}, {"buyCount": 0, "count": 1, "lastTimeReset": 1780601520, "shopId": 23}, {"buyCount": 0, "count": 1, "lastTimeReset": 1780601520, "shopId": 22}, {"buyCount": 0, "count": 1, "lastTimeReset": 1780601520, "shopId": 25}, {"buyCount": 0, "count": 1, "lastTimeReset": 1780601520, "shopId": 24}, {"buyCount": 0, "count": 1, "lastTimeReset": 1780601520, "shopId": 27}, {"buyCount": 0, "count": 1, "lastTimeReset": 1780601520, "shopId": 26}, {"buyCount": 0, "count": 1, "lastTimeReset": 1780601520, "shopId": 29}, {"buyCount": 0, "count": 1, "lastTimeReset": 1780601520, "shopId": 28}, {"buyCount": 0, "count": 1, "lastTimeReset": 1780601520, "shopId": 31}, {"buyCount": 0, "count": 1, "lastTimeReset": 1780601520, "shopId": 30}, {"buyCount": 0, "count": 1, "lastTimeReset": 1780601520, "shopId": 34}, {"buyCount": 0, "count": 1, "lastTimeReset": 1780601520, "shopId": 35}, {"buyCount": 0, "count": 1, "lastTimeReset": 1780601520, "shopId": 32}, {"buyCount": 0, "count": 1, "lastTimeReset": 1780601520, "shopId": 33}, {"buyCount": 0, "count": 1, "lastTimeReset": 1780601520, "shopId": 38}, {"buyCount": 0, "count": 1, "lastTimeReset": 1780601520, "shopId": 39}, {"buyCount": 0, "count": 1, "lastTimeReset": 1780601520, "shopId": 36}, {"buyCount": 0, "count": 1, "lastTimeReset": 1780601520, "shopId": 37}, {"buyCount": 0, "count": 1, "lastTimeReset": 1780601520, "shopId": 42}, {"buyCount": 0, "count": 1, "lastTimeReset": 1780601520, "shopId": 43}, {"buyCount": 0, "count": 1, "lastTimeReset": 1780601520, "shopId": 40}, {"buyC... <truncated in markdown; see decoded_packets.json>
  ```

### Frame 115: up/client_to_server

- **Segments**: `[109]`
- **Timestamp ms**: `1780601526883` .. `1780601526883`
- **Header**: `34ada0a1000096000000000000000036`
- **Total length**: `150` bytes; **payload codec**: `plain`; **format**: `urlencoded_request`
- **Functions**: `PetResearchQuery`
- **Query fields**: `{"bv": "7.0.2", "seq": "54", "session": "02D1B0135ABCDC0D", "sptype": "spv2jodo", "version": "7.0.2"}`
- **Decoded payload**:
  ```json
  [{"func": "PetResearchQuery"}]
  ```

### Frame 116: down/server_to_client

- **Segments**: `[110]`
- **Timestamp ms**: `1780601526909` .. `1780601526909`
- **Header**: `c36c0b0e00005b000e40100000000036`
- **Total length**: `91` bytes; **payload codec**: `plain`; **format**: `json_response`
- **Functions**: `PetResearchQueryResult`
- **Decoded payload**:
  ```json
  [{"func": "PetResearchQueryResult", "info": {"levelInfo": [], "slotList": []}}]
  ```

### Frame 117: up/client_to_server

- **Segments**: `[111]`
- **Timestamp ms**: `1780601526941` .. `1780601526941`
- **Header**: `8ed4a170000092000000000000000037`
- **Total length**: `146` bytes; **payload codec**: `plain`; **format**: `urlencoded_request`
- **Functions**: `RecoverQuery`
- **Query fields**: `{"bv": "7.0.2", "seq": "55", "session": "02D1B0135ABCDC0D", "sptype": "spv2jodo", "version": "7.0.2"}`
- **Decoded payload**:
  ```json
  [{"func": "RecoverQuery"}]
  ```

### Frame 118: down/server_to_client

- **Segments**: `[112]`
- **Timestamp ms**: `1780601526970` .. `1780601526970`
- **Header**: `419345170000a5000e40100000000037`
- **Total length**: `165` bytes; **payload codec**: `plain`; **format**: `json_response`
- **Functions**: `RecoverQueryResult`
- **Decoded payload**:
  ```json
  [{"func": "RecoverQueryResult", "recoverList": [{"isRecover": 1, "recoverCnt": 0, "recoverFunc": 0, "recoverId": 10101, "recoverTotal": 0, "recoveredPara": 0}]}]
  ```

### Frame 119: up/client_to_server

- **Segments**: `[113]`
- **Timestamp ms**: `1780601526995` .. `1780601526995`
- **Header**: `7d08a11b00009f000000000000000038`
- **Total length**: `159` bytes; **payload codec**: `plain`; **format**: `urlencoded_request`
- **Functions**: `TreasureScrambleInfoQuery`
- **Query fields**: `{"bv": "7.0.2", "seq": "56", "session": "02D1B0135ABCDC0D", "sptype": "spv2jodo", "version": "7.0.2"}`
- **Decoded payload**:
  ```json
  [{"func": "TreasureScrambleInfoQuery"}]
  ```

### Frame 120: down/server_to_client

- **Segments**: `[114]`
- **Timestamp ms**: `1780601527022` .. `1780601527022`
- **Header**: `031a885300005d000e40100000000038`
- **Total length**: `93` bytes; **payload codec**: `plain`; **format**: `json_response`
- **Functions**: `TreasureScrambleInfoQueryResult`
- **Decoded payload**:
  ```json
  [{"func": "TreasureScrambleInfoQueryResult", "info": {"exp": 0, "joinCount": 0}}]
  ```

### Frame 121: up/client_to_server

- **Segments**: `[115]`
- **Timestamp ms**: `1780601527046` .. `1780601527046`
- **Header**: `7e40cd0200008f000000000000000039`
- **Total length**: `143` bytes; **payload codec**: `plain`; **format**: `urlencoded_request`
- **Functions**: `CampQuery`
- **Query fields**: `{"bv": "7.0.2", "seq": "57", "session": "02D1B0135ABCDC0D", "sptype": "spv2jodo", "version": "7.0.2"}`
- **Decoded payload**:
  ```json
  [{"func": "CampQuery"}]
  ```

### Frame 122: down/server_to_client

- **Segments**: `[116]`
- **Timestamp ms**: `1780601527072` .. `1780601527072`
- **Header**: `9e4d4f980001e5000e40100000000039`
- **Total length**: `485` bytes; **payload codec**: `plain`; **format**: `json_response`
- **Functions**: `CampQueryResult`
- **Decoded payload**:
  ```json
  [{"camp": {"count": 0, "gid": 0, "id": 0, "jobs": [], "sid": 0, "statistics": [], "weekTask": []}, "func": "CampQueryResult", "info": {"challengeCount": 0, "exp": 0, "id": 0, "lastQuitTime": 0}, "task": [{"id": 500024, "option": 60, "type": 70, "value": 0}, {"id": 500020, "option": 2000, "type": 57, "value": 0}, {"id": 500021, "option": 50000000, "type": 58, "value": 0}, {"id": 500022, "option": 6, "type": 59, "value": 0}, {"id": 500023, "option": 50000, "type": 63, "value": 0}, {"id": 500019, "option": 1000, "type": 56, "value": 0}]}]
  ```

### Frame 123: up/client_to_server

- **Segments**: `[117]`
- **Timestamp ms**: `1780601527100` .. `1780601527100`
- **Header**: `43ed824400009300000000000000003a`
- **Total length**: `147` bytes; **payload codec**: `plain`; **format**: `urlencoded_request`
- **Functions**: `PetOwnedQuery`
- **Query fields**: `{"bv": "7.0.2", "seq": "58", "session": "02D1B0135ABCDC0D", "sptype": "spv2jodo", "version": "7.0.2"}`
- **Decoded payload**:
  ```json
  [{"func": "PetOwnedQuery"}]
  ```

### Frame 124: down/server_to_client

- **Segments**: `[118]`
- **Timestamp ms**: `1780601527128` .. `1780601527128`
- **Header**: `c67fc75100006f000e4010000000003a`
- **Total length**: `111` bytes; **payload codec**: `plain`; **format**: `json_response`
- **Functions**: `PetOwnedQueryResult`
- **Decoded payload**:
  ```json
  [{"biggestNew": [], "biggestOwned": [0], "func": "PetOwnedQueryResult", "petNew": [], "petOwned": []}]
  ```

### Frame 125: up/client_to_server

- **Segments**: `[119]`
- **Timestamp ms**: `1780601527153` .. `1780601527153`
- **Header**: `67d1396f00009500000000000000003b`
- **Total length**: `149` bytes; **payload codec**: `plain`; **format**: `urlencoded_request`
- **Functions**: `StatisticsQuery`
- **Query fields**: `{"bv": "7.0.2", "seq": "59", "session": "02D1B0135ABCDC0D", "sptype": "spv2jodo", "version": "7.0.2"}`
- **Decoded payload**:
  ```json
  [{"func": "StatisticsQuery"}]
  ```

### Frame 126: down/server_to_client

- **Segments**: `[120]`
- **Timestamp ms**: `1780601527179` .. `1780601527179`
- **Header**: `d3a463b3000094000e4010000000003b`
- **Total length**: `148` bytes; **payload codec**: `plain`; **format**: `json_response`
- **Functions**: `StatisticsQueryResult`
- **Decoded payload**:
  ```json
  [{"func": "StatisticsQueryResult", "statisticsValue": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}]
  ```

### Frame 127: up/client_to_server

- **Segments**: `[121]`
- **Timestamp ms**: `1780601527202` .. `1780601527202`
- **Header**: `f3da11770000af00000000000000003c`
- **Total length**: `175` bytes; **payload codec**: `plain`; **format**: `urlencoded_request`
- **Functions**: `FriendHuntQuery`
- **Query fields**: `{"bv": "7.0.2", "seq": "60", "session": "02D1B0135ABCDC0D", "sptype": "spv2jodo", "version": "7.0.2"}`
- **Decoded payload**:
  ```json
  [{"avatarID": "", "func": "FriendHuntQuery"}]
  ```

### Frame 128: down/server_to_client

- **Segments**: `[122]`
- **Timestamp ms**: `1780601527227` .. `1780601527227`
- **Header**: `495299ab000062000e4010000000003c`
- **Total length**: `98` bytes; **payload codec**: `plain`; **format**: `json_response`
- **Functions**: `FriendHuntQueryResult`
- **Decoded payload**:
  ```json
  [{"avatarID": "", "func": "FriendHuntQueryResult", "huntBuyCount": -1, "huntList": []}]
  ```

### Frame 129: up/client_to_server

- **Segments**: `[123]`
- **Timestamp ms**: `1780601527254` .. `1780601527254`
- **Header**: `9ae183260000ab00000000000000003d`
- **Total length**: `171` bytes; **payload codec**: `plain`; **format**: `urlencoded_request`
- **Functions**: `CampHuntQuery`
- **Query fields**: `{"bv": "7.0.2", "seq": "61", "session": "02D1B0135ABCDC0D", "sptype": "spv2jodo", "version": "7.0.2"}`
- **Decoded payload**:
  ```json
  [{"func": "CampHuntQuery", "huntId": ""}]
  ```

### Frame 130: down/server_to_client

- **Segments**: `[124]`
- **Timestamp ms**: `1780601527281` .. `1780601527281`
- **Header**: `9b09b485000086000e4010000000003d`
- **Total length**: `134` bytes; **payload codec**: `plain`; **format**: `json_response`
- **Functions**: `CampHuntQueryResult`
- **Decoded payload**:
  ```json
  [{"biggestBuyCnt": 0, "biggestList": [], "func": "CampHuntQueryResult", "huntId": "", "overLoadBuyCnt": 0, "overLoadList": []}]
  ```

### Frame 131: up/client_to_server

- **Segments**: `[125]`
- **Timestamp ms**: `1780601527306` .. `1780601527306`
- **Header**: `8440bc6800009f00000000000000003e`
- **Total length**: `159` bytes; **payload codec**: `plain`; **format**: `urlencoded_request`
- **Functions**: `QueryAvatarTechnologyTree`
- **Query fields**: `{"bv": "7.0.2", "seq": "62", "session": "02D1B0135ABCDC0D", "sptype": "spv2jodo", "version": "7.0.2"}`
- **Decoded payload**:
  ```json
  [{"func": "QueryAvatarTechnologyTree"}]
  ```

### Frame 132: down/server_to_client

- **Segments**: `[126]`
- **Timestamp ms**: `1780601527333` .. `1780601527333`
- **Header**: `d183119c00004e000e4010000000003e`
- **Total length**: `78` bytes; **payload codec**: `plain`; **format**: `json_response`
- **Functions**: `QueryAvatarTechnologyTreeResult`
- **Decoded payload**:
  ```json
  [{"func": "QueryAvatarTechnologyTreeResult", "technology": []}]
  ```

### Frame 133: up/client_to_server

- **Segments**: `[127]`
- **Timestamp ms**: `1780601527362` .. `1780601527362`
- **Header**: `34f49ec10000b000000000000000003f`
- **Total length**: `176` bytes; **payload codec**: `plain`; **format**: `urlencoded_request`
- **Functions**: `PVPRankingTopQuery`
- **Query fields**: `{"bv": "7.0.2", "seq": "63", "session": "02D1B0135ABCDC0D", "sptype": "spv2jodo", "version": "7.0.2"}`
- **Decoded payload**:
  ```json
  [{"func": "PVPRankingTopQuery", "sectionType": 1}]
  ```

### Frame 134: down/server_to_client

- **Segments**: `[128, 129, 130, 131]`
- **Timestamp ms**: `1780601527390` .. `1780601527391`
- **Header**: `33050484001e33010e4010000000003f`
- **Total length**: `7731` bytes; **payload codec**: `zlib`; **format**: `json_response`
- **Functions**: `PVPRankingTopQueryResult`
- **Decoded payload**:
  ```json
  [{"func": "PVPRankingTopQueryResult", "pvpShowList": [{"prestige": 762, "show": {"avatarID": "716cc804-6090-48c8-9b0b-f8dec36be97b", "avatarName": "FabianTyt", "battlePoint": 7258037, "campId": 1, "chengHaoID": 1009, "comboWin": 26, "comboWinMax": 26, "contentID": 1009, "dollId": 0, "dollName": "", "fightCountTotal": 247, "fightCountWin": 181, "guild": "Warzone", "guildId": 195123738, "headFrame": 24, "lastActive": 1780600247, "level": 83, "masterLevel": 0, "mountEquip": [{"id": 4, "value": 3}, {"id": 5, "value": 1}], "mount_ID": 7004, "petCount": 195, "petShowList": [{"afinity": 66, "id": 20563, "level": 80}, {"afinity": 60, "id": 1022312, "level": 76}, {"afinity": 65, "id": 21451, "level": 72}, {"afinity": 75, "id": 1023522, "level": 83}, {"afinity": 0, "id": 1021511, "level": 1}, {"afinity": 9, "id": 20981, "level": 45}, {"afinity": 63, "id": 1020051, "level": 81}, {"afinity": 74, "id": 1023502, "level": 83}, {"afinity": 74, "id": 23601, "level": 82}], "pet_ID": 1023502, "ranking": 1000001, "rid": 195125267, "rotom_ID": 0, "spriteLevel": 35, "talk": "", "tuxiaongID": 20859, "vip": 14}, "title": 0}, {"prestige": 764, "show": {"avatarID": "b19d03f0-6f6b-4fe8-a07a-e5cd70d60b33", "avatarName": "Isko", "battlePoint": 7868532, "campId": 1, "chengHaoID": 1023, "comboWin": 3, "comboWinMax": 23, "contentID": 2046, "dollId": 0, "dollName": "", "fightCountTotal": 142, "fightCountWin": 90, "guild": "Stars", "guildId": 195125658, "headFrame": 4, "lastActive": 1780588325, "level": 84, "masterLevel": 0, "mountEquip": [], "mount_ID": 0, "petCount": 179, "petShowList": [{"afinity": 76, "id": 1023502, "level": 84}, {"afinity": 71, "id": 21461, "level": 77}, {"afinity": 65, "id": 1023601, "level": 83}, {"afinity": 78, "id": 1023522, "level": 84}, {"afinity": 67, "id": 20433, "level": 78}, {"afinity": 69, "id": 21001, "level": 77}, {"afinity": 58, "id": 1021572, "level": 79}, {"afinity": 66, "id": 23572, "level": 72}, {"afinity": 47, "id": 20562, "level": 75}], "pet_ID": 21082, "ranking": 1000002, "rid": 195125409, "rotom_ID": 1001, "spriteLevel": 35, "talk": "", "tuxiaongID": 21572, "vip": 15}, "title": 0}, {"prestige": 240, "show": {"avatarID": "07a68e7a-21ce-4387-a447-4ed2fb97f147", "avatarName": "Recycler", "battlePoint": 4212099, "campId": 1, "chengHaoID": 0, "comboWin": 22, "comboWinMax": 22, "contentID": 2045, "dollId": 0, "dollName": "", "fightCountTotal": 174, "fightCountWin": 142, "guild": "SG⚘GĐ", "guildId": 195123642, "headFrame": 0, "lastActive": 1780581723, "level": 84, "masterLevel": 0, "mountEquip": [], "mount_ID": 7004, "petCount": 178, "petShowList": [{"afinity": 77, "id": 1023522, "level": 82}, {"afinity": 30, "id": 21022, "level": 45}, {"afinity": 37, "id": 20562, "level": 46}, {"afinity": 76, "id": 21061, "level": 81}], "pet_ID": 1023522, "ranking": 1000003, "rid": 195123693, "rotom_ID": 1002, "spriteLevel": 34, "talk": "", "tuxiaongID": 2045, "vip": 14}, "title": 0}, {"prestige": 81, "show": {"avatarID": "8d413ef0-b103-4b88-bf45-db611d16219b... <truncated in markdown; see decoded_packets.json>
  ```

### Frame 135: up/client_to_server

- **Segments**: `[132]`
- **Timestamp ms**: `1780601527422` .. `1780601527422`
- **Header**: `df1887f8000094000000000000000040`
- **Total length**: `148` bytes; **payload codec**: `plain`; **format**: `urlencoded_request`
- **Functions**: `PetSummonQuery`
- **Query fields**: `{"bv": "7.0.2", "seq": "64", "session": "02D1B0135ABCDC0D", "sptype": "spv2jodo", "version": "7.0.2"}`
- **Decoded payload**:
  ```json
  [{"func": "PetSummonQuery"}]
  ```

### Frame 136: down/server_to_client

- **Segments**: `[133, 134, 135, 136]`
- **Timestamp ms**: `1780601527452` .. `1780601527453`
- **Header**: `5dfcba94001f43010e40100000000040`
- **Total length**: `8003` bytes; **payload codec**: `zlib`; **format**: `json_response`
- **Functions**: `PetSummonQueryResult`
- **Decoded payload**:
  ```json
  [{"func": "PetSummonQueryResult", "petList": [{"AfinityExp": 0, "AfinityLevel": 0, "FettersExp": 0, "FettersLevel": 0, "Fighting": 0, "HouYuanID": 0, "IsFollow": 0, "IsLock": 0, "MarkType": 0, "PetBaseZiZhi": [15, 31, 27, 18, 25, 57], "PetBreakZiZhi": [-1, -1, -1, -1, -1, -1], "PetConfigID": 22279, "PetParams": [], "QiangHuaExp": 0, "QiangHuaLevel": 0, "TeXingIdList": [20411], "XingGeID": 1015, "aidRune": [], "equipments": [-1, -1, -1], "exp": 0, "level": 1, "miSkill": [{"invalid": false, "isLock": 0, "skillId": 0}, {"invalid": false, "isLock": 0, "skillId": 0}, {"invalid": false, "isLock": 0, "skillId": 0}, {"invalid": false, "isLock": 0, "skillId": 0}, {"invalid": false, "isLock": 0, "skillId": 0}, {"invalid": false, "isLock": 0, "skillId": 0}, {"invalid": false, "isLock": 0, "skillId": 0}, {"invalid": false, "isLock": 0, "skillId": 0}], "name": "Lilie's Snowy", "petInfo": {"petAttr": [], "petId": 114, "skillId": [222790, 222791, 222792, 222793, 222794], "skillLevel": [0, 1, 0, 0, 0]}, "sex": 0, "skillLock": 0}, {"AfinityExp": 0, "AfinityLevel": 0, "FettersExp": 0, "FettersLevel": 0, "Fighting": 0, "HouYuanID": 0, "IsFollow": 0, "IsLock": 0, "MarkType": 0, "PetBaseZiZhi": [45, 25, 45, 20, 27, 53], "PetBreakZiZhi": [-1, -1, -1, -1, -1, -1], "PetConfigID": 23441, "PetParams": [], "QiangHuaExp": 0, "QiangHuaLevel": 0, "TeXingIdList": [20180], "XingGeID": 1018, "aidRune": [], "equipments": [-1, -1, -1], "exp": 0, "level": 1, "miSkill": [{"invalid": false, "isLock": 0, "skillId": 0}, {"invalid": false, "isLock": 0, "skillId": 0}, {"invalid": false, "isLock": 0, "skillId": 0}, {"invalid": false, "isLock": 0, "skillId": 0}, {"invalid": false, "isLock": 0, "skillId": 0}, {"invalid": false, "isLock": 0, "skillId": 0}, {"invalid": false, "isLock": 0, "skillId": 0}, {"invalid": false, "isLock": 0, "skillId": 0}], "name": "Meowstick♂", "petInfo": {"petAttr": [], "petId": 139, "skillId": [234410, 234411, 234412, 234413, 234414], "skillLevel": [0, 1, 0, 0, 0]}, "sex": 0, "skillLock": 0}, {"AfinityExp": 0, "AfinityLevel": 0, "FettersExp": 0, "FettersLevel": 0, "Fighting": 0, "HouYuanID": 0, "IsFollow": 0, "IsLock": 0, "MarkType": 0, "PetBaseZiZhi": [52, 42, 54, 66, 28, 32], "PetBreakZiZhi": [-1, -1, -1, -1, -1, -1], "PetConfigID": 20663, "PetParams": [], "QiangHuaExp": 0, "QiangHuaLevel": 0, "TeXingIdList": [20471], "XingGeID": 1001, "aidRune": [], "equipments": [-1, -1, -1], "exp": 0, "level": 1, "miSkill": [{"invalid": false, "isLock": 0, "skillId": 0}, {"invalid": false, "isLock": 0, "skillId": 0}, {"invalid": false, "isLock": 0, "skillId": 0}, {"invalid": false, "isLock": 0, "skillId": 0}, {"invalid": false, "isLock": 0, "skillId": 0}, {"invalid": false, "isLock": 0, "skillId": 0}, {"invalid": false, "isLock": 0, "skillId": 0}, {"invalid": false, "isLock": 0, "skillId": 0}], "name": "Aerodactyl", "petInfo": {"petAttr": [], "petId": 131, "skillId": [206630, 206631, 206632, 206633, 206634], "skillLevel": [0, 1, 0, 0, 0]}, "sex": 0, "skillLock": 0}, {"Afinit... <truncated in markdown; see decoded_packets.json>
  ```

### Frame 137: up/client_to_server

- **Segments**: `[137]`
- **Timestamp ms**: `1780601527478` .. `1780601527478`
- **Header**: `30c80515000095000000000000000041`
- **Total length**: `149` bytes; **payload codec**: `plain`; **format**: `urlencoded_request`
- **Functions**: `OnceRewardQuery`
- **Query fields**: `{"bv": "7.0.2", "seq": "65", "session": "02D1B0135ABCDC0D", "sptype": "spv2jodo", "version": "7.0.2"}`
- **Decoded payload**:
  ```json
  [{"func": "OnceRewardQuery"}]
  ```

### Frame 138: down/server_to_client

- **Segments**: `[138]`
- **Timestamp ms**: `1780601527503` .. `1780601527503`
- **Header**: `5438e784000043000e40100000000041`
- **Total length**: `67` bytes; **payload codec**: `plain`; **format**: `json_response`
- **Functions**: `OnceRewardQueryResult`
- **Decoded payload**:
  ```json
  [{"func": "OnceRewardQueryResult", "valueList": []}]
  ```

### Frame 139: up/client_to_server

- **Segments**: `[139]`
- **Timestamp ms**: `1780601527527` .. `1780601527527`
- **Header**: `58b551f400009a000000000000000042`
- **Total length**: `154` bytes; **payload codec**: `plain`; **format**: `urlencoded_request`
- **Functions**: `PetCoordinationQuery`
- **Query fields**: `{"bv": "7.0.2", "seq": "66", "session": "02D1B0135ABCDC0D", "sptype": "spv2jodo", "version": "7.0.2"}`
- **Decoded payload**:
  ```json
  [{"func": "PetCoordinationQuery"}]
  ```

### Frame 140: down/server_to_client

- **Segments**: `[140]`
- **Timestamp ms**: `1780601527553` .. `1780601527553`
- **Header**: `432d6bf6000055000e40100000000042`
- **Total length**: `85` bytes; **payload codec**: `plain`; **format**: `json_response`
- **Functions**: `PetCoordinationQueryResult`
- **Decoded payload**:
  ```json
  [{"func": "PetCoordinationQueryResult", "petFriend": [], "petSelf": []}]
  ```

### Frame 141: up/client_to_server

- **Segments**: `[141]`
- **Timestamp ms**: `1780601527579` .. `1780601527579`
- **Header**: `02eb8e1b000098000000000000000043`
- **Total length**: `152` bytes; **payload codec**: `plain`; **format**: `urlencoded_request`
- **Functions**: `PetExpeditionQuery`
- **Query fields**: `{"bv": "7.0.2", "seq": "67", "session": "02D1B0135ABCDC0D", "sptype": "spv2jodo", "version": "7.0.2"}`
- **Decoded payload**:
  ```json
  [{"func": "PetExpeditionQuery"}]
  ```

### Frame 142: down/server_to_client

- **Segments**: `[142]`
- **Timestamp ms**: `1780601527604` .. `1780601527604`
- **Header**: `e989287b0000b5000e40100000000043`
- **Total length**: `181` bytes; **payload codec**: `plain`; **format**: `json_response`
- **Functions**: `PetExpeditionQueryResult`
- **Decoded payload**:
  ```json
  [{"func": "PetExpeditionQueryResult", "info": {"missionAccected": [], "missionList": [30007, 30012, 10001], "missionRunning": [], "pidUsedList": [], "refreshTime": 1780601400}}]
  ```

### Frame 143: up/client_to_server

- **Segments**: `[143]`
- **Timestamp ms**: `1780601527636` .. `1780601527636`
- **Header**: `be6bacc40000aa000000000000000044`
- **Total length**: `170` bytes; **payload codec**: `plain`; **format**: `urlencoded_request`
- **Functions**: `DaoguanInfoQuery`
- **Query fields**: `{"bv": "7.0.2", "seq": "68", "session": "02D1B0135ABCDC0D", "sptype": "spv2jodo", "version": "7.0.2"}`
- **Decoded payload**:
  ```json
  [{"func": "DaoguanInfoQuery", "skillId": 0}]
  ```

### Frame 144: down/server_to_client

- **Segments**: `[144]`
- **Timestamp ms**: `1780601527662` .. `1780601527662`
- **Header**: `cb00974f000061000e40100000000044`
- **Total length**: `97` bytes; **payload codec**: `plain`; **format**: `json_response`
- **Functions**: `DaoguanInfoQueryResult`
- **Decoded payload**:
  ```json
  [{"coreList": [], "func": "DaoguanInfoQueryResult", "infoList": [], "numberList": []}]
  ```

### Frame 145: up/client_to_server

- **Segments**: `[145]`
- **Timestamp ms**: `1780601527690` .. `1780601527690`
- **Header**: `adfee7ee000092000000000000000045`
- **Total length**: `146` bytes; **payload codec**: `plain`; **format**: `urlencoded_request`
- **Functions**: `WaiguanQuery`
- **Query fields**: `{"bv": "7.0.2", "seq": "69", "session": "02D1B0135ABCDC0D", "sptype": "spv2jodo", "version": "7.0.2"}`
- **Decoded payload**:
  ```json
  [{"func": "WaiguanQuery"}]
  ```

### Frame 146: down/server_to_client

- **Segments**: `[146]`
- **Timestamp ms**: `1780601527716` .. `1780601527716`
- **Header**: `9c943d6e000042000e40100000000045`
- **Total length**: `66` bytes; **payload codec**: `plain`; **format**: `json_response`
- **Functions**: `WaiguanQueryResult`
- **Decoded payload**:
  ```json
  [{"func": "WaiguanQueryResult", "waiguanList": []}]
  ```

### Frame 147: up/client_to_server

- **Segments**: `[147]`
- **Timestamp ms**: `1780601527745` .. `1780601527745`
- **Header**: `eec9aa1d000096000000000000000046`
- **Total length**: `150` bytes; **payload codec**: `plain`; **format**: `urlencoded_request`
- **Functions**: `BattleTowerQuery`
- **Query fields**: `{"bv": "7.0.2", "seq": "70", "session": "02D1B0135ABCDC0D", "sptype": "spv2jodo", "version": "7.0.2"}`
- **Decoded payload**:
  ```json
  [{"func": "BattleTowerQuery"}]
  ```

### Frame 148: down/server_to_client

- **Segments**: `[148]`
- **Timestamp ms**: `1780601527771` .. `1780601527771`
- **Header**: `1dac57410000f8000e40100000000046`
- **Total length**: `248` bytes; **payload codec**: `plain`; **format**: `json_response`
- **Functions**: `BattleTowerQueryResult`
- **Decoded payload**:
  ```json
  [{"func": "BattleTowerQueryResult", "mode": 0, "petList": [], "status": {"awardPickId": 0, "buffList": [], "coin": 0, "curLevel": 0, "finishAwardList": [], "lootBuffBox": [], "maxLevel": 0, "opponentIndex": 0, "opponentList": [], "point": 0, "pointSum": 0}}]
  ```

### Frame 149: up/client_to_server

- **Segments**: `[149]`
- **Timestamp ms**: `1780601527796` .. `1780601527796`
- **Header**: `3ad4c37f00009d000000000000000047`
- **Total length**: `157` bytes; **payload codec**: `plain`; **format**: `urlencoded_request`
- **Functions**: `ChampionLeagueQueryTime`
- **Query fields**: `{"bv": "7.0.2", "seq": "71", "session": "02D1B0135ABCDC0D", "sptype": "spv2jodo", "version": "7.0.2"}`
- **Decoded payload**:
  ```json
  [{"func": "ChampionLeagueQueryTime"}]
  ```

### Frame 150: down/server_to_client

- **Segments**: `[150]`
- **Timestamp ms**: `1780601527822` .. `1780601527822`
- **Header**: `f8eec04c0000bd000e40100000000047`
- **Total length**: `189` bytes; **payload codec**: `plain`; **format**: `json_response`
- **Functions**: `ChampionLeagueQueryTimeResult`
- **Decoded payload**:
  ```json
  [{"func": "ChampionLeagueQueryTimeResult", "setcion": [1, -1, 1, -1, 1, -1, 1, -1], "time": [1780542000, 1780552800, 1780563600, 1780570800, 1780628400, 1780639200, 1780650000, 1780657200]}]
  ```

### Frame 151: up/client_to_server

- **Segments**: `[151]`
- **Timestamp ms**: `1780601527847` .. `1780601527847`
- **Header**: `1bdb716d000095000000000000000048`
- **Total length**: `149` bytes; **payload codec**: `plain`; **format**: `urlencoded_request`
- **Functions**: `ReturnGiftQuery`
- **Query fields**: `{"bv": "7.0.2", "seq": "72", "session": "02D1B0135ABCDC0D", "sptype": "spv2jodo", "version": "7.0.2"}`
- **Decoded payload**:
  ```json
  [{"func": "ReturnGiftQuery"}]
  ```

### Frame 152: down/server_to_client

- **Segments**: `[152]`
- **Timestamp ms**: `1780601527873` .. `1780601527873`
- **Header**: `2833be3300008d000e40100000000048`
- **Total length**: `141` bytes; **payload codec**: `plain`; **format**: `json_response`
- **Functions**: `ReturnGiftQueryResult`
- **Decoded payload**:
  ```json
  [{"func": "ReturnGiftQueryResult", "returnGift": {"buyCount": [], "giftCharge": [], "giftFree": [], "onlineDays": 0, "returnTime": 0}}]
  ```

### Frame 153: up/client_to_server

- **Segments**: `[153]`
- **Timestamp ms**: `1780601527899` .. `1780601527899`
- **Header**: `fe5ed839000099000000000000000049`
- **Total length**: `153` bytes; **payload codec**: `plain`; **format**: `urlencoded_request`
- **Functions**: `GlobalGuildWarQuery`
- **Query fields**: `{"bv": "7.0.2", "seq": "73", "session": "02D1B0135ABCDC0D", "sptype": "spv2jodo", "version": "7.0.2"}`
- **Decoded payload**:
  ```json
  [{"func": "GlobalGuildWarQuery"}]
  ```

### Frame 154: down/server_to_client

- **Segments**: `[154]`
- **Timestamp ms**: `1780601527927` .. `1780601527927`
- **Header**: `8a1287130000b1000e40100000000049`
- **Total length**: `177` bytes; **payload codec**: `plain`; **format**: `json_response`
- **Functions**: `GlobalGuildWarQueryResult`
- **Decoded payload**:
  ```json
  [{"func": "GlobalGuildWarQueryResult", "status": {"awardList": [], "buyCount": 0, "fightCount": 0, "inspireCount": [], "point": 0, "winCombo": 0}, "timeEnd": 0, "timeStart": 0}]
  ```

### Frame 155: up/client_to_server

- **Segments**: `[155]`
- **Timestamp ms**: `1780601527956` .. `1780601527956`
- **Header**: `a0d6c62400009d00000000000000004a`
- **Total length**: `157` bytes; **payload codec**: `plain`; **format**: `urlencoded_request`
- **Functions**: `DaoguanSkillAwakenQuery`
- **Query fields**: `{"bv": "7.0.2", "seq": "74", "session": "02D1B0135ABCDC0D", "sptype": "spv2jodo", "version": "7.0.2"}`
- **Decoded payload**:
  ```json
  [{"func": "DaoguanSkillAwakenQuery"}]
  ```

### Frame 156: down/server_to_client

- **Segments**: `[156]`
- **Timestamp ms**: `1780601527984` .. `1780601527984`
- **Header**: `338dc7b400004a000e4010000000004a`
- **Total length**: `74` bytes; **payload codec**: `plain`; **format**: `json_response`
- **Functions**: `DaoguanSkillAwakenQueryResult`
- **Decoded payload**:
  ```json
  [{"attrList": [], "func": "DaoguanSkillAwakenQueryResult"}]
  ```

### Frame 157: up/client_to_server

- **Segments**: `[157]`
- **Timestamp ms**: `1780601528009` .. `1780601528009`
- **Header**: `23d46a300000a600000000000000004b`
- **Total length**: `166` bytes; **payload codec**: `plain`; **format**: `urlencoded_request`
- **Functions**: `LeagueTripQuery`
- **Query fields**: `{"bv": "7.0.2", "seq": "75", "session": "02D1B0135ABCDC0D", "sptype": "spv2jodo", "version": "7.0.2"}`
- **Decoded payload**:
  ```json
  [{"func": "LeagueTripQuery", "ltId": 0}]
  ```

### Frame 158: down/server_to_client

- **Segments**: `[158]`
- **Timestamp ms**: `1780601528035` .. `1780601528035`
- **Header**: `cf6e866400006f000e4010000000004b`
- **Total length**: `111` bytes; **payload codec**: `plain`; **format**: `json_response`
- **Functions**: `LeagueTripQueryResult`
- **Decoded payload**:
  ```json
  [{"func": "LeagueTripQueryResult", "ltDailyChallengeRestCnt": 0, "ltDailyRestCnt": 0, "ltList": []}]
  ```

### Frame 159: up/client_to_server

- **Segments**: `[159]`
- **Timestamp ms**: `1780601528059` .. `1780601528059`
- **Header**: `facd576700009300000000000000004c`
- **Total length**: `147` bytes; **payload codec**: `plain`; **format**: `urlencoded_request`
- **Functions**: `WishStarQuery`
- **Query fields**: `{"bv": "7.0.2", "seq": "76", "session": "02D1B0135ABCDC0D", "sptype": "spv2jodo", "version": "7.0.2"}`
- **Decoded payload**:
  ```json
  [{"func": "WishStarQuery"}]
  ```

### Frame 160: down/server_to_client

- **Segments**: `[160]`
- **Timestamp ms**: `1780601528087` .. `1780601528087`
- **Header**: `e69bda6200005c000e4010000000004c`
- **Total length**: `92` bytes; **payload codec**: `plain`; **format**: `json_response`
- **Functions**: `WishStarQueryResult`
- **Decoded payload**:
  ```json
  [{"func": "WishStarQueryResult", "nextLottery": 1, "platList": [], "wslist": []}]
  ```

### Frame 161: up/client_to_server

- **Segments**: `[161]`
- **Timestamp ms**: `1780601528114` .. `1780601528114`
- **Header**: `1d4f7e4700009400000000000000004d`
- **Total length**: `148` bytes; **payload codec**: `plain`; **format**: `urlencoded_request`
- **Functions**: `AtlasInfoQuery`
- **Query fields**: `{"bv": "7.0.2", "seq": "77", "session": "02D1B0135ABCDC0D", "sptype": "spv2jodo", "version": "7.0.2"}`
- **Decoded payload**:
  ```json
  [{"func": "AtlasInfoQuery"}]
  ```

### Frame 162: down/server_to_client

- **Segments**: `[162]`
- **Timestamp ms**: `1780601528140` .. `1780601528140`
- **Header**: `74f3b00d000077000e4010000000004d`
- **Total length**: `119` bytes; **payload codec**: `plain`; **format**: `json_response`
- **Functions**: `AtlasInfoQueryResult`
- **Decoded payload**:
  ```json
  [{"atlasArray": [], "cardArray": [], "friendPoint": 0, "friendProofLevel": 0, "func": "AtlasInfoQueryResult"}]
  ```

### Frame 163: up/client_to_server

- **Segments**: `[163]`
- **Timestamp ms**: `1780601528170` .. `1780601528170`
- **Header**: `ae051be10000aa00000000000000004e`
- **Total length**: `170` bytes; **payload codec**: `plain`; **format**: `urlencoded_request`
- **Functions**: `DaoguanOwnerQuery`
- **Query fields**: `{"bv": "7.0.2", "seq": "78", "session": "02D1B0135ABCDC0D", "sptype": "spv2jodo", "version": "7.0.2"}`
- **Decoded payload**:
  ```json
  [{"dgId": 501, "func": "DaoguanOwnerQuery"}]
  ```

### Frame 164: down/server_to_client

- **Segments**: `[164]`
- **Timestamp ms**: `1780601528196` .. `1780601528196`
- **Header**: `8da08e3e000418010e4010000000004e`
- **Total length**: `1048` bytes; **payload codec**: `zlib`; **format**: `json_response`
- **Functions**: `DaoguanOwnerQueryResult`
- **Decoded payload**:
  ```json
  [{"dgId": 501, "func": "DaoguanOwnerQueryResult", "ownerList": [{"comboWin": 53, "defenderPet": {"paraList": [6500534, 1001, 81, 45400, 0, 28, 0, 0, 0, 0, 0], "petIdList": [300, 30, 272, 0], "petList": [{"petAttr": [688113, 105678, 109242, 59187, 61769, 59108, 1052, 69, 411, 488, 121, 23522, 90358, 3799647, 0, 0, 0, 0], "petId": 1023522, "skillId": [31075, 31074, 2201, 1101, 2202, 935222, 31079, 2204, 935223, 2205, 935220, 2206, 935221, 31076, 31083, 4263, 31085, 31102, 31100, 235224, 235222, 235223, 235220, 31055, 235221, 31054, 31056, 31057, 31058, 40006, 4253, 31065, 31070, 4192, 4203, 20862, 30303, 30293, 20112, 31118, 72018, 72016, 31115, 31108, 31104, 50002, 50001, 400011, 31128, 400012, 30150, 400013, 31120, 31123], "skillLevel": [1, 1, 13, 2, 7, 84, 1, 7, 84, 7, 84, 8, 84, 1, 1, 1, 1, 1, 1, 84, 84, 84, 84, 9, 84, 12, 10, 10, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 10, 9, 1, 1, 1, 1, 1, 1, 1]}, {"petAttr": [509349, 47405, 51197, 37603, 42715, 5542, 1046, 69, 291, 488, 115, 21461, 0, 1554507, 0, 0, 0, 0], "petId": 21461, "skillId": [31075, 1101, 2201, 31074, 2202, 30132, 2204, 31079, 2205, 2206, 31076, 214614, 31083, 30142, 214612, 214613, 214610, 214611, 31085, 20411, 31102, 31100, 31118, 30162, 31115, 31108, 30240, 31104, 50002, 50001, 31055, 31054, 31056, 31057, 31058, 31128, 30150, 31065, 31120, 31070], "skillLevel": [1, 2, 13, 1, 7, 1, 7, 1, 7, 8, 1, 77, 1, 1, 77, 77, 77, 77, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 10, 9, 9, 12, 10, 10, 1, 1, 1, 1, 1, 1]}, {"petAttr": [425442, 34293, 41106, 21236, 25377, 5995, 1046, 69, 371, 488, 415, 20441, 0, 1048690, 0, 0, 0, 0], "petId": 20441, "skillId": [31075, 1101, 2201, 31074, 2202, 30132, 2204, 31079, 2205, 2206, 31076, 31083, 31085, 204411, 204410, 204413, 204412, 204414, 31102, 31100, 20302, 31118, 30162, 31115, 31108, 31104, 50002, 50001, 31055, 31054, 31056, 31057, 31058, 31128, 31065, 31120, 30261, 31070], "skillLevel": [1, 2, 13, 1, 7, 1, 7, 1, 7, 8, 1, 1, 1, 78, 78, 78, 78, 78, 1, 1, 1, 1, 1, 1, 1, 1, 10, 9, 9, 12, 10, 10, 1, 1, 1, 1, 1, 1]}]}, "show": {"avatarID": "b19d03f0-6f6b-4fe8-a07a-e5cd70d60b33", "avatarName": "Isko", "battlePoint": 7868532, "campId": 1, "chengHaoID": 1023, "comboWin": 3, "comboWinMax": 23, "contentID": 2046, "dollId": 0, "dollName": "", "fightCountTotal": 142, "fightCountWin": 90, "guild": "Stars", "guildId": 195125658, "headFrame": 4, "lastActive": 1780588325, "level": 84, "masterLevel": 0, "mountEquip": [], "mount_ID": 0, "petCount": 179, "petShowList": [{"afinity": 76, "id": 1023502, "level": 84}, {"afinity": 71, "id": 21461, "level": 77}, {"afinity": 65, "id": 1023601, "level": 83}, {"afinity": 78, "id": 1023522, "level": 84}, {"afinity": 67, "id": 20433, "level": 78}, {"afinity": 69, "id": 21001, "level": 77}, {"afinity": 58, "id": 1021572, "level": 79}, {"afinity": 66, "id": 23572, "level": 72}, {"afinity": 47, "id": 20562, "level": 75}], "pet_ID": 21082, "ranking": 1000002, "rid": 195125409, "rotom_ID": 1001, "spriteLevel": 35, "talk": "", "tuxiaongID"... <truncated in markdown; see decoded_packets.json>
  ```

### Frame 165: up/client_to_server

- **Segments**: `[165]`
- **Timestamp ms**: `1780601528221` .. `1780601528221`
- **Header**: `8962e53f0000aa00000000000000004f`
- **Total length**: `170` bytes; **payload codec**: `plain`; **format**: `urlencoded_request`
- **Functions**: `DaoguanOwnerQuery`
- **Query fields**: `{"bv": "7.0.2", "seq": "79", "session": "02D1B0135ABCDC0D", "sptype": "spv2jodo", "version": "7.0.2"}`
- **Decoded payload**:
  ```json
  [{"dgId": 502, "func": "DaoguanOwnerQuery"}]
  ```

### Frame 166: down/server_to_client

- **Segments**: `[166]`
- **Timestamp ms**: `1780601528247` .. `1780601528247`
- **Header**: `70c7814a0003be010e4010000000004f`
- **Total length**: `958` bytes; **payload codec**: `zlib`; **format**: `json_response`
- **Functions**: `DaoguanOwnerQueryResult`
- **Decoded payload**:
  ```json
  [{"dgId": 502, "func": "DaoguanOwnerQueryResult", "ownerList": [{"comboWin": 11, "defenderPet": {"paraList": [2699806, 1004, 50, 17000, 0, 28, 0, 0, 0, 0, 0], "petIdList": [177, 260, 254], "petList": [{"petAttr": [277769, 62891, 29147, 22313, 19140, 12039, 1121, 132, 411, 304, 1019, 23502, 90351, 1484158, 0, 0, 0, 0], "petId": 1023502, "skillId": [30133, 23501, 4193, 46525, 935021, 31083, 935020, 935023, 935022, 24220, 20862, 4213, 80060, 4093, 235024, 72016, 31051, 31104, 50002, 400011, 40007, 30150, 400012, 4254, 235022, 235023, 31065, 235020, 235021, 31067, 31068, 31069, 31123, 31070, 21172], "skillLevel": [1, 1, 1, 1, 76, 1, 76, 76, 76, 1, 1, 1, 1, 1, 76, 1, 1, 1, 9, 1, 1, 1, 1, 1, 76, 76, 1, 76, 76, 1, 1, 1, 1, 1, 1]}, {"petAttr": [226840, 35931, 23816, 19520, 19523, 6059, 1121, 132, 411, 304, 1003, 23602, 90351, 891809, 0, 0, 0, 0], "petId": 1023602, "skillId": [30133, 31083, 23601, 236022, 236023, 236020, 236021, 46625, 936022, 936023, 936020, 31051, 936021, 20830, 31104, 50002, 236024, 40001, 4313, 4253, 30150, 31065, 31067, 31068, 31069, 31070, 31122], "skillLevel": [1, 1, 1, 76, 76, 76, 76, 1, 76, 76, 76, 1, 76, 1, 1, 9, 76, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]}, {"petAttr": [138074, 14278, 13057, 6105, 6303, 3297, 1121, 132, 291, 304, 1016, 22571, 0, 275839, 0, 0, 0, 0], "petId": 22571, "skillId": [225711, 20031, 31083, 31065, 31051, 31067, 31068, 31104, 31069, 50002, 31070], "skillLevel": [1, 1, 1, 1, 1, 1, 1, 1, 1, 9, 1]}]}, "show": {"avatarID": "d660c65e-c3d0-43ba-9e46-3eae52dce466", "avatarName": "⚘Civic", "battlePoint": 2788500, "campId": 2, "chengHaoID": 1022, "comboWin": 11, "comboWinMax": 15, "contentID": 1009, "dollId": 0, "dollName": "", "fightCountTotal": 154, "fightCountWin": 119, "guild": "SG⚘GĐ", "guildId": 195123642, "headFrame": 0, "lastActive": 1780583496, "level": 76, "masterLevel": 0, "mountEquip": [], "mount_ID": 7003, "petCount": 152, "petShowList": [{"afinity": 76, "id": 1023502, "level": 76}, {"afinity": 54, "id": 20961, "level": 63}, {"afinity": 29, "id": 21031, "level": 68}, {"afinity": 53, "id": 20222, "level": 76}, {"afinity": 72, "id": 1023602, "level": 76}, {"afinity": 55, "id": 22644, "level": 76}, {"afinity": 35, "id": 20981, "level": 60}, {"afinity": 56, "id": 20441, "level": 63}, {"afinity": 9, "id": 23572, "level": 16}], "pet_ID": 21031, "ranking": 1000008, "rid": 195123507, "rotom_ID": 0, "spriteLevel": 29, "talk": "", "tuxiaongID": 20641, "vip": 12}, "timeAward": 1780572146, "timeWin": 1780387994}]}]
  ```

### Frame 167: up/client_to_server

- **Segments**: `[167]`
- **Timestamp ms**: `1780601528273` .. `1780601528273`
- **Header**: `becd700b0000aa000000000000000050`
- **Total length**: `170` bytes; **payload codec**: `plain`; **format**: `urlencoded_request`
- **Functions**: `DaoguanOwnerQuery`
- **Query fields**: `{"bv": "7.0.2", "seq": "80", "session": "02D1B0135ABCDC0D", "sptype": "spv2jodo", "version": "7.0.2"}`
- **Decoded payload**:
  ```json
  [{"dgId": 503, "func": "DaoguanOwnerQuery"}]
  ```

### Frame 168: down/server_to_client

- **Segments**: `[168]`
- **Timestamp ms**: `1780601528306` .. `1780601528306`
- **Header**: `4544495c0003f6010e40100000000050`
- **Total length**: `1014` bytes; **payload codec**: `zlib`; **format**: `json_response`
- **Functions**: `DaoguanOwnerQueryResult`
- **Decoded payload**:
  ```json
  [{"dgId": 503, "func": "DaoguanOwnerQueryResult", "ownerList": [{"comboWin": 4, "defenderPet": {"paraList": [4917809, 0, 0, 0, 0, 28, 0, 0, 0, 0, 0], "petIdList": [264, 73, 194], "petList": [{"petAttr": [602765, 77091, 71125, 40159, 36341, 12729, 1121, 176, 515, 566, 121, 23522, 90358, 2259371, 0, 0, 0, 0], "petId": 1023522, "skillId": [1101, 2201, 1102, 2202, 30133, 935222, 31079, 935223, 935220, 2206, 935221, 31083, 20862, 4213, 4284, 4998, 31097, 235224, 20182, 31118, 31112, 72018, 72016, 31115, 31108, 31051, 235222, 235223, 31105, 235220, 235221, 400011, 40006, 400014, 31128, 30150, 400012, 4254, 42707, 31065, 31120, 31123, 30262, 31070], "skillLevel": [2, 6, 2, 12, 1, 81, 1, 81, 81, 13, 81, 1, 1, 1, 1, 1, 1, 81, 1, 1, 1, 1, 1, 1, 1, 1, 81, 81, 1, 81, 81, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]}, {"petAttr": [549646, 59318, 33892, 36511, 31844, 9374, 1121, 176, 515, 566, 411, 20051, 0, 1498456, 0, 0, 0, 0], "petId": 1020051, "skillId": [1101, 2201, 1102, 2202, 30133, 31079, 43007, 2206, 31083, 200513, 200512, 200514, 31097, 20112, 200511, 31118, 31112, 40017, 31115, 31108, 31051, 31105, 2005104, 31128, 31065, 31120, 30262, 31070], "skillLevel": [2, 6, 2, 12, 1, 1, 1, 13, 1, 81, 81, 81, 1, 1, 81, 1, 1, 1, 1, 1, 1, 1, 81, 1, 1, 1, 1, 1]}, {"petAttr": [412650, 39460, 37658, 21642, 20120, 7520, 1121, 176, 515, 566, 104, 21511, 0, 1115762, 0, 0, 0, 0], "petId": 1021511, "skillId": [1101, 2201, 1102, 30133, 20212, 2202, 31079, 2206, 31083, 31097, 31118, 215111, 31112, 215110, 31115, 31108, 215113, 31051, 215112, 31105, 46707, 31128, 30150, 31065, 31120, 31070], "skillLevel": [2, 6, 2, 1, 1, 12, 1, 13, 1, 1, 1, 65, 1, 71, 1, 1, 65, 1, 71, 1, 1, 1, 1, 1, 1, 1]}]}, "show": {"avatarID": "d4df0223-ca5d-48f7-9a50-fb408ca21915", "avatarName": "Gió⚘MD", "battlePoint": 6120383, "campId": 1, "chengHaoID": 1009, "comboWin": 0, "comboWinMax": 18, "contentID": 2019, "dollId": 0, "dollName": "", "fightCountTotal": 279, "fightCountWin": 116, "guild": "SG⚘GĐ", "guildId": 195123642, "headFrame": 38, "lastActive": 1780584263, "level": 81, "masterLevel": 0, "mountEquip": [], "mount_ID": 7004, "petCount": 125, "petShowList": [{"afinity": 74, "id": 1023502, "level": 81}, {"afinity": 40, "id": 1020961, "level": 66}, {"afinity": 73, "id": 1023602, "level": 81}, {"afinity": 76, "id": 1023522, "level": 81}, {"afinity": 68, "id": 1021511, "level": 75}, {"afinity": 74, "id": 1020051, "level": 81}, {"afinity": 61, "id": 1020222, "level": 74}, {"afinity": 50, "id": 22644, "level": 75}, {"afinity": 42, "id": 20464, "level": 79}], "pet_ID": 1023522, "ranking": 1000006, "rid": 195123571, "rotom_ID": 1002, "spriteLevel": 33, "talk": "thanhsucmoc", "tuxiaongID": 1022, "vip": 14}, "timeAward": 1780523813, "timeWin": 1779688973}]}]
  ```

### Frame 169: up/client_to_server

- **Segments**: `[169]`
- **Timestamp ms**: `1780601528336` .. `1780601528336`
- **Header**: `61d14e290000aa000000000000000051`
- **Total length**: `170` bytes; **payload codec**: `plain`; **format**: `urlencoded_request`
- **Functions**: `DaoguanOwnerQuery`
- **Query fields**: `{"bv": "7.0.2", "seq": "81", "session": "02D1B0135ABCDC0D", "sptype": "spv2jodo", "version": "7.0.2"}`
- **Decoded payload**:
  ```json
  [{"dgId": 504, "func": "DaoguanOwnerQuery"}]
  ```

### Frame 170: down/server_to_client

- **Segments**: `[170]`
- **Timestamp ms**: `1780601528369` .. `1780601528369`
- **Header**: `20367e4a000409010e40100000000051`
- **Total length**: `1033` bytes; **payload codec**: `zlib`; **format**: `json_response`
- **Functions**: `DaoguanOwnerQueryResult`
- **Decoded payload**:
  ```json
  [{"dgId": 504, "func": "DaoguanOwnerQueryResult", "ownerList": [{"comboWin": 2, "defenderPet": {"paraList": [5279278, 1004, 80, 32000, 0, 28, 0, 0, 0, 0, 0], "petIdList": [234, 25, 258, 0], "petList": [{"petAttr": [517698, 82493, 53225, 36006, 31254, 13743, 1064, 44, 425, 380, 1019, 23502, 90351, 2167123, 0, 0, 0, 0], "petId": 1023502, "skillId": [31075, 2202, 30133, 23501, 2206, 4133, 46525, 31076, 935021, 31083, 935020, 935023, 935022, 20862, 31085, 30303, 4212, 80060, 31097, 31102, 4093, 31103, 31100, 31101, 72021, 30163, 235024, 4172, 30310, 400011, 40007, 4054, 400014, 30150, 400012, 235022, 235023, 31065, 235020, 235021, 31120, 31123, 31070], "skillLevel": [1, 20, 1, 1, 3, 1, 1, 1, 80, 1, 80, 80, 80, 1, 1, 1, 1, 3, 1, 1, 1, 1, 1, 1, 1, 1, 80, 1, 1, 1, 1, 1, 1, 1, 1, 80, 80, 1, 80, 80, 1, 1, 1]}, {"petAttr": [463060, 43951, 32763, 30196, 32206, 6104, 1062, 44, 425, 380, 411, 20051, 0, 1322200, 0, 0, 0, 0], "petId": 1020051, "skillId": [31075, 2005134, 30133, 2202, 2206, 31076, 31083, 31085, 200512, 200514, 31097, 31102, 31103, 31100, 31101, 20112, 200511, 40017, 2005106, 30150, 31065, 31120, 31070], "skillLevel": [1, 80, 1, 20, 3, 1, 1, 1, 80, 80, 1, 1, 1, 1, 1, 1, 80, 1, 80, 1, 1, 1, 1]}, {"petAttr": [459544, 55941, 39180, 37629, 38360, 6812, 1062, 44, 425, 380, 1003, 23602, 90351, 1717395, 0, 0, 0, 0], "petId": 1023602, "skillId": [31075, 2202, 30133, 2206, 31076, 31083, 4074, 31085, 23601, 20832, 4221, 31097, 31102, 31103, 31100, 31101, 236022, 236023, 236020, 4033, 30163, 236021, 46625, 936022, 40028, 936023, 936020, 936021, 236024, 30150, 31065, 72011, 31120, 31070, 31122], "skillLevel": [1, 20, 1, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 80, 80, 80, 1, 1, 80, 1, 80, 1, 80, 80, 80, 80, 1, 1, 1, 1, 1, 1]}]}, "show": {"avatarID": "8d413ef0-b103-4b88-bf45-db611d16219b", "avatarName": "MiH4wk", "battlePoint": 5279278, "campId": 1, "chengHaoID": 1022, "comboWin": 1, "comboWinMax": 21, "contentID": 2037, "dollId": 0, "dollName": "", "fightCountTotal": 199, "fightCountWin": 86, "guild": "SG⚘GĐ", "guildId": 195123642, "headFrame": 0, "lastActive": 1780599443, "level": 80, "masterLevel": 0, "mountEquip": [], "mount_ID": 7004, "petCount": 176, "petShowList": [{"afinity": 70, "id": 1020051, "level": 80}, {"afinity": 29, "id": 1020552, "level": 72}, {"afinity": 75, "id": 1023602, "level": 80}, {"afinity": 52, "id": 20961, "level": 74}, {"afinity": 76, "id": 1023502, "level": 80}, {"afinity": 71, "id": 21451, "level": 77}, {"afinity": 58, "id": 21461, "level": 78}, {"afinity": 47, "id": 1020441, "level": 70}, {"afinity": 30, "id": 20352, "level": 60}], "pet_ID": 1023502, "ranking": 1000004, "rid": 195123794, "rotom_ID": 1002, "spriteLevel": 32, "talk": "Boreee", "tuxiaongID": 2037, "vip": 13}, "timeAward": 1780548828, "timeWin": 1780317178}]}]
  ```

### Frame 171: up/client_to_server

- **Segments**: `[171]`
- **Timestamp ms**: `1780601528401` .. `1780601528401`
- **Header**: `82de8db70000aa000000000000000052`
- **Total length**: `170` bytes; **payload codec**: `plain`; **format**: `urlencoded_request`
- **Functions**: `DaoguanOwnerQuery`
- **Query fields**: `{"bv": "7.0.2", "seq": "82", "session": "02D1B0135ABCDC0D", "sptype": "spv2jodo", "version": "7.0.2"}`
- **Decoded payload**:
  ```json
  [{"dgId": 505, "func": "DaoguanOwnerQuery"}]
  ```

### Frame 172: down/server_to_client

- **Segments**: `[172]`
- **Timestamp ms**: `1780601528429` .. `1780601528429`
- **Header**: `cac720dc00048f010e40100000000052`
- **Total length**: `1167` bytes; **payload codec**: `zlib`; **format**: `json_response`
- **Functions**: `DaoguanOwnerQueryResult`
- **Decoded payload**:
  ```json
  [{"dgId": 505, "func": "DaoguanOwnerQueryResult", "ownerList": [{"comboWin": 7, "defenderPet": {"paraList": [7258037, 1001, 71, 29800, 0, 28, 0, 0, 0, 0, 0], "petIdList": [233, 138, 295, 0], "petList": [{"petAttr": [479393, 73773, 45817, 36139, 39172, 7280, 1213, 257, 605, 542, 1019, 23502, 90351, 1898862, 0, 0, 0, 0], "petId": 1023502, "skillId": [1101, 31074, 30133, 31073, 31072, 2206, 46524, 31083, 31086, 31085, 31102, 31100, 4224, 31051, 31055, 31054, 31056, 40005, 31057, 20742, 31058, 31065, 31066, 31067, 4124, 31068, 31069, 31070, 30263, 23501, 935021, 935020, 935023, 935022, 31116, 31117, 31118, 31112, 31113, 31114, 235024, 72016, 31115, 31108, 31109, 4294, 31110, 4174, 30310, 50002, 31105, 50001, 31106, 31128, 30150, 31131, 235022, 235023, 235020, 235021, 31120, 31122], "skillLevel": [2, 1, 1, 1, 1, 14, 1, 1, 1, 1, 1, 1, 1, 1, 4, 4, 3, 1, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 83, 83, 83, 83, 1, 1, 1, 1, 1, 1, 83, 1, 1, 1, 1, 1, 1, 1, 1, 6, 1, 10, 1, 1, 1, 1, 83, 83, 83, 83, 1, 1]}, {"petAttr": [574757, 99811, 105944, 51937, 56907, 56449, 1213, 257, 605, 542, 121, 23522, 90358, 3535914, 0, 0, 0, 0], "petId": 1023522, "skillId": [1101, 31074, 31073, 31072, 935222, 935223, 935220, 2206, 935221, 31083, 31086, 31085, 4283, 4998, 31102, 31100, 40040, 235224, 31051, 235222, 235223, 235220, 31055, 235221, 31054, 31056, 31057, 31058, 31065, 31066, 31067, 31068, 31069, 48802, 31070, 4192, 4203, 20862, 30303, 20112, 31116, 31117, 31118, 31112, 72018, 31113, 31114, 72016, 31115, 31108, 31109, 4294, 31110, 30310, 31105, 50002, 31106, 50001, 400011, 400014, 31128, 400012, 30150, 31131, 31120, 31123], "skillLevel": [2, 1, 1, 1, 83, 83, 83, 14, 83, 1, 1, 1, 1, 1, 1, 1, 1, 83, 1, 83, 83, 83, 4, 83, 4, 3, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 6, 1, 10, 1, 1, 1, 1, 1, 1, 1, 1]}, {"petAttr": [475096, 60961, 41896, 46227, 54873, 5826, 1213, 257, 605, 542, 103, 23601, 0, 1741171, 0, 0, 0, 0], "petId": 23601, "skillId": [1101, 31074, 30133, 31073, 31072, 2206, 31083, 30142, 4074, 31086, 31085, 31102, 31100, 40028, 4104, 31051, 31055, 31054, 31056, 31057, 31058, 4054, 31065, 31066, 31067, 31068, 31069, 31070, 23601, 31116, 31117, 72021, 30163, 31118, 31112, 31113, 31114, 31115, 31108, 31109, 31110, 50002, 31105, 50001, 31106, 31128, 30150, 31131, 236014, 236013, 236012, 236011, 236010, 31120], "skillLevel": [2, 1, 1, 1, 1, 14, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 4, 4, 3, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 6, 1, 10, 1, 1, 1, 1, 82, 82, 82, 82, 82, 1]}]}, "show": {"avatarID": "716cc804-6090-48c8-9b0b-f8dec36be97b", "avatarName": "FabianTyt", "battlePoint": 7258037, "campId": 1, "chengHaoID": 1009, "comboWin": 26, "comboWinMax": 26, "contentID": 1009, "dollId": 0, "dollName": "", "fightCountTotal": 247, "fightCountWin": 181, "guild": "Warzone", "guildId": 195123738, "headFrame": 24, "lastActive": 1780600247, "level": 83, "masterLevel": 0, "mountEquip": [{"id": 4, "value": 3}, {"id": 5, "value":... <truncated in markdown; see decoded_packets.json>
  ```

### Frame 173: up/client_to_server

- **Segments**: `[173]`
- **Timestamp ms**: `1780601528454` .. `1780601528454`
- **Header**: `a5b973690000aa000000000000000053`
- **Total length**: `170` bytes; **payload codec**: `plain`; **format**: `urlencoded_request`
- **Functions**: `DaoguanOwnerQuery`
- **Query fields**: `{"bv": "7.0.2", "seq": "83", "session": "02D1B0135ABCDC0D", "sptype": "spv2jodo", "version": "7.0.2"}`
- **Decoded payload**:
  ```json
  [{"dgId": 506, "func": "DaoguanOwnerQuery"}]
  ```

### Frame 174: down/server_to_client

- **Segments**: `[174]`
- **Timestamp ms**: `1780601528492` .. `1780601528492`
- **Header**: `f9cf770d0003cc010e40100000000053`
- **Total length**: `972` bytes; **payload codec**: `zlib`; **format**: `json_response`
- **Functions**: `DaoguanOwnerQueryResult`
- **Decoded payload**:
  ```json
  [{"dgId": 506, "func": "DaoguanOwnerQueryResult", "ownerList": [{"comboWin": 2, "defenderPet": {"paraList": [4466894, 1001, 83, 41300, 0, 28, 0, 0, 0, 0, 0], "petIdList": [154, 31, 24], "petList": [{"petAttr": [743764, 75715, 54449, 27202, 25699, 26793, 1064, 73, 285, 186, 121, 23522, 90358, 2645366, 0, 0, 0, 0], "petId": 1023522, "skillId": [31075, 1101, 2202, 30133, 2203, 935222, 935223, 935220, 2206, 935221, 31076, 4323, 20862, 31085, 4998, 4274, 235224, 30163, 20182, 235222, 235223, 235220, 31055, 235221, 31054, 31056, 400011, 40007, 31128, 30150, 400012, 400013, 4254, 31065, 72013, 72011, 31123], "skillLevel": [1, 2, 6, 1, 5, 84, 84, 84, 12, 84, 1, 1, 1, 1, 1, 1, 84, 1, 1, 84, 84, 84, 1, 84, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]}, {"petAttr": [379089, 33408, 30389, 19402, 18461, 6274, 1064, 73, 285, 186, 114, 20961, 0, 1285776, 0, 0, 0, 0], "petId": 20961, "skillId": [31075, 1101, 30133, 2202, 2203, 44007, 2206, 31076, 2096102, 31085, 20902, 2096119, 2096132, 30163, 20182, 31055, 31054, 31056, 40001, 209612, 31128, 30150, 31065], "skillLevel": [1, 2, 1, 6, 5, 1, 12, 1, 84, 1, 1, 84, 84, 1, 1, 1, 1, 1, 1, 84, 1, 1, 1]}, {"petAttr": [250393, 18141, 14697, 8570, 8009, 3056, 1064, 73, 165, 186, 708, 23572, 90359, 463452, 0, 0, 0, 0], "petId": 23572, "skillId": [31075, 1101, 2202, 2203, 2206, 31076, 20222, 235724, 235723, 235722, 235721, 31055, 31085, 235720, 31054, 31056, 31128, 31065], "skillLevel": [1, 2, 6, 5, 12, 1, 1, 75, 75, 75, 75, 1, 1, 75, 1, 1, 1, 1]}]}, "show": {"avatarID": "56350147-1a02-4a63-bf36-a01685fa4e72", "avatarName": "nohatno", "battlePoint": 5493458, "campId": 2, "chengHaoID": 1007, "comboWin": 0, "comboWinMax": 15, "contentID": 1034, "dollId": 0, "dollName": "", "fightCountTotal": 198, "fightCountWin": 97, "guild": "Warzone", "guildId": 195123738, "headFrame": 38, "lastActive": 1780579953, "level": 84, "masterLevel": 0, "mountEquip": [{"id": 2, "value": 1}, {"id": 3, "value": 1}], "mount_ID": 7003, "petCount": 99, "petShowList": [{"afinity": 71, "id": 1023502, "level": 84}, {"afinity": 71, "id": 20961, "level": 84}, {"afinity": 66, "id": 21421, "level": 81}, {"afinity": 58, "id": 20981, "level": 78}, {"afinity": 19, "id": 22643, "level": 70}, {"afinity": 49, "id": 20863, "level": 53}, {"afinity": 81, "id": 1023522, "level": 84}, {"afinity": 30, "id": 21193, "level": 40}, {"afinity": 19, "id": 20222, "level": 70}], "pet_ID": 1023502, "ranking": 1000005, "rid": 195124560, "rotom_ID": 1001, "spriteLevel": 29, "talk": "", "tuxiaongID": 1023501, "vip": 10}, "timeAward": 1780530698, "timeWin": 1779459181}]}]
  ```

### Frame 175: up/client_to_server

- **Segments**: `[175]`
- **Timestamp ms**: `1780601528518` .. `1780601528518`
- **Header**: `361d0a8b0000aa000000000000000054`
- **Total length**: `170` bytes; **payload codec**: `plain`; **format**: `urlencoded_request`
- **Functions**: `DaoguanOwnerQuery`
- **Query fields**: `{"bv": "7.0.2", "seq": "84", "session": "02D1B0135ABCDC0D", "sptype": "spv2jodo", "version": "7.0.2"}`
- **Decoded payload**:
  ```json
  [{"dgId": 507, "func": "DaoguanOwnerQuery"}]
  ```

### Frame 176: down/server_to_client

- **Segments**: `[176]`
- **Timestamp ms**: `1780601528544` .. `1780601528544`
- **Header**: `4d46d1390003d7010e40100000000054`
- **Total length**: `983` bytes; **payload codec**: `zlib`; **format**: `json_response`
- **Functions**: `DaoguanOwnerQueryResult`
- **Decoded payload**:
  ```json
  [{"dgId": 507, "func": "DaoguanOwnerQueryResult", "ownerList": [{"comboWin": 0, "defenderPet": {"paraList": [4156423, 1004, 2, 24100, 0, 28, 0, 0, 0, 15003038, 3], "petIdList": [34, 156, 312, 53], "petList": [{"petAttr": [621707, 55406, 93836, 26814, 34639, 46490, 1104, 121, 600, 589, 121, 23522, 90358, 2635516, 0, 0, 0, 0], "petId": 1023522, "skillId": [1101, 2201, 30133, 935222, 935223, 935220, 935221, 4321, 30303, 4213, 72033, 4274, 31102, 31103, 31116, 31117, 235224, 20182, 31118, 4303, 31112, 31114, 31115, 72031, 31108, 31110, 31051, 30310, 235222, 235223, 31105, 50002, 235220, 50001, 235221, 31107, 400011, 40007, 31128, 30150, 400012, 400013, 4241, 31065, 31123, 48802, 31070, 30263, 12013], "skillLevel": [2, 5, 1, 81, 81, 81, 81, 1, 1, 1, 1, 1, 1, 1, 1, 1, 81, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 81, 81, 1, 8, 81, 10, 81, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]}, {"petAttr": [382543, 29337, 33243, 13163, 13039, 4993, 1104, 121, 480, 589, 1517, 21022, 90351, 737512, 0, 0, 0, 0], "petId": 21022, "skillId": [1101, 2201, 20221, 4222, 4998, 31102, 31103, 31116, 31117, 31118, 210220, 31112, 210221, 210222, 31114, 210223, 31115, 31108, 31051, 31110, 50002, 31105, 50001, 31107, 46706, 40001, 31128, 4241, 210224, 31065, 31070, 31122, 12013], "skillLevel": [2, 5, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 8, 1, 10, 1, 1, 1, 1, 1, 31, 1, 1, 1, 1]}, {"petAttr": [379848, 28146, 31437, 12367, 12199, 4890, 1104, 121, 480, 589, 1517, 21011, 0, 664437, 0, 0, 0, 0], "petId": 21011, "skillId": [2201, 1101, 40039, 210113, 210112, 210114, 31102, 31103, 31116, 31117, 31118, 20300, 31112, 31114, 31115, 31108, 31051, 31110, 210110, 210111, 50002, 31105, 50001, 31107, 31128, 31065, 31070, 12013], "skillLevel": [5, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 8, 1, 10, 1, 1, 1, 1, 1]}]}, "show": {"avatarID": "07a68e7a-21ce-4387-a447-4ed2fb97f147", "avatarName": "Recycler", "battlePoint": 4212099, "campId": 1, "chengHaoID": 0, "comboWin": 22, "comboWinMax": 22, "contentID": 2045, "dollId": 0, "dollName": "", "fightCountTotal": 174, "fightCountWin": 142, "guild": "SG⚘GĐ", "guildId": 195123642, "headFrame": 0, "lastActive": 1780581723, "level": 84, "masterLevel": 0, "mountEquip": [], "mount_ID": 7004, "petCount": 178, "petShowList": [{"afinity": 77, "id": 1023522, "level": 82}, {"afinity": 30, "id": 21022, "level": 45}, {"afinity": 37, "id": 20562, "level": 46}, {"afinity": 76, "id": 21061, "level": 81}], "pet_ID": 1023522, "ranking": 1000003, "rid": 195123693, "rotom_ID": 1002, "spriteLevel": 34, "talk": "", "tuxiaongID": 2045, "vip": 14}, "timeAward": 1780581698, "timeWin": 1780485290}]}]
  ```

### Frame 177: up/client_to_server

- **Segments**: `[177]`
- **Timestamp ms**: `1780601528651` .. `1780601528651`
- **Header**: `6ef3b3100000aa000000000000000055`
- **Total length**: `170` bytes; **payload codec**: `plain`; **format**: `urlencoded_request`
- **Functions**: `DaoguanOwnerQuery`
- **Query fields**: `{"bv": "7.0.2", "seq": "85", "session": "02D1B0135ABCDC0D", "sptype": "spv2jodo", "version": "7.0.2"}`
- **Decoded payload**:
  ```json
  [{"dgId": 508, "func": "DaoguanOwnerQuery"}]
  ```

### Frame 178: down/server_to_client

- **Segments**: `[178]`
- **Timestamp ms**: `1780601528680` .. `1780601528680`
- **Header**: `a709560400042a010e40100000000055`
- **Total length**: `1066` bytes; **payload codec**: `zlib`; **format**: `json_response`
- **Functions**: `DaoguanOwnerQueryResult`
- **Decoded payload**:
  ```json
  [{"dgId": 508, "func": "DaoguanOwnerQueryResult", "ownerList": [{"comboWin": 0, "defenderPet": {"paraList": [4694305, 1004, 79, 31600, 0, 28, 0, 0, 0, 0, 0], "petIdList": [193, 5, 103], "petList": [{"petAttr": [568366, 73259, 63865, 34193, 33110, 36833, 1153, 161, 470, 583, 121, 23522, 90358, 2510231, 0, 0, 0, 0], "petId": 1023522, "skillId": [1101, 2201, 2202, 30133, 20212, 2203, 935222, 935223, 2205, 935220, 2206, 935221, 31085, 30303, 4998, 235224, 20952, 31115, 31108, 30310, 235222, 235223, 235220, 31055, 235221, 31054, 31056, 31057, 400011, 40007, 4253, 31128, 30150, 400012, 400013, 31065, 4243, 72013, 72011, 31069, 31123, 31070, 30263], "skillLevel": [2, 7, 7, 1, 1, 7, 79, 79, 7, 79, 7, 79, 1, 1, 1, 79, 1, 1, 1, 1, 79, 79, 79, 5, 79, 5, 4, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]}, {"petAttr": [364205, 25933, 26988, 15297, 15661, 5953, 1153, 161, 550, 583, 114, 20961, 0, 907239, 0, 0, 0, 0], "petId": 20961, "skillId": [1101, 2201, 30133, 2202, 2203, 2205, 2206, 2096101, 31085, 2096118, 20112, 30163, 31115, 31108, 31055, 31054, 31056, 31057, 209613, 209612, 31128, 30150, 31065, 31069, 31070], "skillLevel": [2, 7, 1, 7, 7, 7, 7, 64, 1, 64, 1, 1, 1, 1, 5, 5, 4, 3, 64, 64, 1, 1, 1, 1, 1]}, {"petAttr": [429659, 46122, 37694, 24733, 22867, 5007, 1153, 161, 550, 583, 708, 23572, 90359, 1197085, 0, 0, 0, 0], "petId": 23572, "skillId": [1101, 2201, 30133, 2202, 2203, 2205, 2206, 20222, 30142, 235724, 235723, 235722, 235721, 31085, 235720, 30302, 40039, 30163, 31115, 31108, 31055, 31054, 31056, 31057, 31128, 30150, 31065, 42705, 31069, 31070], "skillLevel": [2, 7, 1, 7, 7, 7, 7, 1, 1, 72, 72, 72, 72, 1, 72, 1, 1, 1, 1, 1, 5, 5, 4, 3, 1, 1, 1, 1, 1, 1]}]}, "show": {"avatarID": "14fa5938-a9a4-4e99-9cb4-9738723cfcbe", "avatarName": "哈基咪", "battlePoint": 4609727, "campId": 1, "chengHaoID": 1029, "comboWin": 0, "comboWinMax": 29, "contentID": 2014, "dollId": 0, "dollName": "", "fightCountTotal": 245, "fightCountWin": 176, "guild": "SG⚘GĐ", "guildId": 195123642, "headFrame": 13, "lastActive": 1780581190, "level": 80, "masterLevel": 0, "mountEquip": [{"id": 4, "value": 3}], "mount_ID": 7004, "petCount": 203, "petShowList": [{"afinity": 39, "id": 21421, "level": 48}, {"afinity": 46, "id": 21363, "level": 62}, {"afinity": 68, "id": 23572, "level": 72}, {"afinity": 64, "id": 21061, "level": 76}, {"afinity": 42, "id": 22312, "level": 66}, {"afinity": 79, "id": 1023522, "level": 79}, {"afinity": 42, "id": 21541, "level": 50}, {"afinity": 68, "id": 21591, "level": 78}, {"afinity": 58, "id": 20441, "level": 68}, {"afinity": 76, "id": 1021052, "level": 77}, {"afinity": 43, "id": 21041, "level": 77}, {"afinity": 52, "id": 20744, "level": 55}], "pet_ID": 1020592, "ranking": 1000007, "rid": 195123521, "rotom_ID": 0, "spriteLevel": 34, "talk": "", "tuxiaongID": 2014, "vip": 13}, "timeAward": 1780553461, "timeWin": 1779588392}]}]
  ```

### Frame 179: up/client_to_server

- **Segments**: `[179]`
- **Timestamp ms**: `1780601528778` .. `1780601528778`
- **Header**: `d3ceff6b00009f000000000000000056`
- **Total length**: `159` bytes; **payload codec**: `plain`; **format**: `urlencoded_request`
- **Functions**: `ChampionLeagueQueryStatus`
- **Query fields**: `{"bv": "7.0.2", "seq": "86", "session": "02D1B0135ABCDC0D", "sptype": "spv2jodo", "version": "7.0.2"}`
- **Decoded payload**:
  ```json
  [{"func": "ChampionLeagueQueryStatus"}]
  ```

### Frame 180: down/server_to_client

- **Segments**: `[180]`
- **Timestamp ms**: `1780601528804` .. `1780601528804`
- **Header**: `671a18e600026e000e40100000000056`
- **Total length**: `622` bytes; **payload codec**: `plain`; **format**: `json_response`
- **Functions**: `ChampionLeagueQueryStatusResult`
- **Decoded payload**:
  ```json
  [{"func": "ChampionLeagueQueryStatusResult", "status": {"areaSupportList": [], "awardList": [], "fightCount": [0, 0, 0, 0, 0], "fightStatus": 0, "petList": [], "point": 0, "show": {"avatarID": "", "avatarName": "", "battlePoint": 0, "campId": 0, "chengHaoID": 0, "comboWin": 0, "comboWinMax": 0, "contentID": 0, "dollId": 0, "dollName": "", "fightCountTotal": 0, "fightCountWin": 0, "guild": "", "guildId": 0, "headFrame": 0, "lastActive": 0, "level": 0, "masterLevel": 0, "mountEquip": [], "mount_ID": 0, "petCount": 0, "petShowList": [], "pet_ID": 0, "ranking": 0, "rid": 0, "rotom_ID": 0, "spriteLevel": 0, "talk": "", "tuxiaongID": 0, "vip": 0}, "supportGet": 0, "supportList": []}}]
  ```

### Frame 181: up/client_to_server

- **Segments**: `[181]`
- **Timestamp ms**: `1780601528910` .. `1780601528910`
- **Header**: `bda78ab40000f7000000000000000057`
- **Total length**: `247` bytes; **payload codec**: `plain`; **format**: `urlencoded_request`
- **Functions**: `FightRealtimeQuery`
- **Query fields**: `{"bv": "7.0.2", "seq": "87", "session": "02D1B0135ABCDC0D", "sptype": "spv2jodo", "version": "7.0.2"}`
- **Decoded payload**:
  ```json
  [{"avatarId": "f25f2e5d-5ff3-4a83-89d5-4d259303f4bd", "fightId": "", "func": "FightRealtimeQuery"}]
  ```

### Frame 182: down/server_to_client

- **Segments**: `[182]`
- **Timestamp ms**: `1780601528944` .. `1780601528944`
- **Header**: `ee47ff7f000046000e40100000000057`
- **Total length**: `70` bytes; **payload codec**: `plain`; **format**: `json_response`
- **Functions**: `FightRealtimeQueryResult`
- **Decoded payload**:
  ```json
  [{"fightList": [], "func": "FightRealtimeQueryResult"}]
  ```

### Frame 183: up/client_to_server

- **Segments**: `[183]`
- **Timestamp ms**: `1780601529043` .. `1780601529043`
- **Header**: `8be9cc900000a9000000000000000058`
- **Total length**: `169` bytes; **payload codec**: `plain`; **format**: `urlencoded_request`
- **Functions**: `DaoguanGlobalQuery`
- **Query fields**: `{"bv": "7.0.2", "seq": "88", "session": "02D1B0135ABCDC0D", "sptype": "spv2jodo", "version": "7.0.2"}`
- **Decoded payload**:
  ```json
  [{"dgId": 0, "func": "DaoguanGlobalQuery"}]
  ```

### Frame 184: down/server_to_client

- **Segments**: `[184, 185]`
- **Timestamp ms**: `1780601529077` .. `1780601529078`
- **Header**: `824d4055000c3e010e40100000000058`
- **Total length**: `3134` bytes; **payload codec**: `zlib`; **format**: `json_response`
- **Functions**: `DaoguanGlobalQueryResult`
- **Decoded payload**:
  ```json
  [{"func": "DaoguanGlobalQueryResult", "list": [{"awardList": [], "dgid": 102, "ownerList": [{"defenderPet": {"paraList": [1222140], "petIdList": [], "petList": [{"petAttr": [201905, 47592, 29744, 20581, 22867, 5306, 1000, 0, 136, 136, 1914, 22071, 0, 0, 0, 0, 0, 0], "petId": 401311, "skillId": [220712, 220713, 20190, 220710, 220711, 220714], "skillLevel": [85, 85, 1, 85, 85, 85]}, {"petAttr": [143470, 26195, 35342, 24561, 27632, 3579, 1000, 0, 130, 130, 414, 21521, 0, 0, 0, 0, 0, 0], "petId": 401312, "skillId": [215210, 215211, 20211, 215213, 215214, 215212], "skillLevel": [85, 85, 1, 85, 85, 85]}, {"petAttr": [151910, 54051, 33263, 22105, 21492, 3150, 1000, 0, 130, 130, 1417, 20571, 0, 0, 0, 0, 0, 0], "petId": 401313, "skillId": [205711, 205712, 20190, 205714, 205710, 205713], "skillLevel": [85, 85, 1, 85, 85, 85]}]}, "dgTitleId": 1013001, "maxWaveWin": 0, "show": {"avatarID": "", "avatarName": "Elesa", "battlePoint": 1222140, "campId": 0, "chengHaoID": 0, "comboWin": 0, "comboWinMax": 0, "contentID": 387, "dollId": 0, "dollName": "", "fightCountTotal": 0, "fightCountWin": 0, "guild": "", "guildId": 0, "headFrame": 0, "lastActive": 1780497692, "level": 85, "masterLevel": 0, "mountEquip": [], "mount_ID": 0, "petCount": 0, "petShowList": [{"afinity": 0, "id": 401311, "level": 0}, {"afinity": 0, "id": 401312, "level": 0}, {"afinity": 0, "id": 401313, "level": 0}], "pet_ID": 0, "ranking": 0, "rid": -1, "rotom_ID": 0, "spriteLevel": 0, "talk": "I will resign myself to your guidance!", "tuxiaongID": 387, "vip": 0}, "timeWin": 1780497692, "waveWin": 0}], "record": [], "timeReset": 1780261201}, {"awardList": [], "dgid": 103, "ownerList": [{"defenderPet": {"paraList": [9873836, 1004, 50, 35200, 0, 28, 0, 0, 0, 0, 0], "petIdList": [58, 282, 33], "petList": [{"petAttr": [1168407, 222496, 83718, 76254, 90087, 115929, 1143, 173, 593, 641, 1703, 23602, 90351, 6587241, 0, 0, 0, 0], "petId": 1023982, "skillId": [31074, 1101, 30133, 1102, 31072, 31083, 31086, 31085, 939822, 939823, 20340, 939820, 939821, 4995, 239820, 61912, 239821, 239822, 239823, 31055, 70021, 31054, 31056, 31057, 31059, 31060, 239824, 31065, 31066, 31070, 80040, 15002, 30303, 23701, 31112, 31114, 31115, 30310, 31104, 31105, 31107, 400011, 400014, 400012, 30150, 31123], "skillLevel": [1, 2, 1, 2, 1, 1, 1, 1, 89, 89, 1, 89, 89, 1, 89, 1, 89, 89, 89, 2, 1, 4, 1, 1, 1, 5, 89, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]}, {"petAttr": [429634, 39568, 52280, 22112, 27484, 7851, 1139, 173, 593, 641, 417, 20352, 90351, 1592449, 0, 0, 0, 0], "petId": 1020352, "skillId": [1101, 31074, 1102, 30133, 31072, 15002, 2035223, 20512, 31083, 31086, 31085, 30300, 2035209, 31112, 31114, 31115, 31104, 31105, 70021, 31055, 31107, 31054, 203524, 31056, 31057, 31059, 2035239, 31060, 203521, 30150, 31065, 31066, 31070], "skillLevel": [2, 1, 2, 1, 1, 1, 87, 1, 1, 1, 1, 1, 87, 1, 1, 1, 1, 1, 1, 2, 1, 4, 87, 1, 1, 1, 87, 5, 87, 1, 1, 1, 1]}, {"petAttr": [520014, 60168, 51236, 31435, 31200, 10406, 1139, 173, ... <truncated in markdown; see decoded_packets.json>
  ```

### Frame 185: up/client_to_server

- **Segments**: `[186]`
- **Timestamp ms**: `1780601529118` .. `1780601529118`
- **Header**: `c264ff0c00009d000000000000000059`
- **Total length**: `157` bytes; **payload codec**: `plain`; **format**: `urlencoded_request`
- **Functions**: `DecorationHandbookQuery`
- **Query fields**: `{"bv": "7.0.2", "seq": "89", "session": "02D1B0135ABCDC0D", "sptype": "spv2jodo", "version": "7.0.2"}`
- **Decoded payload**:
  ```json
  [{"func": "DecorationHandbookQuery"}]
  ```

### Frame 186: down/server_to_client

- **Segments**: `[187]`
- **Timestamp ms**: `1780601529144` .. `1780601529144`
- **Header**: `99d8b94b00005a000e40100000000059`
- **Total length**: `90` bytes; **payload codec**: `plain`; **format**: `json_response`
- **Functions**: `DecorationHandbookQueryResult`
- **Decoded payload**:
  ```json
  [{"awardList": [], "func": "DecorationHandbookQueryResult", "ownedList": []}]
  ```

### Frame 187: up/client_to_server

- **Segments**: `[188]`
- **Timestamp ms**: `1780601529229` .. `1780601529229`
- **Header**: `be5377ad00009c00000000000000005a`
- **Total length**: `156` bytes; **payload codec**: `plain`; **format**: `urlencoded_request`
- **Functions**: `SecretBaseQueryPrivate`
- **Query fields**: `{"bv": "7.0.2", "seq": "90", "session": "02D1B0135ABCDC0D", "sptype": "spv2jodo", "version": "7.0.2"}`
- **Decoded payload**:
  ```json
  [{"func": "SecretBaseQueryPrivate"}]
  ```

### Frame 188: down/server_to_client

- **Segments**: `[189]`
- **Timestamp ms**: `1780601529255` .. `1780601529255`
- **Header**: `758a2f230000ae000e4010000000005a`
- **Total length**: `174` bytes; **payload codec**: `plain`; **format**: `json_response`
- **Functions**: `SecretBaseQueryPrivateResult`
- **Decoded payload**:
  ```json
  [{"func": "SecretBaseQueryPrivateResult", "sbPrivate": {"actionList": [], "furnitureList": [], "optionTime": [], "petSlotList": [], "themePosAll": [], "themeValid": []}}]
  ```

### Frame 189: up/client_to_server

- **Segments**: `[190]`
- **Timestamp ms**: `1780601529362` .. `1780601529362`
- **Header**: `f1f3331600009a00000000000000005b`
- **Total length**: `154` bytes; **payload codec**: `plain`; **format**: `urlencoded_request`
- **Functions**: `MirrorChallengeQuery`
- **Query fields**: `{"bv": "7.0.2", "seq": "91", "session": "02D1B0135ABCDC0D", "sptype": "spv2jodo", "version": "7.0.2"}`
- **Decoded payload**:
  ```json
  [{"func": "MirrorChallengeQuery"}]
  ```

### Frame 190: down/server_to_client

- **Segments**: `[191]`
- **Timestamp ms**: `1780601529388` .. `1780601529388`
- **Header**: `b75d4905000148000e4010000000005b`
- **Total length**: `328` bytes; **payload codec**: `plain`; **format**: `json_response`
- **Functions**: `MirrorChallengeQueryResult`
- **Decoded payload**:
  ```json
  [{"func": "MirrorChallengeQueryResult", "mcStatus": {"awardList": [], "buyCount": 0, "mirrorList": [130401, 130301], "point": 0, "progress": [{"id": 1, "value": 1}, {"id": 2, "value": 1}, {"id": 3, "value": 1}, {"id": 4, "value": 1}, {"id": 5, "value": 1}, {"id": 6, "value": 1}, {"id": 7, "value": 1}], "recoverCount": 0, "resetCount": 0, "winCount": 0}}]
  ```
