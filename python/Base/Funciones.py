# Definir la función para verificar si un número es múltiplo de 5
# retorna un valor booleano, puede modificar lo necesario pero no las impresiones
def es_multiplo_de_5(numero):
    if numero % 5 == 0:
        return True
    else:
        return False
# Solicitar al usuario ingresar un valor entero
valor = int(input("ingrese un valor:"))
# Llamar a la función y mostrar el resultado
# no modifique el formato de impresión, requerido para la corrección del ejercicio
if es_multiplo_de_5(valor):
    print("Múltiplo de 5")
else:
    print("No es múltiplo de 5")