import pytest

from password_validator.validator import validate_password


def test_valid_password():
    result = validate_password("Teste123!")
    assert result.is_valid
    assert result.errors == []


def test_invalid_password_collects_multiple_errors():
    result = validate_password("abc")
    assert not result.is_valid
    assert len(result.errors) >= 3


def test_empty_password_has_specific_error():
    result = validate_password("")
    assert not result.is_valid
    assert result.errors == ["A senha não pode estar vazia."]


def test_non_string_input_raises_type_error():
    with pytest.raises(TypeError):
        validate_password(123456)  # type: ignore[arg-type]
