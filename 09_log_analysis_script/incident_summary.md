# 📊 데이터 센터 운영(DCO) 교육용 로그 분석 보고서

- **분석 기준일**: 2026-07-19
- **입력 파일**: `sample_dco_log.txt`
- **총 분석 로그 수**: 107 줄

## 1. 심각도(Severity)별 발생 통계
| 심각도 (Severity) | 발생 빈도 (Count) |
| :--- | :--- |
| INFO | 102회 |
| WARNING | 3회 |
| ERROR | 2회 |


## 2. 이벤트(Event) 종류별 발생 통계
| 이벤트명 (Event) | 발생 빈도 (Count) |
| :--- | :--- |
| Normal heartbeat | 92회 |
| Ticket opened | 3회 |
| Ticket escalated | 3회 |
| Maintenance completed | 3회 |
| Fan Alert | 1회 |
| Temperature warning | 1회 |
| SSD failure warning | 1회 |
| CRC error 증가 | 1회 |
| Link Down | 1회 |
| Link Up | 1회 |


## 3. 주의(WARNING) 및 에러/심각(ERROR/CRITICAL) 등급 로그 목록
| 시간 (Timestamp) | 장비명 (Device) | 등급 (Severity) | 이벤트 (Event) | 상세 내용 (Message) |
| :--- | :--- | :--- | :--- | :--- |
| 2026-07-03 01:05:00 | DEMO_CORE_SW_02 | **WARNING** | Fan Alert | Fan module 2 RPM dropped to 15% (Below threshold 20%). IP: 198.51.100.2 |
| 2026-07-03 02:05:00 | EDU_SRV_R04_N12 | **WARNING** | Temperature warning | Chassis temperature reached 42C (Threshold: 40C). IP: 192.0.2.12 |
| 2026-07-03 02:10:00 | EDU_SRV_R04_N12 | **ERROR** | SSD failure warning | Drive Slot 3 SSD wearout indicator FAILING (SMART wear 96%). IP: 192.0.2.12 |
| 2026-07-03 03:05:00 | SAMPLE_TOR_SW_01 | **WARNING** | CRC error 증가 | Interface Gi0/1 CRC error counter increased to 154 within 5 minutes. IP: 192.0.2.1 |
| 2026-07-03 03:06:00 | SAMPLE_TOR_SW_01 | **ERROR** | Link Down | Interface Gi0/1 status changed to DOWN. Connection to server lost. |


## 4. 핵심 이슈 상세 분석 (CRC_ERROR / LINK_DOWN / TICKET_ESCALATED)
인프라 물리 계층(Physical Layer) 및 장애 조치 시스템과 연관된 주요 이벤트 요약입니다.

### 이슈 #1: [TICKET_ESCALATED] 발생 (등급: INFO)
- **발생 시각**: 2026-07-03 01:10:00
- **대상 장비**: `DEMO_CORE_SW_02`
- **상세 메시지**: Ticket EDU-TKT-2026-0001 escalated to Local Infrastructure Team.
- **교육용 개념 돋보기**: 💡 **티켓 에스컬레이션이란?** 모니터링 시스템이 장애를 자동 감지하여 실제 수리를 수행할 현장 엔지니어에게 수리 요청서(Ticket)를 전송하고 담당자를 배정한 상태입니다.

### 이슈 #2: [TICKET_ESCALATED] 발생 (등급: INFO)
- **발생 시각**: 2026-07-03 02:15:00
- **대상 장비**: `EDU_SRV_R04_N12`
- **상세 메시지**: Ticket EDU-TKT-2026-0002 escalated to DCO Hardware Support.
- **교육용 개념 돋보기**: 💡 **티켓 에스컬레이션이란?** 모니터링 시스템이 장애를 자동 감지하여 실제 수리를 수행할 현장 엔지니어에게 수리 요청서(Ticket)를 전송하고 담당자를 배정한 상태입니다.

### 이슈 #3: [CRC_ERROR] 발생 (등급: WARNING)
- **발생 시각**: 2026-07-03 03:05:00
- **대상 장비**: `SAMPLE_TOR_SW_01`
- **상세 메시지**: Interface Gi0/1 CRC error counter increased to 154 within 5 minutes. IP: 192.0.2.1
- **교육용 개념 돋보기**: 💡 **CRC 에러란?** 데이터 전송 중 케이블이나 하드웨어 접촉 불량 등으로 인해 데이터 패킷이 손상되었음을 뜻합니다.

### 이슈 #4: [LINK_DOWN] 발생 (등급: ERROR)
- **발생 시각**: 2026-07-03 03:06:00
- **대상 장비**: `SAMPLE_TOR_SW_01`
- **상세 메시지**: Interface Gi0/1 status changed to DOWN. Connection to server lost.
- **교육용 개념 돋보기**: 💡 **링크 다운이란?** 장치 간의 연결 선이 뽑혔거나 상대 장비가 꺼지는 등 물리적인 연결이 끊어진 긴급 상태를 뜻합니다.

### 이슈 #5: [TICKET_ESCALATED] 발생 (등급: INFO)
- **발생 시각**: 2026-07-03 03:12:00
- **대상 장비**: `SAMPLE_TOR_SW_01`
- **상세 메시지**: Ticket EDU-TKT-2026-0003 escalated to Onsite Cabling Team.
- **교육용 개념 돋보기**: 💡 **티켓 에스컬레이션이란?** 모니터링 시스템이 장애를 자동 감지하여 실제 수리를 수행할 현장 엔지니어에게 수리 요청서(Ticket)를 전송하고 담당자를 배정한 상태입니다.