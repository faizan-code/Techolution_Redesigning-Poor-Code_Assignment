from abc import ABC, abstractmethod


class StorageInterface(ABC):
    @abstractmethod
    def add(self, item):
        """
        Adds a new record to the storage.
        :param item: The item to add, expected to be a dictionary.
        """
        pass

    @abstractmethod
    def update(self, identifier, updated_data, identifier_key="isbn"):
        """Updates an existing record in the storage.
        :param identifier: A unique identifier for the record to update.
        :param updated_data: The updated data as a dictionary.
        :param identifier_key: The key used to identify the item (default "isbn").
        """
        pass

    @abstractmethod
    def delete(self, identifier, identifier_key="isbn"):
        """Deletes a record from the storage.
        :param identifier: A unique identifier for the record to delete.
        :param identifier_key: The key used to identify the item (default "isbn").
        """
        pass

    @abstractmethod
    def find(self, **criteria):
        """Finds records in the storage matching the given criteria.
        :param criteria: Key-value pairs to match against records.
        :return: A list of matching records.
        """
        pass
