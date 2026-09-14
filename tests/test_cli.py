from password_validator import cli


def test_cli_valid_password(monkeypatch, capsys):
    secret = "Teste123!"
    monkeypatch.setattr(cli.getpass, "getpass", lambda _: secret)

    code = cli.main()
    output = capsys.readouterr()

    assert code == 0
    assert "Senha válida." in output.out
    assert secret not in output.out
    assert secret not in output.err


def test_cli_invalid_password(monkeypatch, capsys):
    secret = "abc"
    monkeypatch.setattr(cli.getpass, "getpass", lambda _: secret)

    code = cli.main()
    output = capsys.readouterr()

    assert code == 1
    assert "Senha inválida." in output.out
    assert secret not in output.out
    assert secret not in output.err


def test_cli_handles_cancel(monkeypatch, capsys):
    def cancel(_):
        raise KeyboardInterrupt

    monkeypatch.setattr(cli.getpass, "getpass", cancel)
    code = cli.main()
    output = capsys.readouterr()

    assert code == 1
    assert "Operação cancelada." in output.out
