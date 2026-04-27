""" profesor Joaquin Hernandez Martinez

hacer un ejercicio donde tengamos un callback en el que le metamos los args de CUALQUIER función + su nombre

nos debe guardar en una lista las funciones que hemos ido usando, y debe imprimir esta lista cada vez que usemos el callback """

auditoria = []

def auditar(funcion, *args):
    resultado = funcion(*args)  # aqui evaluo la funcion
    auditoria.append(funcion.__name__)
    print(f"Funciones ejecutadas: {auditoria}")
    return resultado  # si no se devuelve el callback no funciona!

res = auditar(print, "Estoy imprimiendo por pantalla")
print(res)
res = auditar(lambda n1, n2: n1 + n2, 1, 3)
print(res)
res = auditar(lambda n1: n1**2, 4)
print(res)
res = auditar(lambda *num: sum(num), 1, 3, 10, 100, 6)
print(res)
res = auditar(lambda str1, str2, str3: str1 + str2 + str3, "a", "b", "c")
print(res)