# Menú Principal
from secundaria import Secundaria
from pool_de_conexiones import Conexion
from Conexion import *
import matplotlib.pyplot as plt
from logger_base import log
import numpy as np
from Nivel_Primaria_opriginal import *



def menu_principal():  # Visualizar el menú principal
    while True:
        print("###################################")
        print("         MENU PRINCIPAL           ")
        print("###################################")
        print("  1. Primaria      ")
        print("  2. Secundaria    ")
        print("  3. Graficar      ")
        print("  4. Salir         ")

        # Solicitar opción al usuario
        opc = int(input("Selecciona una opción (1-4): "))

        if opc == 1:  # Iniciar el juego de primaria
            print("¡Nuevo juego de primaria iniciado!")
            main_primaria()

        elif opc == 2:  # Iniciar el juego de secundaria
            print("¡Nuevo juego de secundaria iniciado!")
            nombre = input("Ingresa tu nombre: ")
            grado = int(input("Ingresa tu grado (numérico): "))
            puntuacion = 0
            alumno = Secundaria(nombre=nombre, grado=grado, puntuacion=puntuacion)

        elif opc == 3:  # Graficar los datos
            print("Generando gráfica de puntuaciones por grado...")
            graficar_datos()

        elif opc == 4:  # Salir del programa
            print("Saliendo del programa... ¡Hasta pronto!")
            break

        else:
            print("Opción no válida. Inténtalo de nuevo.")


def graficar_datos():
    '''
    Función para graficar los datos de los grados y puntuaciones de los alumnos en la base de datos.
    '''
    with CursorDelPool() as cursor:
        # Ejecuta la consulta SQL para obtener los datos
        cursor.execute('SELECT grado, puntuacion FROM secundaria')
        registros = cursor.fetchall()
        
        # Extraer los grados y puntuaciones en listas separadas
        grados = [registro[0] for registro in registros]
        puntuaciones = [registro[1] for registro in registros]
        
        # Crear una gráfica de barras con estilo mejorado
        fig, ax = plt.subplots(figsize=(10, 6))

        # Crear colores para las barras
        colors = plt.cm.viridis(np.linspace(0.1, 0.9, len(grados)))

        # Gráfica de barras
        ax.bar(grados, puntuaciones, color=colors, edgecolor='black')

        # Estilizando los ejes y título
        ax.set_xlabel('Grado', fontsize=14, fontweight='bold')
        ax.set_ylabel('Puntuación', fontsize=14, fontweight='bold')
        ax.set_title('Puntuación por Grado - Gráfica Estilizada', fontsize=16, fontweight='bold')

        # Añadir cuadrícula
        ax.grid(True, linestyle='--', alpha=0.6)

        # Añadir etiquetas a cada barra
        for i, (grado, puntuacion) in enumerate(zip(grados, puntuaciones)):
            ax.text(grado, puntuacion + 0.5, f'{puntuacion}', ha='center', va='bottom', fontsize=12, fontweight='bold')

        # Mostrar la gráfica
        plt.tight_layout()
        plt.show()

# Llamada al menú principal para ejecutar el programa
menu_principal()
