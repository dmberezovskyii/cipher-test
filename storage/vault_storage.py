import logging
from typing import Optional, Dict
import hvac
from storage.base_provider import IProvider


class VaultStorage(IProvider):
    """
    Interacts with HashiCorp Vault to retrieve secrets.
    """

    def __init__(self, vault_url: str, secret_path: str, vault_token: str):
        """
        Initializes Vault client with URL, secret path, and token.

        :param vault_url: The URL of the Vault server.
        :param secret_path: The path where the secret is stored in Vault.
        :param vault_token: The token used for authentication with Vault.
        """
        self.client = hvac.Client(url=vault_url, token=vault_token)
        self.secret_path = secret_path
        logging.info("VaultStorage initialized with URL: %s and path: %s", vault_url, secret_path)

    def _retrieve_secret(self, version: Optional[int] = None) -> Dict:
        """
        Helper method to retrieve a secret from Vault, optionally using a specific version.

        :param version: The version of the secret to retrieve.
        :return: The secret data.
        """
        try:
            response = self.client.secrets.kv.v2.read_secret_version(
                path=self.secret_path, version=version
            )
            return response.get('data', {}).get('data', {})
        except Exception as e:
            logging.error("Error retrieving secret: %s", str(e))
            raise ValueError("Error retrieving secret.")

    def get_key(self, get_key: bool = False, version: Optional[int] = 1) -> Dict:
        """
        Retrieves the secret from Vault at the given path.

        :param version: The version of the key.
        :param get_key: If True, returns only the data dictionary.
        :return: The secret data.
        """
        secret_data = self._retrieve_secret(version)
        return secret_data if get_key else {'data': secret_data}

    def get_custom_key(self, version: Optional[int] = None, get_key: bool = False) -> Dict:
        """
        Retrieves the secret from Vault at the given path with optional version.

        :param version: The version of the secret to retrieve.
        :param get_key: If True, returns only the data dictionary.
        :return: The secret data.
        """
        return self.get_key(get_key=get_key, version=version)

    def create_key(self, key: Dict) -> Dict:
        """
        Stores a new secret (key) in Vault at the given path.

        :param key: The key (secret) to store in Vault (in the form of a dictionary).
        :return: The response from Vault after storing the key.
        """
        try:
            data = {'data': key}
            response = self.client.secrets.kv.v2.create_or_update_secret(
                path=self.secret_path, secret=data
            )
            logging.info("Secret stored successfully at %s", self.secret_path)
            return response.get('data', {})
        except Exception as e:
            logging.error("Error storing secret in Vault: %s", str(e))
            raise ValueError("Error storing secret in Vault.")
