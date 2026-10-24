"""Integração Validator -> Rules (Prompt B: contrato, erros e limites).

Sem mock de regras: os casos verificam o contrato público do validador
com a implementação real das seis regras, incluindo a denylist local.
"""

import pytest

from password_validator.validator import ValidationResult, validate_password


@pytest.mark.parametrize(
    ("password", "expected_errors"),
    [
        pytest.param("Aa1!xyzz", [], id="tamanho_minimo_aceito"),
        pytest.param(
            "Aa1!xyz",
            ["A senha deve possuir pelo menos 8 caracteres."],
            id="limite_inferior_recusado",
        ),
        pytest.param(
            "",
            ["A senha não pode estar vazia."],
            id="erro_especifico_senha_vazia",
        ),
        pytest.param(
            "PASSWORD",
            [
                "A senha deve possuir pelo menos uma letra minúscula.",
                "A senha deve possuir pelo menos um número.",
                "A senha deve possuir pelo menos um caractere especial.",
                "A senha é muito comum.",
            ],
            id="denylist_case_insensitive",
        ),
        pytest.param(
            " Password ",
            [
                "A senha deve possuir pelo menos um número.",
                "A senha deve possuir pelo menos um caractere especial.",
                "A senha é muito comum.",
            ],
            id="denylist_ignora_espacos_externos",
        ),
        pytest.param(
            "password123",
            [
                "A senha deve possuir pelo menos uma letra maiúscula.",
                "A senha deve possuir pelo menos um caractere especial.",
                "A senha é muito comum.",
            ],
            id="denylist_nao_substitui_outras_regras",
        ),
        pytest.param(
            "Abc123§§",
            ["A senha deve possuir pelo menos um caractere especial."],
            id="contrato_pontuacao_ascii",
        ),
        pytest.param(
            "     ",
            [
                "A senha deve possuir pelo menos 8 caracteres.",
                "A senha deve possuir pelo menos uma letra maiúscula.",
                "A senha deve possuir pelo menos uma letra minúscula.",
                "A senha deve possuir pelo menos um número.",
                "A senha deve possuir pelo menos um caractere especial.",
            ],
            id="entrada_apenas_espacos",
        ),
        pytest.param("  PAssword123!  ", [], id="espacos_externos_em_senha_forte"),
    ],
)
def test_contrato_validador_integrado_as_regras(password, expected_errors):
    result = validate_password(password)

    assert isinstance(result, ValidationResult)
    assert isinstance(result.is_valid, bool)
    assert isinstance(result.errors, list)
    assert result.is_valid is (len(expected_errors) == 0)
    assert result.errors == expected_errors


@pytest.mark.parametrize("invalid", [None, 123456, [], {}])
def test_entrada_de_tipo_invalido_rejeitada_antes_das_regras(invalid):
    with pytest.raises(TypeError, match="A senha precisa ser uma string"):
        validate_password(invalid)


@pytest.mark.parametrize("error_type", [KeyboardInterrupt, EOFError])
def test_cancelamento_entrada_cli_nao_vaza_senha(monkeypatch, capsys, error_type):
    """Exceções da borda de entrada são tratadas sem chamar o validador."""
    from password_validator import cli

    def interromper(_):
        raise error_type

    monkeypatch.setattr(cli.getpass, "getpass", interromper)

    assert cli.main() == 1
    captured = capsys.readouterr()
    assert captured.out == "\nOperação cancelada.\n"
    assert captured.err == ""
