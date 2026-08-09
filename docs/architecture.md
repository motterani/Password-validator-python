# Arquitetura do Projeto

## Visão geral

O Password Validator Python é uma aplicação de linha de comando organizada com foco em separação de responsabilidades, segurança da entrada de dados, testabilidade e facilidade de manutenção.

A documentação de requisitos e especificação está em [`requirements-specification.md`](requirements-specification.md).

## Componentes principais

### `rules.py`

Contém funções pequenas e específicas para verificar regras individuais:

- tamanho mínimo;
- presença de letra maiúscula;
- presença de letra minúscula;
- presença de número;
- presença de caractere especial;
- verificação de senha comum.

### `validator.py`

Contém a função `validate_password`, responsável por coordenar as regras e retornar um `PasswordValidationResult`.

O uso de `dataclass` torna o resultado explícito e simples de testar.

### `cli.py`

Implementa a interface de linha de comando.

Decisões de segurança:

- a senha é solicitada somente com `getpass.getpass()`;
- a CLI não aceita senha como argumento posicional;
- o valor informado não é exibido na saída;
- cancelamentos por `EOFError` e `KeyboardInterrupt` retornam código `130`.

### `tests/`

Contém testes das regras, do validador e da CLI.

A suíte verifica também requisitos de segurança, incluindo:

- não exibição da senha;
- rejeição de senha como argumento;
- tratamento de cancelamento;
- múltiplas violações de regras.

### `.github/workflows/tests.yml`

Executa a suíte de testes automaticamente no GitHub Actions para Python 3.10, 3.11 e 3.12 em `push` e `pull_request`.

## Fluxo de execução

1. O usuário executa `password-validator`.
2. O `argparse` valida a linha de comando.
3. A CLI solicita a senha por entrada oculta.
4. `validate_password()` aplica as regras.
5. O sistema informa se a senha é válida.
6. Se inválida, apresenta os critérios não atendidos.
7. A senha nunca é incluída na resposta.

## Decisões de projeto

- estrutura `src/` para separar código-fonte;
- `pytest` para testes automatizados;
- `dataclass` para representar o resultado;
- regras isoladas em funções pequenas;
- entrada oculta com `getpass`;
- proibição de senha em argumentos;
- CI para reduzir regressões;
- documentação de requisitos ligada aos testes por matriz de rastreabilidade.

## Documentação relacionada

- [Análise e especificação de requisitos](requirements-specification.md)
- [Análise de riscos](risk-analysis.md)
