from storage.base_storage import IStorageManager


class VaultStorage(IStorageManager):
    def __init__(self, vault_client):
        self.vault_client = vault_client

    def get_key(self) -> bytes:
        vault_key = self.vault_client.get_secret(
            secret="TOKEN",  # noqa # nosec
        )
        return vault_key.encode("utf-8")

    def store_key(self, key: bytes):
        raise NotImplementedError("Vault storage does not support storing keys directly.")
