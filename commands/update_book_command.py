from commands.command_interface import CommandInterface
from utils.validators import is_valid_isbn, is_non_empty_string


class UpdateBookCommand(CommandInterface):
    def __init__(self, book_service):
        self.book_service = book_service

    def execute(self):
        isbn = input("Enter ISBN of the book to update: ")
        if not is_valid_isbn(isbn):
            print("Invalid ISBN format.")
            return
        title = input("New title (leave blank to skip): ")
        author = input("New author (leave blank to skip): ")
        # Additional fields can be prompted here as needed

        update_data = {}
        if is_non_empty_string(title):
            update_data["title"] = title
        if is_non_empty_string(author):
            update_data["author"] = author
        # Handle additional fields similarly

        if update_data:
            self.book_service.update(isbn, update_data)
            print("Book updated successfully.")
        else:
            print("No updates provided.")
