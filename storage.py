from typing import Any, Optional

class ResultStorage:
    """
    ResultStorage class provides methods for basic
    CRUD operations on a dictionary-based result storage.
    """

    def __init__(self):
        """
        Initializes an empty dictionary to store results.
        """
        self.results = {}

    def create_result(self, key: str, value: Any):
        """
        Creates a new result in the storage.

        :param key: The key for the result.
        :param value: The value associated with the key.
        """
        self.results[key] = value

    def read_result(self, key: str) -> Optional[Any]:
        """
        Reads the result associated with the given key.

        :param key: The key for the result.

        :return: The value associated with the key, or None if the key does not exist.
        """
        return self.results.get(key)

    def update_result(self, key: str, new_value: Any):
        """
        Updates the result associated with the given key.

        :param key: The key for the result.
        :param new_value: The new value to be associated with the key.
        """
        if key in self.results:
            self.results[key] = new_value
        else:
            print(f"Result with key '{key}' does not exist.")

    def delete_result(self, key: str):
        """
        Deletes the result associated with the given key.

        :param key: The key for the result.
        """
        if key in self.results:
            del self.results[key]
        else:
            print(f"Result with key '{key}' does not exist.")
