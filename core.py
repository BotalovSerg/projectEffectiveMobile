import os
import json

from models import Book


class Library:
    FILE = "library.json"

    def __init__(self) -> None:

        if not os.path.exists(self.FILE):
            initial_data = {"library": []}
            with open(self.FILE, "w", encoding="utf-8") as file:
                json.dump(initial_data, file, indent=4)

        self.books: dict[str, list] = self.load_database()
        print("books: ", self.books)

    def load_database(self) -> dict:
        try:
            with open(self.FILE, "r", encoding="utf-8") as file:
                return json.load(file)
        except FileNotFoundError as e:
            raise Exception(f"{e}")

    def get_books(self) -> list[Book]:
        return self.books

    def add_book(self, data: dict) -> None:
        to_data = data.copy()
        new_id = len(self.books["library"]) + 1
        to_data["id"] = new_id
        book = Book(**to_data)
        self.books["library"].append(book.to_dict())
        self.save_books()

    def delete_book(self, id_book: int):
        for indx, book in enumerate(self.books["library"]):
            if book["id"] == id_book:
                self.books["library"].pop(indx)
                self.save_books()
                break
        else:
            raise KeyError(f"There is no book with this id: {id_book!r}")

    def save_books(self) -> None:
        with open(self.FILE, "w", encoding="utf-8") as file:
            json.dump(self.books, file, indent=4, ensure_ascii=False)
