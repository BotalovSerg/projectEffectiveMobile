from core import (
    Library,
    display_menu,
    in_add_book,
    delete_book_by_id,
    search_books,
    show_books_all,
)


def main():
    library = Library()
    while True:
        display_menu()
        choice = input("Выберите действие: ")

        if choice == "1":
            result = in_add_book(library)
            if result:
                print(f"{result}, добавлена.")
            else:
                print("Ошибка добавления книги.")

        elif choice == "2":
            print(delete_book_by_id(library))

        elif choice == "3":
            search_books(library)

        elif choice == "4":
            show_books_all(library)

        elif choice == "0":
            print("Выход из программы...")
            break

        else:
            print("Ошибка: Пожалуйста, выберите корректное действие.")


if __name__ == "__main__":
    main()
