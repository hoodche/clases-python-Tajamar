import interface
from tools import crear_dado, lanzar_dado

print(interface.TEXTO_INICIO)
dado = None
while True:
    interface.mostrar_menu()
    eleccion = input(interface.TEXTO_OPCION)
    if eleccion in ("n", "no", "stop"):
        break
    if eleccion == "0":
        dado = crear_dado()
    elif eleccion == "1":
        if dado:
            lanzar_dado(dado)
        else:
            print(interface.TEXTO_ERROR_NO_DADO)
    else:
        print(interface.TEXTO_ERROR_OPCION_DESCONOCIDA)
print(interface.TEXTO_FINAL)