import sympy as sp
import random as rd
import math
from NivelAcademico import NivelAcademico
from minijuego import juego_final

class Secundaria(NivelAcademico):  
    cantidad_alumnos = []
    contador_alumnos = 0 

    def __init__(self, nombre, grado):
        super().__init__(nombre, grado)
        Secundaria.contador_alumnos += 1
        self._id = Secundaria.contador_alumnos
        self._puntuacion = 0  # Inicializar puntuación

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def grado(self):
        return self._grado

    @grado.setter
    def grado(self, grado):
        self._grado = grado

    @property
    def puntuacion(self):
        return self._puntuacion

    @puntuacion.setter
    def puntuacion(self, puntuacion):
        self._puntuacion = puntuacion

    # Métodos
    def nivel1(self):
        print(f"--------Bienvenido {self.nombre} al juego Matemático---------")
        print(self.leer_archivo('trama_historia\\ejercicio1.txt'))

        respuesta = input(": ")
        correcta = "redondo y azul"
        self.registrar_respuesta(respuesta, correcta)

        print('''
        Avancemos... ¡Ahora nos adentraremos al BOSQUE DE LOS NÚMEROS!
        ''')
        # A continuación, el cálculo y otros acertijos

    def nivel2(self):
        print(f"Nivel 2: El Puente de las Ecuaciones. \n")
        x = sp.symbols('x')
        a, b, c = rd.randint(1, 10), rd.randint(1, 10), rd.randint(1, 10)
        equation = sp.Eq((a*x - 3)/2 + (b*x + 7)/3 + (c*x - 5), 0)
        solution = sp.solve(equation, x)
        rounded_solution = [sp.N(sol, 2) for sol in solution]

        print(f"Resuelve: ({a}*x - 3)/2 + ({b}*x + 7)/3 + ({c}*x - 5) = 0")
        try:
            respuesta = float(input("Ingresa tu respuesta: "))
            self.registrar_respuesta(respuesta, rounded_solution[0])
        except ValueError:
            print("Por favor ingresa un número válido.")
        
        # Ecuación cuadrática
        print("Resolviendo ecuación cuadrática...")

        a, b, c = rd.randint(1, 20), rd.randint(1, 20), rd.randint(1, 20)
        equation = sp.Eq(a*x**2 + b*x + c, 0)
        solution = sp.solve(equation, x)
        rounded_solution = [sp.N(sol, 2) for sol in solution]
        
        print(f"{a}x^2 + {b}x + {c} = 0")

        try:
            respuesta1 = float(input("Cuanto vale X1: "))
            respuesta2 = float(input("Cuanto vale X2: "))
            self.registrar_doble_respuesta(rounded_solution[0], rounded_solution[1], respuesta1, respuesta2)
        except ValueError:
            print("Por favor ingresa un número válido.")

    def registrar_doble_respuesta(self, correcta1, correcta2, respuesta1, respuesta2):
        if respuesta1 == correcta1 and respuesta2 == correcta2:
            print("¡Ambas respuestas son correctas!")
            self.puntuacion += 2
        else:
            print(f"Respuestas incorrectas. Las correctas eran: {correcta1} y {correcta2}.")

if __name__ == '__main__':
    alumno1 = Secundaria("Eduardo", "secundaria")
    alumno1.nivel2()
    print(alumno1.puntuacion)
