from __future__ import annotations

import sys

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
