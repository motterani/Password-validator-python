"""Password validation rules."""

from __future__ import annotations

import string

MIN_LENGTH = 8
SPECIAL_CHARACTERS = set(string.punctuation)
COMMON_PASSWORDS = {
    "123456",
    "12345678",
    "123456789",
    "password",
    "senha",
    "qwerty",
    "abc123",
    "admin",
    "letmein",
}


def has_minimum_length(password: str, minimum: int = MIN_LENGTH) -> bool:
    """Return True when the password has at least the minimum length."""
    return len(password) >= minimum


def has_uppercase(password: str) -> bool:
    """Return True when the password contains at least one uppercase letter."""
    return any(char.isupper() for char in password)


def has_lowercase(password: str) -> bool:
    """Return True when the password contains at least one lowercase letter."""
    return any(char.islower() for char in password)


def has_digit(password: str) -> bool:
    """Return True when the password contains at least one digit."""
    return any(char.isdigit() for char in password)


def has_special_character(password: str) -> bool:
    """Return True when the password contains at least one special character."""
    return any(char in SPECIAL_CHARACTERS for char in password)


def is_common_password(password: str) -> bool:
    """Return True when the password is listed as commonly used."""
    return password.strip().lower() in COMMON_PASSWORDS
