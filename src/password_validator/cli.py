"""Command-line interface for the password validator."""

import getpass

from .validator import validate_password


def main() -> int:
    """Run the interactive CLI and return a process-style status code."""
    try:
        password = getpass.getpass("Digite a senha para validação: ")
    except (KeyboardInterrupt, EOFError):
        print("\nOperação cancelada.")
        return 1

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
