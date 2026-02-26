import random
import interface
from typing import Optional

class Dado:
    def __init__(self, caras: int):
        self.caras = list(range(1, caras + 1))
        self.ultima_cara = caras
        
    def tirar_dado(self):
        return random.choice(self.caras)
    
contador = 1
def crear_dado() -> Dado:
    caras = int(input("Dime las caras del dado que quieres crear: "))
    dado = Dado(caras)
    print(f"Has creado un dado con {caras} caras")
    return dado
    
def lanzar_dado(dado: Optional[Dado]) -> int:
    global contador
    if dado:
        print(f"\nLanzamiento {contador}")
        contador += 1
        resultado = dado.tirar_dado()
        print(f"Lanzando dado de {dado.ultima_cara} es {resultado}")
    else:
        print(interface.TEXTO_ERROR_NO_DADO)