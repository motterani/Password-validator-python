# Password Validator Python

Mini-projeto em Python para validar a força de senhas por meio de uma interface de linha de comando (CLI).

O projeto foi desenvolvido com foco em boas práticas de engenharia de software, segurança, separação de responsabilidades, testes automatizados e gestão de riscos.

## Funcionalidades

O validador verifica se a senha possui:

- pelo menos 8 caracteres;
- pelo menos uma letra maiúscula;
- pelo menos uma letra minúscula;
- pelo menos um número;
- pelo menos um caractere especial;
- bloqueio de senhas comuns, como `123456`, `password`, `senha`, entre outras.

A senha é solicitada de forma oculta, não é exibida na resposta e não pode ser informada como argumento do terminal.

## Estrutura do projeto

```text
password-validator-python/
├── docs/
│   ├── architecture.md
│   └── risk-analysis.md
├── src/
│   └── password_validator/
│       ├── __init__.py
│       ├── cli.py
│       ├── rules.py
│       └── validator.py
├── tests/
│   ├── __init__.py
│   ├── test_cli.py
│   ├── test_rules.py
│   └── test_validator.py
├── .gitignore
├── ALTERACOES.md
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
git clone https://github.com/motterani/Password-validator-python.git
cd Password-validator-python
```

### 2. Criar ambiente virtual

No Windows:

```bash
python -m venv .venv
.venv\Scripts\activate
```

No Linux ou macOS:

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

```bash
password-validator
```

Também é possível executar como módulo:

```bash
python -m password_validator.cli
```

O programa solicitará a senha sem exibi-la no terminal.

## Exemplo de uso

```text
Digite a senha para validação:
Senha válida.
```

Para uma senha inválida:

```text
Digite a senha para validação:
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
18 passed
```

## Gestão de riscos

A análise detalhada está em [`docs/risk-analysis.md`](docs/risk-analysis.md). Os principais riscos identificados foram:

- exposição da senha no terminal, histórico ou lista de processos;
- lista limitada de senhas comuns;
- cobertura insuficiente de testes;
- divergência entre documentação e implementação;
- sugestões incorretas ou inseguras geradas por IA.

A resposta prioritária foi mitigar a exposição da senha. A aplicação agora utiliza `getpass`, não aceita senha como argumento e possui testes que garantem que o valor não seja impresso.

## Como a IA generativa apoiou o desenvolvimento

A IA generativa apoiou a organização do projeto, a identificação e classificação de riscos, a definição de estratégias de resposta, a revisão da CLI, a elaboração de testes e a atualização da documentação.

As sugestões foram revisadas manualmente e validadas com testes automatizados. A IA foi utilizada como ferramenta de apoio, não como substituta da análise humana.

## Limitações e cuidados no uso da IA

A IA pode gerar código desnecessário, controles incompletos, mensagens inconsistentes ou documentação diferente do comportamento real. Por isso, foram adotados revisão humana, execução de testes, comparação entre código e documentação e avaliação específica dos riscos de segurança.

## Licença

Este projeto está licenciado sob a licença MIT.
