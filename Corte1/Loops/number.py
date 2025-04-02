import random
from matplotlib import pyplot as obj #type:ignore

num_a = range(1,21) #El segundo número de este rango debe ser n+1 siendo n el rango del for de la línea 5.
num_b = [random.randint(1,1000) for a in range (20)]

obj.plot(num_a,num_b)
obj.show()

print("------------------------------------------")
print("Saliendo del programa.")
