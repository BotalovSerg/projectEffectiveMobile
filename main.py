from core import Library


def main():
    library = Library()
    while True:
        print("1. Добавить книгу")
        print("2. Удалить книгу")
        print("3. Найти книги")
        print("4. Показать все книги")
        print("5. Изменить статус книги")
        print("0. Выход")
        choice = input("Выберите действие: ")
        if choice == "1":
            title = input("Введите название книги: ")
            author = input("Введите автора книги: ")
            year = input("Год издания книги: ")
            data = {
                "title": title,
                "author": author,
                "year": year,
            }
            library.save_book(data)


if __name__ == "__main__":
    main()
