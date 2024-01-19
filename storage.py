"""
storage.py.

This module stores request data.
"""
from typing import Any, Optional


class ResultStorage:
    """ResultStorage class.
 
    ResultStorage class provides methods for basic
    CRUD operations on a dictionary-based result storage.
    """

    def __init__(self):
        """Initialize an empty dictionary to store results."""
        self.results = {}

    def create_result(self, key: str, value: Any):
        """
        Create a new result in the storage.

        Parameters:
            key: The key for the result.
            value: The value associated with the key.
        """
        self.results[key] = value

    def read_result(self, key: str) -> Optional[Any]:
        """
        Read the result associated with the given key.

        Parameters:
            key: The key for the result.

        Returns:
            The value associated with the key,
            or None if the key does not exist.
        """
        return self.results.get(key)

    def update_result(self, key: str, new_value: Any):
        """
        Update the result associated with the given key.

        Parameters:
            key: The key for the result.
            new_value: The new value to be associated with the key.
        """
        if key in self.results:
            self.results[key] = new_value
        else:
            print(f"Result with key '{key}' does not exist.")

    def delete_result(self, key: str):
        """
        Delete the result associated with the given key.

        Parameters:
            key: The key for the result.
        """
        if key in self.results:
            del self.results[key]
        else:
            print(f"Result with key '{key}' does not exist.")
