# Библиотечная Программа на Python

## Описание

Эта программа позволяет управлять библиотекой, добавляя, удаляя и обновляя книги, также доступен поиск книг по названию книги, автору и году издания.

### Команда для запуска

```
python3 main.py
```

## Функционал

В программе доступны следующие функции:

### Класс Library

Класс Library обеспечивает функциональность для управления библиотекой:

1. Загрузка базы данных: Загружает данные о книгах из файла library.json. Если файл не существует, создаёт файл с начальной структурой.
2. Добавление книги: Добавляет новую книгу с автоматически присвоенным ID.
3. Удаление книги: Удаляет книгу по ID из библиотеки.
4. Поиск книг: Позволяет искать книги по названию, автору и году издания.
5. Обновление книги: Изменяет статус книги (например, "в наличии" или "выдана").
6. Сохранение данных: Сохраняет обновленную базу данных в файл library.json.

### Функции управления библиотекой

1. load_database: Загружает книги из файла.
2. add_book: Добавляет новую книгу и сохраняет изменения.
3. delete_book: Удаляет книгу по заданному идентификатору.
4. search_book: Поиск книг по различным параметрам.
5. update_book: Обновляет статус книги.
6. save_books: Сохраняет изменения в файле.

## Класс Book

представляет книгу с атрибутами, необходимыми для управления библиотекой.

Атрибуты:

1. id: Уникальный идентификатор книги.
2. title: Название книги.
3. author: Автор книги.
4. year: Год издания книги.
5. status: Статус книги (по умолчанию "в наличии").

Методы:

1. to_dict: Преобразует объект книги в словарь.
2. **repr**: Возвращает строковое представление книги.

## Примеры использования

После запуска программы следуйте инструкциям на экране. Выбирайте нужное действие, вводите данные по запросу, и программа выполнит необходимые операции.
