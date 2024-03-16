# base_service.py


class BaseService:
    def __init__(self, storage):
        self.storage = storage

    def add(self, item):
        self.storage.add(item.to_dict())

    def find(self, **criteria):
        found_items = self.storage.find(**criteria)
        return [self.model_class(**item) for item in found_items]

    # def update(self, identifier, updated_data):
    #     self.storage.update(identifier, updated_data)

    def update(self, identifier, updated_data, identifier_key="id"):
        # Passes identifier_key to the storage's update method
        self.storage.update(identifier, updated_data, identifier_key)

    def delete(self, identifier):
        self.storage.delete(identifier)
