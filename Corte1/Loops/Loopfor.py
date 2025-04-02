import time

palabra = "Colombia"
print("------------------------------------------")

for letra in palabra:
    if letra == 'o':
        continue
    print(letra)
    time.sleep(0.750)
print("------------------------------------------")
print("Saliendo del programa.")
