palabras = []

def contador_palabras(texto):
    """"
    Esta funcion crea un diccionario donde la clave es la cantidad de veces que aparece la palabra
    en el texto introducido. Y cada palabara es una entrada del diccionario y el es valor
    Parametros:
        -texto: es el texto introducido
    Salidas:
        -dic_frecuencia: es el diccionario que tiene por claves la frecuencia y por valor las palabras qu
                         que componen el texto
    """
    dic_frecuencia = {}
    palabras = texto.split()
    for i in palabras:
        dic_frecuencia[palabras.count(i)] = i
    return dic_frecuencia

def max_frec(diccionario):
    """"
    Esta funcion usa el diccionario creado en la funcion contador_palabras y saca la palabra con mas frecuncia
    (mayor valor de la clave)
    Parametros:
        -diccicionario: es la variable donde esta guardada el diccionario de la anterior funcion
    Salidas:
        -diccionario[max(frecuencia)]: saca el valor asociada a la calve mas alta del diccionario.
    """

    frecuencia = diccionario.keys()
    return diccionario[max(frecuencia)]

texto = input("Introduzca el texto que quiere contear:\n")
diccionario = contador_palabras(texto)
print(contador_palabras(texto))
print("La palabra que más se repite es:",max_frec(diccionario))
help(contador_palabras)
help(max_frec)