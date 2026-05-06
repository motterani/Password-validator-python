"""Command-line interface for the password validator."""

from __future__ import annotations

import argparse

from password_validator.validator import validate_password


def build_parser() -> argparse.ArgumentParser:
    """Build and return the CLI argument parser."""
    parser = argparse.ArgumentParser(
        prog="password-validator",
        description="Validador de senhas em Python.",
    )
    parser.add_argument(
        "password",
        nargs="?",
        help="Senha a ser validada. Se omitida, será solicitada no terminal.",
    )
    return parser


def main() -> int:
    """Run the password validator CLI."""
    parser = build_parser()
    args = parser.parse_args()

    password = args.password or input("Digite a senha para validação: ")
    result = validate_password(password)

    print(f"\nSenha informada: {password}\n")

    if result.is_valid:
        print("Senha válida.")
        return 0

    print("Senha inválida.")
    for error in result.errors:
        print(f"- {error}")

    return 1


if __name__ == "__main__":
    raise SystemExit(main())