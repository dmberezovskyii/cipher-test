# Cipher-test
`Cipher` test is a Python library for encrypting and decrypting passwords, designed for integration with automated testing frameworks such as Selenium, Appium, Playwright, and others. It ensures secure password storage and allows retrieving keys from remote vaults to decrypt configuration files.

## Features

- **Encryption and Decryption**: Encrypt and decrypt passwords using a Fernet key.
- **Key Management**: Support for loading, creating, saving, and deleting encryption keys from a local file.
- **Password Generation**: Generate secure, random passwords of a specified length.
- **Multiple Vault Types**: Currently supports a "local" vault type for file-based key storage.

## Requirements

- Python 3.10 +
- `cryptography` library for encryption/decryption functionality.

Install the required dependencies:

### Local Usage

1. Clone this repository:
   ```bash
   git clone <repository-url>
   ```
2. Install required dependencies:
   ```bash
   pip install poetry
   poetry shell
   poetry install
   ```
