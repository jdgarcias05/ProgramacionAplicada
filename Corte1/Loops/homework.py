a = input("Ingresa un número 1: \n")
a = int(a)
b = input("Ingresa un número 2: \n")
b = float(b)
c = a + b
print(" ------------------------------------------ ")

if a == b:
    print("Los números ingresados, son iguales.")
    print(" ------------------------------------------ ")
else:
    print("Los números ingresados, son distintos.")
    print(" ------------------------------------------ ")

print ("El tipo del número a es: ", type(a))
print ("El tipo del número b es: ", type(b))
print ("El resultado de la suma es: ", c)
print(" ------------------------------------------ ")

if type(a) == type(b):
    print("Los tipos de cada número son iguales.")
    print(" ------------------------------------------ ")
    print("Saliendo del programa.")
else:
    print("Los tipos de cada número, son distintos.")
    print(" ------------------------------------------ ")
    print("Saliendo del programa. \n")