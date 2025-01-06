from storage.base_storage import IStorageManager


class KeyManager:
    def __init__(self, storage_manager: IStorageManager):
        self.storage_manager = storage_manager

    def get_or_generate_key(self) -> bytes:
        try:
            return self.storage_manager.get_key()
        except FileNotFoundError:
            return self.generate_and_store_key()

    def generate_and_store_key(self) -> bytes:
        key = Fernet.generate_key()
        self.storage_manager.store_key(key)
        return key
