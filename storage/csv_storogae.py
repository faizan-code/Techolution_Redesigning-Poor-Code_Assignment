import csv
from storage.storage_interface import StorageInterface


class CSVStorage(StorageInterface):
    def __init__(self, file_name):
        self.file_name = file_name

    def _load_data(self):
        try:
            with open(self.file_name, mode="r", newline="") as file:
                return list(csv.DictReader(file))
        except FileNotFoundError:
            return []

    def _save_data(self, data):
        if data:
            with open(self.file_name, mode="w", newline="") as file:
                writer = csv.DictWriter(file, fieldnames=data[0].keys())
                writer.writeheader()
                writer.writerows(data)

    def add(self, item):
        data = self._load_data()
        data.append(item)
        self._save_data(data)

    def update(self, identifier, updated_data):
        data = self._load_data()
        for item in data:
            if item.get("identifier") == identifier:
                item.update(updated_data)
                break
        self._save_data(data)

    def delete(self, identifier):
        data = self._load_data()
        data = [item for item in data if item.get("identifier") != identifier]
        self._save_data(data)

    def find(self, **criteria):
        data = self._load_data()
        return [
            item for item in data if all(item.get(k) == v for k, v in criteria.items())
        ]
