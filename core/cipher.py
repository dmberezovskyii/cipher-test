import secrets
import string
import pathlib
from typing import Optional, Literal
from cryptography.fernet import Fernet, InvalidToken
import logging

from storage.storage_factory import StorageFactory


class Cipher:
    def __init__(
        self,
        base_path: pathlib.Path,
        key_file_name: str = "key.properties",
        vault_type: Literal["vault", "local"] = "vault",
        save_locally: bool = True,
        **kwargs,
    ):
        """
        the Cipher class with key management and password encryption/decryption .

         Args:
             base_path: The directory where the key file is located.
                         Defaults to the "config" directory adjacent to this script.
             key_file_name: The name of the key file. Defaults to "key.properties".
             vault_type: Determines the type of vault for storing keys.
                     Currently supports only "local" for file-based keys.

        """
        self.base_path = base_path
        self.key_file_path = self.base_path / key_file_name
        self.vault_type = vault_type

        self.save_locally = save_locally
        self.kwargs = kwargs

        if vault_type == "local":
            self.fernet = Fernet(self.load_key())
        else:
            self.storage_instance = StorageFactory.get_instance(vault_type, **kwargs)

    def _load_key_from_vault(self, key_version: int = None, get_key: bool = True):
        secret = self.storage_instance.get_key(get_key=get_key, version=key_version)
        key = secret.get("key")
        if not key:
            raise ValueError("The key 'key' was not found in the secret.")
        return key

    def load_key(self) -> bytes:
        """
        Read the encryption key from the key file.

        Returns:
            bytes: The encryption key.

        Raises:
            FileNotFoundError: If the key file does not exist.
            ValueError: If the key file is empty.
            RuntimeError: If there is any other issue reading the key.
        """

        try:
            if self.key_file_path.exists() and self.key_file_path.stat().st_size > 0:
                with open(self.key_file_path, "rb") as key_file:
                    key = key_file.read()
                    return key
            else:
                return self.create_key()
        except Exception as e:
            raise RuntimeError(f"An error occurred while loading the key: {e}")

    def create_key(self) -> bytes:
        """
        Generate, return and store a new encryption key.

        Returns:
            bytes: The newly generated encryption key.
        """
        self.base_path.mkdir(parents=True, exist_ok=True)
        key = Fernet.generate_key()
        with open(self.key_file_path, "wb") as key_file:
            key_file.write(key)

        return key

    def save_key(self, key: Optional[bytes] = None) -> bytes:
        """
        Save the encryption key to the key file.

        Args:
            key (Optional[bytes]): The key to save. If None, a new key is generated.

        Returns:
            bytes: The saved encryption key.
        """

        if self.key_file_path.exists():
            with open(self.key_file_path, "wb") as key_file:
                key_file.write(key)
                return key

    def delete_key(self):
        """
        Delete the encryption key file.

        Raises:
            FileNotFoundError: If the key file does not exist.
        """
        try:
            if self.key_file_path.exists():
                self.key_file_path.unlink()
                self.key_file_path.touch()
            else:
                raise FileNotFoundError(
                    f"Key file not found at {self.key_file_path}"
                )
        except Exception as e:
            logging.error(f"Failed to delete key: {e}")
            raise

    def encrypt(self, password: str) -> bytes:
        """
        Encrypt a password using the fernet key.

        Args:
            password (str): The password to encrypt.

        Returns:
            bytes: The encrypted password.

        Raises:
            ValueError: If the password is an empty string.
        """
        if not password:
            raise ValueError("Password must be a non-empty string.")
        return self.fernet.encrypt(password.encode("utf-8"))

    def decrypt(self, encrypted_pass: bytes) -> str:
        """
        Decrypt an encrypted password.

        Args:
            encrypted_pass (bytes): The encrypted password.

        Returns:
            str: The decrypted password.

        Raises:
            ValueError: If the password is invalid or corrupted.
        """
        try:
            return self.fernet.decrypt(encrypted_pass).decode("utf-8")
        except InvalidToken:
            raise ValueError("Invalid or corrupted encrypted password.")

    def generate_password(self, length: int = 12) -> str:
        """
        Generate a random password of a specified length.

        Args:
            length (int): The length of the generated password. Defaults to 12.

        Returns:
            str: A randomly generated password.

        Raises:
            ValueError: If the length is non-positive.
        """
        if length <= 0:
            raise ValueError("Password length must be a positive integer.")
        return "".join(
            secrets.choice(string.ascii_letters + string.digits)
            for _ in range(length)
        )