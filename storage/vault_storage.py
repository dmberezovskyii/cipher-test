from storage.base_storage import IStorage


class VaultStorage(IStorage):
    def __init__(self, vault):
        self.vault = vault

    def get_key(self) -> bytes:
        return self.vault.get_secret(secret="CRYPTO_TOKEN").encode("utf-8")

    def store_key(self, key: bytes):
        raise NotImplementedError("Storing key in Vault is not supported.")
