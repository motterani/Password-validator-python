from password_validator.rules import (
    has_digit,
    has_lowercase,
    has_minimum_length,
    has_special_character,
    has_uppercase,
    is_common_password,
)


def test_has_minimum_length_returns_true_for_valid_length():
    assert has_minimum_length("Abc123!@") is True


def test_has_minimum_length_returns_false_for_short_password():
    assert has_minimum_length("A1!") is False


def test_has_uppercase():
    assert has_uppercase("abcD123!") is True
    assert has_uppercase("abcd123!") is False


def test_has_lowercase():
    assert has_lowercase("ABCd123!") is True
    assert has_lowercase("ABCD123!") is False


def test_has_digit():
    assert has_digit("Abc123!") is True
    assert has_digit("Abcdef!") is False


def test_has_special_character():
    assert has_special_character("Abc123!") is True
    assert has_special_character("Abc1234") is False


def test_is_common_password():
    assert is_common_password("password") is True
    assert is_common_password("SenhaForte123!") is False
