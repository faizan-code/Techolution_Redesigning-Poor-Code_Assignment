from commands.command_interface import CommandInterface


class DeleteUserCommand(CommandInterface):
    def __init__(self, user_service):
        self.user_service = user_service

    def execute(self):
        user_id = input("Enter the user ID of the user to delete: ")
        self.user_service.delete(user_id)
        print("User deleted successfully if it existed.")
