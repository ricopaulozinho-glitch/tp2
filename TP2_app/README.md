# BiblioConsole 📚

Aplicação de **consola** em Python para gestão de uma biblioteca: livros, utentes, empréstimos, devoluções, multas por atraso e relatórios.

Projeto da UC **Ambientes de Desenvolvimento Colaborativo** – ISE, Universidade do Algarve.

## Funcionalidades

- **CRUD de livros** (adicionar, listar, editar, remover) com ISBN único
- **CRUD de utentes** com validação de email, suspensão e reativação
- **Empréstimos e devoluções** com prazo de 14 dias e limite de 3 livros por utente
- **Multa por atraso** (0,10 €/dia) calculada na devolução
- **Pesquisa** por título, autor, categoria ou ISBN, com filtro de disponibilidade
- **Relatórios**: resumo geral, empréstimos em atraso, livros mais emprestados
- **Persistência** em JSON com gravação atómica

## Requisitos

- Python 3.10 ou superior
- Nenhuma dependência externa para executar (apenas `pytest`/`pdoc` para desenvolvimento)

## Instalação e execução

```bash
git clone <URL-do-repositorio>
cd TP2_app
python -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
pip install -r requirements-dev.txt

PYTHONPATH=src python -m biblioteca    # Windows (PowerShell): $env:PYTHONPATH="src"; python -m biblioteca
```

Os dados ficam guardados em `dados/biblioteca.json` (criado automaticamente).

## Testes

```bash
python -m pytest
```

## Documentação do código

A documentação é gerada a partir das *docstrings* com o [pdoc](https://pdoc.dev):

```bash
PYTHONPATH=src pdoc biblioteca -o docs_api
```

## Estrutura do projeto

```
TP2_app/
├── src/biblioteca/
│   ├── models.py        # dataclasses: Livro, Utente, Emprestimo
│   ├── repository.py    # persistência em JSON
│   ├── services.py      # regras de negócio (classe Biblioteca)
│   ├── cli.py           # menus de consola
│   └── __main__.py      # python -m biblioteca
├── tests/               # testes pytest
├── docs/                # wiki e documentação do projeto
├── .github/workflows/   # integração contínua
└── pyproject.toml
```

## Arquitetura

Três camadas, com dependências num só sentido:

`cli.py` → `services.py` → `repository.py` / `models.py`

A interface não contém regras de negócio, o que permite testar tudo sem a consola.

## Contribuir

Ver [docs/WORKFLOW_GIT.md](docs/WORKFLOW_GIT.md) para o fluxo de ramos, convenção de commits e *pull requests*.

## Equipa

| Nome | Número | Função |
|---|---|---|
| _(preencher)_ | | Scrum Master |
| _(preencher)_ | | Product Owner |
| _(preencher)_ | | Developer |

## Licença

Projeto académico.
