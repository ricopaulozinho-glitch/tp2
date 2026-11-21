# BiblioConsole – Trabalho Prático de Ambientes de Desenvolvimento Colaborativo

Tema: **Gestão de biblioteca** (aplicação de consola em Python).

| Parte | Pasta | Conteúdo |
|---|---|---|
| TP1 – Gestão do projeto | [`TP1_backlog/`](TP1_backlog/BACKLOG.md) | Product Backlog Scrum: 57 user stories, 10 épicos, sprints, riscos |
| TP2 – Aplicação | [`TP2_app/`](TP2_app/README.md) | App Python com CRUD, testes `pytest`, docstrings, wiki e fluxo Git |
| TP3 – Site | [`TP3_site/`](TP3_site/) | Site Docusaurus (`npm install && npm start`) |

## Antes de entregar – o que o grupo tem de fazer

1. **Validar o tema** com o professor e escolher que user stories implementar no TP2.
2. **Criar o repositório remoto** (GitHub/GitLab) e preencher nomes/números da equipa
   (`TP2_app/README.md`, `TP3_site/src/pages/equipa.md`, `TP1_backlog/BACKLOG.md`).
3. **Trabalhar em equipa no Git**: ramos `feature/*`, pull requests, issues e commits de *todos* os
   elementos. A avaliação valoriza o histórico real, por isso não o simulem nem o apaguem.
4. **Criar a wiki** no repositório a partir de `TP2_app/docs/WIKI.md`.
5. **Atualizar o site**: `url`, `organizationName` e `projectName` em `TP3_site/docusaurus.config.js`.
6. **Ler e perceber o código**: pode haver defesa individual (reprovar nela implica reprovar na UC).

## Verificação feita

- `python -m pytest` → 22 testes a passar
- `npm run build` no site → compilado sem erros
