"""Individual password validation rules."""

import string

MIN_LENGTH = 8

COMMON_PASSWORDS = {
    "123456",
    "12345678",
    "password",
    "password123",
    "qwerty",
    "admin",
    "senha",
    "senha123",
}


def has_minimum_length(password: str) -> bool:
    """Return True when the password has at least MIN_LENGTH characters."""
    return len(password) >= MIN_LENGTH


def has_uppercase(password: str) -> bool:
    """Return True when the password contains an uppercase letter."""
    return any(character.isupper() for character in password)


def has_lowercase(password: str) -> bool:
    """Return True when the password contains a lowercase letter."""
    return any(character.islower() for character in password)


def has_number(password: str) -> bool:
    """Return True when the password contains a digit."""
    return any(character.isdigit() for character in password)


def has_special_character(password: str) -> bool:
    """Return True when the password contains an ASCII punctuation character."""
    return any(character in string.punctuation for character in password)


def is_common_password(password: str) -> bool:
    """Return True when the normalized password is in the local denylist."""
    return password.lower().strip() in COMMON_PASSWORDS
