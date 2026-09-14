# Arquitetura

## Visão geral

O Password Validator é uma aplicação local de linha de comando. A arquitetura separa interação, orquestração de regras e regras elementares para que cada responsabilidade possa ser testada e modificada isoladamente.

## Componentes

- **CLI (`cli.py`)**: recebe a senha de forma oculta com `getpass`, chama o validador e apresenta somente o resultado.
- **Validator (`validator.py`)**: coordena as regras e devolve um `ValidationResult` consolidado.
- **Rules (`rules.py`)**: implementa as verificações individuais e mantém a pequena lista local de senhas comuns.
- **Tests (`tests/`)**: verifica regras, orquestração e propriedades relevantes da CLI, inclusive não ecoar a senha.

## Decisões arquiteturais

1. A senha não é aceita por argumento de linha de comando, reduzindo risco de exposição em histórico e listagem de processos.
2. A aplicação não persiste senhas.
3. Regras são funções pequenas e independentes.
4. A CLI depende do validador; o validador depende das regras. As regras não dependem da interface.
5. A lista de senhas comuns é local na versão atual, evitando integração externa em tempo de execução.

## Diagramas versionáveis

Os diagramas arquiteturais são mantidos em Mermaid diretamente no `README.md` e também em `docs/diagrams/`.

Essa decisão permite que os diagramas sejam versionados junto ao código, revisados em pull requests, renderizados diretamente pelo GitHub e usados como contexto por ferramentas e agentes de IA.

Sempre que houver alteração significativa na arquitetura ou no fluxo de validação, os diagramas devem ser revisados juntamente com o código.
