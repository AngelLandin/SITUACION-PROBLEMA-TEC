import sympy as sp #Libreria para el uso de algebra
import random as rd #Libreria para la generación de numeros aleatorios
class Secundaria(): #MODULO SECUNDARIA
    '''
    Class Secundaria: Clase exclusiva para alumnos del nivel secundaria, la cual contendra
    temas de algebra y geometria.
    '''
    cantidad_alumnos = []
    contador_alumnos = 0 #Variable de clase: Para contar la cantidad de alumnos que se vayan registrando
    puntuacion = 0 #Dato estadistico: Puntuación que contendra cada alumno de 0 - 10
    def __init__(self, nombre, grado, id, puntuacion):
        id_alumno = Secundaria.contador_alumnos
        id_alumno += 1
        self._id = id_alumno
        self._nombre = nombre
        self._grado = grado
        self._puntuacion = Secundaria.puntuacion

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

    #PROBLEMAS ALGEBRAICOS
    def ecuacion_primer_grado(self):
        pass

    def ecuacion_segundo_grado(self):
        pass

    def binomio_cuadratico(self):
        pass

    def distancia_puntos(self):
        pass

#PARTE TEORICA CON VERIFICACION DE STR.
#CLASE PARA TENER CONTROL DE DATOS.

if __name__ == '__main__':
    print("NIVEL SECUNDARIA: ALGEBRA Y GEOMETRIA")


