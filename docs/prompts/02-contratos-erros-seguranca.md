# Prompt B — testes de contrato, exceções e segurança observável

## Tipo

**Prompt baseado em contrato e casos adversariais (contract-based / negative testing), com oráculos explícitos.** Objetivo: avaliar interfaces entre componentes, condições de falha, tipos aceitos e propriedades de segurança verificáveis.

## Formulação inicial (genérica)

> Gere testes de erro e segurança para o sistema de validação de senhas.

**Limitação identificada na revisão:** termos como “segurança” e “erro” não definem as garantias do software. O modelo pode inventar armazenamento, requisitos de autenticação ou rejeição de Unicode que não existem no código.

## Prompt ajustado e aplicado

> Analise o contrato real de `validate_password(password: str) -> ValidationResult`, que devolve `is_valid: bool` e `errors: list[str]`. Uma entrada de tipo diferente de `str` lança `TypeError`; uma string vazia resulta em `ValidationResult(False, ["A senha não pode estar vazia."])`. As regras aplicam-se em ordem: tamanho, maiúscula, minúscula, número, pontuação ASCII e denylist (`lower().strip()`). Elabore testes **Validator → Rules**, usando o código real das regras, para confirmar forma do retorno, ordem exata das mensagens, fronteiras, coexistência da denylist com outras falhas, comparação sem diferenciar maiúsculas e remoção de espaços somente na verificação da denylist. Inclua tipos inválidos e cancelamento de entrada na CLI via `KeyboardInterrupt` e `EOFError`, verificando tratamento sem vazamentos em stdout/stderr. Use pytest, inclua `id`s descritivos e **não faça afirmações sobre hashing, autenticação, logs externos ou API REST, pois não existem neste projeto**. Não altere o comportamento de produção.

## Evidência de aplicação

- Arquivo: [`tests/integration/test_validator_rules_contract.py`](../../tests/integration/test_validator_rules_contract.py)
- **9 cenários parametrizados** para `Validator → Rules` sem substituição de regras internas.
- **4 casos de tipo de entrada inválido** e **2 casos de cancelamento da entrada**.
- Comando de reprodução: `pytest -q tests/integration/test_validator_rules_contract.py`.

## Impacto sobre os testes

As condições explícitas transformaram a análise em testes com resultados precisos, inclusive a **ordem das mensagens** e o contrato `ValidationResult`. A separação entre o comportamento observado e funcionalidades inexistentes limitou suposições indevidas. Os casos de cancelamento verificam a fronteira entre a CLI e a entrada externa; nesses dois casos o fluxo é interrompido antes de chamar o validador.
