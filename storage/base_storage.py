from abc import ABC, abstractmethod


class IStorage(ABC):
    """
    Interface for storage managers. Implementations must provide methods to
    get and store keys.
    """

    @abstractmethod
    def get_key(self) -> bytes:
        """Retrieve a key from the storage."""
        pass

    @abstractmethod
    def store_key(self, key: bytes):
        """Store a key in the storage."""
        pass
