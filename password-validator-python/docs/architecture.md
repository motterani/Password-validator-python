# Arquitetura do Projeto

Este mini-projeto foi organizado com base em separação de responsabilidades.

## Camadas principais

### `rules.py`

Contém funções pequenas e específicas responsáveis por verificar regras individuais da senha, como presença de letras maiúsculas, números, caracteres especiais e tamanho mínimo.

### `validator.py`

Contém a função principal `validate_password`, que coordena a aplicação das regras e retorna um objeto com o resultado da validação.

### `cli.py`

Contém a interface de linha de comando. Essa camada recebe a entrada do usuário, chama o validador e exibe o resultado no terminal.

### `tests/`

Contém os testes automatizados do projeto, cobrindo regras individuais e o comportamento geral do validador.

## Decisões de projeto

- Uso de `src/` para separar código-fonte dos arquivos de configuração.
- Uso de `pytest` para facilitar a criação e execução dos testes.
- Uso de `dataclass` para representar o resultado da validação de maneira simples e legível.
- Separação entre lógica de negócio e interface CLI.

## Fluxo de execução

1. O usuário executa o comando no terminal.
2. A senha é recebida via argumento ou entrada.
3. A função `validate_password` aplica as regras.
4. O resultado é exibido no terminal.
