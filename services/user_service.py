# user_service.py
from models.user import User
from storage.json_storage import JSONStorage
from services.base_service import BaseService


class UserService(BaseService):
    def __init__(self, storage_path="users.json"):
        storage = JSONStorage(storage_path)
        super().__init__(storage)
        self.model_class = User

    def add_user(self, name, user_id):
        new_user = User(name=name, user_id=user_id)
        self.add(new_user)

    # In UserService:

    def find_users(self, **criteria):
        return self.find(**criteria)

    def list_all_users(self):
        return self.find()

    # Assuming BaseService.find method or similar is used to retrieve users
    def reconstruct_user(self, user_data):
        # Exclude 'checked_out_books' during instantiation
        user = User(name=user_data["name"], user_id=user_data["user_id"])
        # Handle 'checked_out_books' separately, if necessary
        # This step might involve fetching Book objects by ISBN and adding them to the user
        return user

    # In UserService:

    def delete(self, user_id):
        super().delete(user_id, identifier_key="user_id")

    def update(self, user_id, updated_data):
        super().update(user_id, updated_data, identifier_key="user_id")

    # The add, find, update, and delete operations are inherited from BaseService.
