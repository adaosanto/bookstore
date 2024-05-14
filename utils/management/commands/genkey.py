import os
from getpass import getuser

import gnupg
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Gpg gen key"

    def get_gnupghome(self):
        user = getuser()
        return f"/home/{user}/.gnupg"

    def add_arguments(self, parser):
        parser.add_argument(
            "-p",
            "--password",
            type=str,
            default=os.environ.get("GEN_KEY_ENCRYPT_BACKUP_PASSWORD"),
        )
        parser.add_argument(
            "--email", type=str, default=os.environ.get("GEN_KEY_ENCRYPT_BACKUP_EMAIL")
        )
        parser.add_argument(
            "--name", type=str, default=os.environ.get("GEN_KEY_ENCRYPT_BACKUP_NAME")
        )
        parser.add_argument("--gnupghome", type=str, default=self.get_gnupghome())
        parser.add_argument("--no-verify-exists", action="store_true")
        parser.add_argument("--no-output-env", action="store_true")

    def handle(self, *args, **options):
        gpg = gnupg.GPG(gnupghome=options["gnupghome"])
        key_str = None

        if not options["no_verify_exists"]:
            keys = gpg.list_keys()
            for key in keys:
                if options["email"] in str(key["uids"]):
                    key_str = key["fingerprint"]

        if not key_str:
            input_data = gpg.gen_key_input(
                name_real=options["name"],
                name_email=options["email"],
                passphrase=options["password"],
            )
            key = gpg.gen_key(input_data)
            key_str = str(key)

        if not options["no_output_env"]:
            with open(".env", "a") as file:
                file.write(f"\nDBBACKUP_GPG_RECIPIENT={key_str}\n")

            return

        return key_str
