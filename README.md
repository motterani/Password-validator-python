# Password Validator Python

Validador de senhas em Python executado por linha de comando (CLI), desenvolvido com foco em **engenharia de software, segurança, especificação de requisitos, testes automatizados e uso responsável de Inteligência Artificial Generativa**.

**Versão atual: 1.2.0**

## Funcionalidades

O validador verifica se a senha possui:

- pelo menos 8 caracteres;
- pelo menos uma letra maiúscula;
- pelo menos uma letra minúscula;
- pelo menos um número;
- pelo menos um caractere especial;
- bloqueio de senhas comuns cadastradas na aplicação.

A senha:

- é solicitada com entrada oculta por `getpass`;
- não é exibida na resposta;
- não pode ser informada como argumento posicional;
- não é armazenada pelo projeto.

> Neste projeto, “força de senha” significa atendimento à política de validação implementada. A aplicação não calcula entropia ou tempo estimado de quebra.

## Documentação da atividade

A documentação de requisitos foi organizada para registrar os artefatos de especificação utilizados na atividade prática.

- [Análise e especificação de requisitos](docs/requirements-specification.md)
- [Arquitetura](docs/architecture.md)
- [Análise de riscos](docs/risk-analysis.md)
- [Histórico de alterações](ALTERACOES.md)

A especificação contém:

- requisitos funcionais;
- regras de negócio;
- requisitos não funcionais;
- histórias de usuário;
- critérios de aceitação;
- caso de uso;
- matriz de rastreabilidade;
- lacunas e ambiguidades;
- registro de como a IA apoiou o trabalho;
- sugestões de IA aproveitadas, modificadas e descartadas.

## Artefatos escolhidos

Foram priorizados:

1. histórias de usuário;
2. critérios de aceitação;
3. caso de uso textual;
4. matriz de rastreabilidade;
5. análise de lacunas e ambiguidades;
6. análise de riscos.

Esses artefatos são adequados porque a aplicação possui um fluxo curto e objetivo em CLI. Protótipos visuais não foram priorizados, pois não existe interface gráfica.

## Estrutura do projeto

```text
Password-validator-python/
├── .github/
│   └── workflows/
│       └── tests.yml
├── docs/
│   ├── architecture.md
│   ├── requirements-specification.md
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

## Como executar

### 1. Clonar o repositório

```bash
git clone https://github.com/motterani/Password-validator-python.git
cd Password-validator-python
```

### 2. Criar ambiente virtual

Windows:

```bash
python -m venv .venv
.venv\Scripts\activate
```

Linux ou macOS:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Instalar dependências

```bash
pip install -r requirements.txt
pip install -e .
```

### 4. Executar

```bash
password-validator
```

Ou:

```bash
python -m password_validator.cli
```

O programa solicita a senha sem exibi-la no terminal.

## Exemplos

Senha válida:

```text
Digite a senha para validação:
Senha válida.
```

Senha inválida:

```text
Digite a senha para validação:
Senha inválida.
- A senha deve conter pelo menos uma letra maiúscula.
- A senha deve conter pelo menos um caractere especial.
```

## Testes automatizados

Execute:

```bash
pytest
```

Saída esperada:

```text
22 passed
```

A versão 1.2.0 também adiciona **GitHub Actions**. Os testes são executados automaticamente em `push` e `pull_request` para Python 3.10, 3.11 e 3.12.

## Segurança

As principais decisões de segurança são:

- entrada oculta;
- senha não exibida;
- senha não aceita como argumento;
- senha não armazenada;
- tratamento de cancelamento;
- testes contra regressões na CLI.

A análise completa está em [`docs/risk-analysis.md`](docs/risk-analysis.md).

## Como a IA Generativa apoiou o desenvolvimento

A IA Generativa foi utilizada como apoio para:

- organizar o projeto;
- revisar a arquitetura;
- identificar riscos e estratégias de resposta;
- revisar a segurança da CLI;
- sugerir cenários de teste;
- identificar lacunas e ambiguidades;
- estruturar a documentação de requisitos.

As sugestões não foram utilizadas automaticamente. Elas foram revisadas e comparadas com o código, os requisitos e os testes.

Exemplos:

- **aproveitada:** uso de `getpass`;
- **aproveitada:** separação entre regras, validador e CLI;
- **aproveitada:** ampliação dos testes e inclusão de CI;
- **modificada:** estratégia de entrada da senha após análise do risco de argumentos;
- **descartada:** exibir a senha no resultado;
- **não adotada nesta versão:** integração com base externa de senhas comprometidas;
- **descartada para o escopo:** interface gráfica.

Mais detalhes em [`docs/requirements-specification.md`](docs/requirements-specification.md).

## Limitações conhecidas

- lista local de senhas comuns é pequena;
- não existe cálculo de entropia;
- política de Unicode pode ser detalhada futuramente;
- não existe limite máximo de comprimento;
- espaços internos são aceitos pela implementação atual.

## Licença

Este projeto está licenciado sob a licença MIT.
