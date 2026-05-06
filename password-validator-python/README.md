# Password Validator Python

Mini-projeto em Python para validar a força de senhas por meio de uma interface de linha de comando (CLI).

O projeto foi desenvolvido com foco em boas práticas de engenharia de software, incluindo separação de responsabilidades, testes automatizados, documentação e organização de repositório.

## Funcionalidades

O validador verifica se a senha possui:

- pelo menos 8 caracteres;
- pelo menos uma letra maiúscula;
- pelo menos uma letra minúscula;
- pelo menos um número;
- pelo menos um caractere especial;
- bloqueio de senhas comuns, como `123456`, `password`, `senha`, entre outras.

## Estrutura do projeto

```text
password-validator-python/
├── docs/
│   └── architecture.md
├── src/
│   └── password_validator/
│       ├── __init__.py
│       ├── cli.py
│       ├── rules.py
│       └── validator.py
├── tests/
│   ├── __init__.py
│   ├── test_rules.py
│   └── test_validator.py
├── .gitignore
├── LICENSE
├── pyproject.toml
├── README.md
└── requirements.txt
```

## Requisitos

- Python 3.10 ou superior
- pip

## Como executar o projeto

### 1. Clonar o repositório

```bash
git clone https://github.com/SEU-USUARIO/password-validator-python.git
cd password-validator-python
```

### 2. Criar ambiente virtual

No Windows:

```bash
python -m venv .venv
.venv\Scripts\activate
```

No Linux/Mac:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Instalar dependências

```bash
pip install -r requirements.txt
pip install -e .
```

### 4. Executar o validador

Passando a senha diretamente:

```bash
password-validator "SenhaForte123!"
```

Ou solicitando a senha de forma oculta:

```bash
password-validator
```

Também é possível executar como módulo:

```bash
python -m password_validator.cli "SenhaForte123!"
```

## Exemplos de uso

Senha válida:

```bash
password-validator "SenhaForte123!"
```

Saída esperada:

```text
Senha válida.
```

Senha inválida:

```bash
password-validator "senha123"
```

Saída esperada:

```text
Senha inválida.
- A senha deve conter pelo menos uma letra maiúscula.
- A senha deve conter pelo menos um caractere especial.
```

## Como rodar os testes

```bash
pytest
```

Saída esperada:

```text
16 passed
```

## Como a IA generativa apoiou o desenvolvimento

A IA generativa foi utilizada como apoio para estruturar o projeto, sugerir a organização dos arquivos, criar a primeira versão das funções de validação, auxiliar na escrita dos testes unitários e melhorar a documentação do README.

Mesmo com esse apoio, o código foi revisado manualmente, os imports foram conferidos, os testes foram executados e as regras de validação foram analisadas para garantir que o comportamento do programa estivesse correto.

## Desafios encontrados

Os principais desafios foram organizar o projeto seguindo uma estrutura profissional em Python, separar corretamente as responsabilidades entre regras, validação e interface de linha de comando, além de garantir que os testes cobrissem os principais cenários de senha válida e inválida.

Também foi necessário revisar as sugestões da IA para evitar código desnecessário, mensagens confusas ou estruturas incompatíveis com a execução real do projeto.

## Cuidados de validação

Foram adotados os seguintes cuidados:

- revisão manual do código gerado;
- execução dos testes com `pytest`;
- validação de senhas fortes e fracas;
- conferência da estrutura de pastas;
- revisão do README;
- execução do programa via terminal.

## Licença

Este projeto está licenciado sob a licença MIT.
