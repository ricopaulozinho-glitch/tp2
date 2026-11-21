"""Interface de consola (menus de texto) do BiblioConsole."""

from __future__ import annotations

from .repository import Repositorio
from .services import Biblioteca, ErroBiblioteca

MENU = """
=== BiblioConsole ===
 1) Livros: adicionar        6) Utentes: adicionar
 2) Livros: listar           7) Utentes: listar
 3) Livros: editar           8) Utentes: editar / suspender
 4) Livros: remover          9) Utentes: remover
 5) Livros: pesquisar       10) Utentes: pesquisar
11) Emprestar livro         12) Devolver livro
13) Empréstimos ativos      14) Empréstimos em atraso
15) Resumo e estatísticas    0) Sair
"""


def pedir(texto: str) -> str:
    """Pede uma linha de texto ao utilizador."""
    return input(f"{texto}: ").strip()


def pedir_int(texto: str) -> int:
    """Pede um número inteiro, repetindo até ser válido."""
    while True:
        try:
            return int(pedir(texto))
        except ValueError:
            print("  Valor inválido: introduza um número inteiro.")


def mostrar_livros(livros) -> None:
    """Imprime uma tabela de livros."""
    if not livros:
        print("  (sem resultados)")
        return
    print(f"  {'ID':>3}  {'Título':<30} {'Autor':<20} {'Disp.':>5}")
    for l in livros:
        print(f"  {l.id:>3}  {l.titulo[:30]:<30} {l.autor[:20]:<20} {l.disponiveis:>2}/{l.exemplares:<2}")


def mostrar_utentes(utentes) -> None:
    """Imprime uma tabela de utentes."""
    if not utentes:
        print("  (sem resultados)")
        return
    for u in utentes:
        estado = " [SUSPENSO]" if u.suspenso else ""
        print(f"  {u.id:>3}  {u.nome:<25} {u.email}{estado}")


def mostrar_emprestimos(bib: Biblioteca, emprestimos) -> None:
    """Imprime uma tabela de empréstimos."""
    if not emprestimos:
        print("  (sem resultados)")
        return
    for e in emprestimos:
        livro = bib.repo.livros.get(e.livro_id)
        utente = bib.repo.utentes.get(e.utente_id)
        atraso = e.dias_atraso()
        extra = f"  ATRASO {atraso}d" if atraso else ""
        print(f"  #{e.id:<3} {livro.titulo if livro else '?':<28} "
              f"{utente.nome if utente else '?':<20} até {e.data_prevista}{extra}")


def executar(opcao: str, bib: Biblioteca) -> bool:
    """Executa a opção de menu. Devolve ``False`` para terminar."""
    if opcao == "0":
        return False
    if opcao == "1":
        l = bib.adicionar_livro(pedir("Título"), pedir("Autor"), pedir("ISBN"),
                                pedir_int("Ano"), pedir("Categoria"), pedir_int("Exemplares"))
        print(f"  Livro adicionado com ID {l.id}.")
    elif opcao == "2":
        mostrar_livros(bib.listar_livros())
    elif opcao == "3":
        lid = pedir_int("ID do livro")
        livro = bib.obter_livro(lid)
        print(f"  A editar '{livro.titulo}'. Deixe em branco para manter.")
        campos = {}
        for campo in ("titulo", "autor", "categoria"):
            v = pedir(campo.capitalize())
            if v:
                campos[campo] = v
        ex = pedir("Exemplares")
        if ex:
            campos["exemplares"] = int(ex)
        bib.editar_livro(lid, **campos)
        print("  Livro atualizado.")
    elif opcao == "4":
        lid = pedir_int("ID do livro")
        if pedir("Confirmar remoção (s/n)").lower() == "s":
            bib.remover_livro(lid)
            print("  Livro removido.")
    elif opcao == "5":
        mostrar_livros(bib.pesquisar_livros(pedir("Pesquisar"),
                                            pedir("Só disponíveis (s/n)").lower() == "s"))
    elif opcao == "6":
        u = bib.adicionar_utente(pedir("Nome"), pedir("Email"), pedir("Telefone"))
        print(f"  Utente registado com ID {u.id}.")
    elif opcao == "7":
        mostrar_utentes(bib.listar_utentes())
    elif opcao == "8":
        uid = pedir_int("ID do utente")
        utente = bib.obter_utente(uid)
        acao = pedir("Alterar nome (n), email (e) ou suspender/reativar (s)").lower()
        if acao == "n":
            bib.editar_utente(uid, nome=pedir("Novo nome"))
        elif acao == "e":
            bib.editar_utente(uid, email=pedir("Novo email"))
        elif acao == "s":
            bib.editar_utente(uid, suspenso=not utente.suspenso)
        else:
            print("  Opção inválida.")
            return True
        print("  Utente atualizado.")
    elif opcao == "9":
        uid = pedir_int("ID do utente")
        if pedir("Confirmar remoção (s/n)").lower() == "s":
            bib.remover_utente(uid)
            print("  Utente removido.")
    elif opcao == "10":
        mostrar_utentes(bib.pesquisar_utentes(pedir("Pesquisar")))
    elif opcao == "11":
        e = bib.emprestar(pedir_int("ID do livro"), pedir_int("ID do utente"))
        print(f"  Empréstimo #{e.id} registado. Devolver até {e.data_prevista}.")
    elif opcao == "12":
        e = bib.devolver(pedir_int("ID do empréstimo"))
        msg = f" Multa: {e.multa:.2f} €." if e.multa else ""
        print(f"  Devolução registada.{msg}")
    elif opcao == "13":
        mostrar_emprestimos(bib, bib.listar_emprestimos_ativos())
    elif opcao == "14":
        mostrar_emprestimos(bib, bib.listar_atrasos())
    elif opcao == "15":
        r = bib.resumo()
        print(f"  Livros: {r['livros']} ({r['exemplares']} exemplares) | Utentes: {r['utentes']}")
        print(f"  Empréstimos ativos: {r['emprestimos_ativos']} | Em atraso: {r['em_atraso']}")
        print("  Mais emprestados:")
        for livro, n in bib.livros_mais_emprestados():
            print(f"    {n}x {livro.titulo}")
    else:
        print("  Opção inválida.")
    return True


def main() -> None:
    """Ponto de entrada: ciclo principal do menu."""
    bib = Biblioteca(Repositorio())
    while True:
        print(MENU)
        try:
            if not executar(pedir("Opção"), bib):
                break
        except ErroBiblioteca as erro:
            print(f"  Erro: {erro}")
        except (EOFError, KeyboardInterrupt):
            print()
            break
    print("Até breve!")
