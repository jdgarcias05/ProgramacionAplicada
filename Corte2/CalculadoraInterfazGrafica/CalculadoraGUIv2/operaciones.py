class Calculadora:
    def suma(self, a, b):
        return a + b

    def resta(self, a, b):
        return a - b

    def multiplicacion(self, a, b):
        return a * b

    def division(self, a, b):
        if b == 0:
            return "Error: división por cero"
        return a / b

    def modulo(self, a, b):
        if b == 0:
            return "Error: módulo por cero"
        return a % b
