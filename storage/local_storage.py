import pathlib

from storage.base_storage import IStorageManager


class LocalStorage(IStorageManager):
    def __init__(self, key_file_path: pathlib.Path):
        self.key_file_path = key_file_path

    def get_key(self) -> bytes:
        if self.key_file_path.exists() and self.key_file_path.stat().st_size > 0:
            with open(self.key_file_path, "rb") as key_file:
                return key_file.read()
        else:
            raise FileNotFoundError("Key file not found or is empty.")

    def store_key(self, key: bytes):
        with open(self.key_file_path, "wb") as key_file:
            key_file.write(key)
