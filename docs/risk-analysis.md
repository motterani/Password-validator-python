# Análise de riscos

A avaliação abaixo usa uma escala simples de probabilidade e impacto de 1 a 3. O nível é o produto `probabilidade x impacto`.

| Risco | Prob. | Impacto | Nível | Mitigação atual |
|---|---:|---:|---:|---|
| Senha aparecer durante a digitação | 2 | 3 | 6 | Entrada com `getpass` |
| Senha parar no histórico do shell | 2 | 3 | 6 | Não aceitar a senha como argumento CLI |
| Senha ser persistida acidentalmente | 1 | 3 | 3 | Não há banco, arquivo ou logging da senha |
| Lista de senhas comuns ser insuficiente | 3 | 2 | 6 | Lacuna documentada; ampliar denylist em evolução futura |
| Alteração quebrar regra existente | 2 | 2 | 4 | Testes automatizados com `pytest` |
| Documentação divergir do código | 2 | 2 | 4 | Diagramas e documentação versionados no mesmo repositório |
| Código/diagrama sugerido por IA introduzir decisão inexistente | 2 | 2 | 4 | Revisão humana comparando geração com código e escopo reais |

## Risco residual

O projeto não deve ser interpretado como sistema completo de autenticação. Ele apenas valida uma senha candidata contra uma política local. Para uso em produção seriam necessárias decisões adicionais de política, threat modeling, critérios de senha comprometida, observabilidade segura e integração com o sistema consumidor.
