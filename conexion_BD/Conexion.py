from logger_base import log
import sys
from psycopg2 import pool #Importamos el pool de conexiones.

class Conexion:
    _DATABASE = 'test_db' #Cambiar el nombre de la base de datos.
    _PASSWORD = 'admin'
    _USERNAME = 'postgres'
    _BD_PORT = '5432'
    _HOST = '127.0.0.1'
    _MIN_CON = 1
    _MAX_CON = 10
    _pool = None

    @classmethod
    def obtenerPool(cls):
        if cls._pool is None:
            try:
                cls._pool = pool.SimpleConnectionPool(cls._MIN_CON, cls._MAX_CON,
                                                      host = cls._HOST,
                                                      user = cls._USERNAME,
                                                      password = cls._PASSWORD,
                                                      port = cls._BD_PORT,
                                                      database = cls._DATABASE)
                log.debug(f'Creación del pool exitosa: {cls._pool}')
                return cls._pool
            except Exception as e:
                log.error(f'Ocurrió un error')
                sys.exit()
        else:
            return cls._pool

    @classmethod
    def obtenerConexion(cls):
        pass


if __name__ == '__main__':
    pass