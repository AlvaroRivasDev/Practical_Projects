edad = int(input (" ingrese su edad: "))
if edad > 19:
        print('mayor de edad')
else:
        print("menor de edad")

num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
num3 = float(input("Ingrese el tercer número: "))

promedio = (num1 + num2 + num3) / 3

if promedio > num1:
    print("El promedio es:", promedio)
else:
    producto = num1 * num2 * num3
    print("El producto es:", producto)