# Alterações

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
