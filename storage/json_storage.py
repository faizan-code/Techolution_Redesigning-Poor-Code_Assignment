import json
from storage.storage_interface import StorageInterface


class JSONStorage(StorageInterface):
    def __init__(self, file_name):
        self.file_name = file_name

    def _load_data(self):
        try:
            with open(self.file_name, "r") as file:
                return json.load(file)
        except FileNotFoundError:
            return []

    def _save_data(self, data):
        with open(self.file_name, "w") as file:
            json.dump(data, file, indent=4)

    def add(self, item):
        data = self._load_data()
        data.append(item)
        self._save_data(data)

    # def update(self, identifier, updated_data, identifier_key="isbn"):
    #     data = self._load_data()
    #     for i, item in enumerate(data):
    #         if item.get(identifier_key) == identifier:
    #             data[i].update(updated_data)
    #             break
    #     self._save_data(data)

    def update(self, identifier, updated_data, identifier_key="isbn"):
        data = self._load_data()
        updated = False
        for item in data:
            if item.get(identifier_key) == identifier:
                item.update(updated_data)
                updated = True
                break
        if updated:
            self._save_data(data)

    def delete(self, identifier, identifier_key="isbn"):
        data = self._load_data()
        data = [item for item in data if item.get(identifier_key) != identifier]
        self._save_data(data)

    def find(self, **criteria):
        data = self._load_data()
        return [
            item for item in data if all(item.get(k) == v for k, v in criteria.items())
        ]
