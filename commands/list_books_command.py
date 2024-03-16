from commands.command_interface import CommandInterface


class ListBooksCommand(CommandInterface):
    def __init__(self, book_service):
        self.book_service = book_service

    def execute(self):
        books = self.book_service.list_all_books()
        if books:
            for book in books:
                print(
                    f"Title: {book.title}, Author: {book.author}, ISBN: {book.isbn}, Available: {'Yes' if book.available else 'No'}"
                )
        else:
            print("No books found.")
