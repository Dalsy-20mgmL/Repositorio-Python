#Ejercicio 3
#David Simino Medina

while True:
    try:
        entrada = int(input("Introduzca un número entero: "))

        if entrada % 2 == 0:
            print("Es un número par. No es válido.")
        else:
            print("Es un número impar. Es válido.")
            break

    except ValueError:
        print("Error. Debe introducir un número entero.")