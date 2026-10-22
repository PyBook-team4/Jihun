# services/book_manager.py
import os
from models.book import Book
from utils.file_handler import FileHandler

class BookManager:
    def __init__(self, filename="data/books.json"):
        self.filename = filename
        self.books = {}  # {book_id: Book 객체}
        self.load_books()

    def load_books(self):
        """프로그램 실행 시 JSON 파일에서 도서 정보 불러오기"""
        if os.path.exists(self.filename):
            data_list = FileHandler.load_json(self.filename)
            for item in data_list:
                book = Book.from_dict(item)
                self.books[book.book_id] = book

    def save_books(self):
        """도서 정보 변경 시 JSON 파일에 저장"""
        os.makedirs(os.path.dirname(self.filename), exist_ok=True)
        data_list = [book.to_dict() for book in self.books.values()]
        FileHandler.save_json(self.filename, data_list)

    def register_book(self):
        """도서 등록"""
        print("\n--- [신규 도서 등록] ---")
        book_id = input("도서 식별번호(ISBN/ID): ").strip()
        if book_id in self.books:
            print("이미 등록된 도서 번호입니다.")
            return

        title = input("도서명: ").strip()
        author = input("저자: ").strip()
        publisher = input("출판사: ").strip()
        genre = input("장르(소설/IT/인문 등): ").strip() or "일반"

        if not (book_id and title and author):
            print("도서번호, 제목, 저자는 필수 입력 항목입니다.")
            return

        new_book = Book(book_id, title, author, publisher, genre)
        self.books[book_id] = new_book
        self.save_books()
        print(f"도서 '{title}'이(가) 등록되었습니다.")

    def list_all_books(self):
        """전체 도서 목록 조회"""
        print("\n--- [전체 도서 목록] ---")
        if not self.books:
            print("등록된 도서가 없습니다.")
            return
        print(f"{'코드':<10} | {'제목':<22} | {'저자':<15} | {'출판사':<12} | {'장르'}")
        print("-" * 75)
        for b in self.books.values():
            print(f"{b.book_id:<10} | {b.title:<22} | {b.author:<15} | {b.publisher:<12} | {b.genre}")

    def search_books(self):
        """도서명 또는 저자 검색"""
        keyword = input("\n검색할 도서명 또는 저자 입력: ").strip().lower()
        if not keyword:
            print("검색어를 입력해주세요.")
            return
        results = [b for b in self.books.values() if keyword in b.title.lower() or keyword in b.author.lower()]

        print(f"\n--- [검색 결과: {len(results)}건] ---")
        if not results:
            print("일치하는 도서가 없습니다.")
            return
        for b in results:
            print(f"[{b.book_id}] {b.title} | {b.author} | {b.publisher} ({b.genre})")

    def update_book(self):
        """도서 정보 수정"""
        book_id = input("\n수정할 도서 식별번호 입력: ").strip()
        book = self.books.get(book_id)
        if not book:
            print("해당 도서를 찾을 수 없습니다.")
            return

        print(f"현재 제목 [{book.title}]")
        new_title = input("새 제목 (엔터 시 유지): ").strip()
        new_author = input(f"새 저자 [{book.author}]: ").strip()
        new_publisher = input(f"새 출판사 [{book.publisher}]: ").strip()
        new_genre = input(f"새 장르 [{book.genre}]: ").strip()

        if new_title: book.title = new_title
        if new_author: book.author = new_author
        if new_publisher: book.publisher = new_publisher
        if new_genre: book.genre = new_genre

        self.save_books()
        print("도서 정보가 성공적으로 수정되었습니다.")

    def delete_book(self):
        """도서 삭제"""
        book_id = input("\n삭제할 도서 식별번호 입력: ").strip()
        if book_id in self.books:
            del self.books[book_id]
            self.save_books()
            print("도서가 삭제되었습니다.")
        else:
            print("해당 도서를 찾을 수 없습니다.")