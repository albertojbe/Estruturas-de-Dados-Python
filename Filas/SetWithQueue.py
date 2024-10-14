from FilaArray import FilaArray

class SetWithQueue:
    def __init__(self) -> None:
        self._fila = FilaArray()
        self._hash = {}

    def add(self, e):
        if not self.contains(e):
            self._fila.enqueue(e)
            self._hash[e] = True

    def remove(self, e):
        if not self.contains(e):
            raise ValueError('Element not found')
        filaTemp = FilaArray()
        for _ in range(self._fila.size()):
            first = self._fila.dequeue()
            if not first == e:
                filaTemp.enqueue(first)
        self._fila = filaTemp

    
    def contains(self, e):
        if self._hash.get(e) == None:
            return False
        else:
            return True
        
        '''try:
            if self._hash[e] == True:
                return True
        except KeyError:
            return False'''

    def size(self):
        return self._fila.size()

    def list(self):
        return self._fila.list()