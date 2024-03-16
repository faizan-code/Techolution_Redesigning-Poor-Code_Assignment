"""

As the documenation says The Book class should include properties such as title, author, ISBN, and availability status. 
It should also include methods for updating these properties

"""


class Book:
    def __init__(self, title, author, isbn, available=True):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = available

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if not value:
            raise ValueError("Title cannot be empty.")
        self._title = value

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        if not value:
            raise ValueError("Author cannot be empty.")
        self._author = value

    @property
    def isbn(self):
        return self._isbn

    @isbn.setter
    def isbn(self, value):
        if not value:
            raise ValueError("ISBN cannot be empty.")
        self._isbn = value

    @property
    def available(self):
        return self._available

    @available.setter
    def available(self, value):
        if not isinstance(value, bool):
            raise ValueError("Availability must be a boolean.")
        self._available = value

    def to_dict(self):
        return {
            "title": self.title,
            "author": self.author,
            "isbn": self.isbn,
            "available": self.available,
        }

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}, Available: {'Yes' if self.available else 'No'}"
