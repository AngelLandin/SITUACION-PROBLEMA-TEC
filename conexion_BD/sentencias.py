import psycopg2 as bd
from Conexion import Conexion

class Sentencias():

    conexion = Conexion()

    def insert():
        sentencia = 'INSERT INTO persona(nombre, apellido, email) VALUES(%s,%s,%s)'

    def update():
        sentencia = 'UPDATE persona SET nombre=%s, apellido=%s, email=%s WHERE id_persona=%s'



    def delete():
        pass

    def select():
        sentencia = 'SELECT * FROM persona'
        
    #Falta configurar las sentencias SQL con los datos de los alumnos registrados.  

    try:
        with conexion:
            with conexion.cursor() as cursor:
                sentencia = 'INSERT INTO persona(nombre, apellido, email) VALUES(%s,%s,%s)'
                valores = ("Elon", "Musk", "Musk.Elon@gmail.com")
                cursor.execute(sentencia, valores)
                sentencia = 'UPDATE persona SET nombre=%s, apellido=%s, email=%s WHERE id_persona=%s'
                valores = ('Leonardito', 'Carreño', 'LeoCarreño@gmail.com', 14)
                cursor.execute(sentencia, valores)
                print("Se hizo la transacción, se hizo commit.")
    except Exception as e:
        print(f'ocurrio un error, se hizo rollback: {e}')
    finally:
        conexion.close()    