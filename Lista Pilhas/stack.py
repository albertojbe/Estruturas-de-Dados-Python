class PilhaVazia(Exception):
    pass

class Pilha:
    def __init__(self):
        self.pilha = []
    
    def __len__(self):
        return len(self.pilha)
    
    def __str__(self):
        return str(self.pilha)
    
    def push(self, valor):
        return self.pilha.append(valor)
    
    def pop(self):
        if self.__len__() == 0:
            raise PilhaVazia('A pilha está vazia')
        return self.pilha.pop()
    
    def top(self):
        return self.pilha[-1]
    
    def size(self):
        tamanho = self.__len__()
        if tamanho == 0:
            raise PilhaVazia('A pilha está vazia')
        return tamanho

    def isEmpity(self):
        return self.__len__() == 0
    
        