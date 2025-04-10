capitales = ['Bogotá', 'Montería', 'Barranquilla', 'Ibagué', 'Medellín', 'Sincelejo']

print(capitales)
print(type(capitales))
print(capitales[1])

ncapital = str(input("\n Ingrese una nueva capital: "))

capitales.append(ncapital)
print(capitales)