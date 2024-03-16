from commands.command_interface import CommandInterface
from utils.validators import is_non_empty_string


class AddUserCommand(CommandInterface):
    def __init__(self, user_service):
        self.user_service = user_service

    def execute(self):
        name = input("Enter user name: ")
        user_id = input("Enter user ID: ")
        if is_non_empty_string(name) and is_non_empty_string(user_id):
            self.user_service.add_user(name, user_id)
            print("User added successfully.")
        else:
            print("Invalid input. Please try again.")
