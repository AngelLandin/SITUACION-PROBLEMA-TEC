import sympy as sp  # Librería para el uso de álgebra simbólica
import random as rd  # Librería para la generación de números aleatorios
from NivelAcademico import NivelAcademico  # Importa la clase base NivelAcademico
import math  # Librería para cálculos matemáticos
from minijuego import juego_final  # Importa el módulo del minijuego

class Secundaria(NivelAcademico): 
    '''
    Class Secundaria: Clase exclusiva para alumnos del nivel secundaria, la cual contendrá
    temas de álgebra y geometría. Hereda de NivelAcademico.
    '''
    cantidad_alumnos = []  # Lista para almacenar a los alumnos
    contador_alumnos = 0  # Contador de alumnos registrados

    # Constructor de la clase
    def __init__(self, nombre, grado, puntuacion):
        '''
        Inicializa los atributos nombre, grado y puntuación del alumno.
        Pregunta si el usuario quiere iniciar el juego.
        '''
        self._nombre = nombre 
        self._grado = grado
        self._puntuacion = puntuacion

        # Preguntar si el usuario quiere iniciar el juego
        self.iniciar_juego()

    # Métodos de encapsulamiento para los atributos protegidos
    @property
    def nombre(self):
        '''Getter para el atributo nombre'''
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        '''Setter para el atributo nombre'''
        self._nombre = nombre

    @property
    def grado(self):
        '''Getter para el atributo grado'''
        return self._grado

    @grado.setter
    def grado(self, grado):
        '''Setter para el atributo grado'''
        self._grado = grado

    @property
    def puntuacion(self):
        '''Getter para el atributo puntuacion'''
        return self._puntuacion

    @puntuacion.setter
    def puntuacion(self, puntuacion):
        '''Setter para el atributo puntuacion'''
        self._puntuacion = puntuacion        

    # Método para iniciar el juego basado en la decisión del usuario
    def iniciar_juego(self):
        '''
        Pregunta al usuario si desea iniciar el juego.
        Si la respuesta es afirmativa, muestra el menú de niveles.
        Si la respuesta es negativa, sale del método.
        '''
        print("¿Quieres iniciar el juego? (si/no)")
        respuesta = input().lower()

        if respuesta == "si":
            self.mostrar_menu_niveles()  # Muestra el menú de niveles si el jugador acepta iniciar el juego
        else:
            print("Juego no iniciado. ¡Gracias por visitar!")
            return  # Sale del método para no continuar con el flujo del programa

    # Método para mostrar el menú de niveles
    def mostrar_menu_niveles(self):
        '''
        Muestra un menú con las opciones de los diferentes niveles del juego
        y permite al usuario seleccionar cuál desea jugar.
        '''
        while True:
            print("\nSelecciona un nivel para jugar:")
            print("1. Nivel 1: El Bosque de los Números")
            print("2. Nivel 2: El Puente de las Ecuaciones")
            print("3. Nivel 3: La Montaña de la Geometría")
            print("4. Desafío Final")
            print("5. Salir del juego")
            
            seleccion = input("Elige una opción (1-5): ")
            
            if seleccion == "1":
                self.nivel1()
            elif seleccion == "2":
                self.nivel2()
            elif seleccion == "3":
                self.nivel3()
            elif seleccion == "4":
                self.desafio_final()
            elif seleccion == "5":
                print("Saliendo del juego. ¡Hasta pronto!")
                break
            else:
                print("Opción inválida. Inténtalo de nuevo.")

    # Primer nivel: acertijos matemáticos en el "Bosque de los Números"
    def nivel1(self):
        '''
        Nivel 1 del juego: "El Bosque de los Números".
        Presenta acertijos matemáticos simples al jugador.
        '''
        print(f"--------Bienvenido {self.nombre} al juego Matemático--------- \n Historia: Te adentras en el bosque donde los números viven en armonía. Para avanzar, debes resolver acertijos simples que te ayudarán a encontrar el camino correcto.")
        with open('trama_historia\\ejercicio1.txt', 'r', encoding='UTF-8') as archivo:
            print(archivo.read())

        # Respuesta del jugador
        respuesta = input(": ")
        correcta = "redondo y azul"
        self.registrar_respuesta(respuesta, correcta)
        print('''
Avancemos... \u26D4 Ahora nos adentraremos al BOSQUE DE LOS NÚMEROS!!! \u26D4 
              Mientras avanzas por el Bosque de los Números, encuentras un anciano sabio 
              que te presenta tres acertijos matemáticos. 
              Para continuar tu camino, debes resolverlos.
''')

        # Generación de números aleatorios para el ejercicio matemático
        x = rd.randint(1,25)
        x2 = rd.randint(1,10)
        x3 = rd.randint(1,10)
        x4 = rd.randint(1,10)
        x5 = rd.randint(1,10)
        print(f"Calcula: {x}({x2}+{x3})-({x4}^2)+({x5}^4): ", end="")
        respuesta = int(input(""))
        correcta = x*(x2+x3) - (x4**2) + (x5**4)

        # Verificar respuesta
        self.registrar_respuesta(respuesta, correcta)
        print("------------- Sigamos avanzando por el BOSQUE DE LOS NÚMEROS!!! ----------------")

        # Otro ejercicio matemático
        numero_asientos = rd.randint(1,500)
        print(f'''
        Encuentro con los Animales: Un cine en el bosque tiene {numero_asientos} asientos. 
        Si el 70% están ocupados, ¿cuántos asientos quedan libres? 
        ''', end="")
        respuesta = float(input(""))
        correcta = (numero_asientos * 30) / 100
        self.registrar_respuesta(respuesta=respuesta, correcta=correcta)

        # Tercer ejercicio del nivel 1
        with open('trama_historia\\ejercicio3.txt', 'r', encoding='UTF-8') as archivo:
            print(archivo.read())
        respuesta = input(": ").lower()
        correcta = "e"
        self.registrar_respuesta(respuesta=respuesta, correcta=correcta)
        print(f"¡Felicidades {self.nombre}! Has recorrido con éxito el Bosque de los Números. \n El sendero ahora te lleva hacia un puente en el horizonte. ¡Continúa, aventurero, el desafío apenas comienza!")

    # Segundo nivel: el "Puente de las Ecuaciones"
    def nivel2(self):
        '''
        Nivel 2 del juego: "El Puente de las Ecuaciones".
        Presenta ecuaciones que el jugador debe resolver.
        '''
        print(f"Nivel 2: El Puente de las Ecuaciones. \n Bienvenido de nuevo {self.nombre}, esta vez frente a ti, un largo y antiguo puente se extiende sobre un cañón. \n Pero no está solo. Un guardián enigmático custodia el paso, exigiendo que aquellos que deseen \n cruzar resuelvan ecuaciones para demostrar su sabiduría.")
        x = sp.symbols('x')  # Definir variable simbólica
        a = rd.randint(1,10)
        b = rd.randint(1,10)
        c = rd.randint(1,10)
        equation = sp.Eq((a*x - 3)/2 + (b*x + 7)/3 + (c*x - 5), 0)  # Definir ecuación
        solution = sp.solve(equation, x)  # Resolver la ecuación
        rounded_solution = [sp.N(sol, 2) for sol in solution]  # Redondear la solución a dos decimales
        print(f'''
“El guardián del puente te mira con ojos penetrantes. Solo los que resuelven los misterios de las ecuaciones 
              pueden cruzar, dice en voz profunda. Las cuerdas del puente vibran al compás
               de los números que flotan en el aire. Para avanzar, deberás desentrañar cada
               ecuación que el guardián te plantee.” (Responde con solo dos decimales)
            Resolver: ({a}*x - 3)/2 + ({b}*x + 7)/3) + ({c}*x - 5) = 0
''')
        
        try:
            respuesta = float(input(""))
            self.registrar_respuesta(respuesta, rounded_solution[0])

            print(f'''Excelente, prosigramos {self.nombre}, 
                Para demostrar tu valía, deberás resolver la siguiente ecuación que ha protegido este puente por siglos. 
                Si logras encontrar las soluciones, el camino hacia el templo se abrirá para ti.''')
            
            a = rd.randint(1,20)
            b = rd.randint(1,20)
            c = rd.randint(1,20)
            equation = sp.Eq((a*x**2 - 3) + (b*x) + (c), 0)
            solution = sp.solve(equation, x)
            rounded_solution = [sp.N(sol, 2) for sol in solution]

            print(f'''
    {a}x^2 + {b}x + {c} = 0
    ''')

            respuesta1 = float(input("Cuánto vale X1: "))
            respuesta2 = float(input("Cuánto vale X2: "))
            self.registrar_doble_respuesta(correcta1=rounded_solution[0], correcta2=rounded_solution[1], respuesta1=respuesta1, respuesta2=respuesta2)
        except Exception as ex:
            print(f"Ocurrió un Error: {ex}")

        # Tercer ejercicio del nivel 2
        with open('trama_historia\\ejercicio6.txt', 'r', encoding='UTF-8') as archivo:
            print(archivo.read())
        respuesta = int(input(""))
        correcta = 3
        self.registrar_respuesta(respuesta=respuesta, correcta=correcta)
        print('''
            Has cruzado el puente con éxito y te diriges hacia la Montaña de la Geometría,
            donde nuevos desafíos te esperan.
''')

    # Tercer nivel: la "Montaña de la Geometría"
    def nivel3(self):
        '''
        Nivel 3 del juego: "La Montaña de la Geometría".
        Presenta acertijos relacionados con geometría.
        '''
        with open('trama_historia\\nivel3.txt', 'r', encoding='UTF-8') as archivo_leer:
            print(archivo_leer.read())

        lado = rd.randint(1,25)  # Valor aleatorio para el lado del triángulo
        print(f"Dado un triángulo equilátero con un lado de {lado} cm, calcula su altura y su área.")
        
        correcta1 = float("{:.2f}".format(math.sqrt(lado**2-(lado/2)**2)))  # Cálculo de la altura
        correcta2 = float("{:.2f}".format((lado*correcta1)/2))  # Cálculo del área
        respuesta = float(input("Altura: "))
        respuesta2 = float(input("Área: "))
        self.registrar_doble_respuesta(correcta1=correcta1, correcta2=correcta2, respuesta1=respuesta, respuesta2=respuesta2)

        # Segundo ejercicio del nivel 3
        theta = rd.randint(1, 360)  # Ángulo aleatorio
        PI = 3.1416
        r = rd.randint(1,50)  # Radio aleatorio
        formula_area = float("{:.2f}".format((theta/360) * (PI*(r**2))))  # Cálculo del área del sector
        formula_longitud = float("{:.2f}".format((theta/360)*(PI*(2*r))))  # Cálculo de la longitud del arco

        print(f'''
        Un sector circular tiene un ángulo central de {theta}° y un radio de {r} cm.
        Calcula el área del sector y la longitud del arco:
        ''')
        respuesta = float(input("Área del sector: "))
        respuesta2 = float(input("Longitud del arco: "))
        self.registrar_doble_respuesta(formula_area, formula_longitud, respuesta, respuesta2)

        # Tercer ejercicio del nivel 3
        lado_octaedro = rd.randint(1,25)
        volumen_octaedro = self.calcular_volumen_octaedro(lado_octaedro)
        area_octaedro = self.calcular_area_octaedro(lado_octaedro)
        print(f"Un octaedro regular tiene lados de {lado_octaedro} cm. Calcula su volumen y el área total de sus caras.")
        volumen_respuesta = float(input("Volumen: "))
        area_respuesta = float(input("Área: "))
        self.registrar_doble_respuesta(volumen_octaedro, area_octaedro, volumen_respuesta, area_respuesta)

        print('''
        Con una precisión impecable, logras desvelar los misterios del octaedro. El poliedro brilla 
        intensamente antes de desvanecerse en una ráfaga de luz. El aire se siente más 
        ligero mientras avanzas. Sabes que la cima está cerca, y el Templo del Gran Desafío se 
        eleva ante ti. ¡Solo un último esfuerzo, aventurero, y el secreto será tuyo!
''')

    # Desafío final: minijuego
    def desafio_final(self):
        '''
        Desafío final del juego: Minijuego Blastar.
        '''
        juego_final.Blastar()  # Iniciar minijuego Blastar
        with open('trama_historia\\mensaje_final.txt', 'r', encoding='UTF-8') as archivo_leer:
            print(archivo_leer.read())  # Mostrar mensaje final del juego

    # Método para calcular el volumen de un octaedro regular
    def calcular_volumen_octaedro(self, lado):
        '''Calcula el volumen de un octaedro regular'''
        volumen = float("{:.2f}".format((math.sqrt(2) / 3) * (lado ** 3)))
        return volumen

    # Método para calcular el área total de un octaedro regular
    def calcular_area_octaedro(self, lado):
        '''Calcula el área de un octaedro regular'''
        area_total = float("{:.2f}".format(2 * math.sqrt(3) * (lado ** 2)))
        return area_total


if __name__ == '__main__':
    # Muestra el mensaje de bienvenida leyendo un archivo de texto
    with open('trama_historia\\mensaje_bienvenida.txt', 'r', encoding='UTF-8') as archivo_bienvenida:
        print(archivo_bienvenida.read())

    # Creación del objeto de la clase Secundaria
    alumno1 = Secundaria("Eduardo", "secundaria", 0)

    print(f'Tu puntuación es: {alumno1.puntuacion}/10')

    print('''
        ¡Lo lograste! Has esquivado cada figura con precisión y gracia. 
        Mientras te acercas al altar, una luz cegadora inunda la sala, y el secreto del templo se revela ante ti... 
        Has superado todas las pruebas y demostrado tu valía como aventurero. 
        El Gran Secreto ahora es tuyo, ¡felicidades!
''')

