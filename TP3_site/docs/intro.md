---
sidebar_position: 1
slug: /intro
---

# Introdução

O **BiblioConsole** é uma aplicação de consola escrita em Python para gerir uma pequena biblioteca: catálogo de livros, utentes, empréstimos, devoluções e multas.

:::tip Porquê a consola?
Sem interface gráfica nem servidor web, a aplicação arranca em milissegundos, corre em qualquer sistema com Python e é fácil de testar e de automatizar.
:::

## O que pode fazer

| Área | Funcionalidades |
|---|---|
| Livros | Adicionar, listar, editar, remover, pesquisar |
| Utentes | Registar, editar, suspender, remover |
| Empréstimos | Emprestar, devolver, listar ativos e em atraso |
| Relatórios | Resumo geral, livros mais emprestados |

## Instalação rápida

```bash
git clone https://github.com/grupo-ade/biblioconsole.git
cd biblioconsole/TP2_app
PYTHONPATH=src python -m biblioteca
```

:::info Requisitos
Python **3.10** ou superior. Não são necessárias dependências para executar.
:::

## Próximos passos

- [Instalação detalhada](./instalacao.md)
- [Gerir livros](./utilizacao/livros.md)
- [Empréstimos e multas](./utilizacao/emprestimos.md)
- [Arquitetura](./desenvolvimento/arquitetura.md)
