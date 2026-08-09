# Análise de Riscos do Projeto

## Contexto

O projeto é um validador de senhas executado por linha de comando. A análise considera riscos de segurança, qualidade, manutenção e uso de Inteligência Artificial Generativa durante o desenvolvimento.

## Critérios de avaliação

Probabilidade e impacto são classificados de 1 a 5. O nível corresponde a `probabilidade x impacto`:

- 1 a 4: baixo;
- 5 a 9: moderado;
- 10 a 16: alto;
- 17 a 25: crítico.

## Registro de riscos

| ID | Risco | Prob. | Impacto | Nível | Estratégia de resposta | Situação |
|---|---|---:|---:|---:|---|---|
| R1 | Exposição da senha na tela, histórico ou lista de processos | 4 | 5 | 20 — crítico | Usar `getpass`, não imprimir a senha e não aceitá-la como argumento | Mitigado |
| R2 | Lista local de senhas comuns ser limitada | 4 | 4 | 16 — alto | Ampliar/versionar a lista e avaliar fonte externa futuramente | Em acompanhamento |
| R3 | Regressões passarem sem execução de testes | 3 | 4 | 12 — alto | Testes automatizados e execução por GitHub Actions | Mitigado nesta versão |
| R4 | Documentação divergir do comportamento real | 3 | 3 | 9 — moderado | Atualizar README, arquitetura e especificação junto às mudanças | Mitigado nesta versão |
| R5 | Sugestões incorretas ou inseguras produzidas por IA | 3 | 4 | 12 — alto | Revisão humana, testes e comparação com requisitos | Em acompanhamento |

## Estratégia prioritária

O risco mais importante é R1, porque a senha é um dado sensível.

Medidas aplicadas:

1. entrada somente por `getpass.getpass()`;
2. remoção do argumento posicional de senha;
3. remoção da impressão do valor informado;
4. testes que verificam que a senha não aparece em `stdout` ou `stderr`;
5. teste que confirma a rejeição de senha como argumento.

## Risco residual

Mesmo com entrada oculta, riscos do ambiente permanecem fora do controle da aplicação, como:

- terminal sem suporte adequado;
- máquina comprometida;
- captura por malware;
- gravação de tela ou observação física.

## Comunicação e acompanhamento

| Informação | Canal | Gatilho |
|---|---|---|
| Mudança em regra de senha | README + especificação + Git | A cada alteração |
| Resultado dos testes | GitHub Actions / terminal | Push, pull request ou execução local |
| Novo risco | `docs/risk-analysis.md` | Quando identificado |
| Mudança de arquitetura | `docs/architecture.md` | Quando necessária |

## Uso de IA generativa

A IA foi usada para apoiar organização, análise de riscos, revisão da CLI, elaboração de testes, identificação de lacunas e atualização da documentação.

As sugestões não são aceitas automaticamente. Elas devem ser revisadas por uma pessoa e validadas contra requisitos, implementação e testes.
