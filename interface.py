TEXTO_INICIO = f"SIMULADOR DE LANZAMIENTO DE DADOS\n{"="*36}"
TEXTO_FINAL = "Cerrando programa..."
TEXTO_OPCION = "\tElije tu opcion ---> "
TEXTO_ERROR_NO_DADO = "Antes de lanzar el dado, tienes que crearlo"
TEXTO_ERROR_OPCION_DESCONOCIDA = "Opcion desconocida, repitiendo instrucciones..."

def mostrar_menu():
    mensaje = """
    0 - Crear un dado
    1 - Lanzar el dado
    no o stop para el programa
    
    """
    print(mensaje)