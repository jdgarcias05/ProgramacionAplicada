import tkinter as tk
from tkinter import messagebox
from operaciones import Calculadora

class InterfazCalculadora:
    def __init__(self):
        self.calculadora = Calculadora()
        self.ventana = tk.Tk()
        self.ventana.title("Calculadora OOP")
        self.ventana.geometry("300x320")
        self.crear_componentes()
        self.ventana.mainloop()

    def crear_componentes(self):
        tk.Label(self.ventana, text="Número 1:").pack()
        self.entrada1 = tk.Entry(self.ventana)
        self.entrada1.pack()

        tk.Label(self.ventana, text="Número 2:").pack()
        self.entrada2 = tk.Entry(self.ventana)
        self.entrada2.pack()

        operaciones = [
            ("Sumar", self.calculadora.suma),
            ("Restar", self.calculadora.resta),
            ("Multiplicar", self.calculadora.multiplicacion),
            ("Dividir", self.calculadora.division),
            ("Módulo", self.calculadora.modulo)
        ]

        for texto, funcion in operaciones:
            tk.Button(self.ventana, text=texto, command=lambda f=funcion: self.operar(f)).pack(pady=2)

        self.resultado = tk.Label(self.ventana, text="Resultado:")
        self.resultado.pack(pady=10)

    def operar(self, funcion_operacion):
        try:
            a = float(self.entrada1.get())
            b = float(self.entrada2.get())
            resultado = funcion_operacion(a, b)
            self.resultado.config(text=f"Resultado: {resultado}")
        except ValueError:
            messagebox.showerror("Error", "Por favor ingresa valores numéricos válidos.")

if __name__ == "__main__":
    InterfazCalculadora()
