class Noh:
    def __init__(self, data):
        self._data = data
        self._next = None

    def setData(self, data):
        self._data = data
    def getData(self):
        return self._data
    
    def setNext(self, next):
        self._next = next
    def getNext(self):
        return self._next