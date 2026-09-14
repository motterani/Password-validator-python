"""Password validation orchestration."""

from dataclasses import dataclass

from .rules import (
    MIN_LENGTH,
    has_lowercase,
    has_minimum_length,
    has_number,
    has_special_character,
    has_uppercase,
    is_common_password,
)


@dataclass(frozen=True)
class ValidationResult:
    """Consolidated result returned by the password validator."""

    is_valid: bool
    errors: list[str]


def validate_password(password: str) -> ValidationResult:
    """Validate a candidate password against the project's current policy."""
    if not isinstance(password, str):
        raise TypeError("A senha precisa ser uma string.")

    if not password:
        return ValidationResult(False, ["A senha não pode estar vazia."])

    errors: list[str] = []

    if not has_minimum_length(password):
        errors.append(f"A senha deve possuir pelo menos {MIN_LENGTH} caracteres.")
    if not has_uppercase(password):
        errors.append("A senha deve possuir pelo menos uma letra maiúscula.")
    if not has_lowercase(password):
        errors.append("A senha deve possuir pelo menos uma letra minúscula.")
    if not has_number(password):
        errors.append("A senha deve possuir pelo menos um número.")
    if not has_special_character(password):
        errors.append("A senha deve possuir pelo menos um caractere especial.")
    if is_common_password(password):
        errors.append("A senha é muito comum.")

    return ValidationResult(is_valid=not errors, errors=errors)
