def dec_bin(decimal):
    """"
    Esta funcion convierte el numero decimal introducido a su equivalente en binario

    Parametros:
        -decimal= es el numero que introduce el usuario para ser convertido a binario
    Salidas:
        -binraio= es el deciaml numero ya convertido a binario
    """
    binario = 0
    multiply = 1
    while decimal != 0:
        binario = binario + decimal % 2 * multiply
        decimal //= 2
        multiply *= 10
    return binario


def bin_dec(binario):
    """"
    Esta funcion convierte el numero binario introducido a su equivalente en decimal

    Parametros:
        -binario= es el numero que introduce el usuario para ser convertido a binario
    Salidas:
        -decimal= es el numero binario introducido ya convertido a decimal
    """
    decimal = 0
    for posicion, digito in enumerate(binario[::-1]):
        decimal += int(digito) * 2 ** posicion
    return decimal


print(dec_bin(int(input("Introduzca el numero decimal que quieres convertir a binario:\n"))))
print(bin_dec(input("Introduzca el numero binario que quieres convertir a decimal:\n")))