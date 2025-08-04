def par(n):
    divisor==2
    if n%divisor==0:
        return True
    else:
        return False

n=int(input("numero:"))
divisor=2
print("el divisor utilizado para el calculo:",divisor)
if par(n)==True:
    print("el numero es par.")
else:
    print("el numero es impar")