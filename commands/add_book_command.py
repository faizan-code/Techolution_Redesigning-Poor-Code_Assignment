from commands.command_interface import CommandInterface
from utils.validators import is_valid_isbn, is_non_empty_string


class AddBookCommand(CommandInterface):
    def __init__(self, book_service):
        self.book_service = book_service

    def execute(self):
        title = input("Enter book title: ")
        author = input("Enter author name: ")
        isbn = input("Enter ISBN: ")
        if (
            is_non_empty_string(title)
            and is_non_empty_string(author)
            and is_valid_isbn(isbn)
        ):
            self.book_service.add_book(title, author, isbn)
            print("Book added successfully.")
        else:
            print("Invalid input. Please try again.")
