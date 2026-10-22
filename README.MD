===현재까지 디렉토리 구조=====
PyBook/
├── .env                          # Google Books API 키 및 환경 변수 설정
├── .gitignore                    # .env, data/*.json, __pycache__, venv/ 제외 설정
├── requirements.txt              # 필수 라이브러리 목록 (requests, python-dotenv, matplotlib, scikit-learn 등)
├── main.py                       # 애플리케이션 진입점 (콘솔 메뉴 라우터 & 컨트롤러)
│
├── data/                         # JSON 기반 영구 저장소 (데이터 베이스 역할)
│   ├── members.json              # 회원 정보 (ID, PW, 이름, 포인트, 등급, 마지막 로그인일 등)
│   ├── books.json                # 도서 서지 정보 (ID, 제목, 저자, 장르, 평점, 재고 상태 등)
│   ├── loans.json                # 대출/반납 이력 (대출 ID, 회원 ID, 도서 ID, 대출일, 반납예정일, 상태)
│   └── records.json              # 독서 기록 및 감상평 (별점, 감성 분석 결과, 리뷰 텍스트 등)
│
├── models/                       # 도메인 데이터 객체 모델 (OOP 클래스 정의)
│   ├── __init__.py
│   ├── member.py                 # Member 클래스 (회원 속성 및 등급/포인트 메서드)
│   ├── book.py                   # Book 클래스 (도서 서지 정보 객체)
│   ├── loan.py                   # Loan 클래스 (대출 거래 내역 객체)
│   └── record.py                 # Record 클래스 (독서 노트 및 평점 객체)
│
├── services/                     # 비즈니스 로직 및 핵심 기능 모듈 (CRUD & 서비스)
│   ├── __init__.py
│   ├── member_service.py         # 회원가입, 로그인, 정보수정, 탈퇴, 관리자 휴면 회원 조회
│   ├── book_service.py           # 수동 도서 등록, Google Books API 연동, 베스트셀러/오늘의 추천 관리
│   ├── loan_service.py           # 도서 대출/반납, 등급별 대출 제한/기한 체크, 포인트 적립, 다독왕 선정
│   ├── search_service.py         # 관심분야 1차/2차 키워드 필터링, 정렬(이름/저자/연도/평점), 퍼지 검색
│   ├── ai_service.py             # AI 퀴즈 생성, AI 챗봇 인터페이스, 코사인 유사도 기반 AI 도서 추천
│   └── analytics_service.py      # 나만의 독서 연대기 집계, 목표치 설정 및 달성률 계산
│
└── utils/                        # 공통 유틸리티 및 외부 연동 도구
    ├── __init__.py
    ├── file_handler.py           # JSON 파일 읽기/쓰기 및 영속성 관리 공통 유틸리티
    ├── api_client.py             # Google Books API 호출 클라이언트
    ├── fuzzy_matcher.py          # 레벤슈타인 거리 알고리즘 기반 오타 허용 검색 유틸리티
    └── visualizer.py             # Matplotlib 기반 장르별 독서 비율 파이/바 차트 시각화 유틸리티

=======참고용=======================

book_project/
│
├── main.py                  #  프로그램 실행 진입점 (메인 메뉴 제어)
├── README.md                #  프로젝트 소개 및 실행 가이드
│
├── models/                  #  데이터 구조(클래스) 정의 패키지
│   ├── __init__.py
│   ├── member.py            # 회원 데이터 클래스
│   ├── book.py              # 도서 데이터 클래스
│   └── record.py            # 독서 기록(상태, 별점, 감상평) 클래스
│
├── services/                # 핵심 비즈니스 로직 및 CRUD 처리 패키지
│   ├── __init__.py
│   ├── member_manager.py    # 회원가입, 로그인, 정보 수정/삭제
│   ├── book_manager.py      # 도서 등록, 상세 조회, 수정/삭제
│   └── record_manager.py    # 독서 상태 관리, 검색, 정렬, 통계
│
├── utils/                   # 공통 유틸리티 및 외부 연동 패키지
│   ├── __init__.py
│   ├── file_handler.py      # JSON/CSV 파일 입출력 공통 함수
│   └── api_client.py        # Open Library API 책 정보 자동 조회 연동
│
├── data/                    # 데이터 영속성 저장소 (JSON/CSV 파일)
│   ├── members.json
│   ├── books.json
│   └── records.json
│
└── tests/                   # 단위 테스트 및 통합 테스트 코드[cite: 1]
    ├── __init__.py
    ├── test_member.py
    └── test_book.py



    # Book Record Management System (독서 기록 관리 시스템)

