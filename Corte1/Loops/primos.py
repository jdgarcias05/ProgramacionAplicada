import time

inicio = time.time()
print("------------------------------------------")

print("VERIFICADOR DE NÚMEROS PRIMOS\n")
print("A continuación, se le solicitará establecer los límites para la verificación de números primos. \n")
n1 = int(input("Ingresa el número menor:\n"))
n2 = int(input("Ingresa el número mayor:\n"))

print("------------------------------------------")

for a in range(n1,n2):
    contador = 0
    for b in range(1,a+1):
        residuo = a%b
        if residuo == 0:
            contador = contador + 1
    
    if contador == 2:
        print(a," es un número primo.")

final = time.time()
tiempo = (final-inicio)*1000 #Tiempo en segundos

print("La duración de ejecución este código fue de: ",tiempo)
print("------------------------------------------")
print("Saliendo del programa.")