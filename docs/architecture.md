# Arquitetura do Projeto

Este mini-projeto foi organizado com base em separação de responsabilidades.

## Camadas principais

### `rules.py`

Contém funções pequenas e específicas responsáveis por verificar regras individuais da senha, como presença de letras maiúsculas, números, caracteres especiais e tamanho mínimo.

### `validator.py`

Contém a função principal `validate_password`, que coordena a aplicação das regras e retorna um objeto com o resultado da validação.

### `cli.py`

Contém a interface de linha de comando. A senha é solicitada exclusivamente por `getpass.getpass()`, sem eco no terminal. A CLI não aceita a senha como argumento e não exibe o valor informado.

### `tests/`

Contém os testes automatizados das regras, do validador e da interface de linha de comando. Os testes da CLI verificam que a senha não é escrita na saída padrão ou de erro.

## Decisões de projeto

- Uso de `src/` para separar código-fonte dos arquivos de configuração.
- Uso de `pytest` para facilitar a criação e execução dos testes.
- Uso de `dataclass` para representar o resultado da validação de maneira simples e legível.
- Separação entre lógica de negócio e interface CLI.
- Entrada oculta para reduzir o risco de exposição de dados sensíveis.
- Proibição de senha em argumento de terminal para evitar histórico de comandos e exposição na lista de processos.

## Fluxo de execução

1. O usuário executa o comando no terminal.
2. A CLI solicita a senha de forma oculta.
3. A função `validate_password` aplica as regras.
4. Somente o resultado e as regras não atendidas são exibidos.

A análise completa de riscos está em [`risk-analysis.md`](risk-analysis.md).
