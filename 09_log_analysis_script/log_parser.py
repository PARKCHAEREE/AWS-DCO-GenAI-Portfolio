# -*- coding: utf-8 -*-
"""
DCO(Data Center Operations) 교육용 샘플 로그 분석 스크립트
작성일: 2026-07-19
설명: 이 스크립트는 데이터 센터 장비에서 생성된 교육용 샘플 로그 파일을 읽어 분석하고,
      그 결과를 마크다운 형식의 보고서(incident_summary.md)로 저장합니다.
      파이썬 기본 라이브러리(Standard Library)만 사용하여 비전공자도 쉽게 공부할 수 있도록 작성되었습니다.
"""
import os
# 1. 파일 경로 정의
# 분석할 입력 로그 파일과 결과를 저장할 출력 파일의 이름을 설정합니다.
INPUT_FILE = "sample_dco_log.txt"
OUTPUT_FILE = "incident_summary.md"
def analyze_dco_logs():
    print("=========================================")
    print("DCO 로그 분석을 시작합니다...")
    print("=========================================")
    # 입력 파일이 존재하는지 먼저 확인합니다 (오류 방지)
    if not os.path.exists(INPUT_FILE):
        print(f"오류: 입력 파일 '{INPUT_FILE}'을 찾을 수 없습니다.")
        print("같은 디렉토리에 로그 파일이 있는지 확인해 주세요.")
        return
    # 분석에 필요한 변수들을 초기화합니다.
    total_lines = 0               # 1. 전체 로그 줄 수
    severity_counts = {}          # 2. 심각도(Severity)별 개수를 저장할 딕셔너리
    event_counts = {}             # 3. 이벤트(Event)별 개수를 저장할 딕셔너리
    warning_or_critical_logs = [] # 4. WARNING 또는 CRITICAL 로그 목록을 저장할 리스트
    key_events_summary = []       # 5. 주요 이벤트(CRC_ERROR, LINK_DOWN, TICKET_ESCALATED) 요약
    # 2. 로그 파일 읽기 및 분석
    # 'with' 문을 사용하면 파일을 안전하게 열고 작업이 끝난 후 자동으로 닫아줍니다.
    # utf-8 인코딩을 지정하여 한글이나 특수기호가 깨지지 않게 합니다.
    with open(INPUT_FILE, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()  # 줄 끝의 줄바꿈 문자(\n)나 공백을 제거합니다.
            if not line:         # 빈 줄은 건너뜁니다.
                continue
            total_lines += 1     # 줄 수 카운트 증가
            # 로그 형식: YYYY-MM-DD HH:MM:SS | DEVICE | SEVERITY | EVENT | MESSAGE
            # 파이프 기호('|')를 기준으로 데이터를 나눕니다.
            parts = [part.strip() for part in line.split("|")]
            # 데이터가 정상적으로 5개 영역으로 나뉘었는지 확인합니다.
            if len(parts) < 5:
                continue
            # 각 영역의 데이터를 변수에 할당합니다.
            timestamp = parts[0]
            device = parts[1]
            severity = parts[2]
            event = parts[3]
            message = parts[4]
            # (1) 심각도(Severity)별 개수 집계
            # 딕셔너리에 키가 없으면 기본값 0을 설정하고 1을 더합니다.
            severity_counts[severity] = severity_counts.get()severity, 0) + 1
            # (2) 이벤트(Event)별 개수 집계
            event_counts[event] = event_counts.get()event, 0) + 1
            # (3) WARNING, ERROR 또는 CRITICAL 로그 필터링
            if severity in ["WARNING", "ERROR", "CRITICAL"]:
                warning_or_critical_logs.append({
                    "timestamp": timestamp,
                    "device": device,
                    "severity": severity,
                    "event": event,
                    "message": message
                })
            # (4) 주요 이벤트 (CRC_ERROR, LINK_DOWN, TICKET_ESCALATED) 요약
            # 이 세 가지 키워드가 이벤트 이름에 포함되어 있는 경우 따로 요약 리스트에 보관합니다.
            # 다양한 형식의 이벤트를 동일하게 매핑하여 학습 효과를 극대화합니다.
            matched_event = None
            if event == "CRC_ERROR" or "CRC" in event.upper():
                matched_event = "CRC_ERROR"
            elif event == "LINK_DOWN" or "LINK DOWN" in event.upper():
                matched_event = "LINK_DOWN"
            elif event == "TICKET_ESCALATED" or "ESCALATE" in event.upper():
                matched_event = "TICKET_ESCALATED"
            if matched_event:
                key_events_summary.append({
                    "timestamp": timestamp,
                    "device": device,
                    "severity": severity,
                    "event": matched_event,
                    "message": message
                })
    # 3. 결과 출력용 마크다운 형식 텍스트 구성
    # 비전공자도 보기 편하도록 깔끔한 표(Table)와 리스트(List) 구조로 보고서를 만듭니다.
    markdown_content = []
    markdown_content.append("# 📊 데이터 센터 운영(DCO) 교육용 로그 분석 보고서\n")
    markdown_content.append(f"- **분석 기준일**: 2026-07-19")
    markdown_content.append(f"- **입력 파일**: `{INPUT_FILE}`")
    markdown_content.append(f"- **총 분석 로그 수**: {total_lines} 줄\n")
    # 3.1 심각도(Severity)별 통계
    markdown_content.append("## 1. 심각도(Severity)별 발생 통계")
    markdown_content.append("| 심각도 (Severity) | 발생 빈도 (Count) |")
    markdown_content.append("| :--- | :--- |")
    # 높은 심각도 우선순위 또는 빈도수로 정렬하여 표를 완성합니다.
    for sev, count in sorted(severity_counts.items(), key=lambda x: x[1], reverse=True):
        markdown_content.append(f"| {sev} | {count}회 |")
    markdown_content.append("\n")
    # 3.2 이벤트(Event)별 통계
    markdown_content.append("## 2. 이벤트(Event) 종류별 발생 통계")
    markdown_content.append("| 이벤트명 (Event) | 발생 빈도 (Count) |")
    markdown_content.append("| :--- | :--- |")
    for ev, count in sorted(event_counts.items(), key=lambda x: x[1], reverse=True):
        markdown_content.append(f"| {ev} | {count}회 |")
    markdown_content.append("\n")
    # 3.3 WARNING, ERROR 및 CRITICAL 로그 목록
    markdown_content.append("## 3. 주의(WARNING) 및 에러/심각(ERROR/CRITICAL) 등급 로그 목록")
    markdown_content.append("| 시간 (Timestamp) | 장비명 (Device) | 등급 (Severity) | 이벤트 (Event) | 상세 내용 (Message) |")
    markdown_content.append("| :--- | :--- | :--- | :--- | :--- |")
    for item in warning_or_critical_logs:
        markdown_content.append(
            f"| {item['timestamp']} | {item['device']} | **{item['severity']}** | {item['event']} | {item['message']} |"
        )
    markdown_content.append("\n")
    # 3.4 주요 이슈 요약 (CRC_ERROR, LINK_DOWN, TICKET_ESCALATED)
    markdown_content.append("## 4. 핵심 이슈 상세 분석 (CRC_ERROR / LINK_DOWN / TICKET_ESCALATED)")
    markdown_content.append("인프라 물리 계층(Physical Layer) 및 장애 조치 시스템과 연관된 주요 이벤트 요약입니다.\n")
    
    if not key_events_summary:
        markdown_content.append("- 해당 주요 이벤트가 발견되지 않았습니다.\n")
    else:
        for idx, item in enumerate(key_events_summary, 1):
            markdown_content.append(f"### 이슈 #{idx}: [{item['event']}] 발생 (등급: {item['severity']})")
            markdown_content.append(f"- **발생 시각**: {item['timestamp']}")
            markdown_content.append(f"- **대상 장비**: `{item['device']}`")
            markdown_content.append(f"- **상세 메시지**: {item['message']}")
            
            # 교육적인 부가설명 추가 (비전공자 맞춤 가이드)
            explanation = ""
            if item['event'] == 'CRC_ERROR':
                explanation = "💡 **CRC 에러란?** 데이터 전송 중 케이블이나 하드웨어 접촉 불량 등으로 인해 데이터 패킷이 손상되었음을 뜻합니다."
            elif item['event'] == 'LINK_DOWN':
                explanation = "💡 **링크 다운이란?** 장치 간의 연결 선이 뽑혔거나 상대 장비가 꺼지는 등 물리적인 연결이 끊어진 긴급 상태를 뜻합니다."
            elif item['event'] == 'TICKET_ESCALATED':
                explanation = "💡 **티켓 에스컬레이션이란?** 모니터링 시스템이 장애를 자동 감지하여 실제 수리를 수행할 현장 엔지니어에게 수리 요청서(Ticket)를 전송하고 담당자를 배정한 상태입니다."
            
            markdown_content.append(f"- **교육용 개념 돋보기**: {explanation}\n")
    # 4. 분석 결과 파일 쓰기
    # 구성된 마크다운 텍스트 리스트를 하나의 문자열로 결합하여 저장합니다.
    report_text = "\n".join(markdown_content)
    with open(OUTPUT_FILE, "w", encoding="utf-8") as out_file:
        out_file.write(report_text)
    print(f"분석 완료! 결과가 '{OUTPUT_FILE}' 파일로 성공적으로 저장되었습니다.")
    print("=========================================")
if __name__ == "__main__":
    analyze_dco_logs()