# main.py
import sys
from services.member_manager import MemberManager
from services.book_manager import BookManager
from utils.console import clear_console, action_view
from utils.auth import verify_admin_password

@action_view
def run_action(target_func, *args, **kwargs):
    """데코레이터가 적용된 액션 실행 래퍼"""
    return target_func(*args, **kwargs)

# ==========================================
# 1. 일반 회원 전용 메뉴
# ==========================================

def run_book_menu_for_user(book_manager):
    """일반 회원용 도서 메뉴 (조회 및 검색만 가능)"""
    while True:
        clear_console()
        print("=" * 35)
        print("         [ 도서 목록 및 검색 ]")
        print("=" * 35)
        print("1. 전체 도서 목록")
        print("2. 도서 검색 (제목/저자)")
        print("h. 메인 메뉴로 돌아가기")
        print("-" * 35)
        choice = input("선택: ").strip().lower()

        if choice == '1':
            run_action(book_manager.list_all_books)
        elif choice == '2':
            run_action(book_manager.search_books)
        elif choice in ('b', 'e'):
            break
        else:
            print("잘못된 입력입니다. 다시 선택해주세요.")

def run_member_menu(member_manager):
    """내 정보 관리 메뉴 (일반 회원용)"""
    while True:
        clear_console()
        print("=" * 35)
        print("          [ 내 정보 관리 ]")
        print("=" * 35)
        print("1. 내 프로필 확인")
        print("2. 내 정보 수정")
        print("3. 회원 탈퇴")
        print("h. 메인 메뉴로 돌아가기")
        print("-" * 35)
        choice = input("선택: ").strip().lower()

        if choice == '1':
            run_action(member_manager.show_my_info)
        elif choice == '2':
            run_action(member_manager.update_my_info)
        elif choice == '3':
            # 이름/비밀번호 2중 검증 통과 시 상위 루프 탈출 신호
            if run_action(member_manager.delete_account):
                return "deleted"
        elif choice in ('h', 'e'):
            break
        else:
            print("잘못된 입력입니다. 다시 선택해주세요.")
    return None

def logged_in_main(member_manager, book_manager):
    """로그인 상태 사용자 메인 메뉴"""
    while member_manager.current_user:
        clear_console()
        print("=" * 45)
        print(f"📚 Pybook [접속자: {member_manager.current_user.name} 님]")
        print("=" * 45)
        print("1. 도서 목록 및 검색")
        print("2. 내 정보 관리")
        print("3. 로그아웃")
        print("e. 프로그램 종료")
        print("-" * 45)
        choice = input("메뉴 선택: ").strip().lower()

        if choice == '1':
            run_book_menu_for_user(book_manager)
        elif choice == '2':
            status = run_member_menu(member_manager)
            if status == "deleted":
                break
        elif choice == '3':
            run_action(member_manager.logout)
            break
        elif choice == 'e':
            clear_console()
            print("프로그램을 종료합니다.")
            sys.exit(0)
        else:
            print("잘못된 입력입니다. 다시 선택해주세요.")

# ==========================================
# 2. 어드민 전용 메뉴 (Hidden)
# ==========================================

def run_admin_menu(member_manager, book_manager):
    """어드민 관리 메뉴"""
    while True:
        clear_console()
        print("=" * 45)
        print("        [시스템 관리자 모드]")
        print("=" * 45)
        print("--- [회원 관리] ---")
        print("1. 전체 회원 목록 조회")
        print("2. 회원 강제 삭제")
        print("--- [도서 관리 (CRUD)] ---")
        print("3. 신규 도서 등록")
        print("4. 전체 도서 목록 조회")
        print("5. 도서 검색")
        print("6. 도서 정보 수정")
        print("7. 도서 삭제")
        print("--- [기타] ---")
        print("h. 관리자 모드 종료 (메인 메뉴로 이동)")
        print("-" * 45)
        choice = input("관리자 메뉴 선택: ").strip().lower()

        if choice == '1':
            run_action(member_manager.list_all_members)
        elif choice == '2':
            run_action(member_manager.admin_delete_member)
        elif choice == '3':
            run_action(book_manager.register_book)
        elif choice == '4':
            run_action(book_manager.list_all_books)
        elif choice == '5':
            run_action(book_manager.search_books)
        elif choice == '6':
            run_action(book_manager.update_book)
        elif choice == '7':
            run_action(book_manager.delete_book)
        elif choice in ('h', 'e'):
            print("\n관리자 모드를 종료합니다.")
            break
        else:
            print("잘못된 입력입니다. 다시 선택해주세요.")

# ==========================================
# 3. 최상위 시작점
# ==========================================

def main():
    member_manager = MemberManager()
    book_manager = BookManager()

    while True:
        clear_console()
        print("=" * 35)
        print("📚 Pybook에 오신것을 환영합니다.")
        print("=" * 35)
        print("1. 회원가입")
        print("2. 로그인")
        print("e. 프로그램 종료")
        print("-" * 35)
        choice = input("메뉴 선택: ").strip()

        if choice == '1':
            run_action(member_manager.register)
        elif choice == '2':
            if run_action(member_manager.login):
                logged_in_main(member_manager, book_manager)
        elif choice.lower() == 'e':
            clear_console()
            print("프로그램을 종료합니다. 이용해 주셔서 감사합니다.")
            break
        elif choice.lower() == 'admin':
            # 숨겨진 어드민 진입 트리거: 비밀번호 검증 후 진입
            if run_action(verify_admin_password):
                run_admin_menu(member_manager, book_manager)
        else:
            print("잘못된 입력입니다. 다시 선택해주세요.")

if __name__ == "__main__":
    main()