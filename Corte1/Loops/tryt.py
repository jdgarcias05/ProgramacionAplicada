print("------------------------------------------")
print("VERIFICADOR DE SUMAS")
print("------------------------------------------")
print("\nA continuación, se le solicatará ingresar tres números enteros. \n")
print("------------------------------------------")

a = int(input("Ingresa el primer número:\n"))
b = int(input("Ingresa el segundo número:\n"))
c = int(input("Ingresa el número resultado que quieres comprobar:\n"))

verificacion = a + b == c
vreal = a + b

print("El resultado para la verificación de los números ingresados es: ",verificacion)

if verificacion == False:
    print("El resultado correcto es: ",vreal)
print("------------------------------------------")
print("Saliendo del programa.")
