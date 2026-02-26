import random

class Dado:
    def __init__(self, caras: int):
        self.caras = list(range(1, caras + 1))
        
    def tirar_dado(self):
        return random.choice(self.caras)