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
    
    

