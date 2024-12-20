BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]


class Book:
    """Класс, представляющий книгу."""

    def __init__(self, book_id, name, pages):
        """Инициализация книги с идентификатором, названием и количеством страниц."""
        self.id = book_id
        self.name = name
        self.pages = pages

    def __str__(self):
        """Возвращает строковое представление книги."""
        return f'Книга "{self.name}"'

    def __repr__(self):
        """Возвращает официальное строковое представление книги."""
        return f"Book(id={self.id}, name='{self.name}', pages={self.pages})"

if __name__ == '__main__':
    # инициализируем список книг
    list_books = [
        Book(book_id=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    for book in list_books:
        print(book)  # проверяем метод __str__

    print(list_books)  # проверяем метод __repr__
