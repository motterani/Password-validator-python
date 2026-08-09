"""Command-line interface for the password validator."""

from __future__ import annotations

import argparse
import getpass
import sys

from password_validator.validator import validate_password


def build_parser() -> argparse.ArgumentParser:
    """Build and return the CLI argument parser."""
    return argparse.ArgumentParser(
        prog="password-validator",
        description=(
            "Validador de senhas em Python. "
            "A senha é solicitada de forma oculta no terminal."
        ),
    )


def main() -> int:
    """Run the password validator CLI without exposing the password."""
    parser = build_parser()
    parser.parse_args()

    try:
        password = getpass.getpass("Digite a senha para validação: ")
    except (EOFError, KeyboardInterrupt):
        print("\nValidação cancelada.", file=sys.stderr)
        return 130

    result = validate_password(password)

    if result.is_valid:
        print("Senha válida.")
        return 0

    print("Senha inválida.")
    for error in result.errors:
        print(f"- {error}")

    return 1


if __name__ == "__main__":
    raise SystemExit(main())
