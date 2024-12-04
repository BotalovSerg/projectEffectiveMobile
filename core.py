import json

from models import Book

FILE = "library.json"


class Library:
    def __init__(self) -> None:
        self.books = self.load_books()

    def load_books(self):
        try:
            with open(FILE, "r", encoding="utf-8") as file:
                return json.load(file)
        except FileNotFoundError:
            return []

    def get_books(self) -> list[Book]:
        return self.books

    def save_book(self, data: dict):
        to_data = data.copy()
        new_id = len(self.books) + 1
        to_data["id"] = new_id
        book = Book(**to_data)
        with open(FILE, "w", encoding="utf-8") as file:
            json.dump(book.to_dict(), file, indent=4, ensure_ascii=False)
