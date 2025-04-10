import csv

capitales = ['Bogotá', 'Montería', 'Barranquilla', 'Ibagué', 'Medellín', 'Sincelejo']


with open('capitales.csv', 'w', newline='', encoding='utf-8') as archivo_csv:
    escritor_csv = csv.writer(archivo_csv)
    escritor_csv.writerows(capitales)

print("Archivo guardado.")
