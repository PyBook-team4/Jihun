# 관리자 비밀번호 관리 추가

# utils/auth.py
from datetime import datetime, timedelta

def verify_admin_password():
    """
    어드민 비밀번호 검증: (현재 시스템 날짜 - 1일)
    형식: YYYYMMDD (예: 오늘이 2026-10-21인 경우 비밀번호는 '20261020')
    """
    yesterday = datetime.now() - timedelta(days=1)
    correct_password = yesterday.strftime("%Y%m%d")

    print("\n" + "=" * 35)
    print("       🔒 [관리자 인증 시스템]")
    print("=" * 35)
    entered_pw = input("어드민 비밀번호를 입력하세요: ").strip().replace("-", "")

    if entered_pw == correct_password:
        print("✅ 관리자 인증에 성공하였습니다.")
        return True
    else:
        print("❌ 인증 실패: 비밀번호가 올바르지 않습니다.")
        return False