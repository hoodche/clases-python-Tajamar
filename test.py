from tools import Dado

def test_tirar_muchos_dados(numero_caras: int):
    dado = Dado(numero_caras)
    lista_resultados = []
    print(f"Test con {numero_caras} caras")
    for _ in range(10000):
        lista_resultados.append(dado.tirar_dado())

    for resultado in lista_resultados:
        if 0 < resultado < numero_caras + 1:
            continue
        raise ValueError(f"Esta tirada esta mal, su valor es {resultado}")
    print("El test fue exitoso")

numero_caras_test = 6
test_tirar_muchos_dados(numero_caras_test)

numero_caras_test = 8
test_tirar_muchos_dados(numero_caras_test)

numero_caras_test = 100
test_tirar_muchos_dados(numero_caras_test)

print("El codigo esta perfecto!")