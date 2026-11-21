---
sidebar_position: 1
---

# Arquitetura

A aplicação tem três camadas, com dependências num só sentido:

```text
cli.py  →  services.py  →  repository.py
                 ↘             ↙
                   models.py
```

| Módulo | Responsabilidade |
|---|---|
| `models.py` | `Livro`, `Utente` e `Emprestimo` (dataclasses) |
| `repository.py` | Carregar/guardar JSON com gravação atómica |
| `services.py` | Regras de negócio na classe `Biblioteca` |
| `cli.py` | Menus e leitura de dados da consola |

## Porquê esta separação?

A interface **não contém regras de negócio**. Assim, toda a lógica é testável com `pytest` sem simular a consola, e a interface pode ser substituída no futuro.

## Exemplo de uso como biblioteca

```python
from biblioteca.services import Biblioteca

bib = Biblioteca()  # em memória
livro = bib.adicionar_livro("Mensagem", "Fernando Pessoa", "222", 1934, "Poesia")
utente = bib.adicionar_utente("Ana", "ana@exemplo.pt")
emprestimo = bib.emprestar(livro.id, utente.id)
print(emprestimo.data_prevista)
```

## Persistência

Os dados ficam num único ficheiro JSON. A gravação escreve primeiro para um ficheiro temporário e só depois o substitui, para nunca deixar o ficheiro a meio.
