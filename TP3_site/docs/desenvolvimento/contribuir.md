---
sidebar_position: 2
---

# Contribuir

## Fluxo Git

| Ramo | Finalidade |
|---|---|
| `main` | Versão estável |
| `develop` | Integração |
| `feature/US##-descricao` | Uma user story |

```bash
git checkout develop && git pull
git checkout -b feature/US16-emprestar-livro
git commit -m "feat(US16): validar limite de empréstimos"
git push -u origin feature/US16-emprestar-livro
```

Depois abra um **pull request** para `develop` e peça revisão a um colega.

## Convenção de commits

`tipo(US##): descrição` — tipos: `feat`, `fix`, `docs`, `test`, `refactor`, `chore`.

## Checklist de pull request

- [x] Testes a passar (`python -m pytest`)
- [x] Docstrings escritas
- [x] Ligado a uma *issue*
- [ ] Revisto por pelo menos 1 colega
