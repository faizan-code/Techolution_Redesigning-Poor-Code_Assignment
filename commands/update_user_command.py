from commands.command_interface import CommandInterface
from utils.validators import is_non_empty_string


class UpdateUserCommand(CommandInterface):
    def __init__(self, user_service):
        self.user_service = user_service

    def execute(self):
        user_id = input("Enter the user ID to update: ")
        new_name = input(
            "Enter the new name of the user (leave blank to keep current): "
        )

        update_data = {}
        if is_non_empty_string(new_name):
            update_data["name"] = new_name

        if update_data:
            self.user_service.update(user_id, update_data)
            print("User updated successfully.")
        else:
            print("No updates provided.")
