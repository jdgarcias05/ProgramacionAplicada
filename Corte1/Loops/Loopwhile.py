print("------------------------------------------")
print("LISTA DE NÚMEROS")
print("------------------------------------------")
print("\nA continuación, se solicitarán dos números enteros para conocer\n","los números enteros que hay entre ellos. Sin incluir a los que ingreses.")
print("------------------------------------------")

a = int(input("Ingresa tu primer número: \n"))
b = int(input("Ingresa tu segundo número: (mayor al número anterior al menos, en dos unidades.) \n"))
print("------------------------------------------")

if a<b:
    for ind in range (a,b):
        d=b-2
        while ind <= d:
            ind += 1
            print (ind)
        break
else:
    print("Error. El segundo número es menor o igual al primero.\n","Intente nuevamente.")
print("------------------------------------------")
print("Saliendo del programa.")
print("------------------------------------------")
