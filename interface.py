from tools import Dado

TEXTO_INICIO = "Vas a lanzar un dado"
TEXTO_FINAL = "Cerrando programa..."
TEXTO_OPCIONES = "Quieres continuar? (y/n)\n"

contador = 1
def interfaz():
    global contador
    print(f"Lanzamiento {contador}")
    caras = int(input("Dime las caras del dado que quieres lanzar: "))
    dado = Dado(caras)
    resultado = dado.tirar_dado()
    print(f"El resultado de tirar un dado de {caras} caras es {resultado}")
    contador += 1