from __future__ import annotations

import sys

import pytest

from password_validator import cli


def test_main_reads_password_without_echoing_it(monkeypatch, capsys):
    password = "SenhaForte123!"
    monkeypatch.setattr(sys, "argv", ["password-validator"])
    monkeypatch.setattr(cli.getpass, "getpass", lambda _prompt: password)

    exit_code = cli.main()
    captured = capsys.readouterr()

    assert exit_code == 0
    assert "Senha válida." in captured.out
    assert password not in captured.out
    assert password not in captured.err


def test_main_does_not_echo_invalid_password(monkeypatch, capsys):
    password = "senha123"
    monkeypatch.setattr(sys, "argv", ["password-validator"])
    monkeypatch.setattr(cli.getpass, "getpass", lambda _prompt: password)

    exit_code = cli.main()
    captured = capsys.readouterr()

    assert exit_code == 1
    assert "Senha inválida." in captured.out
    assert password not in captured.out
    assert password not in captured.err


def test_cli_rejects_password_as_positional_argument():
    parser = cli.build_parser()

    with pytest.raises(SystemExit) as exc_info:
        parser.parse_args(["SenhaForte123!"])

    assert exc_info.value.code == 2


@pytest.mark.parametrize("exception_type", [EOFError, KeyboardInterrupt])
def test_main_handles_cancelled_input(monkeypatch, capsys, exception_type):
    monkeypatch.setattr(sys, "argv", ["password-validator"])

    def raise_exception(_prompt):
        raise exception_type

    monkeypatch.setattr(cli.getpass, "getpass", raise_exception)

    exit_code = cli.main()
    captured = capsys.readouterr()

    assert exit_code == 130
    assert "Validação cancelada." in captured.err
