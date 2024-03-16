from commands.command_interface import CommandInterface


class DeleteBookCommand(CommandInterface):
    def __init__(self, book_service):
        self.book_service = book_service

    def execute(self):
        isbn = input("Enter ISBN of the book to delete: ")
        self.book_service.delete(isbn)
        print("Book deleted successfully if it existed.")
