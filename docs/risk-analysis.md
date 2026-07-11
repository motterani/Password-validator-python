# Análise de Riscos do Projeto

## Contexto

O projeto é um validador de força de senhas executado por linha de comando. A análise considera riscos de segurança, qualidade, manutenção e uso de Inteligência Artificial Generativa durante o desenvolvimento.

## Critérios de avaliação

Probabilidade e impacto são classificados de 1 a 5. O nível do risco corresponde ao produto `probabilidade x impacto`:

- 1 a 4: baixo;
- 5 a 9: moderado;
- 10 a 16: alto;
- 17 a 25: crítico.

## Registro de riscos

| ID | Risco | Prob. | Impacto | Nível | Estratégia de resposta | Situação |
|---|---|---:|---:|---:|---|---|
| R1 | Exposição da senha na tela, no histórico do terminal ou na lista de processos | 4 | 5 | 20 — crítico | Mitigar: usar `getpass`, não imprimir a senha e não aceitá-la como argumento da CLI | Mitigado |
| R2 | Lista limitada de senhas comuns permitir combinações conhecidas não cadastradas | 4 | 4 | 16 — alto | Mitigar: ampliar e versionar a lista; avaliar integração futura com base de senhas comprometidas | Em acompanhamento |
| R3 | Cobertura de testes insuficiente deixar regressões passarem despercebidas | 3 | 4 | 12 — alto | Mitigar: manter testes unitários das regras, do validador e da CLI; automatizar testes no CI | Parcialmente mitigado |
| R4 | Documentação divergir do comportamento real da aplicação | 3 | 3 | 9 — moderado | Mitigar: revisar README e arquitetura junto com cada alteração funcional | Mitigado nesta versão |
| R5 | Sugestões incorretas ou inseguras produzidas por IA generativa | 3 | 4 | 12 — alto | Mitigar: revisão humana, execução dos testes e validação das decisões de segurança | Em acompanhamento |

## Estratégia prioritária

A resposta mais importante é a mitigação do risco **R1**, pois a senha é um dado sensível. A versão anterior aceitava a senha como argumento e a exibia no terminal. Isso poderia expor o valor no histórico de comandos, em ferramentas de monitoramento de processos ou para pessoas próximas à tela.

As seguintes medidas foram aplicadas:

1. entrada da senha somente por `getpass.getpass()`;
2. remoção do argumento posicional de senha;
3. remoção de qualquer impressão do valor informado;
4. testes automatizados que verificam que a senha não aparece na saída padrão nem na saída de erro.

O risco residual inclui limitações do próprio ambiente de execução, como terminais sem suporte adequado a entrada oculta, máquinas comprometidas ou captura por malware. Esses cenários estão fora do escopo do aplicativo.

## Comunicação e acompanhamento

| Informação | Público | Canal | Frequência ou gatilho | Responsável |
|---|---|---|---|---|
| Mudanças nas regras de validação | Desenvolvedores e avaliadores | README e histórico do Git | A cada alteração | Mantenedor do projeto |
| Risco de segurança identificado | Mantenedor | Issue privada ou comunicação direta | Imediatamente | Pessoa que identificou o risco |
| Resultado dos testes | Desenvolvedores | Terminal e futura automação de CI | Em cada alteração | Autor da mudança |
| Atualização do registro de riscos | Equipe do projeto | `docs/risk-analysis.md` | Em cada revisão relevante | Mantenedor do projeto |

## Apoio da IA generativa

A IA generativa apoiou a revisão da estrutura do projeto, a identificação de riscos, a proposta de respostas, a atualização da documentação e a elaboração de testes para o comportamento seguro da CLI.

## Limitações e cuidados no uso da IA

As respostas da IA podem conter inconsistências, sugerir controles incompletos ou descrever funcionalidades diferentes do código real. Por isso, as sugestões precisam ser revisadas por uma pessoa, comparadas com a implementação, executadas em testes e avaliadas conforme o contexto do projeto. A IA foi utilizada como apoio, não como autoridade final de segurança.
