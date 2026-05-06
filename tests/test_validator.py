import pytest

from password_validator.validator import validate_password


def test_validate_password_accepts_strong_password():
    result = validate_password("SenhaForte123!")

    assert result.is_valid is True
    assert result.errors == []


def test_validate_password_rejects_empty_password():
    result = validate_password("")

    assert result.is_valid is False
    assert "A senha não pode estar vazia." in result.errors


def test_validate_password_rejects_short_password():
    result = validate_password("A1!")

    assert result.is_valid is False
    assert "A senha deve ter pelo menos 8 caracteres." in result.errors


def test_validate_password_rejects_password_without_uppercase():
    result = validate_password("senha123!")

    assert result.is_valid is False
    assert "A senha deve conter pelo menos uma letra maiúscula." in result.errors


def test_validate_password_rejects_password_without_lowercase():
    result = validate_password("SENHA123!")

    assert result.is_valid is False
    assert "A senha deve conter pelo menos uma letra minúscula." in result.errors


def test_validate_password_rejects_password_without_digit():
    result = validate_password("SenhaForte!")

    assert result.is_valid is False
    assert "A senha deve conter pelo menos um número." in result.errors


def test_validate_password_rejects_password_without_special_character():
    result = validate_password("Senha1234")

    assert result.is_valid is False
    assert "A senha deve conter pelo menos um caractere especial." in result.errors


def test_validate_password_rejects_common_password():
    result = validate_password("password")

    assert result.is_valid is False
    assert "A senha é muito comum e não deve ser utilizada." in result.errors


def test_validate_password_raises_type_error_for_non_string():
    with pytest.raises(TypeError):
        validate_password(12345678)  # type: ignore[arg-type]
