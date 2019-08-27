from typing import List


class Book:
    def __init__(self, name: str):
        self.name = name


class BookShelf:
    def __init__(self, books: List[Book]):
        self.books = books

    def __str__(self):
        return f"Bookshelf with {len(self.books)} books."


book1 = Book('Jones')
book2 = Book('Maline')

shelf = BookShelf([book1, book2])
print(shelf)
