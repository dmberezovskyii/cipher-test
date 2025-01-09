Features
--------

1. **Key Management**
   - Load, create, save, and delete encryption keys.
   - Supports loading keys from a file or from a vault (e.g., a local vault).
   - Automatically generates a new key if the key file does not exist.

2. **Password Encryption and Decryption**
   - Encrypt passwords using the ``Fernet`` (cryptography) encryption method.
   - Decrypt passwords that were encrypted with the ``Fernet`` key.

3. **Password Generation**
   - Generates random passwords of a specified length.
   - Allows customization of the password length (default is 12 characters).
   - Supports alphanumeric characters for random password generation.

4. **Vault Support**
   - Supports loading keys from a remote vault if configured, using the ``StorageFactory`` class.
   - Currently supports ``local`` and ``HashiCorp Vault`` vault types, with the option to extend for additional vault implementations.
