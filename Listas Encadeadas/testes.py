from ListaEncadeadaCircular import *

def mostrar_membros_projeto():
    eu = Membro('Alberto Cesar Pinheiro da Silva', 'albertocesar.be@gmail.com')
    print(eu)

def teste_adicao_membros():
    lista = ListaEncadeadaCircular()
    lista.adicionar_membro("Alice")
    lista.adicionar_membro("Bob")
    lista.adicionar_membro("Charlie")

    assert lista.proximo_responsavel() == "Bob", "Erro no primeiro responsável"
    assert lista.proximo_responsavel() == "Charlie", "Erro no segundo responsável"
    assert lista.proximo_responsavel() == "Alice", "Erro no terceiro responsável"
    assert lista.proximo_responsavel() == "Bob", "Erro na rotação cíclica"

def teste_remocao_membros():
    lista = ListaEncadeadaCircular()
    lista.adicionar_membro("Alice")
    lista.adicionar_membro("Bob")
    lista.adicionar_membro("Charlie")

    lista.remover_membro("Bob")

    assert lista.proximo_responsavel() == "Charlie", "Erro após remover membro"
    assert lista.proximo_responsavel() == "Alice", "Erro na rotação após remoção"
    assert lista.proximo_responsavel() == "Charlie", "Erro na rotação cíclica após remoção"

def teste_proximo_responsavel():
    lista = ListaEncadeadaCircular()
    lista.adicionar_membro("Alice")
    lista.adicionar_membro("Bob")

    assert lista.proximo_responsavel() == "Bob", "Erro no próximo responsável"
    assert lista.proximo_responsavel() == "Alice", "Erro no próximo responsável"
    assert lista.proximo_responsavel() == "Bob", "Erro na rotação cíclica"

# Executando os testes
if __name__ == '__main__':
    try:
        teste_adicao_membros()
        print("teste_adicao_membros passou com sucesso")
    except AssertionError as e:
        print(f"teste_adicao_membros falhou: {e}")

    try:
        teste_remocao_membros()
        print("teste_remocao_membros passou com sucesso")
    except AssertionError as e:
        print(f"teste_remocao_membros falhou: {e}")

    try:
        teste_proximo_responsavel()
        print("teste_proximo_responsavel passou com sucesso")
    except AssertionError as e:
        print(f"teste_proximo_responsavel falhou: {e}")
        
    mostrar_membros_projeto()
