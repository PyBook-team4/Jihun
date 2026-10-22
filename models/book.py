# models/book.py

class Book:
    """도서 서지 정보 데이터 모델"""
    def __init__(self, book_id, title, author, publisher, genre="일반"):
        self.book_id = str(book_id)
        self.title = title
        self.author = author
        self.publisher = publisher
        self.genre = genre

    def to_dict(self):
        """JSON 저장용 딕셔너리 변환"""
        return {
            "book_id": self.book_id,
            "title": self.title,
            "author": self.author,
            "publisher": self.publisher,
            "genre": self.genre
        }

    @classmethod
    def from_dict(cls, data):
        """JSON 로드용 팩토리 메서드"""
        return cls(
            data["book_id"],
            data["title"],
            data["author"],
            data["publisher"],
            data.get("genre", "일반")
        )