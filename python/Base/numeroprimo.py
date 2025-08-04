# Definir la función para verificar si un número es primo
import math
def es_numero_primo(numero):
    if numero <=1:
        return False
    if numero ==2:
        return True
    if numero % 2 == 0:
        return False


# Solicitar al usuario ingresar un valor entero
    for  i in(3, int(math.sqrt(numero)) + 1, 2):
        if numero % i == 0:
            return False
    return True
valor_ingresado = int(input("valor:"))
    # Llamar a la función y mostrar el resultado
    # no modifique el formato de impresión, requerido para la calificación del ejercicio
if es_numero_primo(valor_ingresado):
    print("Es primo")
else:
    print("No es primo")