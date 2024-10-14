class FilaVazia(Exception):
    pass

class FilaArray:
    def __init__(self, capacidade = 5):
        self._fila = [None] * capacidade
        self._capacidade = capacidade
        self._inicio = 0
        self._final = 0
        self._tamanho = 0
        
    
    
    def __len__(self):
        return self._tamanho
    
    def __str__(self):
        fila = []
        posicao = self._inicio
        for x in range (self._tamanho):
            fila.append(self._fila[posicao])
            posicao = (posicao + 1) % len(self._fila)
        return str(fila)

    def is_empty(self):
        return self._tamanho == 0
    
    
    def enqueue(self, element):
        if self._capacidade == self._tamanho:
            self._aumenta_capacidade()
        self._fila[self._final] = element
        self._tamanho += 1
        self._final = (self._final + 1) % len(self._fila)
    
    def dequeue(self):
        if self.is_empty():
            raise FilaVazia('A fila está vazia')
        primeiro, self._fila[self._inicio] = self._fila[self._inicio], None
        self._inicio = (self._inicio + 1) % len(self._fila)
        self._tamanho -= 1
        return primeiro
    
    def rodar(self):
        valor = self.dequeue()
        self.enqueue(valor)
        
    def _aumenta_capacidade(self):
        antiga_fila = self._fila
        self._capacidade = self._capacidade * 2
        self._fila = [None] * self._capacidade
        posicao = self._inicio
        for i in range(self._tamanho):
            self._fila[i] = antiga_fila[posicao]
            posicao = (posicao + 1) % len(antiga_fila)
        self._inicio = 0
        self._final = self._tamanho

    def first(self):
        if self.is_empty():
            raise FilaVazia('a fila está vazia')
        return self._fila[self._inicio]
    
    def size(self):
        return self._tamanho

    def list(self):
        fila = []
        posicao = self._inicio
        for x in range (self._tamanho):
            fila.append(self._fila[posicao])
            posicao = (posicao + 1) % len(self._fila)
        return fila


    
