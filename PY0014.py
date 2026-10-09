#Ejercicio 4
#David Simino Medina

n1 = float(input("Introduzca el primer número: "))
n2 = float(input("Introduzca el segundo número: "))
n3 = float(input("Introduzca el tercer número: "))

try:

    n1 = n1 * 0.15
    n2 = n2 * 0.35
    n3 = n3 * 0.50

    media = n1 + n2 + n3

    print(f"El resultado es: {media:.2f}")


except ValueError:
    print("Error. Valor introducido no válido.")