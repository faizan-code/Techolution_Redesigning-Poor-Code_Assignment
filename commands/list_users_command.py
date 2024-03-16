from commands.command_interface import CommandInterface


class ListUsersCommand(CommandInterface):
    def __init__(self, user_service):
        self.user_service = user_service

    def execute(self):
        users = self.user_service.list_all_users()
        if users:
            for user in users:
                print(user)
        else:
            print("No users found.")
