# Fluxo de trabalho Git

## Ramos

| Ramo | Finalidade |
|---|---|
| `main` | Versão estável, só recebe merges de `develop` no fim de cada sprint |
| `develop` | Integração contínua do trabalho da equipa |
| `feature/<us>-<descricao>` | Uma user story (ex.: `feature/US16-emprestar-livro`) |
| `fix/<descricao>` | Correção de erros |
| `docs/<descricao>` | Documentação |

## Passos para trabalhar numa user story

```bash
git checkout develop
git pull origin develop
git checkout -b feature/US16-emprestar-livro

# ... trabalhar, testar (python -m pytest) ...
git add .
git commit -m "feat(US16): validar limite de empréstimos por utente"

git push -u origin feature/US16-emprestar-livro
# abrir Pull Request para develop, pedir revisão a um colega
```

## Convenção de commits

`tipo(US##): descrição curta no imperativo`

Tipos: `feat`, `fix`, `docs`, `test`, `refactor`, `chore`.

## Regras

1. Ninguém faz *push* direto para `main` ou `develop`.
2. Todo o merge passa por *pull request* com pelo menos 1 revisão.
3. Os testes têm de passar antes do merge.
4. Cada *issue* do GitHub corresponde a uma user story do backlog.
5. Apagar o ramo `feature/*` depois do merge.

## Comandos úteis (cheat-sheet)

| Objetivo | Comando |
|---|---|
| Ver estado | `git status` |
| Ver histórico | `git log --oneline --graph --all` |
| Atualizar ramo | `git pull --rebase origin develop` |
| Desfazer alterações num ficheiro | `git restore <ficheiro>` |
| Guardar trabalho temporário | `git stash` / `git stash pop` |
| Resolver conflito | editar ficheiro → `git add` → `git commit` |
