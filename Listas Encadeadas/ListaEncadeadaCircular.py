from Noh import *

class Membro:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email

    def __str__(self):
        return f"\nNome: {self.nome}\nEmail: {self.email}"

class ListaEncadeadaCircular:
    def __init__(self) -> None:
        self._head = None
        self._tail = None
        self._atual = None

    def is_empty(self):
        return self._head == None
    
    def adicionar_membro(self, data):
        temp = Noh(data)
        if self._head == None:
            self._head = temp
            self._head.setNext(self._head)
            self._atual = self._head
        else:
            atual = self._head
            while atual.getNext() != self._head:
                atual = atual.getNext()
            atual.setNext(temp)
            temp.setNext(self._head)
        

    def remover_membro(self, data):
        if self._head == None:
            return
        if self._head.getData() == data:
            if self._head.getNext() == self._head:
                self._head = None
            else:
                atual = self._head
                while atual.getNext() != self._head:
                    atual = atual.getNext()
                atual.setNext(self._head.getNext())
                self._head = self._head.getNext()
            return
        
        anterior = self._head
        atual = self._head.getNext()
        while atual != self._head:
            if atual.getData() == data:
                anterior.setNext(atual.getNext())
                return
            anterior = atual
            atual = atual.getNext()

    def proximo_responsavel(self):
        self._atual = self._atual.getNext()
        return str(self._atual.getData())
            
    def mostrar_lista(self):
        if self._head == None:
            return "[]"
        lista = "[" + str(self._head.getData())
        atual = self._head.getNext()
        while atual != self._head:
            lista += ", "
            lista += str(atual.getData())
            atual = atual.getNext()

        lista += "]"
        return lista
        

