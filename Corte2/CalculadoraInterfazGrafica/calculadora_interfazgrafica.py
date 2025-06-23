import tkinter as tk
from tkinter import messagebox

class Calculadora:
    def suma(self, a, b):
        return a + b

    def resta(self, a, b):
        return a - b

    def multiplicacion(self, a, b):
        return a * b

    def division(self, a, b):
        try:
            return a / b
        except ZeroDivisionError:
            return "Error: división por cero"

    def modulo(self, a, b):
        try:
            return a % b
        except ZeroDivisionError:
            return "Error: módulo por cero"

# Funciones de la interfaz
def operar(operacion):
    try:
        n1 = float(entrada1.get())
        n2 = float(entrada2.get())
    except ValueError:
        messagebox.showerror("Entrada inválida", "Por favor ingresa números válidos.")
        return

    calc = Calculadora()
    resultado = ""

    if operacion == "suma":
        resultado = calc.suma(n1, n2)
    elif operacion == "resta":
        resultado = calc.resta(n1, n2)
    elif operacion == "multiplicacion":
        resultado = calc.multiplicacion(n1, n2)
    elif operacion == "division":
        resultado = calc.division(n1, n2)
    elif operacion == "modulo":
        resultado = calc.modulo(n1, n2)

    etiqueta_resultado.config(text=f"Resultado: {resultado}")

# Interfaz gráfica
ventana = tk.Tk()
ventana.title("Calculadora Básica")
ventana.geometry("300x300")

tk.Label(ventana, text="Número 1:").pack()
entrada1 = tk.Entry(ventana)
entrada1.pack()

tk.Label(ventana, text="Número 2:").pack()
entrada2 = tk.Entry(ventana)
entrada2.pack()

tk.Button(ventana, text="Sumar", command=lambda: operar("suma")).pack(pady=2)
tk.Button(ventana, text="Restar", command=lambda: operar("resta")).pack(pady=2)
tk.Button(ventana, text="Multiplicar", command=lambda: operar("multiplicacion")).pack(pady=2)
tk.Button(ventana, text="Dividir", command=lambda: operar("division")).pack(pady=2)
tk.Button(ventana, text="Módulo", command=lambda: operar("modulo")).pack(pady=2)

etiqueta_resultado = tk.Label(ventana, text="Resultado:")
etiqueta_resultado.pack(pady=10)

ventana.mainloop()
