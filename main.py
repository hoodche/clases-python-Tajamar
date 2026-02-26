from interface import TEXTO_INICIO, TEXTO_FINAL, mostrar_menu
from tools import crear_dado, lanzar_dado

print(TEXTO_INICIO)
dado = None
while True:
    mostrar_menu()
    eleccion = input("\tElije tu opcion ---> ")
    if eleccion == "0":
        dado = crear_dado()
    if eleccion == "1":
        lanzar_dado(dado)
    if eleccion in ("n", "no", "stop"):
        break    
print(TEXTO_FINAL)