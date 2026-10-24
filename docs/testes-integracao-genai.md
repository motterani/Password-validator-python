# Unidade III — Experimento com prompts para testes de integração

## 1. Cenário e objetivo

O projeto **Password Validator Python** é uma aplicação de linha de comando, **não uma API REST**. O cenário real de integração é:

```text
Usuário → CLI (getpass) → Validator (validate_password)
                                  ↓
                              Rules / denylist
                                  ↓
           CLI ← ValidationResult ← Validator
           ↓
      stdout e status de retorno
```

**Objetivo:** usar uma LLM (ChatGPT) como apoio à criação de casos automatizados que atravessem fronteiras reais dos módulos, mantendo os testes originais e evitando a construção de componentes fictícios.

## 2. Tipos de prompt experimentados

| Tipo e intenção | Prompt documentado | Artefato resultante |
| --- | --- | --- |
| **A. Baseado em cenários**: fluxos normais, dados variados, limites e múltiplas falhas | [`prompts/01-cenarios-de-integracao.md`](prompts/01-cenarios-de-integracao.md) | `tests/integration/test_cli_validator_rules.py` |
| **B. Baseado em contrato e casos adversariais**: tipos, respostas, exceções e segurança observável | [`prompts/02-contratos-erros-seguranca.md`](prompts/02-contratos-erros-seguranca.md) | `tests/integration/test_validator_rules_contract.py` |

Cada documento contém uma formulação inicial genérica, uma versão ajustada com o contexto fornecido à LLM e a descrição do resultado incorporado ao repositório. O código gerado foi confrontado com `src/password_validator/` e executado, em vez de ser aceito como correto apenas porque foi produzido por IA.

## 3. Casos de teste integrados ao repositório

| Grupo | Cobertura verificada | Casos |
| --- | --- | ---: |
| A — CLI → Validator → Rules | sucesso, falha individual por regra, limites de 7/8 caracteres, erros simultâneos, denylist, vazio, Unicode, sigilo da senha, status de retorno | **12** |
| B — Validator → Rules | contrato `ValidationResult`, ordem de erros, normalização da denylist, falhas simultâneas, espaço em branco, pontuação ASCII | **9** |
| B — tipos inválidos | `None`, número, lista, dicionário produzem `TypeError` | **4** |
| B — interrupções da entrada | `KeyboardInterrupt` e `EOFError`, sem exceção não tratada nem eco da entrada | **2** |
| **Total adicional** | **Casos novos de teste** | **27** |

Os testes adicionais estão em `tests/integration/`. Os **13 testes anteriores** permanecem inalterados. Os dois casos de interrupção verificam a fronteira de entrada e não executam a integração com as regras, pois a CLI cancela antes dela; são incluídos para avaliar o contrato de erro da interface.

### Critérios de aprovação

- **Resultados funcionais:** `status` de saída e lista ordenada de mensagens de erro/êxito.
- **Contrato interno:** objeto `ValidationResult`, tipos esperados e erro de tipo para entrada inválida.
- **Segurança observável:** não imprimir a **senha completa** em `stdout` ou `stderr` nos casos parametrizados; a suite não pretende provar ausência de vazamentos em outros canais.
- **Isolamento:** só se substitui `getpass` no fluxo CLI; não há mocks de `validate_password` nem das regras.

## 4. Influência de cada tipo de prompt

**Prompt A — diversidade funcional:** deu cobertura aos caminhos executados pelo usuário e a combinações de dados que atravessam todos os módulos. A exigência de testar o retorno e a saída completa evitou testes superficiais que só verificariam `True` ou `False`. Os limites 7/8 e os múltiplos erros aumentaram a variedade dos cenários.

**Prompt B — precisão e robustez do contrato:** resultou em verificações mais específicas de tipos, mensagens ordenadas, denylist com comparação case-insensitive e espaços externos, além de exceções na entrada. As restrições impedem que a LLM invente autenticação, persistência, regras de Unicode ou endpoints inexistentes.

Os dois tipos se complementam: o primeiro confirma **fluxos de negócio ponta a ponta** e o segundo verifica **contratos e condições de erro nas interfaces entre módulos**.

## 5. Ajustes de prompt necessários

1. **Arquitetura explícita:** trocar “teste API REST” por `CLI → Validator → Rules`; este projeto não possui servidor HTTP.
2. **Fronteiras de mocks:** permitir simular apenas `getpass`, nunca `validate_password` ou as regras internas; caso contrário, o teste ficaria isolado demais para ser de integração.
3. **Oráculos concretos:** exigir retorno 0/1, mensagens e ordem exatas, `stdout` e `stderr`, reduzindo asserções vagas.
4. **Diversidade verificável:** citar 7/8 caracteres, denylist, erros combinados, vazio, Unicode e tipos inválidos.
5. **Escopo e segurança:** restringir as expectativas ao código existente; não inferir hashing, base de dados ou verificação remota de senhas.

As versões iniciais registradas nos arquivos de prompt são exemplos genéricos de ponto de partida; a evidência reproduzível da aplicação e revisão é a **suite final versionada e executada**. Não são apresentados como medições de respostas independentes de múltiplas sessões da LLM.

## 6. Execução e resultado

A partir da raiz do repositório, após `pip install -e .[dev]`:

```bash
pytest -q tests/integration
pytest -q
```

Resultado observado durante a preparação desta revisão:

```text
27 passed   # somente os novos testes de integração/contrato
40 passed   # suíte completa: 13 originais + 27 novos
```

**Ambiente de execução desta revisão:** Python 3.13, pytest 9.0.2. O projeto requer Python 3.10+ e o workflow GitHub Actions usa Python 3.12. Como todo teste automatizado, o resultado local não substitui a confirmação posterior do workflow de CI no GitHub.

## 7. Limitações e próximos passos

- A aplicação **não possui endpoints REST**, então não foram inventados testes HTTP ou contratos OpenAPI.
- A suíte verifica fluxos em processo e não simula um terminal interativo real.
- A propriedade de sigilo testada é limitada às saídas capturadas, não a todos os canais do sistema operacional.
- Uma evolução futura poderia adicionar testes de subprocesso/PTY em ambientes compatíveis e, **somente caso seja implementada uma API**, testes reais cliente-servidor.

## 8. Referência para o fórum

Repositório: https://github.com/motterani/Password-validator-python

Texto pronto para publicação após o envio da nova revisão: [`postagem-forum.md`](postagem-forum.md).
