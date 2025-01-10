import pathlib
import click
from core.cipher import Cipher


@click.command()
@click.option(
    '--base-path',
    default=pathlib.Path(__file__).resolve().parent.parent / "config",
    type=pathlib.Path,
    help="The directory where the key file will be stored."
)
def quick_start(base_path):
    # Instantiate Cipher with the specified base_path
    cipher = Cipher(vault_type="local", base_path=base_path)

    # Ensure the base path directory exists
    base_path.mkdir(parents=True, exist_ok=True)

    # Create the key
    key = cipher.create_key()

    click.echo(f"Created key.properties at {base_path} with the key {key}")