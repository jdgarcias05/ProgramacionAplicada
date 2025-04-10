import csv
import random

num = [['#', 'Número aleatorio']]

for i in range(10):
    numero = random.random()
    num.append([i + 1, numero])

with open('numeros_aleatorios.csv', 'w', newline='', encoding='utf-8') as archivo_csv:
    escribir = csv.writer(archivo_csv)
    escribir.writerows(num)

print("Se guardaron 10 numeros aleatorios en 'valores_aleatorios.csv'")
