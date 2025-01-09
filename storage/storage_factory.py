from storage.vault_storage import VaultStorage
from storage.aws_storage import AWSStorage
from storage.base_provider import IProvider


class StorageFactory:
    """
    Factory to create storage manager instances based on a storage type.
    """

    @staticmethod
    def get_instance(storage_type: str, **kwargs) -> IProvider:
        """
        :param storage_type: The type of storage to create ('aws', 'vault', 'azure').
        :param kwargs: Arguments to pass to the storage class constructor.
        :return: An instance of the corresponding storage class.
        :raises ValueError: If the storage type is unsupported.
        """
        # Mapping of storage types to their classes
        storage_classes = {
            "aws": AWSStorage,
            "vault": VaultStorage
        }

        # Check if the storage type is valid
        if storage_type not in storage_classes:
            raise ValueError(f"Unsupported storage type: {storage_type}")

        storage_class = storage_classes[storage_type]

        return storage_class(**kwargs)
