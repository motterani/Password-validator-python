# Análise e Especificação de Requisitos

**Projeto:** Password Validator Python  
**Versão:** 1.2.0  
**Repositório:** https://github.com/motterani/Password-validator-python  
**Data da revisão:** 09/08/2026

---

## 1. Objetivo

Este documento consolida os resultados da análise de requisitos do projeto, incluindo:

- requisitos funcionais;
- regras de negócio;
- requisitos não funcionais;
- histórias de usuário;
- critérios de aceitação;
- caso de uso;
- lacunas e ambiguidades;
- matriz de rastreabilidade;
- decisões relacionadas ao uso de Inteligência Artificial Generativa.

O objetivo é tornar explícito o comportamento esperado do sistema e relacioná-lo à implementação e aos testes.

---

## 2. Contexto e escopo

O Password Validator Python é uma aplicação CLI que verifica se uma senha atende a um conjunto mínimo de critérios definidos pelo projeto.

O usuário informa a senha de forma oculta e recebe:

- `Senha válida.` quando todos os critérios são atendidos; ou
- `Senha inválida.` acompanhada dos critérios não atendidos.

### Dentro do escopo

- entrada de senha pela CLI;
- entrada oculta;
- validação de regras de composição;
- verificação de senha comum;
- retorno dos motivos de invalidação;
- proteção contra exibição da senha;
- testes automatizados;
- execução automática dos testes em CI.

### Fora do escopo

- cadastro de usuários;
- autenticação;
- armazenamento de senhas;
- hash ou criptografia de credenciais;
- geração de senhas;
- cálculo de entropia;
- consulta online a bases de vazamentos;
- interface gráfica;
- banco de dados.

---

## 3. Atores

### AT01 — Usuário

Pessoa que executa a aplicação para avaliar uma senha.

### AT02 — Mantenedor

Pessoa responsável por alterar regras, testes, documentação e decisões técnicas.

---

## 4. Requisitos funcionais

### RF01 — Solicitar senha
O sistema deve solicitar uma senha ao usuário pela interface de linha de comando.

### RF02 — Ocultar a entrada
O sistema deve receber a senha sem exibir os caracteres digitados.

### RF03 — Aplicar as regras
O sistema deve aplicar todas as regras de negócio definidas para a senha.

### RF04 — Informar senha válida
Quando todas as regras forem atendidas, o sistema deve informar que a senha é válida.

### RF05 — Informar senha inválida
Quando uma ou mais regras não forem atendidas, o sistema deve informar que a senha é inválida.

### RF06 — Informar motivos
Para uma senha inválida, o sistema deve listar os critérios não atendidos.

### RF07 — Rejeitar senha vazia
Uma senha vazia deve ser rejeitada.

### RF08 — Verificar senhas comuns
O sistema deve rejeitar senhas presentes em sua lista local de senhas comuns.

### RF09 — Não aceitar senha por argumento
A aplicação não deve aceitar a senha como argumento posicional da linha de comando.

### RF10 — Tratar cancelamento
Quando a leitura da senha for interrompida por `EOFError` ou `KeyboardInterrupt`, o sistema deve informar o cancelamento e retornar código `130`.

---

## 5. Regras de negócio

### RN01 — Tamanho mínimo
A senha deve ter pelo menos **8 caracteres**.

### RN02 — Maiúscula
A senha deve conter pelo menos uma letra maiúscula.

### RN03 — Minúscula
A senha deve conter pelo menos uma letra minúscula.

### RN04 — Número
A senha deve conter pelo menos um caractere reconhecido como dígito pelo Python.

### RN05 — Caractere especial
A senha deve conter pelo menos um caractere pertencente a `string.punctuation`.

### RN06 — Senha comum
A senha não pode corresponder a uma entrada da lista `COMMON_PASSWORDS`.

A comparação usa `strip().lower()`.

### RN07 — Atendimento simultâneo
A senha somente é válida quando todas as regras aplicáveis são atendidas.

### RN08 — Entrada vazia
String vazia deve ser rejeitada imediatamente.

---

## 6. Requisitos não funcionais

### RNF01 — Segurança da entrada
A senha deve ser lida com entrada oculta.

### RNF02 — Segurança da saída
A senha não deve aparecer em `stdout` nem em `stderr`.

### RNF03 — Segurança da execução
A senha não deve ser aceita como argumento posicional.

### RNF04 — Manutenibilidade
Regras, validação e CLI devem permanecer separadas em módulos distintos.

### RNF05 — Testabilidade
As principais regras e fluxos devem possuir testes automatizados.

### RNF06 — Integração contínua
Os testes devem ser executados automaticamente no GitHub Actions em `push` e `pull_request`.

### RNF07 — Compatibilidade
O projeto deve suportar Python 3.10 ou superior.

### RNF08 — Clareza
As mensagens de erro devem indicar o critério violado sem revelar a senha.

### RNF09 — Consistência documental
Mudanças funcionais devem ser acompanhadas de revisão da documentação.

---

## 7. Artefatos de especificação escolhidos

Foram produzidos:

1. histórias de usuário;
2. critérios de aceitação;
3. caso de uso textual;
4. matriz de rastreabilidade;
5. análise de lacunas e ambiguidades;
6. análise de riscos.

### Por que esses artefatos foram escolhidos?

A solução possui um fluxo pequeno e objetivo em linha de comando. Por isso:

- **histórias de usuário** representam o valor esperado;
- **critérios de aceitação** permitem transformar expectativas em condições verificáveis;
- **caso de uso textual** descreve o fluxo sem exigir diagramas complexos;
- **matriz de rastreabilidade** liga requisito, código e teste;
- **lacunas e ambiguidades** registram decisões ainda incompletas;
- **análise de riscos** é relevante porque a aplicação manipula um dado sensível.

Protótipos visuais não foram priorizados, pois não existe interface gráfica.

---

## 8. Histórias de usuário e critérios de aceitação

### US01 — Validar uma senha

**Como** usuário,  
**quero** verificar se uma senha atende à política do sistema,  
**para** identificar se ela pode ser considerada válida.

Critérios:

- CA01 — senha que atende todas as regras deve ser válida;
- CA02 — senha com menos de 8 caracteres deve ser inválida;
- CA03 — senha sem maiúscula deve ser inválida;
- CA04 — senha sem minúscula deve ser inválida;
- CA05 — senha sem número deve ser inválida;
- CA06 — senha sem caractere especial deve ser inválida;
- CA07 — senha comum deve ser inválida;
- CA08 — senha vazia deve ser inválida.

### US02 — Informar a senha com segurança

**Como** usuário,  
**quero** digitar a senha sem que ela apareça no terminal ou na resposta,  
**para** reduzir o risco de exposição.

Critérios:

- CA09 — a digitação deve usar entrada oculta;
- CA10 — a senha não deve aparecer em `stdout`;
- CA11 — a senha não deve aparecer em `stderr`;
- CA12 — a senha não deve ser aceita como argumento posicional.

### US03 — Entender a rejeição

**Como** usuário,  
**quero** receber os motivos da invalidação,  
**para** saber quais critérios precisam ser corrigidos.

Critérios:

- CA13 — cada regra violada deve gerar uma mensagem correspondente;
- CA14 — múltiplas falhas devem poder ser apresentadas na mesma validação;
- CA15 — as mensagens não devem revelar a senha.

### US04 — Cancelar a entrada

**Como** usuário,  
**quero** poder interromper a entrada,  
**para** encerrar a operação sem comportamento inesperado.

Critérios:

- CA16 — `EOFError` deve ser tratado;
- CA17 — `KeyboardInterrupt` deve ser tratado;
- CA18 — cancelamento deve retornar código `130`.

---

## 9. Caso de uso

### CU01 — Validar senha

**Ator:** Usuário  
**Objetivo:** verificar uma senha.

#### Pré-condições

- Python 3.10 ou superior;
- aplicação instalada ou executável como módulo.

#### Fluxo principal

1. O usuário executa `password-validator`.
2. A aplicação valida os argumentos.
3. O sistema solicita a senha de forma oculta.
4. O usuário informa a senha.
5. O sistema aplica todas as regras.
6. Todas as regras são atendidas.
7. O sistema exibe `Senha válida.`
8. A aplicação retorna código `0`.

#### Fluxo alternativo A — Senha inválida

1. Uma ou mais regras são violadas.
2. O sistema exibe `Senha inválida.`
3. O sistema lista os motivos.
4. A aplicação retorna código `1`.

#### Fluxo alternativo B — Senha passada como argumento

1. O usuário tenta executar `password-validator "MinhaSenha123!"`.
2. O `argparse` rejeita o argumento não reconhecido.
3. A senha não é processada pela aplicação.

#### Fluxo alternativo C — Cancelamento

1. O usuário interrompe a leitura.
2. O sistema informa `Validação cancelada.`
3. A aplicação retorna código `130`.

---

## 10. Matriz de rastreabilidade

| Requisito | Implementação | Teste/Evidência |
|---|---|---|
| RF01 / RF02 | `cli.py` | `test_main_reads_password_without_echoing_it` |
| RF03 | `validator.py` | `tests/test_validator.py` |
| RF04 / RF05 | `cli.py` | testes de CLI válida e inválida |
| RF06 | `validator.py` + `cli.py` | testes do validador |
| RF07 / RN08 | `validator.py` | teste de senha vazia |
| RF08 / RN06 | `rules.py` | teste de senha comum |
| RF09 / RNF03 | `cli.py` | `test_cli_rejects_password_as_positional_argument` |
| RF10 | `cli.py` | `test_main_handles_cancelled_input` |
| RN01 | `has_minimum_length()` | testes de comprimento |
| RN02 | `has_uppercase()` | `test_has_uppercase` |
| RN03 | `has_lowercase()` | `test_has_lowercase` |
| RN04 | `has_digit()` | `test_has_digit` |
| RN05 | `has_special_character()` | `test_has_special_character` |
| RN07 | `validate_password()` | senha forte + múltiplas falhas |
| RNF01 / RNF02 | `cli.py` | testes que não ecoam senha |
| RNF04 | arquitetura modular | `docs/architecture.md` |
| RNF05 | `tests/` | `pytest` |
| RNF06 | GitHub Actions | `.github/workflows/tests.yml` |
| RNF07 | `pyproject.toml` | `requires-python >=3.10` |
| RNF09 | documentação | revisão manual |

---

## 11. Lacunas identificadas

### L01 — Lista pequena de senhas comuns

A lista local é limitada e pode não conter diversas senhas conhecidas.

**Decisão:** manter como limitação conhecida e avaliar ampliação futura.

### L02 — Ausência de comprimento máximo

Não existe requisito de tamanho máximo.

**Decisão:** não criar um limite arbitrário sem necessidade explícita.

### L03 — Política de espaços

A implementação permite espaços internos; `strip()` é usado somente na comparação com senhas comuns.

**Lacuna:** a política ainda pode ser formalizada de maneira mais explícita.

### L04 — Unicode

`isupper()`, `islower()` e `isdigit()` aceitam caracteres Unicode, enquanto `string.punctuation` é baseado em pontuação ASCII.

**Lacuna:** a política de caracteres internacionais ainda pode ser detalhada.

### L05 — Significado de “força”

O sistema valida uma política de composição. Ele não calcula entropia, probabilidade de quebra ou pontuação criptográfica.

**Decisão:** deixar essa limitação explícita.

---

## 12. Ambiguidades e decisões

| ID | Questão | Decisão |
|---|---|---|
| A01 | O que é caractere especial? | `string.punctuation` |
| A02 | Qual o tamanho mínimo? | 8 caracteres |
| A03 | Existe tamanho máximo? | Não nesta versão |
| A04 | O que é senha comum? | Entrada da lista `COMMON_PASSWORDS` |
| A05 | A senha pode ser argumento? | Não |
| A06 | A senha é armazenada? | Não |
| A07 | Há consulta externa? | Não |
| A08 | “Força” significa entropia? | Não; significa atendimento às regras |

---

## 13. Apoio da Inteligência Artificial Generativa

A IA Generativa foi utilizada como ferramenta de apoio em:

- organização da estrutura;
- revisão da separação de responsabilidades;
- identificação e classificação de riscos;
- revisão da segurança da CLI;
- criação e ampliação de cenários de teste;
- identificação de lacunas e ambiguidades;
- elaboração e revisão da documentação;
- comparação entre requisito, implementação e teste.

As respostas foram revisadas manualmente. A decisão final permaneceu humana.

---

## 14. Sugestões da IA: aproveitadas, modificadas ou descartadas

| Sugestão/proposta | Decisão | Justificativa |
|---|---|---|
| Separar regras, validador e CLI | Aproveitada | Melhora manutenção e teste |
| Usar `pytest` | Aproveitada | Permite critérios verificáveis |
| Usar `getpass` | Aproveitada | Reduz exposição da senha |
| Não imprimir a senha | Aproveitada | Proteção de dado sensível |
| Remover senha dos argumentos | Aproveitada após revisão | Evita histórico/processos |
| Criar análise de riscos | Aproveitada | Formaliza riscos e respostas |
| Ampliar testes da CLI | Aproveitada | Aumenta rastreabilidade |
| Adicionar CI | Aproveitada nesta versão | Automatiza testes |
| Manter senha como argumento | Descartada | Risco de segurança |
| Exibir a senha no resultado | Descartada | Exposição desnecessária |
| Consultar base externa imediatamente | Não adotada | Fora do escopo atual |
| Criar GUI/protótipo visual | Descartada | CLI é suficiente para o escopo |

---

## 15. Validação e qualidade

A versão 1.2.0 possui **22 testes automatizados** cobrindo:

- regras individuais;
- senha válida;
- senha vazia;
- cada regra principal de rejeição;
- tipo inválido;
- múltiplas falhas;
- CLI com senha válida;
- CLI com senha inválida;
- não exposição da senha;
- rejeição de senha como argumento;
- cancelamento por `EOFError`;
- cancelamento por `KeyboardInterrupt`.

Os testes também são executados automaticamente pelo GitHub Actions em Python 3.10, 3.11 e 3.12.

---

## 16. Conclusão

Os artefatos escolhidos representam de forma adequada um sistema pequeno e orientado a comportamento.

A especificação agora liga requisitos, regras, critérios de aceitação, código e testes, permitindo rastrear o que foi solicitado e como foi implementado.

A IA Generativa contribuiu como apoio à análise e à revisão, mas suas sugestões foram filtradas, modificadas ou descartadas conforme segurança, escopo e evidências dos testes.

Documentos relacionados:

- [Arquitetura](architecture.md)
- [Análise de riscos](risk-analysis.md)
