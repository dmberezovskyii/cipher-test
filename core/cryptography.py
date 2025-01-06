from cryptography.fernet import Fernet, InvalidToken


class Cryptography:
    def __init__(self, key: bytes):
        self.fernet = Fernet(key)

    def encrypt_password(self, password: str) -> bytes:
        if not password:
            raise ValueError("Password must be a non-empty string.")
        return self.fernet.encrypt(password.encode("utf-8"))

    def decrypt_password(self, encrypted_pass: bytes) -> str:
        try:
            return self.fernet.decrypt(encrypted_pass).decode("utf-8")
        except InvalidToken:
            raise ValueError("Invalid or corrupted encrypted password.")
