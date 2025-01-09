Common Functions
======================

The `Cipher` class provides encryption, decryption, key management, and password generation functionalities. Below are the key functions in the `Cipher` class:


2. **`_load_key_from_vault`**
   Loads the encryption key from the vault.

   **Args**:
   - `key_version (int)`: The version of the key to load (optional).
   - `get_key (bool)`: Whether to retrieve the key. Defaults to `True`.

   **Returns**:
   - `bytes`: The encryption key loaded from the vault.

   **Raises**:
   - `ValueError`: If the key is not found in the vault.

3. **`_load_key`**
   Reads the encryption key from the key file.

   **Returns**:
   - `bytes`: The encryption key.

   **Raises**:
   - `FileNotFoundError`: If the key file does not exist.
   - `ValueError`: If the key file is empty.
   - `RuntimeError`: If there is any other issue reading the key.

4. **`create_key`**
   Generates, returns, and stores a new encryption key.

   **Returns**:
   - `bytes`: The newly generated encryption key.

5. **`save_key`**
   Saves the encryption key to the key file.

   **Args**:
   - `key (Optional[bytes])`: The key to save. If `None`, a new key is generated.

   **Returns**:
   - `bytes`: The saved encryption key.

6. **`delete_key`**
   Deletes the encryption key file.

   **Raises**:
   - `FileNotFoundError`: If the key file does not exist.

7. **`encrypt`**
   Encrypts a password using the `Fernet` encryption.

   **Args**:
   - `password (str)`: The password to encrypt.

   **Returns**:
   - `bytes`: The encrypted password.

   **Raises**:
   - `ValueError`: If the password is an empty string.

8. **`decrypt`**
   Decrypts an encrypted password.

   **Args**:
   - `encrypted_pass (bytes)`: The encrypted password.

   **Returns**:
   - `str`: The decrypted password.

   **Raises**:
   - `ValueError`: If the password is invalid or corrupted.

9. **`generate_password`**
   Generates a random password of the specified length.

   **Args**:
   - `length (int)`: The length of the generated password. Defaults to `12`.

   **Returns**:
   - `str`: The randomly generated password.

   **Raises**:
   - `ValueError`: If the length is non-positive.

Example usage of the `Cipher` class and methods:

```python
# Example of creating a Cipher instance
cipher = Cipher()

# Generate a random password
password = cipher.generate_password()

# Encrypt the password
encrypted_password = cipher.encrypt(password)

# Decrypt the password
decrypted_password = cipher.decrypt(encrypted_password)
