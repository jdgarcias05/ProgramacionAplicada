#vocales =  {"Primera": "a", "Segunda": "e", "Tercera": "i", "Cuarta": "o", "Quinta": "u"}

#print("Las vocales son: ", vocales)

## Diccionario para gestión logística de cursos académicos.
cantidad_estudiantes = {'Programacion Aplicada': "64",'Programacion Basica': "98",'Programacion Orientada a Objetos': "87"}

salones = { 'Programacion Aplicada': 'Sabio Caldas 506','Programacion Basica': 'Sabio Caldas 503','Programacion Orientada a Objetos': 'Administrativo 402'}

print("\n A continuación, se mostrarán las materias y su cantidad de estudiantes.")
print(" ------------------------------- ")
print(cantidad_estudiantes)

print("\n A continuación, se mostrarán las materias y los salones donde se dicta.")
print(" ------------------------------- ")
print(salones)

materianueva = input("\nIngrese el nombre para la nueva materia: ")
cantidad_estudiantesmaterianueva = input("Ingrese la cantidad de usuarios para la nueva materia: ")
salon = input("Ingrese el salón en el que se dicta la nueva materia: ")

cantidad_estudiantes.update({materianueva: cantidad_estudiantesmaterianueva})
salones.update({materianueva: salon})

print("\n A continuación, se muestran las listas actualizadas:")
print(cantidad_estudiantes)
print(" ------------------------------- ")
print(salones)

