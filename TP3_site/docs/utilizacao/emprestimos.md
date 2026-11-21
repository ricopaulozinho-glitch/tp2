---
sidebar_position: 3
---

# Empréstimos e multas

## Regras

| Parâmetro | Valor |
|---|---|
| Prazo de empréstimo | 14 dias |
| Limite por utente | 3 livros em simultâneo |
| Multa por atraso | 0,10 € por dia |

## Emprestar (opção 11)

Indique o ID do livro e o ID do utente. O empréstimo falha se:

1. o utente estiver suspenso;
2. não houver exemplares disponíveis;
3. o utente já tiver 3 empréstimos ativos;
4. o utente já tiver esse mesmo livro.

## Devolver (opção 12)

Indique o ID do **empréstimo**. Se houver atraso, a multa é calculada automaticamente:

```python
multa = dias_de_atraso * 0.10
```

Exemplo: 6 dias de atraso → **0,60 €**.

## Consultar

- **Opção 13** – empréstimos ativos, por data de devolução.
- **Opção 14** – empréstimos em atraso, com o número de dias.
- **Opção 15** – resumo geral e livros mais emprestados.
