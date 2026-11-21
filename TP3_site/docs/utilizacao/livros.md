---
sidebar_position: 1
---

# Gerir livros

## Adicionar um livro

Escolha a opção **1** do menu e preencha os campos:

```text
Opção: 1
Título: Os Maias
Autor: Eça de Queirós
ISBN: 9789722034524
Ano: 1888
Categoria: Romance
Exemplares: 2
  Livro adicionado com ID 1.
```

:::caution Regras
- O **ISBN** é único: não pode haver dois livros com o mesmo.
- O número de **exemplares** tem de ser pelo menos 1.
:::

## Listar e pesquisar

- **Opção 2** lista todo o catálogo por ordem alfabética de título.
- **Opção 5** pesquisa por título, autor, categoria ou ISBN (sem distinguir maiúsculas) e permite mostrar apenas livros disponíveis.

## Editar

A **opção 3** pede o ID do livro. Deixe um campo em branco para manter o valor atual.

## Remover

A **opção 4** remove um livro, mas só se **não tiver empréstimos ativos**.

:::danger
A remoção é definitiva. Peça sempre confirmação ao utilizador antes de apagar.
:::
