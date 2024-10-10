class NivelAcademico:
    contador = 0
    def __init__(self):
        self._puntuacion = 0

    @classmethod
    def registrar_respuesta(cls, respuesta, correcta):
        if respuesta == correcta:
            print("\u2705 Excelente, respuesta CORRECTA!!! \u2705")
            cls.contador += 1
            return cls.contador
        else:
            print(f"\U0001F625 INCORRECTO!!! \U0001F625, la respuesta correcta es: {correcta}")

    def registrar_doble_respuesta(self, correcta1, correcta2, respuesta1, respuesta2):
        if (respuesta1 == correcta1) and (respuesta2 == correcta2):
            print("\u2705 Excelente, ambas respuestas CORRECTAS!!! \u2705")
            cls.contador += 1
            return cls.contador
        else:
            print(f"\U0001F625 INCORRECTO!!! \U0001F625, la respuesta correcta es: {correcta1} y {correcta2}")
        print(f'Tu puntuación actual es de: {self._puntuacion}')
    
    # Propiedad nombre
    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    # Propiedad nivel
    @property
    def nivel(self):
        return self._grado  # Debe devolver el grado, no _nivel

    @nivel.setter
    def nivel(self, nivel):
        self._grado = nivel  # Almacenar el nivel en grado

    # Propiedad puntuacion
    @property
    def puntuacion(self):
        return self._puntuacion

    @puntuacion.setter
    def puntuacion(self, puntuacion):
        self._puntuacion = puntuacion

    # Propiedad grado
    @property
    def grado(self):
        return self._grado

    @grado.setter
    def grado(self, grado):
        self._grado = grado

# Ejemplo de uso de la clase
if __name__ == '__main__':
    print(f" \U0001F625 INCORRECTO!!! \U0001F625, ")
