class FilaVazia(Exception):
    pass

class FilaArray:
    def __init__(self, capacidade = 5):
        self._fila = []
        self._capacidade = capacidade
        self._inicio = 0
        self._tamanho = 0
        
    
    
    def __len__(self):
        return self._tamanho
    
    def is_empty(self):
        return self._tamanho == 0
    
    def enqueue(self, element):
        self._tamanho = 

    
