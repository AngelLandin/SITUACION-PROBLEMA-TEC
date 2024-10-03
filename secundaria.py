import sympy as sp #Libreria para el uso de algebra
import random as rd #Libreria para la generación de numeros aleatorios
from NivelAcademico import NivelAcademico
class Secundaria(NivelAcademico): #MODULO SECUNDARIA
    '''
    Class Secundaria: Clase exclusiva para alumnos del nivel secundaria, la cual contendra
    temas de algebra y geometria.
    '''
    cantidad_alumnos = []
    contador_alumnos = 0 #Variable de clase: Para contar la cantidad de alumnos que se vayan registrando
    def __init__(self, nombre, grado):
        super().__init__(nombre, grado) #Herencia de atributos de la clase padre.
        Secundaria.contador_alumnos += 1
        self._id = Secundaria.contador_alumnos
        #self._puntuacion = 0

#Encapsulamiento de atributos protegidos
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

    #PROBLEMAS ALGEBRAICOS
    def nivel1(self):
        print("--------Bienvenido al juego Matemático--------- \n Historia: Te adentras en el bosque donde los números viven en armonía. Para avanzar, debes resolver acertijos simples que te ayudarán a encontrar el camino correcto.")
        respuesta = input('''Luis escondió un objeto en su sombrero mágico, le dijo a Manuel que si adivinaba el color y la forma
        le regalaba un dulce. Para hacerlo más justo, Luis le dio las siguientes pistas:
        ■ Si es azul, entonces es redondo.
        ■ Si es cuadrado, entonces es rojo.
        ■ Es azul o amarillo.
        ■ Si es amarillo, entonces es cuadrado
        ■ Es cuadrado o redondo.
        ¿Cómo es el objeto?
        ''').lower()
        correcta = "redondo y azul"
        self.registrar_respuesta(respuesta, correcta)
        print('''
Avancemos... \u26D4 Ahora nos adentraremos al BOSQUE DE LOS NÚMEROS!!! \u26D4 
              Mientras avanzas por el Bosque de los Números, encuentras un anciano sabio 
              que te presenta tres acertijos matemáticos. 
              Para continuar tu camino, debes resolverlos.
''')
        x = rd.randint(1,25)
        x2 = rd.randint(1,10)
        x3 = rd.randint(1,10)
        x4 = rd.randint(1,10)
        x5 = rd.randint(1,10)
        x6 = rd.randint(1,10)
        print(f"Calcula: {x}({x2}+{x3})-({x4}^2)+({x5}^4): ", end="")
        respuesta = int(input(""))
        correcta = x*(x2+x3) - (x4**2) + (x5**4)

        self.registrar_respuesta(respuesta, correcta)

    def nivel2(self):
        print('''
Un tren sale de una ciudad a las 2:00 PM y viaja a 80 km/h. ¿A qué hora llegará a su destino si está a 240 km de distancia?


''')

    def nivel3(self):
        pass
    
    def desafio(self):
        pass


#PARTE TEORICA CON VERIFICACION DE STR.
#CLASE PARA TENER CONTROL DE DATOS.

if __name__ == '__main__':
    print("""
          Bienvenido al Desafío Matemático Nivel Secundaria. 
          Te cuento un poco la historia: eres un aventurero que necesita llegar a un lugar secreto, 
          un antiguo templo escondido en lo profundo de un bosque misterioso. Para descubrir su gran SECRETO, 
          debes superar una serie de desafíos matemáticos que te pondrán a prueba. 
          Cada nivel te acercará más a tu destino, y solo los más astutos lograrán desvelar el misterio.
""")

    alumno1 = Secundaria("Eduardo", "secundaria")

    alumno1.nivel1()
    #print(alumno1.puntuacion)

