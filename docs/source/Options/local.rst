Quick Start with Local Storage
==============================

1. Initialize the library:

   .. code:: python

      cip = Cipher(vault_type="local")

2. Generate a new encryption key to encrypt and decrypt passwords or other data:

   .. code:: python

      key = cip.create_key()

   If the key has already been saved, you don't need to regenerate it. To retrieve the key, use:

   .. code:: python

      key = cip.load_key()

3. Save the key to a file `key.properties`:

   .. code:: python

      cip.save_key(key)

4. Encrypt passwords and data:

   .. code:: python

      e_password = cip.encrypt("seccure password")

5. Decrypt the password:

   .. code:: python

      e_decrypt = cip.decrypt(b'gAAAAABngEQFmQDVnv_70wulu1lv5NwokxT-bi8XcizL1xH9oBiG-sqIWKV_RNubaQpF4z94Hbo5sSmSkH-W0YQDLN8w2cFKYw==')
