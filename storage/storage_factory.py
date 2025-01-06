from typing import Type, Optional
from storage.base_storage import IStorage
from storage.aws_storage import AWSStorage
from storage.vault_storage import VaultStorage


class StorageFactory:
    """
    Factory to create storage manager instances based on a storage type.
    """

    @staticmethod
    def get_key(storage_type: str,  **kwargs) -> IStorage:
        """
        :param storage_type: The type of storage to create ('aws', 'local', 'vault').
        :param kwargs: Arguments to pass to the storage class constructor.
        :return: An instance of the corresponding storage class.
        """
        storage_classes: dict[str, Type[IStorage]] = {
            "local": LocalStorage,
            "aws": AWSStorage,
            "vault": VaultStorage,
            # Add more storage types as needed
        }

        if storage_type not in storage_classes:
            raise ValueError(f"Unsupported storage type: {storage_type}")

        # Get the corresponding storage class
        storage_class = storage_classes[storage_type]

        # Return an instance of the class, passing the provided kwargs to the constructor
        return storage_class(**kwargs)