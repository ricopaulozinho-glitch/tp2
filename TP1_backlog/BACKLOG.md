# TP1 – Product Backlog: Sistema de Gestão de Biblioteca (consola)

**UC:** Ambientes de Desenvolvimento Colaborativo – ISE, Universidade do Algarve
**Metodologia:** Agile / Scrum
**Produto:** *BiblioConsole* – aplicação Python de consola para gestão de uma biblioteca

> Estimativas em *story points* (sequência de Fibonacci). Prioridade: **Alta / Média / Baixa** (MoSCoW: M = Must, S = Should, C = Could, W = Won't now).
> Este backlog é propositadamente mais abrangente do que o que será implementado no TP2 (momento de criatividade).

## 1. Visão do produto

Para **bibliotecários e pequenas bibliotecas** que precisam de **gerir livros, utentes e empréstimos**, o *BiblioConsole* é uma **aplicação de consola em Python** que permite **registar, consultar, atualizar e remover** dados e acompanhar empréstimos e devoluções. Ao contrário de folhas de cálculo soltas, mantém os dados consistentes e calcula multas e atrasos automaticamente.

## 2. Papéis (personas)

| Papel | Descrição |
|---|---|
| Bibliotecário | Gere o catálogo, utentes e empréstimos |
| Administrador | Gere configurações, utilizadores do sistema e backups |
| Utente | Consulta catálogo, empréstimos e reservas |

## 3. Épicos

| ID | Épico |
|---|---|
| E1 | Gestão de livros (CRUD) |
| E2 | Gestão de utentes (CRUD) |
| E3 | Empréstimos e devoluções |
| E4 | Pesquisa e consulta |
| E5 | Reservas |
| E6 | Multas e penalizações |
| E7 | Relatórios e estatísticas |
| E8 | Persistência, import/export e backups |
| E9 | Autenticação e perfis |
| E10 | Qualidade, documentação e DevOps |

## 4. User Stories

### E1 – Gestão de livros

| ID | História | Critérios de aceitação | Pts | Prioridade |
|---|---|---|---|---|
| US01 | Como bibliotecário, quero **adicionar um livro** (título, autor, ISBN, ano, categoria, nº de exemplares) para o disponibilizar no catálogo. | ISBN único; campos obrigatórios validados; exemplares ≥ 1; mensagem de confirmação. | 3 | Alta (M) |
| US02 | Como bibliotecário, quero **listar todos os livros** para ver o catálogo. | Mostra ID, título, autor, disponíveis/total; ordenação por título. | 2 | Alta (M) |
| US03 | Como bibliotecário, quero **ver o detalhe de um livro** para consultar toda a informação. | Pesquisa por ID ou ISBN; mostra estado dos exemplares. | 2 | Alta (M) |
| US04 | Como bibliotecário, quero **editar um livro** para corrigir dados. | Não permite reduzir exemplares abaixo dos emprestados; ISBN continua único. | 3 | Alta (M) |
| US05 | Como bibliotecário, quero **remover um livro** para limpar o catálogo. | Bloqueado se houver empréstimos ativos; pede confirmação. | 2 | Alta (M) |
| US06 | Como bibliotecário, quero **registar vários exemplares físicos** com cota/localização para os encontrar na estante. | Cada exemplar tem código e localização. | 5 | Baixa (C) |
| US07 | Como bibliotecário, quero **associar vários autores** a um livro. | Lista de autores; pesquisa por qualquer autor. | 3 | Baixa (C) |
| US08 | Como bibliotecário, quero **marcar um livro como danificado/perdido** para refletir o seu estado. | Exemplar deixa de estar disponível. | 3 | Média (S) |

### E2 – Gestão de utentes

| ID | História | Critérios de aceitação | Pts | Prioridade |
|---|---|---|---|---|
| US09 | Como bibliotecário, quero **registar um utente** (nome, email, telefone) para poder emprestar-lhe livros. | Email único e válido; ID gerado automaticamente. | 3 | Alta (M) |
| US10 | Como bibliotecário, quero **listar utentes**. | Mostra ID, nome, email, nº empréstimos ativos. | 2 | Alta (M) |
| US11 | Como bibliotecário, quero **ver o detalhe/histórico de um utente**. | Mostra empréstimos ativos e passados. | 3 | Alta (M) |
| US12 | Como bibliotecário, quero **editar dados de um utente**. | Validações mantidas. | 2 | Alta (M) |
| US13 | Como bibliotecário, quero **remover um utente**. | Bloqueado com empréstimos ativos ou multas por pagar. | 2 | Alta (M) |
| US14 | Como bibliotecário, quero **suspender/reativar um utente** para aplicar sanções. | Utente suspenso não pode pedir livros. | 3 | Média (S) |
| US15 | Como bibliotecário, quero **definir tipos de utente** (estudante, professor, externo) com limites diferentes. | Limite de livros e prazo por tipo. | 5 | Baixa (C) |

### E3 – Empréstimos e devoluções

| ID | História | Critérios de aceitação | Pts | Prioridade |
|---|---|---|---|---|
| US16 | Como bibliotecário, quero **emprestar um livro a um utente**. | Verifica disponibilidade, limite de empréstimos e suspensão; define data de devolução (14 dias). | 5 | Alta (M) |
| US17 | Como bibliotecário, quero **registar a devolução** de um livro. | Atualiza disponibilidade; calcula atraso. | 3 | Alta (M) |
| US18 | Como bibliotecário, quero **listar empréstimos ativos**. | Ordenados por data de devolução. | 2 | Alta (M) |
| US19 | Como bibliotecário, quero **listar empréstimos em atraso**. | Mostra dias de atraso e utente. | 3 | Alta (M) |
| US20 | Como bibliotecário, quero **renovar um empréstimo**. | Máx. 2 renovações; não permitido se houver reserva. | 3 | Média (S) |
| US21 | Como bibliotecário, quero **ver o histórico de empréstimos** de um livro. | Lista cronológica. | 2 | Média (S) |
| US22 | Como utente, quero **receber lembrete** de devolução próxima. | Aviso em consola ao iniciar. | 3 | Baixa (C) |

### E4 – Pesquisa e consulta

| ID | História | Critérios de aceitação | Pts | Prioridade |
|---|---|---|---|---|
| US23 | Como utilizador, quero **pesquisar livros por título/autor** (texto parcial, sem distinguir maiúsculas). | Resultados em lista. | 3 | Alta (M) |
| US24 | Como utilizador, quero **filtrar por categoria**. | Lista de categorias disponível. | 2 | Média (S) |
| US25 | Como utilizador, quero **filtrar só por livros disponíveis**. | Mostra apenas com exemplares > 0. | 2 | Média (S) |
| US26 | Como utilizador, quero **pesquisar utentes por nome/email**. | Pesquisa parcial. | 2 | Média (S) |
| US27 | Como utilizador, quero **ordenar resultados** por diferentes campos. | Título, autor, ano. | 2 | Baixa (C) |
| US28 | Como utilizador, quero **sugestões de livros semelhantes**. | Mesma categoria/autor. | 5 | Baixa (C) |

### E5 – Reservas

| ID | História | Critérios de aceitação | Pts | Prioridade |
|---|---|---|---|---|
| US29 | Como utente, quero **reservar um livro indisponível**. | Entra em fila de espera. | 5 | Média (S) |
| US30 | Como bibliotecário, quero **ver a fila de reservas** de um livro. | Ordem de chegada. | 2 | Média (S) |
| US31 | Como utente, quero **cancelar uma reserva**. | Remove da fila. | 2 | Média (S) |
| US32 | Como sistema, quero **notificar o próximo da fila** quando o livro for devolvido. | Mensagem na devolução. | 3 | Baixa (C) |

### E6 – Multas

| ID | História | Critérios de aceitação | Pts | Prioridade |
|---|---|---|---|---|
| US33 | Como sistema, quero **calcular multa por atraso** (0,10 €/dia). | Calculada na devolução. | 3 | Média (S) |
| US34 | Como bibliotecário, quero **registar o pagamento** de uma multa. | Marca como paga. | 3 | Média (S) |
| US35 | Como bibliotecário, quero **listar multas por pagar**. | Totais por utente. | 2 | Média (S) |
| US36 | Como administrador, quero **configurar o valor da multa e prazos**. | Ficheiro de configuração. | 3 | Baixa (C) |

### E7 – Relatórios e estatísticas

| ID | História | Critérios de aceitação | Pts | Prioridade |
|---|---|---|---|---|
| US37 | Como bibliotecário, quero ver **livros mais emprestados**. | Top 10. | 3 | Média (S) |
| US38 | Como bibliotecário, quero ver **utentes mais ativos**. | Top 10. | 3 | Baixa (C) |
| US39 | Como bibliotecário, quero um **resumo geral** (nº livros, utentes, empréstimos ativos, atrasos). | Painel em consola. | 3 | Média (S) |
| US40 | Como administrador, quero **exportar relatórios para CSV**. | Ficheiro gerado. | 3 | Baixa (C) |
| US41 | Como bibliotecário, quero **estatísticas por categoria**. | Contagens agregadas. | 3 | Baixa (C) |

### E8 – Persistência, import/export e backups

| ID | História | Critérios de aceitação | Pts | Prioridade |
|---|---|---|---|---|
| US42 | Como utilizador, quero que os **dados sejam guardados** entre execuções. | Ficheiro JSON; gravação atómica. | 5 | Alta (M) |
| US43 | Como administrador, quero **importar livros de CSV**. | Valida linhas, relata erros. | 5 | Baixa (C) |
| US44 | Como administrador, quero **exportar o catálogo para CSV/JSON**. | Ficheiro gerado. | 3 | Baixa (C) |
| US45 | Como administrador, quero **criar e restaurar backups**. | Cópia com data/hora. | 3 | Baixa (C) |
| US46 | Como equipa, quero **migrar para SQLite**. | Mesma interface de repositório. | 8 | Baixa (W) |

### E9 – Autenticação e perfis

| ID | História | Critérios de aceitação | Pts | Prioridade |
|---|---|---|---|---|
| US47 | Como administrador, quero **criar contas de bibliotecário**. | Password com hash. | 5 | Baixa (C) |
| US48 | Como bibliotecário, quero **iniciar sessão**. | Sessão em memória. | 3 | Baixa (C) |
| US49 | Como administrador, quero **registo de auditoria** das operações. | Log com data, ação, utilizador. | 5 | Baixa (C) |

### E10 – Qualidade, documentação e DevOps

| ID | História | Critérios de aceitação | Pts | Prioridade |
|---|---|---|---|---|
| US50 | Como equipa, quero **testes unitários** das regras de negócio. | `pytest` passa. | 5 | Alta (M) |
| US51 | Como equipa, quero **docstrings e documentação gerada**. | Docstrings em módulos/funções. | 3 | Alta (M) |
| US52 | Como equipa, quero um **README completo**. | Instalação, uso, estrutura. | 2 | Alta (M) |
| US53 | Como equipa, quero uma **wiki do projeto**. | Fluxo Git, estrutura, dados. | 3 | Alta (M) |
| US54 | Como equipa, quero **integração contínua** (GitHub Actions). | Corre testes em cada push. | 3 | Média (S) |
| US55 | Como equipa, quero um **site Docusaurus** que publicite a aplicação. | Site com docs e blog. | 8 | Alta (M) |
| US56 | Como equipa, quero uma **ajuda interativa** (`ajuda`) na consola. | Lista comandos. | 2 | Média (S) |
| US57 | Como utilizador, quero **mensagens de erro claras**. | Sem *stack traces*. | 2 | Alta (M) |

**Total:** 57 user stories · 10 épicos.

## 5. Planeamento de Sprints

Definição de *Done*: código revisto (pull request), testes a passar, docstrings escritas, merge em `develop`.

| Sprint | Datas | Objetivo | Stories |
|---|---|---|---|
| Sprint 0 | 01/10 – 18/10 | Backlog, repositório, fluxo Git (**TP1**) | US53 |
| Sprint 1 | 19/10 – 01/11 | CRUD de livros e utentes + persistência | US01–05, US09–13, US42, US57 |
| Sprint 2 | 02/11 – 15/11 | Empréstimos, devoluções, pesquisa | US16–19, US23, US50 |
| Sprint 3 | 16/11 – 22/11 | Documentação e fecho do **TP2** | US51, US52, US56 |
| Sprint 4 | 23/11 – 20/12 | Site Docusaurus (**TP3**) | US55, US54 |

## 6. Riscos

| Risco | Mitigação |
|---|---|
| Conflitos de merge | Ramos curtos e *pull requests* pequenos |
| Estimativas otimistas | Rever velocidade no fim de cada sprint |
| Dados corrompidos | Gravação atómica + backups |

## 7. Registo de pontos a validar com o professor

- [ ] Tema aceite (gestão de biblioteca)
- [ ] User stories a implementar no TP2
