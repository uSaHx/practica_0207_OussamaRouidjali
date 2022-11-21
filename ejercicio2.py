def factorial_recursivo(n):
    """
    Esta funcion imprime el calculo factorial del numero introducido
    mediante una funcion recursiva

    Parametros:
        -n_user: es el numero con que se calcula
    Salidas:
        -factorial: es el resultado del calculo
    """
    if n != 0:
        return n * factorial_recursivo(n-1)
    else:
        return 1

def factorial_iterativa(n):
    """"
    Esta funcion imprime el calculo factorial del numero introducido
    mediante una funcion iterativa

     Parametros:
        -n_user: es el numero con que se calcula
    Salidas:
        -factorial: es el resultado del calculo
    """
    fac = 1
    for y in range(1, n + 1):
        fac = fac * y
    return fac
n_user = int(input("Introduzca el numero para calcular el factorial:\n"))
print(factorial_iterativa(n_user))
print(factorial_recursivo(n_user))
help(factorial_iterativa)
help(factorial_recursivo)
