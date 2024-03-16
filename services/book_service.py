# book_service.py
from models.book import Book
from storage.json_storage import JSONStorage
from services.base_service import BaseService


class BookService(BaseService):
    def __init__(self, storage_path="books.json"):
        storage = JSONStorage(storage_path)
        super().__init__(storage)
        self.model_class = Book

    def update_book_availability(self, isbn, available):
        books = self.find(isbn=isbn)
        for book in books:
            book.available = available
            self.update(book.isbn, book.to_dict())

    # In BookService:

    def find_books(self, **criteria):
        return self.find(**criteria)

    def list_all_books(self):
        # Utilizes the inherited find method from BaseService to get all books
        return (
            self.find()
        )  # This assumes find() returns all items if called without args

    def add_book(self, title, author, isbn, available=True):
        new_book = Book(title=title, author=author, isbn=isbn, available=available)
        self.add(new_book)

    def list_all_books(self):
        return self.find()

    def update(self, isbn, updated_data):
        """Updates book details based on the isbn."""
        super().update(isbn, updated_data, identifier_key="isbn")

    # The add, find, update, and delete operations are inherited from BaseService.
