import psycopg2 as bd
from Conexion import CursorDelPool
from secundaria import Secundaria
from logger_base import log

class Sentencias:

    _SELECT = 'SELECT * FROM secundaria ORDER BY id_alumno'
    _INSERTAR = 'INSERT INTO secundaria(nombre, grado, puntuacion) VALUES(%s, %s, %s)'
    _ACTUALIZAR = 'UPDATE secundaria SET nombre=%s, grado=%s, puntuacion=%s WHERE id_alumno=%s'
    _ELIMINAR = 'DELETE FROM secundaria WHERE id_alumno=%s'

    @classmethod
    def seleccionar(cls):
        with CursorDelPool() as cursor:
            cursor.execute(cls._SELECT)
            alumnos = cursor.fetchall()
            usuarios = []
            for registro in alumnos:
                persona = Secundaria(registro[0], registro[1], registro[2])
                print(persona)
                usuarios.append(persona)
            return usuarios
'''
    @classmethod
    def insertar(cls, Secundaria):
        with CursorDelPool() as cursor:
            valores = (Secundaria.nombre, Secundaria.grado, Secundaria.puntuacion)
            cursor.execute(cls._INSERTAR, valores)
            log.debug(f'Persona insertada: {Secundaria}')
            return cursor.rowcount
'''
'''
    @classmethod
    def actualizar(cls, secundaria):
        with CursorDelPool() as cursor:
            valores = (secundaria.nombre, secundaria.apellido, persona.email, persona.id_persona)
            cursor.execute(cls._ACTUALIZAR, valores)
            log.debug(f'Persona actualizada: {persona}')
            return cursor.rowcount

    @classmethod
    def eliminar(cls, persona):
        with CursorDelPool() as cursor:
            valores = (persona.id_persona,)
            cursor.execute(cls._ELIMINAR, valores)
            log.debug(f'Objeto eliminado: {persona}')
            return cursor.rowcount
'''

if __name__ == '__main__':
    #alumno = Secundaria("Jaimez", "3", 10)
    #Sentencias.seleccionar()