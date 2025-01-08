from abc import ABC, abstractmethod
from typing import Optional


class IProvider(ABC):
    """
    Interface for storage managers. Implementations must provide methods to
    get and store keys.
    """

    @abstractmethod
    def get_key(self, get_key: bool = False, version: Optional[int] = 1) -> dict:
        """
        Retrieves a secret or key from the storage.

        :param version: key version
        :param get_key: If True, only returns the data dictionary.
        :return: The secret or key data.
        """
        pass

    @abstractmethod
    def create_key(self, key: dict) -> dict:
        """
        Stores a new key (secret) in the storage system.

        :param key: The key (secret) to store.
        :return: The response after storing the secret.
        """
        pass
