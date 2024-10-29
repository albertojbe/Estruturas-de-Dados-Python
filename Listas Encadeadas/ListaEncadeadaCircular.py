from Noh import *

class ListaEncadeadaCircular:
    def __init__(self) -> None:
        self._head = None
        self._tail = None

    def is_empty(self):
        return self._head == None
    
    def add(self, data):
        temp = Noh(data)
        if self._head == None:
            self._head = temp
            self._tail = temp
            self._head.setNext(self._tail)
            self._tail.setNext(self._head)
        else:
            temp.setNext(self._head)
            self._tail.setNext(temp)
            self._tail = temp

    def remove(self, data):
        temp = Noh(data)
        atual = self._head
        do while atual
