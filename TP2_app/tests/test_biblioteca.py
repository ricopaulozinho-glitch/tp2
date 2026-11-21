"""Testes unitários das regras de negócio."""

from datetime import date, timedelta

import pytest

from biblioteca.repository import Repositorio
from biblioteca.services import Biblioteca, ErroBiblioteca


@pytest.fixture
def bib():
    b = Biblioteca()
    b.adicionar_livro("Os Maias", "Eça de Queirós", "111", 1888, "Romance", 2)
    b.adicionar_livro("Mensagem", "Fernando Pessoa", "222", 1934, "Poesia", 1)
    b.adicionar_utente("Ana Silva", "ana@ex.pt")
    b.adicionar_utente("Rui Costa", "rui@ex.pt")
    return b


# ---------------------------------------------------------------- Livros
def test_adicionar_livro_isbn_duplicado(bib):
    with pytest.raises(ErroBiblioteca):
        bib.adicionar_livro("Outro", "X", "111", 2000, "Geral")


def test_adicionar_livro_dados_invalidos(bib):
    with pytest.raises(ErroBiblioteca):
        bib.adicionar_livro("", "X", "999", 2000, "Geral")
    with pytest.raises(ErroBiblioteca):
        bib.adicionar_livro("T", "X", "999", 2000, "Geral", exemplares=0)


def test_listar_livros_ordenado(bib):
    assert [l.titulo for l in bib.listar_livros()] == ["Mensagem", "Os Maias"]


def test_editar_livro(bib):
    bib.editar_livro(1, titulo="Os Maias (ed.)")
    assert bib.obter_livro(1).titulo == "Os Maias (ed.)"


def test_editar_isbn_duplicado(bib):
    with pytest.raises(ErroBiblioteca):
        bib.editar_livro(1, isbn="222")


def test_remover_livro(bib):
    bib.remover_livro(2)
    with pytest.raises(ErroBiblioteca):
        bib.obter_livro(2)


def test_remover_livro_emprestado_falha(bib):
    bib.emprestar(1, 1)
    with pytest.raises(ErroBiblioteca):
        bib.remover_livro(1)


# --------------------------------------------------------------- Utentes
def test_utente_email_invalido_e_duplicado(bib):
    with pytest.raises(ErroBiblioteca):
        bib.adicionar_utente("Z", "sem-arroba")
    with pytest.raises(ErroBiblioteca):
        bib.adicionar_utente("Z", "ANA@ex.pt")


def test_remover_utente_com_emprestimo_falha(bib):
    bib.emprestar(1, 1)
    with pytest.raises(ErroBiblioteca):
        bib.remover_utente(1)


def test_suspender_utente_impede_emprestimo(bib):
    bib.editar_utente(1, suspenso=True)
    with pytest.raises(ErroBiblioteca):
        bib.emprestar(1, 1)


# ----------------------------------------------------------- Empréstimos
def test_emprestar_e_devolver(bib):
    emp = bib.emprestar(1, 1)
    assert bib.obter_livro(1).disponiveis == 1
    bib.devolver(emp.id)
    assert bib.obter_livro(1).disponiveis == 2
    assert not bib.repo.emprestimos[emp.id].ativo


def test_sem_exemplares_disponiveis(bib):
    bib.emprestar(2, 1)
    with pytest.raises(ErroBiblioteca):
        bib.emprestar(2, 2)


def test_mesmo_livro_duas_vezes(bib):
    bib.emprestar(1, 1)
    with pytest.raises(ErroBiblioteca):
        bib.emprestar(1, 1)


def test_limite_de_emprestimos(bib):
    for i in range(3):
        bib.adicionar_livro(f"L{i}", "A", f"9{i}", 2000, "Geral")
    for lid in (3, 4, 5):
        bib.emprestar(lid, 1)
    with pytest.raises(ErroBiblioteca):
        bib.emprestar(1, 1)


def test_devolucao_com_atraso_calcula_multa(bib):
    inicio = date.today() - timedelta(days=20)  # prazo 14 dias -> 6 de atraso
    emp = bib.emprestar(1, 1, hoje=inicio)
    emp = bib.devolver(emp.id)
    assert emp.dias_atraso() == 6
    assert emp.multa == pytest.approx(0.60)


def test_devolucao_no_prazo_sem_multa(bib):
    emp = bib.emprestar(1, 1)
    assert bib.devolver(emp.id).multa == 0


def test_devolver_duas_vezes_falha(bib):
    emp = bib.emprestar(1, 1)
    bib.devolver(emp.id)
    with pytest.raises(ErroBiblioteca):
        bib.devolver(emp.id)


def test_listar_atrasos(bib):
    bib.emprestar(1, 1, hoje=date.today() - timedelta(days=30))
    bib.emprestar(2, 2)
    assert len(bib.listar_atrasos()) == 1


# -------------------------------------------------------------- Pesquisa
def test_pesquisa_case_insensitive_e_disponiveis(bib):
    assert [l.titulo for l in bib.pesquisar_livros("pessoa")] == ["Mensagem"]
    bib.emprestar(2, 1)
    assert bib.pesquisar_livros("pessoa", apenas_disponiveis=True) == []


def test_pesquisar_utentes(bib):
    assert [u.nome for u in bib.pesquisar_utentes("rui")] == ["Rui Costa"]


# ------------------------------------------------------------ Relatórios
def test_resumo_e_top(bib):
    bib.emprestar(1, 1)
    bib.emprestar(1, 2)
    r = bib.resumo()
    assert r["livros"] == 2 and r["emprestimos_ativos"] == 2
    assert bib.livros_mais_emprestados(1)[0][1] == 2


# ----------------------------------------------------------- Persistência
def test_persistencia_json(tmp_path):
    caminho = tmp_path / "b.json"
    b1 = Biblioteca(Repositorio(caminho))
    b1.adicionar_livro("Livro", "Autor", "123", 2000, "Geral")
    b1.adicionar_utente("Ana", "a@b.pt")
    b1.emprestar(1, 1)
    b2 = Biblioteca(Repositorio(caminho))
    assert b2.obter_livro(1).emprestados == 1
    assert b2.adicionar_livro("Outro", "A", "456", 2001, "Geral").id == 2
