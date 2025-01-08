from typing import Optional

import hvac
import requests
from storage.base_provider import IProvider
import logging


class VaultStorage(IProvider):
    """
    Interacts with HashiCorp Vault to retrieve secrets.
    """

    def __init__(self, vault_url: str, secret_path: str, vault_token: str):
        """
        Initializes Vault client with URL, secret path, and token.

        :parameters:
        vault_url (str): The URL of the Vault server.
        secret_path (str): The path where the secret is stored in Vault.
        vault_token (str): The token used for authentication with Vault.
        """
        self.client = hvac.Client(url=vault_url)
        self.secret_path = secret_path
        self.client.token = vault_token
        self.vault_url = vault_url

    def _request_secret(self, version: int = None) -> dict:
        """
        Helper method to send a request to Vault to retrieve the secret.

        :param version: The version of the secret to retrieve.
        :return: The secret data in JSON format.
        """
        secret_url = f"{self.vault_url}/v1/{self.secret_path}"
        if version:
            secret_url = f"{secret_url}?version={version}"

        headers = {"X-Vault-Token": self.client.token}

        try:
            response = requests.get(secret_url, headers=headers, verify=False)

            # Raise an exception for non-2xx responses
            response.raise_for_status()

            return response.json()
        except requests.exceptions.RequestException as e:
            logging.error(f"Error retrieving secret from Vault: {str(e)}")
            raise ValueError(f"Error retrieving secret from Vault: {str(e)}")

    def get_key(self, get_key: bool = False, version: Optional[int] = 1) -> dict:
        """
        Retrieves the secret from Vault at the given path.

        :param version: version of the key
        :param get_key: If True, returns only the data dictionary.
        :return: The secret data.
        """
        try:
            response = self.client.secrets.kv.v2.read_secret_version(
                path=self.secret_path, version=version, raise_on_deleted_version=True
            )

            if response and "data" in response:
                return response["data"]["data"] if get_key else response

            raise ValueError("Secret not found.")
        except Exception as e:
            logging.error(f"Error retrieving secret: {str(e)}")
            raise ValueError(f"Error retrieving secret: {str(e)}")

    def get_custom_key(self, version: int = None, get_key: bool = False) -> dict:
        """
        Retrieves the secret from Vault at the given path with optional version.

        :param version: The version of the secret to retrieve.
        :param get_key: If True, returns only the data dictionary.
        :return: The secret data.
        """
        try:
            secret_data = self._request_secret(version)

            if get_key:
                return secret_data.get("data", {}).get("data")

            return secret_data
        except Exception as e:
            logging.error(f"Error retrieving custom secret: {str(e)}")
            raise ValueError(f"Error retrieving secret from Vault: {str(e)}")

    def create_key(self, key: dict) -> dict:
        """
        Stores a new secret (key) in Vault at the given path.

        :param key: The key (secret) to store in Vault (in the form of a dictionary).
        :return: The response from Vault after storing the key.
        """
        try:
            # Prepare the payload for storing the secret
            data = {"data": key}

            # Using Vault (KV v2)
            response = self.client.secrets.kv.v2.create_or_update_secret(
                path=self.secret_path, secret=data
            )

            if response and "data" in response:
                logging.info(f"Secret stored successfully at {self.secret_path}")
                return response["data"]
            else:
                raise ValueError("Failed to store secret.")
        except Exception as e:
            logging.error(f"Error storing secret in Vault: {str(e)}")
            raise ValueError(f"Error storing secret in Vault: {str(e)}")
