from core import Library


def main():
    library = Library()
    while True:
        print("1. Добавить книгу")
        print("2. Удалить книгу")
        print(
            "3. Найти книги"
        )  # : Пользователь может искать книги по title, author или year.
        print(
            "4. Показать все книги"
        )  # Приложение выводит список всех книг с их id, title, author, year и status.
        print(
            "5. Изменить статус книги"
        )  # Пользователь вводит id книги и новый статус (“в наличии” или “выдана”).
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
            library.add_book(data)
        if choice == "2":
            id_book = int(input("Ведите ID книги: "))
            text = library.delete_book(id_book=id_book)
            print(text)
        if choice == "3":
            fields_search = input("Для поиска книг, введите через запятую параметры поиска (title, author, year): ")
            result = library.search_book(fields_search)
            print("result ", result)
        if choice == "0":
            break


if __name__ == "__main__":
    main()
