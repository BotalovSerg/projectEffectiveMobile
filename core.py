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
        self.__last_id = self.__get_last_id()

    def load_database(self) -> dict:
        try:
            with open(self.FILE, "r", encoding="utf-8") as file:
                return json.load(file)
        except FileNotFoundError as e:
            raise Exception(f"{e}")

    def __get_last_id(self) -> int:
        if self.books["library"]:
            return max(book["id"] for book in self.books["library"])
        return 0

    def get_books(self) -> list[dict]:
        return self.books["library"]

    def add_book(self, data: dict) -> Book:
        to_data = data.copy()
        self.__last_id += 1
        to_data["id"] = self.__last_id
        book = Book(**to_data)
        self.books["library"].append(book.to_dict())
        self.save_books()
        return book

    def delete_book(self, id_book: int) -> str:
        for indx, book in enumerate(self.books["library"]):
            if book["id"] == id_book:
                self.books["library"].pop(indx)
                self.save_books()
                return f"Книга с ID {id_book}, удалена."
        else:
            return f"Книга с ID {id_book}, нет."

    def search_book(self, fields_search: str) -> list[dict] | None:
        books = []
        if fields_search:
            fields = fields_search.split(", ")
            for book in self.books["library"]:
                if (
                    book["title"] in fields
                    or book["author"] in fields
                    or book["year"] in fields
                ):
                    books.append(book)
            return books
        return None

    def save_books(self) -> None:
        with open(self.FILE, "w", encoding="utf-8") as file:
            json.dump(self.books, file, indent=4, ensure_ascii=False)


def display_menu() -> None:
    print("1. Добавить книгу")
    print("2. Удалить книгу")
    print("3. Найти книги")
    print("4. Показать все книги")
    print(
        "5. Изменить статус книги"
    )  # Пользователь вводит id книги и новый статус (“в наличии” или “выдана”).
    print("0. Выход")


def in_add_book(library: Library) -> Book:
    title = input("Введите название книги: ")
    author = input("Введите автора книги: ")
    year = input("Год издания книги: ")
    data = {
        "title": title,
        "author": author,
        "year": year,
    }
    book = library.add_book(data)
    return book


def delete_book_by_id(library: Library) -> str:
    try:
        id_book = int(input("Ведите ID книги: "))
        text = library.delete_book(id_book=id_book)
    except ValueError as e:
        return f"Ошибка: ID должен быть числом. {e}"
    return text


def print_books(list_books: list[dict]) -> None:
    for book in list_books:
        print(
            f"ID: {book['id']}. Название: {book['title']}.\n"
            f"Статус: {book['status']}, автор: {book['author']}, год издания: {book['year']}\n"
        )
        print("-" * 10, end="\n\n")


def search_books(library: Library) -> None:
    fields_search = input(
        "Для поиска книг, введите через запятую параметры поиска (title, author, year): "
    )
    result = library.search_book(fields_search)
    if result:
        print("\nРезультаты поиска:\n")
        print_books(result)
    else:
        print("Таких книг нет.")


def show_books_all(library: Library) -> None:
    list_books = library.get_books()
    print("\nСписок всех книг:\n")
    print_books(list_books)
