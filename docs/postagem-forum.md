# Postagem para o fórum — Unidade III

**Repositório:** https://github.com/motterani/Password-validator-python

Para a atividade, utilizei o Password Validator Python, que integra três módulos: `CLI → Validator → Rules`. Como o sistema é uma aplicação de linha de comando, optei por testar essa comunicação real em vez de criar artificialmente uma API REST.

Experimentei **dois tipos de prompt com apoio do ChatGPT**. O primeiro foi um **prompt baseado em cenários**, voltado à geração de testes de fluxo completo, limites, dados válidos e inválidos, senhas comuns e múltiplas regras violadas. O segundo foi um **prompt baseado em contratos e casos adversariais**, focado em tipos de entrada, mensagens de erro, ordenação dos resultados, cancelamentos e não exposição da senha nas saídas.

O primeiro tipo aumentou a **diversidade funcional** dos testes, porque obrigou a considerar diferentes percursos da entrada até a resposta exibida ao usuário. O segundo aumentou a **precisão das verificações**, pois passou a exigir comportamentos observáveis e contratos explícitos entre módulos, em vez de asserções genéricas.

Os principais **ajustes nos prompts** foram: descrever a arquitetura verdadeira; deixar claro que não existe API HTTP; proibir mocks do validador e das regras (simulando apenas a entrada interativa); exigir código de retorno, mensagens exatas e proteção contra exposição de senhas; e especificar casos de fronteira como 7 e 8 caracteres.

Foram incorporados **27 casos novos** em `tests/integration/`, preservando os **13 testes anteriores**. A execução local da suíte completa resultou em **40 testes aprovados**. Registrei os prompts, ajustes, casos e limitações em [`docs/testes-integracao-genai.md`](https://github.com/motterani/Password-validator-python/blob/main/docs/testes-integracao-genai.md) e em `docs/prompts/`.

**Conclusão:** a LLM foi útil como copiloto, especialmente para diversificar cenários e explicitar contratos. Entretanto, foi essencial conferir os testes com o código real e executá-los, já que prompts genéricos poderiam sugerir integrações que não existem no projeto.

> **Antes de postar:** publique a nova revisão no repositório e confirme que os links da documentação correspondem à branch padrão. Se a branch não for `main`, ajuste o link `blob/main` acima.
