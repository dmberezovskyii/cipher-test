Examples
========

Remote usage: Loading key from remote vault (HashiCorp Vault) and Saving Key to local:
--------------------------------------------------------------------------------------

.. code-block:: python

    vault_config = {
        "vault_url": "your-vault-url",
        "secret_path": "aqa/data/stage/cipher",
        "vault_token": "your secret",
    }

    cip = Cipher(vault_type="vault", save_locally=True, **vault_config)
    key = cip._load_key_from_vault()
    print(key)
    cip._save_key(key=key)

Local usage: Generating key and saving Key to local `key.properties`:
---------------------------------------------------------------------

.. code-block:: python

    base_path = pathlib.Path(__file__).resolve().parent.parent / "config"
    cip = Cipher(vault_type="local", base_path=base_path)
    key = cip.load_key()
    cip.save_key(key=key)
