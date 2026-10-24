# Alterações

## 1.4.0

### Testes de integração com apoio de GenAI — Unidade III

- adicionados 12 cenários de integração `CLI → Validator → Rules` sem simular o validador ou as regras;
- adicionados 9 cenários de contrato `Validator → Rules`, 4 casos de tipos inválidos e 2 de interrupção na entrada;
- asseguradas verificações de código de retorno, mensagens na ordem correta e não exposição da senha em `stdout`/`stderr` nos cenários exercitados;
- documentados dois tipos de prompt, formulações iniciais, versões ajustadas, exemplos, análise crítica e limitações em `docs/testes-integracao-genai.md` e `docs/prompts/`;
- preparado texto da atividade em `docs/postagem-forum.md`;
- ampliada a suite para **40 testes (13 anteriores + 27 novos)**, mantendo o comportamento de produção;
- mantida execução automatizada no GitHub Actions.

## 1.3.0

### Documentação arquitetural — Unidade III

- adicionada fase de discovery arquitetural;
- documentados escopo, nível da visão, limites, responsabilidades, integrações, restrições e lacunas;
- adicionado diagrama estrutural em Mermaid;
- adicionado diagrama de sequência da jornada crítica em Mermaid;
- adicionadas versões `.mmd` dos diagramas em `docs/diagrams/`;
- registradas inferências realizadas com GenAI e os ajustes feitos após revisão humana;
- documentadas informações ainda necessárias para um agente implementar ou evoluir o sistema sem inventar decisões.

### Qualidade

- mantidos testes automatizados das regras e do validador;
- adicionados testes da CLI verificando que a senha não aparece em `stdout` ou `stderr`;
- configurado GitHub Actions para executar os testes em pushes e pull requests.
