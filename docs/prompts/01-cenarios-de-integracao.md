# Prompt A — geração de cenários de integração (fluxos e dados)

## Tipo

**Prompt baseado em cenários (scenario-based prompting), com restrições de contexto e critérios de aceitação.** Objetivo: ampliar a cobertura funcional e a diversidade das entradas.

## Formulação inicial (genérica)

> Gere testes de integração para um validador de senhas em Python usando pytest.

**Limitação identificada na revisão:** a instrução não informa arquitetura, fronteiras de integração, regras nem comportamento esperado; pode resultar em testes unitários isolados ou até na proposta de uma API REST inexistente.

## Prompt ajustado e aplicado

> Você é uma pessoa engenheira de testes. Considere um projeto Python 3.10+ sem API HTTP, formado por `cli.py`, `validator.py` e `rules.py`. A CLI lê a senha por `getpass.getpass`, chama `validate_password` e imprime o resultado. `validate_password` executa seis regras: mínimo de oito caracteres, maiúscula, minúscula, número, pontuação ASCII e bloqueio por denylist local. Senhas válidas retornam código 0 e a linha `Senha válida.`; inválidas retornam 1, `Senha inválida.` e as mensagens de cada regra violada. Gere testes **de integração CLI → Validator → Rules** com `pytest.mark.parametrize`. Substitua **somente** a entrada `getpass` para evitar um terminal interativo; use o validador e as regras reais, sem simular as respostas internas. Inclua: fluxo válido, fronteira de tamanho 7/8, cada regra ausente, múltiplos erros, senha comum, senha vazia e casos Unicode coerentes com o código. Verifique código de saída, sequência exata de mensagens, stderr vazio e que a senha não apareça em stdout ou stderr. Não introduza novas dependências nem modifique a política atual.

## Evidência de aplicação

- Arquivo: [`tests/integration/test_cli_validator_rules.py`](../../tests/integration/test_cli_validator_rules.py)
- **12 cenários parametrizados**, cada um percorrendo a CLI, o validador e as regras reais.
- Apenas `getpass.getpass` é substituído, como fronteira externa de entrada; **o comportamento de validação não é mockado**.
- Comando de reprodução: `pytest -q tests/integration/test_cli_validator_rules.py`.

## Impacto sobre os testes

A explicitação do fluxo real ajudou a evitar a criação fictícia de endpoints REST e gerou casos que validam também a apresentação final das mensagens, a sequência de erros e a ausência de exposição da entrada. O pedido de casos de fronteira trouxe exemplos de 7 e 8 caracteres, enquanto o pedido de regras combinadas revelou a necessidade de validar múltiplas mensagens em uma mesma execução.
