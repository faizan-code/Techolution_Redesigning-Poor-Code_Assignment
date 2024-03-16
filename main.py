from services.book_service import BookService
from services.user_service import UserService
from commands.add_book_command import AddBookCommand
from commands.list_books_command import ListBooksCommand
from commands.add_user_command import AddUserCommand
from commands.list_users_command import ListUsersCommand
from commands.update_book_command import UpdateBookCommand
from commands.delete_book_command import DeleteBookCommand
from commands.update_user_command import UpdateUserCommand
from commands.delete_user_command import DeleteUserCommand
from utils.logger import Logger


class LibraryManagementSystem:
    def __init__(self):
        self.logger = Logger()
        self.book_service = BookService()
        self.user_service = UserService()
        self.commands = {
            "1": AddBookCommand(self.book_service),
            "2": ListBooksCommand(self.book_service),
            "3": AddUserCommand(self.user_service),
            "4": ListUsersCommand(self.user_service),
            "5": UpdateBookCommand(self.book_service),
            "6": DeleteBookCommand(self.book_service),
            "7": UpdateUserCommand(self.user_service),
            "8": DeleteUserCommand(self.user_service),
        }

    def main_menu(self):
        print("\nLibrary Management System")
        print("1. Add Book - Add a new book to the library.")
        print("2. List All Books - Display a list of all books in the library.")
        print("3. Add User - Register a new user in the system.")
        print("4. List All Users - Show a list of all users registered in the system.")
        print("5. Update Book - Update details of an existing book.")
        print("6. Delete Book - Remove a book from the library.")
        print("7. Update User - Update details of an existing user.")
        print("8. Delete User - Remove a user from the system.")
        print("9. Exit - Close the application.")
        print("0. Help - Show information about how to use the system.")

    def show_help(self):
        print("\nHelp Guide:")
        print("0. Help: Show this help message.")
        print(
            "1. Add Book: Allows you to enter details for a new book to add to the library. Include title, author, and ISBN."
        )
        print(
            "2. List All Books: Displays every book currently in the library with title, author, ISBN, and availability status."
        )
        print(
            "3. Add User: Lets you register a new user in the system by providing a name and a unique user ID."
        )
        print("4. List All Users: Shows all users registered in the system.")
        print(
            "5. Update Book: Update the details (title, author) of an existing book by ISBN."
        )
        print("6. Delete Book: Remove an existing book from the library by ISBN.")
        print(
            "7. Update User: Update the details (name) of an existing user by user ID."
        )
        print("8. Delete User: Remove an existing user from the system by user ID.")
        print(
            "9. Exit: Closes the application. Make sure to complete all operations before exiting."
        )

    def run(self):
        while True:
            self.main_menu()
            choice = input("Enter your choice: ")

            if choice == "9":
                print("Exiting the Library Management System.")
                break
            elif choice == "0":
                self.show_help()
            elif choice in self.commands:
                try:
                    self.commands[choice].execute()
                except Exception as e:
                    self.logger.log(f"Error: {str(e)}", level="ERROR")
                    print(f"An error occurred: {str(e)}")
            else:
                print("Invalid choice. Please try again.")


if __name__ == "__main__":
    system = LibraryManagementSystem()
    system.run()
