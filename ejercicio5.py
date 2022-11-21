lista_numeros = []
lista_numeros_sqr = []


def list_exp(lista_numeros):
    """"
    Esta funcion crear una lista con los numeros introducidos por el usuario
    y crea una nueva lista con esos mismos numeros al cuadrado
    Parametros:
        -lista_numeros: es la lista creada con los numeros que introduce el usuario
    Salidas:
        -lista_numeros_sqr: es
    """
    while True:
        numero = int(input("Añade un numero al conjunto:\n"))
        if numero == 0:
            break

        lista_numeros.append(numero)
    for n in lista_numeros:
        n2 = 0
        n2 = n ** 2
        lista_numeros_sqr.append(n2)
    return lista_numeros_sqr


list_exp(lista_numeros)
help(list_exp)
print("Su lista de numeros al cuadrado es:", lista_numeros_sqr)