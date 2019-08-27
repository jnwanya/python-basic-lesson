from typing import List


class TooManyPageReadError(ValueError):
    pass


class BusinessLogicConflictError(Exception):
    def __init__(self, error_description: str, error: List[str]):
        super().__init__(error_description)
        self.errors = error


class Book:
    def __init__(self, name: str, page_count: int):
        self.name = name
        self.page_count = page_count
        self.pages_read = 0

    def __repr__(self):
        return f"<Book('{self.name}','{self.page_count})>"

    def read(self, pages: int):
        if self.pages_read + pages > self.page_count:
            raise TooManyPageReadError(f'You tried {self.pages_read + pages}, but there are only {self.page_count} pages')
        self.pages_read += pages
        print(f"You have now read {self.pages_read} out of {self.page_count} pages")


python101 = Book("Python101", 50)
try:
    python101.read(30)
    python101.read(55)
except TooManyPageReadError as e:
    print(e)
