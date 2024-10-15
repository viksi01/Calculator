class Memory:
    def __init__(self):
        self._value = 0  

    def store(self, value):
        self._value = value

    def add(self, value):
        self._value += value

    def clear(self):
        self._value = 0

    def recall(self):
        return self._value