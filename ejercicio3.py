def area_circulo(radio):
    """"
    Esta funcion imprime el area de un ciruclo con el radio introducido

    Parametros:
        -radio: es el radio del circulo que queremos calcular
    Salidas:
        -area: el area del circulo
    """
    area = 3.14 * (radio ** 2)
    return area


def volumen_cilindro(altura):
    """"
    Esta funcion imprime el volumen del cilindro apartir de la funcion area_circulo

    Parametros:
        -altura: la altura del cilindro
    Salidas:
        -volumen: es el volumen resultante del calculo
    """
    area = area_circulo(radio)
    volumen = area * altura
    return volumen


radio = float(input("Introduzca el radio del circulo:\n"))
area = area_circulo(radio)
altura = float(input("Introduzca la altura del cilindro:\n"))
volumen = volumen_cilindro(altura)

help(area_circulo)
help(volumen_cilindro)
print("El area del circulo es,", area, "metros cuadrados")
print("El volumen del cilindro es,", volumen, "metros cubicos")