"""Regras de negócio da biblioteca (CRUD, empréstimos, pesquisa, relatórios)."""

from __future__ import annotations

import re
from datetime import date
from typing import Optional

from .models import (
    LIMITE_EMPRESTIMOS_UTENTE,
    MULTA_POR_DIA,
    Emprestimo,
    Livro,
    Utente,
    data_prevista_devolucao,
)
from .repository import Repositorio

EMAIL_RE = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")


class ErroBiblioteca(Exception):
    """Erro de regra de negócio, com mensagem apresentável ao utilizador."""


class Biblioteca:
    """Camada de serviço que implementa as operações da biblioteca."""

    def __init__(self, repo: Optional[Repositorio] = None):
        """Cria a biblioteca sobre um repositório (em memória se omitido)."""
        self.repo = repo if repo is not None else Repositorio(None)

    # ------------------------------------------------------------ Livros
    def adicionar_livro(self, titulo: str, autor: str, isbn: str, ano: int,
                        categoria: str, exemplares: int = 1) -> Livro:
        """Adiciona um livro ao catálogo (US01).

        Raises:
            ErroBiblioteca: se os dados forem inválidos ou o ISBN já existir.
        """
        titulo, autor, isbn, categoria = (s.strip() for s in (titulo, autor, isbn, categoria))
        if not titulo or not autor or not isbn:
            raise ErroBiblioteca("Título, autor e ISBN são obrigatórios.")
        if exemplares < 1:
            raise ErroBiblioteca("O número de exemplares deve ser pelo menos 1.")
        if not 0 < ano <= date.today().year:
            raise ErroBiblioteca("Ano de publicação inválido.")
        if any(l.isbn == isbn for l in self.repo.livros.values()):
            raise ErroBiblioteca(f"Já existe um livro com o ISBN {isbn}.")
        livro = Livro(self.repo.novo_id("livro"), titulo, autor, isbn, ano,
                      categoria or "Geral", exemplares)
        self.repo.livros[livro.id] = livro
        self.repo.guardar()
        return livro

    def obter_livro(self, livro_id: int) -> Livro:
        """Devolve o livro com o ID dado (US03)."""
        try:
            return self.repo.livros[livro_id]
        except KeyError:
            raise ErroBiblioteca(f"Livro {livro_id} não encontrado.") from None

    def listar_livros(self) -> list[Livro]:
        """Lista os livros ordenados por título (US02)."""
        return sorted(self.repo.livros.values(), key=lambda l: l.titulo.lower())

    def editar_livro(self, livro_id: int, **campos) -> Livro:
        """Edita campos de um livro (US04).

        Args:
            livro_id: ID do livro.
            **campos: ``titulo``, ``autor``, ``isbn``, ``ano``, ``categoria``, ``exemplares``.
        """
        livro = self.obter_livro(livro_id)
        permitidos = {"titulo", "autor", "isbn", "ano", "categoria", "exemplares"}
        invalidos = set(campos) - permitidos
        if invalidos:
            raise ErroBiblioteca(f"Campos inválidos: {', '.join(sorted(invalidos))}.")
        if "isbn" in campos and any(
            l.isbn == campos["isbn"] and l.id != livro_id for l in self.repo.livros.values()
        ):
            raise ErroBiblioteca(f"Já existe um livro com o ISBN {campos['isbn']}.")
        if "exemplares" in campos and campos["exemplares"] < livro.emprestados:
            raise ErroBiblioteca("Exemplares não podem ser menos do que os emprestados.")
        for nome, valor in campos.items():
            setattr(livro, nome, valor)
        self.repo.guardar()
        return livro

    def remover_livro(self, livro_id: int) -> None:
        """Remove um livro do catálogo (US05)."""
        livro = self.obter_livro(livro_id)
        if livro.emprestados > 0:
            raise ErroBiblioteca("Não é possível remover: existem empréstimos ativos.")
        del self.repo.livros[livro_id]
        self.repo.guardar()

    # ----------------------------------------------------------- Utentes
    def adicionar_utente(self, nome: str, email: str, telefone: str = "") -> Utente:
        """Regista um novo utente (US09)."""
        nome, email = nome.strip(), email.strip().lower()
        if not nome:
            raise ErroBiblioteca("O nome é obrigatório.")
        if not EMAIL_RE.match(email):
            raise ErroBiblioteca("Email inválido.")
        if any(u.email == email for u in self.repo.utentes.values()):
            raise ErroBiblioteca(f"Já existe um utente com o email {email}.")
        utente = Utente(self.repo.novo_id("utente"), nome, email, telefone.strip())
        self.repo.utentes[utente.id] = utente
        self.repo.guardar()
        return utente

    def obter_utente(self, utente_id: int) -> Utente:
        """Devolve o utente com o ID dado."""
        try:
            return self.repo.utentes[utente_id]
        except KeyError:
            raise ErroBiblioteca(f"Utente {utente_id} não encontrado.") from None

    def listar_utentes(self) -> list[Utente]:
        """Lista os utentes ordenados por nome (US10)."""
        return sorted(self.repo.utentes.values(), key=lambda u: u.nome.lower())

    def editar_utente(self, utente_id: int, **campos) -> Utente:
        """Edita dados de um utente (US12, US14)."""
        utente = self.obter_utente(utente_id)
        permitidos = {"nome", "email", "telefone", "suspenso"}
        invalidos = set(campos) - permitidos
        if invalidos:
            raise ErroBiblioteca(f"Campos inválidos: {', '.join(sorted(invalidos))}.")
        if "email" in campos:
            campos["email"] = campos["email"].strip().lower()
            if not EMAIL_RE.match(campos["email"]):
                raise ErroBiblioteca("Email inválido.")
            if any(u.email == campos["email"] and u.id != utente_id
                   for u in self.repo.utentes.values()):
                raise ErroBiblioteca("Esse email já está em uso.")
        for nome, valor in campos.items():
            setattr(utente, nome, valor)
        self.repo.guardar()
        return utente

    def remover_utente(self, utente_id: int) -> None:
        """Remove um utente (US13)."""
        self.obter_utente(utente_id)
        if self.emprestimos_ativos_do_utente(utente_id):
            raise ErroBiblioteca("Não é possível remover: o utente tem empréstimos ativos.")
        del self.repo.utentes[utente_id]
        self.repo.guardar()

    # ------------------------------------------------------- Empréstimos
    def emprestimos_ativos_do_utente(self, utente_id: int) -> list[Emprestimo]:
        """Lista os empréstimos ativos de um utente."""
        return [e for e in self.repo.emprestimos.values()
                if e.utente_id == utente_id and e.ativo]

    def emprestar(self, livro_id: int, utente_id: int, hoje: Optional[date] = None) -> Emprestimo:
        """Empresta um livro a um utente (US16)."""
        hoje = hoje or date.today()
        livro = self.obter_livro(livro_id)
        utente = self.obter_utente(utente_id)
        if utente.suspenso:
            raise ErroBiblioteca("O utente está suspenso.")
        if livro.disponiveis < 1:
            raise ErroBiblioteca("Não há exemplares disponíveis.")
        ativos = self.emprestimos_ativos_do_utente(utente_id)
        if len(ativos) >= LIMITE_EMPRESTIMOS_UTENTE:
            raise ErroBiblioteca(f"Limite de {LIMITE_EMPRESTIMOS_UTENTE} empréstimos atingido.")
        if any(e.livro_id == livro_id for e in ativos):
            raise ErroBiblioteca("O utente já tem este livro emprestado.")
        emp = Emprestimo(self.repo.novo_id("emprestimo"), livro_id, utente_id,
                         hoje.isoformat(), data_prevista_devolucao(hoje).isoformat())
        livro.emprestados += 1
        self.repo.emprestimos[emp.id] = emp
        self.repo.guardar()
        return emp

    def devolver(self, emprestimo_id: int, hoje: Optional[date] = None) -> Emprestimo:
        """Regista a devolução e calcula a multa por atraso (US17, US33)."""
        hoje = hoje or date.today()
        emp = self.repo.emprestimos.get(emprestimo_id)
        if emp is None:
            raise ErroBiblioteca(f"Empréstimo {emprestimo_id} não encontrado.")
        if not emp.ativo:
            raise ErroBiblioteca("Este empréstimo já foi devolvido.")
        emp.data_devolucao = hoje.isoformat()
        emp.multa = round(emp.dias_atraso() * MULTA_POR_DIA, 2)
        self.repo.livros[emp.livro_id].emprestados -= 1
        self.repo.guardar()
        return emp

    def listar_emprestimos_ativos(self) -> list[Emprestimo]:
        """Lista empréstimos ativos por data de devolução prevista (US18)."""
        return sorted((e for e in self.repo.emprestimos.values() if e.ativo),
                      key=lambda e: e.data_prevista)

    def listar_atrasos(self, hoje: Optional[date] = None) -> list[Emprestimo]:
        """Lista empréstimos ativos em atraso (US19)."""
        hoje = hoje or date.today()
        return [e for e in self.listar_emprestimos_ativos() if e.dias_atraso(hoje) > 0]

    # ---------------------------------------------------------- Pesquisa
    def pesquisar_livros(self, texto: str, apenas_disponiveis: bool = False) -> list[Livro]:
        """Pesquisa livros por título, autor, categoria ou ISBN (US23, US25)."""
        t = texto.strip().lower()
        res = [l for l in self.repo.livros.values()
               if t in l.titulo.lower() or t in l.autor.lower()
               or t in l.categoria.lower() or t in l.isbn.lower()]
        if apenas_disponiveis:
            res = [l for l in res if l.disponiveis > 0]
        return sorted(res, key=lambda l: l.titulo.lower())

    def pesquisar_utentes(self, texto: str) -> list[Utente]:
        """Pesquisa utentes por nome ou email (US26)."""
        t = texto.strip().lower()
        return sorted((u for u in self.repo.utentes.values()
                       if t in u.nome.lower() or t in u.email),
                      key=lambda u: u.nome.lower())

    # -------------------------------------------------------- Relatórios
    def resumo(self, hoje: Optional[date] = None) -> dict:
        """Devolve um resumo geral da biblioteca (US39)."""
        return {
            "livros": len(self.repo.livros),
            "exemplares": sum(l.exemplares for l in self.repo.livros.values()),
            "utentes": len(self.repo.utentes),
            "emprestimos_ativos": len(self.listar_emprestimos_ativos()),
            "em_atraso": len(self.listar_atrasos(hoje)),
        }

    def livros_mais_emprestados(self, n: int = 5) -> list[tuple[Livro, int]]:
        """Devolve os ``n`` livros mais emprestados (US37)."""
        contagem: dict[int, int] = {}
        for e in self.repo.emprestimos.values():
            contagem[e.livro_id] = contagem.get(e.livro_id, 0) + 1
        top = sorted(contagem.items(), key=lambda kv: kv[1], reverse=True)[:n]
        return [(self.repo.livros[i], c) for i, c in top if i in self.repo.livros]
