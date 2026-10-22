# 콘솔창 초기화 추가

# utils/console.py
import functools

# ANSI 이스케이프 코드: 커서 맨 위 이동(\033[H), 화면 삭제(\033[2J), 스크롤 버퍼 삭제(\033[3J)
CLEAR = "\033[H\033[2J\033[3J"

def clear_console():
    """콘솔 화면을 즉시 초기화"""
    print(CLEAR, end="", flush=True)

def action_view(func):
    """
    각 서브 기능 실행 시 화면을 먼저 비우고,
    실행 완료 후 사용자가 결과를 확인하도록 [Enter] 대기를 자동 처리하는 데코레이터
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(CLEAR, end="", flush=True)
        result = func(*args, **kwargs)
        input("\n[Enter] 키를 누르면 메뉴로 돌아갑니다...")
        return result
    return wrapper