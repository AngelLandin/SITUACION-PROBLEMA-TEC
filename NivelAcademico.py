class NivelAcademico():
    def __init__(self, nombre, nivel):
        self._nombre = nombre
        self._nivel = nivel
        self._puntuacion = 0
        #self._ejercicios = []

    def registrar_respuesta(self, respuesta, correcta):
        if respuesta == correcta:
            print("\u2705 Excelente, respuesta CORRECTA!!! \u2705")
            self.puntuacion += 1
        else:
            print(f"\U0001F625 INCORRECTO!!! \U0001F625, la respuesta correcta es: {correcta}")

    def registrar_respuesta_doble(self, respuesta1, respuesta2, correcta1, correcta2):
        if (respuesta1 == correcta1) or (respuesta1 == correcta2):
            print("\u2705 Excelente, respuesta CORRECTA!!! \u2705")
            self.puntuacion += .5
        if (respuesta2 == correcta1) or (respuesta2 == correcta2):
            print("\u2705 Excelente, respuesta CORRECTA!!! \u2705")
            self.puntuacion += .5
        else:
            print(f"\U0001F625 INCORRECTO!!! \U0001F625, la respuesta correcta es: {correcta1} y {correcta2}")

    def mostrar_puntuacion(self):
        print(f'Tu puntuacion actual es de: {self.puntuacion}')

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def nivel(self):
        return self._nivel

    @nivel.setter
    def nivel(self, nivel):
        self._nivel = nivel

    @property
    def puntuacion(self):
        return self._puntuacion

    @puntuacion.setter
    def nivel(self, puntuacion):
        self._puntuacion = puntuacion

    @property
    def ejercicios(self):
        return self._ejercicios

    @ejercicios.setter
    def ejercicios(self, ejercicios):
        self._ejercicios = ejercicios

if __name__ == '__main__':
    print(f" \U0001F625 INCORRECTO!!! \U0001F625, ")

    
