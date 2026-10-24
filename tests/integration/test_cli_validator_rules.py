"""Integração CLI -> Validator -> Rules (Prompt A: cenários de fluxo).

Apenas a entrada interativa (getpass) é substituída. O validador, as
regras e a saída da CLI são executados de verdade em todos os casos.
"""

import pytest

from password_validator import cli


@pytest.mark.parametrize(
    ("password", "expected_status", "expected_lines"),
    [
        pytest.param("Teste123!", 0, ["Senha válida."], id="fluxo_valido"),
        pytest.param("Aa1!xyzz", 0, ["Senha válida."], id="limite_oito_caracteres"),
        pytest.param(
            "Aa1!xyz",
            1,
            ["Senha inválida.", "- A senha deve possuir pelo menos 8 caracteres."],
            id="abaixo_do_limite",
        ),
        pytest.param(
            "teste123!",
            1,
            ["Senha inválida.", "- A senha deve possuir pelo menos uma letra maiúscula."],
            id="sem_maiuscula",
        ),
        pytest.param(
            "TESTE123!",
            1,
            ["Senha inválida.", "- A senha deve possuir pelo menos uma letra minúscula."],
            id="sem_minuscula",
        ),
        pytest.param(
            "TesteABC!",
            1,
            ["Senha inválida.", "- A senha deve possuir pelo menos um número."],
            id="sem_numero",
        ),
        pytest.param(
            "Teste1234",
            1,
            ["Senha inválida.", "- A senha deve possuir pelo menos um caractere especial."],
            id="sem_especial",
        ),
        pytest.param(
            "abc",
            1,
            [
                "Senha inválida.",
                "- A senha deve possuir pelo menos 8 caracteres.",
                "- A senha deve possuir pelo menos uma letra maiúscula.",
                "- A senha deve possuir pelo menos um número.",
                "- A senha deve possuir pelo menos um caractere especial.",
            ],
            id="multiplas_violacoes",
        ),
        pytest.param(
            "password",
            1,
            [
                "Senha inválida.",
                "- A senha deve possuir pelo menos uma letra maiúscula.",
                "- A senha deve possuir pelo menos um número.",
                "- A senha deve possuir pelo menos um caractere especial.",
                "- A senha é muito comum.",
            ],
            id="senha_na_denylist",
        ),
        pytest.param(
            "",
            1,
            ["Senha inválida.", "- A senha não pode estar vazia."],
            id="senha_vazia",
        ),
        pytest.param("Árvore12!", 0, ["Senha válida."], id="unicode_letras"),
        pytest.param(
            "Abc123§§",
            1,
            ["Senha inválida.", "- A senha deve possuir pelo menos um caractere especial."],
            id="simbolo_nao_ascii_nao_e_pontuacao_ascii",
        ),
    ],
)
def test_fluxo_completo_cli_validador_regras(
    monkeypatch, capsys, password, expected_status, expected_lines
):
    """Valida decisão, ordem das mensagens, retorno e sigilo da entrada."""
    prompts = []

    def input_oculto(prompt):
        prompts.append(prompt)
        return password

    monkeypatch.setattr(cli.getpass, "getpass", input_oculto)

    status = cli.main()
    captured = capsys.readouterr()

    assert prompts == ["Digite a senha para validação: "]
    assert status == expected_status
    assert captured.out.splitlines() == expected_lines
    assert captured.err == ""
    if password:
        assert password not in captured.out
        assert password not in captured.err
