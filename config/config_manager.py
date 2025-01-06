import pathlib
from typing import Literal

from core.cryptography import Cryptography
from core.key_manager import KeyManager
from storage.base_storage import IStorageManager


class ConfigManager:
    def __init__(
        self,
        store_key: Literal["vault", "file", "file_vault"],
        vault_client=None,
        key_file_path=None
    ):
        self.store_key = store_key
        self.vault_client = vault_client
        self.key_file_path = key_file_path or (
            pathlib.Path(__file__).resolve().parent.parent / "config" / "data" / "key.properties"
        )

    def initialize_crypto_manager(self) -> Cryptography:
        storage_manager = self._create_storage_manager()
        key_manager = KeyManager(storage_manager)
        key = key_manager.get_or_generate_key()
        return Cryptography(key)

    def _create_storage_manager(self) -> IStorageManager:
        if self.store_key == "vault":
            return VaultStorageManager(self.vault_client)
        elif self.store_key in {"file", "file_vault"}:
            return FileStorageManager(self.key_file_path)
        else:
            raise ValueError("Invalid key storage option.")
