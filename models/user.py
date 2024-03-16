class User:
    def __init__(self, name, user_id):
        self._name = name
        self._user_id = user_id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not value:
            raise ValueError("Name cannot be empty.")
        self._name = value

    @property
    def user_id(self):
        return self._user_id

    def to_dict(self):
        return {
            "name": self._name,
            "user_id": self._user_id,
        }

    def __str__(self):
        return f"User: {self._name}, ID: {self._user_id}"
