import os
from models.member import Member
from utils.file_handler import FileHandler

class MemberManager:
    def __init__(self, filename="data/members.json"):
        self.filename = filename
        self.members = {}  # {user_id: Member 객체}
        self.current_user = None  # 현재 로그인한 회원 객체
        self.load_members()

    def load_members(self):
        """프로그램 실행 시 JSON 파일에서 회원 정보를 불러옴"""
        data_list = FileHandler.load_json(self.filename)
        for item in data_list:
            member = Member.from_dict(item)
            self.members[member.user_id] = member

    def save_members(self):
        """회원 정보 변경 시 JSON 파일에 즉시 저장"""
        # data 폴더가 없으면 생성
        os.makedirs(os.path.dirname(self.filename), exist_ok=True)
        data_list = [member.to_dict() for member in self.members.values()]
        FileHandler.save_json(self.filename, data_list)

    def check_duplicate(self, user_id):
        """동일한 회원 아이디 등록 방지 (중복 검사)"""
        return user_id in self.members

    def register(self):
        """회원가입 기능"""
        print("\n--- [회원가입] ---")
        user_id = input("아이디 입력: ").strip()
        
        if self.check_duplicate(user_id):
            print("이미 존재하는 아이디입니다.")
            return False
        
        password = input("비밀번호 입력: ").strip()
        name = input("이름 입력: ").strip()
        phone = input("연락처 입력: ").strip()
        email = input("이메일 입력: ").strip()

        new_member = Member(user_id, password, name, phone, email)
        self.members[user_id] = new_member
        self.save_members()
        print("회원가입이 완료되었습니다!")
        return True

    def login(self):
        """로그인 기능"""
        print("\n--- [로그인] ---")
        user_id = input("아이디 입력: ").strip()
        password = input("비밀번호 입력: ").strip()

        member = self.members.get(user_id)
        if member and member.password == password:
            self.current_user = member
            print(f"로그인 성공! [{member.name}]님 환영합니다.")
            return True
        else:
            print("아이디 또는 비밀번호가 일치하지 않습니다.")
            return False

    def logout(self):
        """로그아웃 기능"""
        if self.current_user:
            print(f"[{self.current_user.name}]님이 로그아웃하셨습니다.")
            self.current_user = None
        else:
            print("로그인된 사용자가 없습니다.")

    # === 기존 MemberManager 클래스 내부 하단에 추가 ===

########## 여기서부터 추가
    def show_my_info(self):
        """내 정보 조회"""
        if not self.current_user:
            print("로그인 상태가 아닙니다.")
            return
        u = self.current_user
        print("\n--- [내 회원 정보] ---")
        print(f"아이디 : {self.current_user.user_id}")
        print(f"이름   : {self.current_user.name}")
        print(f"연락처 : {self.current_user.phone}")
        print(f"이메일 : {self.current_user.email}")

    def update_my_info(self):
        """내 정보 수정"""
        if not self.current_user:
            print("로그인 상태가 아닙니다.")
            return
        u = self.current_user
        print("\n--- [내 정보 수정 (아이디는 변경할 수 없습니다.)---\n변경하지 않으려면 엔터)] ")
        new_password = input("새 비밀번호: ").strip()
        new_name = input(f"새 이름 [{self.current_user.name}]: ").strip()
        new_phone = input(f"새 연락처 [{self.current_user.phone}]: ").strip()
        new_email = input(f"새 이메일 [{self.current_user.email}]: ").strip()

        if new_password:
            self.current_user.password = new_password
        if new_name:
            self.current_user.name = new_name
        if new_phone:
            self.current_user.phone = new_phone
        if new_email:
            self.current_user.email = new_email

        self.save_members()
        print("회원 정보가 수정되었습니다.")

    def delete_account(self):
        """회원 탈퇴 (이름 및 비밀번호 2중 검증)"""
        if not self.current_user:
            print("로그인 상태가 아닙니다.")
            return False

        print("\n--- [회원 탈퇴 본인 확인] ---")
        input_name = input("회원 이름 입력: ").strip()
        input_password = input("비밀번호 입력: ").strip()

        # 1차 검증: 회원 이름 일치 여부
        if input_name != self.current_user.name:
            print("입력하신 이름이 회원 정보와 일치하지 않습니다.")
            return False

        # 2차 검증: 비밀번호 일치 여부
        if input_password != self.current_user.password:
            print("비밀번호가 일치하지 않습니다.")
            return False

        confirm = input("\n정말로 탈퇴하시겠습니까? 모든 정보가 삭제됩니다. (y/n): ").strip().lower()
        if confirm == 'y':
            del self.members[self.current_user.user_id]
            self.save_members()
            print(f"[{input_name}]님의 탈퇴 처리가 정상적으로 완료되었습니다.")
            self.current_user = None
            return True
        else:
            print("탈퇴가 취소되었습니다.")
            return False

    def admin_delete_member(self):
        """[관리자 전용] 특정 회원 강제 삭제"""
        print("\n--- [관리자: 회원 강제 삭제] ---")
        user_id = input("삭제할 회원 ID 입력: ").strip()
        if user_id not in self.members:
            print(f"회원 ID '{user_id}'을(를) 찾을 수 없습니다.")
            return

        target = self.members[user_id]
        confirm = input(f"정말로 회원 [{target.name}({user_id})]을(를) 영구 삭제하시겠습니까? (y/n): ").strip().lower()
        if confirm == 'y':
            del self.members[user_id]
            self.save_members()
            print(f"회원 '{user_id}'이(가) 데이터베이스에서 영구 삭제되었습니다.")
        else:
            print("삭제가 취소되었습니다.")

    def list_all_members(self):
        """전체 회원 목록 조회 (관리자/테스트용)"""
        print("\n--- [전체 회원 목록] ---")
        if not self.members:
            print("등록된 회원이 없습니다.")
            return
        print(f"{'아이디':<15} | {'이름':<10} | {'연락처':<15} | {'이메일'}")
        print("-" * 50)
        for m in self.members.values():
            print(f"{m.user_id:<15} | {m.name:<10} | {m.phone:<15} | {m.email}")