# Solicitar al usuario ingresar un nombre y un apellido
nombre = str(input("nombre:"))
apellido = str(input("apellido:"))

# Contar los caracteres de cada cadena
print(len(nombre))
print(len(apellido))

# Calcular la cantidad total de caracteres
total_caracteres = len(nombre + apellido)

# Imprimir el resultado, no modifique el formato de impresión, requerido para la calificación
print(f"Cantidad de caracteres entre '{nombre}' y '{apellido}' es: {total_caracteres}")
