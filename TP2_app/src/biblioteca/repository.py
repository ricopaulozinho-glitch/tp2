"""Persistência dos dados da biblioteca em ficheiro JSON."""

from __future__ import annotations

import json
import os
import tempfile
from pathlib import Path

from .models import Emprestimo, Livro, Utente

DADOS_POR_OMISSAO = Path("dados") / "biblioteca.json"


class Repositorio:
    """Guarda e carrega livros, utentes e empréstimos num ficheiro JSON.

    A gravação é atómica: escreve para um ficheiro temporário e
    depois substitui o original, evitando ficheiros corrompidos.
    """

    def __init__(self, caminho: Path | str | None = DADOS_POR_OMISSAO):
        """Cria o repositório.

        Args:
            caminho: Caminho do ficheiro JSON. Se ``None``, os dados
                ficam apenas em memória (útil nos testes).
        """
        self.caminho = Path(caminho) if caminho else None
        self.livros: dict[int, Livro] = {}
        self.utentes: dict[int, Utente] = {}
        self.emprestimos: dict[int, Emprestimo] = {}
        self.proximo_id = {"livro": 1, "utente": 1, "emprestimo": 1}
        if self.caminho and self.caminho.exists():
            self.carregar()

    def novo_id(self, tipo: str) -> int:
        """Gera o próximo identificador para ``tipo`` (livro/utente/emprestimo)."""
        valor = self.proximo_id[tipo]
        self.proximo_id[tipo] += 1
        return valor

    def carregar(self) -> None:
        """Carrega os dados do ficheiro JSON."""
        with open(self.caminho, encoding="utf-8") as f:
            dados = json.load(f)
        self.livros = {d["id"]: Livro.from_dict(d) for d in dados.get("livros", [])}
        self.utentes = {d["id"]: Utente.from_dict(d) for d in dados.get("utentes", [])}
        self.emprestimos = {d["id"]: Emprestimo.from_dict(d) for d in dados.get("emprestimos", [])}
        self.proximo_id = dados.get("proximo_id", self.proximo_id)

    def guardar(self) -> None:
        """Grava os dados no ficheiro JSON (não faz nada se for só em memória)."""
        if not self.caminho:
            return
        self.caminho.parent.mkdir(parents=True, exist_ok=True)
        dados = {
            "livros": [l.to_dict() for l in self.livros.values()],
            "utentes": [u.to_dict() for u in self.utentes.values()],
            "emprestimos": [e.to_dict() for e in self.emprestimos.values()],
            "proximo_id": self.proximo_id,
        }
        fd, tmp = tempfile.mkstemp(dir=self.caminho.parent, suffix=".tmp")
        with os.fdopen(fd, "w", encoding="utf-8") as f:
            json.dump(dados, f, ensure_ascii=False, indent=2)
        os.replace(tmp, self.caminho)
