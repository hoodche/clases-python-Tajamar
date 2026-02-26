from tools import tirar_dado

def test_tirar_muchos_dados(numero_caras: int):
    lista_resultados = []
    print(f"Test con {numero_caras} caras")
    for _ in range(10000):
        lista_resultados.append(tirar_dado(numero_caras))

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