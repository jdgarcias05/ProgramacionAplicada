class Calculadora:
    def __init__(self):
        pass

    def suma(self, a, b):
        return a+b
    
    def resta(self,a,b):
        return a-b
    
    def multiplicacion(self,a,b,):
        return a*b
    
    def division(self,a,b,):
        try:
            return a/b
        except ZeroDivisionError:
            print("No es posible dividir entre cero.")
        else:
            print("La divisón pudo ser realizada con éxito.\n")

    def modulo(self,a,b):
        try:
            return a%b
        except ZeroDivisionError:
            print("No es posible dividir entre cero.")
        else:
            print("El módulo pudo ser obtenido con éxito.\n")
    
    from operaciones import Calculadora #importar clase

op = Calculadora() #creación objeto

try:
    print("\n----------------------------------------------\n")
    n1 = int(input("Ingresa un primer número entero. \n"))
    n2 = int(input("\n Ingresa un segundo número entero.\n"))
except ValueError:
    print("\n----------------------------------------------\n")
    print("Error: solo debes ingresar números.")
    print("\n----------------------------------------------\n")
else:
    try:
        divisor = op.division(n1,n2)
        mod = op.modulo(n1,n2)
    except ZeroDivisionError:
        print("\n----------------------------------------------\n")
        print("Error: no es posible dividir entre cero.")
        print("\n----------------------------------------------\n")
    else:
        print("\nLos resultados para las operaciones suma, resta, multiplicación, división y módulo de los números ingresados, son: \n")
        print(op.suma(n1,n2),"|", op.resta(n1,n2),"|", op.multiplicacion(n1,n2),"|", divisor,"|",mod, "|")
        print("\n----------------------------------------------\n")


