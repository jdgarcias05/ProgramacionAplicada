import csv

try:
    with open('lectura.csv', 'r', encoding='utf-8') as archivo_csv:
        lector_csv = csv.reader(archivo_csv)
        print("Contenido del archivo:\n")
        for fila in lector_csv:
            print(fila)
except FileNotFoundError:
    print("El archivo no existe. Primero tienes que crearlo con el otro código.")
