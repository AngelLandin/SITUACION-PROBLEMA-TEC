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
        print(f"--------Bienvenido {self.nombre} al juego Matemático--------- \n Historia: Te adentras en el bosque donde los números viven en armonía. Para avanzar, debes resolver acertijos simples que te ayudarán a encontrar el camino correcto.")
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
        print("------------- Sigamos avanzandos por el BOSQUE DE LOS NÚMEROS!!! ----------------")

        numero_asientos = rd.randint(1,500)
        print(f'''
        Encuentro con los Animales: Un cine en el bosque tiene {numero_asientos} asientos. 
        Si el 70% están ocupados, ¿cuántos asientos quedan libres? 
        ''', end="")
        respuesta = float(input(""))
        correcta = (numero_asientos * 30) / 100
        self.registrar_respuesta(respuesta=respuesta, correcta=correcta) #Registrando respuesta.

        print("Ahora por último, para cruzar el BOSQUE DE LOS NÚMEROS debes analizar la siguiente afirmación")
        print('''
         Solo una de las siguientes afirmaciones es verdadera. ¿Cual es?
        (a) “(b) es verdadera”
        (b) “(e) es falsa”
        (c) “las afirmaciones desde (a) hasta (e) son verdaderas”
        (d) “las afirmaciones desde (a) hasta (e) son falsas”
        (e) “(a) es falsa”
        ''')
        respuesta = input(": ").lower()

        correcta = "e"

        self.registrar_respuesta(respuesta=respuesta, correcta=correcta)

        print(f"¡Felicidades {self.nombre}! Has recorrido con éxito el Bosque de los Números. \n El sendero ahora te lleva hacia un puente en el horizonte. ¡Continúa, aventurero, el desafío apenas comienza!")



    def nivel2(self):
        print(f"Nivel 2: El Puente de las Ecuaciones. \n Bienvenido de nuevo {self.nombre}, esta vez frente a ti, un largo y antiguo puente se extiende sobre un cañón. \n Pero no está solo. Un guardián enigmático custodia el paso, exigiendo que aquellos que deseen \n cruzar resuelvan ecuaciones para demostrar su sabiduría.")
        x = sp.symbols('x')
        a = rd.randint(1,10)
        b = rd.randint(1,10)
        c = rd.randint(1,10)
        equation = sp.Eq((a*x - 3)/2 + (b*x + 7)/3, c*x - 5)
        solution = sp.solve(equation, x)
        # Redondear la solución a 2 decimales
        rounded_solution = [sp.N(sol, 2) for sol in solution]
        print(f'''
“El guardián del puente te mira con ojos penetrantes. Solo los que resuelven los misterios de las ecuaciones 
              pueden cruzar, dice en voz profunda. Las cuerdas del puente vibran al compás
               de los números que flotan en el aire. Para avanzar, deberás desentrañar cada
               ecuación que el guardián te plantee.” (Responde con solo dos decimales)
            Resolver: ({a}*x - 3)/2 + ({b}*x + 7)/3, {c}*x - 5) = 0
''')
        respuesta = float(input(""))

        self.registrar_respuesta(respuesta, rounded_solution)

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

    #alumno1.nivel1()
    alumno1.nivel2()
    print(alumno1.puntuacion)

#"Has atravesado el Bosque de los Números y ahora puedes continuar tu aventura."