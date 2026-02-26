import random

def tirar_dado(numero_caras: int) -> int:
    caras = list(range(1, numero_caras + 1))
    return random.choice(caras)