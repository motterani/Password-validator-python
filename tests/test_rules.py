from password_validator.rules import (
    has_lowercase,
    has_minimum_length,
    has_number,
    has_special_character,
    has_uppercase,
    is_common_password,
)


def test_minimum_length():
    assert has_minimum_length("Teste123!")
    assert not has_minimum_length("A1!")


def test_uppercase():
    assert has_uppercase("Teste123!")
    assert not has_uppercase("teste123!")


def test_lowercase():
    assert has_lowercase("Teste123!")
    assert not has_lowercase("TESTE123!")


def test_number():
    assert has_number("Teste123!")
    assert not has_number("TesteABC!")


def test_special_character():
    assert has_special_character("Teste123!")
    assert not has_special_character("Teste123")


def test_common_password_is_case_insensitive_and_trimmed():
    assert is_common_password("  PASSWORD  ")
    assert not is_common_password("UmaSenhaForte123!")
