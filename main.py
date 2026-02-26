from interface import TEXTO_INICIO, TEXTO_FINAL, TEXTO_OPCIONES, interfaz

print(TEXTO_INICIO)
continuar = ""
while continuar.lower() not in ("no", "n", "stop"):
    interfaz()
    continuar = input(TEXTO_OPCIONES)
print(TEXTO_FINAL)