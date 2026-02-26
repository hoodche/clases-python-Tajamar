from tools import tirar_dado

lista_resultados = []

for _ in range(10000):
    lista_resultados.append(tirar_dado())

for resultado in lista_resultados:
    if 0 < resultado < 7:
        continue
    raise ValueError(f"Esta tirada esta mal, su valor es {resultado}")
print("El codigo esta perfecto!")