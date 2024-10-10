import random
import statistics
import emoji

class Primaria:
    def __init__(self, nombre, grado):
        self.nombre = nombre
        self.grado = grado
        self.main_primaria()  # Llamamos al menú principal automáticamente

    def español_primaria(self):  # función de juegos de español para 1° a 3°
        while True:
            print(f"------Comencemos con Español, {self.nombre} -------")
            print("~~~~~~Silabas SIMPLES~~~~~~")
            aciertos_1 = 0
            print("Ejercicio 1: \n Escribe 5 palabras que tengan dos sílabas simples")
            for i in range(5):
                sil = str(input("Palabra: "))
                sila = len(str(sil))
                if sila <= 4:
                    print("Correcto")
                    aciertos_1 += 1
                else:
                    print("Algo está mal, ¿son solo dos sílabas?")
            print(f"Lograste {aciertos_1} palabras")

            usuario = input("Deseas continuar (si/no): ").lower()
            if usuario == "no":
                break
            else:
                print("Perfecto!, continuemos...")

                # Continuación con la segunda actividad de completar palabras
                acierto_2 = 0
                print("Completa la palabra")
                ejercicios = [
                    ("Pelí_ula", "c"),
                    ("S_lla", "i"),
                    ("Mon_da", "e"),
                    ("To_lla", "a"),
                    ("Nar_anj_", "a a"),
                    ("T_lef_no", "e o"),
                    ("C_m_da", "o i"),
                    ("Es_al_ra", "c e"),
                    ("_migo", "a"),
                    ("M_ri_os_", "a p a")
                ]

                for pregunta, respuesta_correcta in ejercicios:
                    p = str(input(f"{pregunta} (completa): "))
                    if p == respuesta_correcta:
                        print(f"Correcto: {pregunta.replace('_', respuesta_correcta)}")
                        acierto_2 += 1
                    else:
                        print("Incorrecto, intenta con otra")
                print(f"Obtuviste {acierto_2} / 10")
                break

    def matematicas_primaria(self):  # Función de juegos de matemáticas para 1° a 3°
        while True:
            print(f"--------Sigamos con Matemáticas, {self.nombre} --------")
            acierto = 0
            for m in range(3):
                n = random.randint(2, 5)
                print('🚀 ' * n)
                cont = n * n
                res = int(input("¿Cuántos cohetes hay?: "))
                if res == cont:
                    print("¡Correcto!")
                else:
                    print("Incorrecto, vuelve a intentarlo")
                acierto += 1

            usuario = input("¿Deseas continuar (si/no)?: ").lower()
            if usuario == "no":
                break
            elif usuario == "si":
                print("Esa es la actitud, sigamos avanzando...")

                # Actividad de ordenar una lista
                acierto = 0
                while acierto < 3:
                    lista = [random.randint(1, 10) for _ in range(5)]
                    print(lista)
                    lista_orden = [int(input("Ordena: ")) for _ in range(5)]
                    if lista_orden == sorted(lista):
                        print("¡Correcto!")
                        acierto += 1
                    else:
                        print(f"Incorrecto, la respuesta es: {sorted(lista)}")

                print("¡Completaste 3 listas correctamente!")
                break

    def español_primaria_2(self):  # Función para 4° a 6°
        while True:
            print(f"~~~~~Bienvenido a la sección Español, {self.nombre} ~~~~")
            print("--------Comprensión Lectora--------")
            r1 = input("¿Dónde pone Jorge la bicicleta por las noches? (a) Afuera (b) Adentro (c) En la escuela: ").lower()
            if r1 == "b":
                print("Correcto")
            else:
                print("Incorrecto")
            
            usuario = input("¿Deseas continuar (si/no)?: ").lower()
            if usuario == "no":
                break

    def matematicas_primaria_2(self):  # Función para 4° a 6° en matemáticas
        while True:
            print(f"------------Sigamos con Matemáticas, {self.nombre} --------------")
            aciertos_1 = 0
            while aciertos_1 < 3:
                num = random.randint(100, 10000)
                print(num, "gramos a kg: ")
                s = float(input("Resultado: "))
                kg = num / 1000
                if s == kg:
                    print("Muy bien!")
                    aciertos_1 += 1
                else:
                    print("Sigue practicando")
            break

    def nivel_1p(self):  # Para 1° a 3°
        self.español_primaria()
        mat = input("¿Deseas continuar con la parte de matemáticas? (si/no): ").lower()
        if mat == "si":
            self.matematicas_primaria()

    def nivel_2p(self):  # Para 4° a 6°
        print("Listo para aprender?")
        self.español_primaria_2()
        mat = input("¿Deseas continuar con la parte de matemáticas? (si/no): ").lower()
        if mat == "si":
            self.matematicas_primaria_2()

    def main_primaria(self):  # Menú principal
        print(f"------Bienvenido {self.nombre} al Nivel Primaria------")
        while True:
            print("~~~Menú principal~~~")
            nivel = int(input("Selecciona una opción: \n 1° a 3° grado (1) \n 4° a 6° grado (2) \n Salir del juego (3): "))
            if nivel == 1:
                self.nivel_1p()
            elif nivel == 2:
                self.nivel_2p()
            elif nivel == 3:
                print(f"Gracias por jugar, {self.nombre}!")
                break
            else:
                print("Elige una opción válida (1 o 2)")


# Crear la instancia de la clase con nombre y grado
nombre = input("Ingresa tu nombre: ")
grado = int(input("Ingresa tu grado: "))
jugador = Primaria(nombre, grado)
