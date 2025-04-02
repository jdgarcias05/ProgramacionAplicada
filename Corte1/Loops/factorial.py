while True:
    num = int(input("Ingresa un número entero positivo: "))
    print("\n Número: ", num, "\n")
    a = isinstance(num, int)
    if a == True and num > 0:
        factorial = 1
        for i in range (1, num + 1):
            factorial = factorial * i
        print(f"El factorial de ", num, " es:", factorial, "\n")
    else:
        print("Ingresa un valor válido. (Entero positivo) \n")