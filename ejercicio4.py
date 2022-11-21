def media(lista_numeros):
    """"
    Esta funcion realiza la media aretimetica con los numeros introducidos

    -Parametros:
        -lista_numeros: es la lista de numeros creada por los numeros introducidos por el usuario
    -Salidas:
        -media: es el resultado de la media aritmetica
    """
    while True:
        numero = int(input("Añade un numero al conjunto:\n"))
        if numero == 0:
            break
        lista_numeros.append(numero)
        sumatorio = sum(lista_numeros)
        n_numero = len(lista_numeros)
        media = sumatorio / n_numero
    return media


lista_numeros = []

print("La media aritmetica es", media(lista_numeros))
help(media)
