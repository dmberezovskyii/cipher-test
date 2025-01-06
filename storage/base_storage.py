from abc import ABC, abstractmethod


class IStorageManager(ABC):
    @abstractmethod
    def get_key(self) -> bytes:
        pass

    @abstractmethod
    def store_key(self, key: bytes):
        pass
