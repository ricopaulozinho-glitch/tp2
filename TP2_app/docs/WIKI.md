# Wiki do projeto BiblioConsole

Conteúdo sugerido para a wiki do repositório (GitHub/GitLab). Copiar cada secção para uma página da wiki.

## Página: Início

Objetivo do projeto, equipa, ligações para o backlog e o site.

## Página: Repositório

- **Clonar:** `git clone <URL>`
- **Ramos:** `main`, `develop`, `feature/*` (ver `WORKFLOW_GIT.md`)
- **Políticas:** pull request obrigatório, 1 revisão, testes a passar

## Página: Estrutura de pastas

Ver secção *Estrutura do projeto* do README.

## Página: Estruturas de dados

| Entidade | Campos principais |
|---|---|
| Livro | id, titulo, autor, isbn (único), ano, categoria, exemplares, emprestados |
| Utente | id, nome, email (único), telefone, suspenso |
| Emprestimo | id, livro_id, utente_id, data_emprestimo, data_prevista, data_devolucao, multa |

Em memória usam-se dicionários `{id: objeto}`; em disco, um único ficheiro JSON.

## Página: Base de dados

Não é usada base de dados. A persistência é feita em `dados/biblioteca.json` com gravação atómica
(escrita para ficheiro temporário + `os.replace`). Migração para SQLite prevista no backlog (US46).

## Página: Wireframe da aplicação

```
=== BiblioConsole ===
 1) Livros: adicionar        6) Utentes: adicionar
 2) Livros: listar           7) Utentes: listar
 ...
11) Emprestar livro         12) Devolver livro
15) Resumo e estatísticas    0) Sair
Opção:
```

## Página: Parâmetros importantes

| Parâmetro | Valor | Ficheiro |
|---|---|---|
| Prazo de empréstimo | 14 dias | `models.py` |
| Limite por utente | 3 livros | `models.py` |
| Multa | 0,10 € por dia | `models.py` |

## Página: Intenção do projeto

Mostrar um fluxo de trabalho colaborativo (Scrum + Git) aplicado a uma aplicação simples e bem estruturada.

## Página: Cheat-sheet

- Git: ver `WORKFLOW_GIT.md`
- Testes: `python -m pytest`
- Documentação: `PYTHONPATH=src pdoc biblioteca -o docs_api`
