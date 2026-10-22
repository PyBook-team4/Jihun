import os
import requests
from dotenv import load_dotenv

# book_pj/.env 파일 경로 설정 (현재 위치에 따라 경로 조정)
load_dotenv(dotenv_path=".env")

# 환경 변수에서 API 키 불러오기
api_key = os.getenv("API_KEY")

if not api_key:
    print("❌ API 키를 불러오지 못했습니다. .env 파일 경로와 변수명을 확인해주세요.")
else:
    print(f"🔑 API 키 로드 성공: {api_key[:4]}********")

def test_api_connection():
    # 📌 첨부하신 가이드 문서(국립중앙도서관 등)의 오픈 API 엔드포인트 URL로 변경하세요.
    #url = "https://www.nl.go.kr/NL/search/openApi/search.do"
    url="https://www.nl.go.kr/NL/search/openApi/search.do"
    #url="https://www.nl.go.kr/NL/search/openApi/search.do?key=1cfb17fdc5494dc73fee5d757b7d6399183918aa496d18c88f0cbe481dfcf32e&kwd=%ED%86%A0%EC%A7%80"
    # API 요청 시 필요한 파라미터 구성 (예시)
    params = {
        "key": api_key,         # .env에서 불러온 실제 API 키 변수 삽입
        "kwd": "파이썬",          # 테스트 검색어
        "apiType": "json",      # 다루기 쉬운 JSON 형식으로 요청
        "srchTarget": "total",
        "pageSize": 1,
        "pageNum": 1
    }
    
    try:
        print("🚀 API 호출 테스트 중...")
        # requests가 url과 params를 안전하게 조합해서 요청을 보냅니다.
        response = requests.get(url, params=params, timeout=100)
        
        print(f"📡 응답 상태 코드 (Status Code): {response.status_code}")
        
        if response.status_code == 200:
            print("✅ API 호출 성공! 데이터 응답 정상 수신")
            
            # JSON 형태로 데이터가 잘 오는지 확인
            try:
                data = response.json()
                print("📦 응답 데이터 일부 확인:", str(data)[:300])
            except Exception:
                print(response.text[:300])
                
        else:
            print(f"❌ API 호출 실패. 상태 코드: {response.status_code}")
            print(response.text)
            
    except Exception as e:
        print(f"⚠️ 요청 중 에러가 발생했습니다: {e}")

if __name__ == "__main__":
    test_api_connection()