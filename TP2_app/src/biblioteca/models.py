"""Modelos de dados da biblioteca (dataclasses)."""

from __future__ import annotations

from dataclasses import dataclass, field, asdict
from datetime import date, timedelta
from typing import Optional

PRAZO_EMPRESTIMO_DIAS = 14
LIMITE_EMPRESTIMOS_UTENTE = 3
MULTA_POR_DIA = 0.10


@dataclass
class Livro:
    """Um livro do catálogo.

    Attributes:
        id: Identificador numérico único.
        titulo: Título do livro.
        autor: Autor do livro.
        isbn: ISBN (único no catálogo).
        ano: Ano de publicação.
        categoria: Categoria/género.
        exemplares: Número total de exemplares.
        emprestados: Número de exemplares atualmente emprestados.
    """

    id: int
    titulo: str
    autor: str
    isbn: str
    ano: int
    categoria: str
    exemplares: int = 1
    emprestados: int = 0

    @property
    def disponiveis(self) -> int:
        """Número de exemplares disponíveis para empréstimo."""
        return self.exemplares - self.emprestados

    def to_dict(self) -> dict:
        """Converte o livro num dicionário serializável."""
        return asdict(self)

    @classmethod
    def from_dict(cls, d: dict) -> "Livro":
        """Cria um livro a partir de um dicionário."""
        return cls(**d)


@dataclass
class Utente:
    """Um utente (sócio) da biblioteca."""

    id: int
    nome: str
    email: str
    telefone: str = ""
    suspenso: bool = False

    def to_dict(self) -> dict:
        """Converte o utente num dicionário serializável."""
        return asdict(self)

    @classmethod
    def from_dict(cls, d: dict) -> "Utente":
        """Cria um utente a partir de um dicionário."""
        return cls(**d)


@dataclass
class Emprestimo:
    """Um empréstimo de um livro a um utente.

    As datas são guardadas em formato ISO (``AAAA-MM-DD``).
    """

    id: int
    livro_id: int
    utente_id: int
    data_emprestimo: str
    data_prevista: str
    data_devolucao: Optional[str] = None
    multa: float = 0.0

    @property
    def ativo(self) -> bool:
        """Indica se o empréstimo ainda não foi devolvido."""
        return self.data_devolucao is None

    def dias_atraso(self, hoje: Optional[date] = None) -> int:
        """Calcula os dias de atraso (0 se não houver atraso)."""
        fim = date.fromisoformat(self.data_devolucao) if self.data_devolucao else (hoje or date.today())
        previsto = date.fromisoformat(self.data_prevista)
        return max(0, (fim - previsto).days)

    def to_dict(self) -> dict:
        """Converte o empréstimo num dicionário serializável."""
        return asdict(self)

    @classmethod
    def from_dict(cls, d: dict) -> "Emprestimo":
        """Cria um empréstimo a partir de um dicionário."""
        return cls(**d)


def data_prevista_devolucao(inicio: date) -> date:
    """Devolve a data prevista de devolução para um empréstimo iniciado em ``inicio``."""
    return inicio + timedelta(days=PRAZO_EMPRESTIMO_DIAS)
