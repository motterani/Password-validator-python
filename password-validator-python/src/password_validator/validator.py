"""Core password validation logic."""

from __future__ import annotations

from dataclasses import dataclass

from password_validator.rules import (
    MIN_LENGTH,
    has_digit,
    has_lowercase,
    has_minimum_length,
    has_special_character,
    has_uppercase,
    is_common_password,
)


@dataclass(frozen=True)
class PasswordValidationResult:
    """Represents the result of a password validation."""

    is_valid: bool
    errors: list[str]


def validate_password(password: str) -> PasswordValidationResult:
    """Validate a password according to predefined security rules."""
    errors: list[str] = []

    if not isinstance(password, str):
        raise TypeError("Password must be a string.")

    if not password:
        errors.append("A senha não pode estar vazia.")
        return PasswordValidationResult(is_valid=False, errors=errors)

    if not has_minimum_length(password, MIN_LENGTH):
        errors.append(f"A senha deve ter pelo menos {MIN_LENGTH} caracteres.")

    if not has_uppercase(password):
        errors.append("A senha deve conter pelo menos uma letra maiúscula.")

    if not has_lowercase(password):
        errors.append("A senha deve conter pelo menos uma letra minúscula.")

    if not has_digit(password):
        errors.append("A senha deve conter pelo menos um número.")

    if not has_special_character(password):
        errors.append("A senha deve conter pelo menos um caractere especial.")

    if is_common_password(password):
        errors.append("A senha é muito comum e não deve ser utilizada.")

    return PasswordValidationResult(is_valid=len(errors) == 0, errors=errors)
