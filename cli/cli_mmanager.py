import click
from core.cipher import Cipher

cipher = Cipher(vault_type="local")


@click.command()
def quick_start():
    base_path = cipher.base_path
    base_path.mkdir(parents=True, exist_ok=True)
    key = cipher.create_key()

    click.echo(f"Created key.properties at {base_path} with the key {key}")