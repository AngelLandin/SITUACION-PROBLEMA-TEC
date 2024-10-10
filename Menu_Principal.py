#Menú Principal
from secundaria import Secundaria
from pool_de_conexiones import Conexion
from Conexion import Conexion
from Conexion import CursorDelPool
import matplotlib.pyplot as plt
from pool_de_conexiones import Conexion
from logger_base import log
import numpy as np
from Nivel_Primaria_opriginal import *


def menu(): #Visualizar el menu principal
    print("###################################")
    print("         MENU PRINCIPAL           ")
    print("###################################")
    print("  1. Primaria      ")
    print("  2. Secundaria    ")
    print("  3. Graficar       ")
    print("  4. Salir         ")  


def menu_principal():
    #menu donde se define el rumbo del usuario
    #en esta funcón se ejecuta la sección del juego que el usuario decida, hasta que elija la opción de terminar el juego.
    
    print("~~~~~~~BIENVENIDO AL JUEGO ~~~~~~~")
    print("Estas listo para aprender? \nA continuación te presentamos 4 diferentes opciones: \nEn la opción 1 y 2, elegiras el grado académico " )
    print( "La tienda es un apartado de premios!, aprende y disfuta del juego.....")
    
    while True: #ciclo que se mostrará al usuario siempre y cuando continue jugando.
        menu()
        opcion = input("Selecciona una opción (1-4): ") #variable de entrada principal que define el juego
        
        if opcion == '1': #Clase de primaria
            print("¡Nuevo juego iniciado!")
            print("Cargando partida...")
            print("°°°°°°°°°°°°°°°°°°°°")
            main_primaria()
        elif opcion == '2': #Clase de secundaria
            print("¡Nuevo juego iniciado!")
            print("Cargando partida...")
            print("°°°°°°°°°°°°°°°°°°°°")
            nombre = input("Ingresa tu nombre: ")
            grado = int(input("Ingresa tu grado (numerico): ")) 
            puntuacion = 0
            alumno = Secundaria(nombre=nombre, grado=grado, puntuacion=puntuacion)
            graficar_datos()
    

        elif opcion == '3': #Tienda 
            print("¡Nuevo juego iniciado!")
            print("Cargando partida...")
            print("°°°°°°°°°°°°°°°°°°°°")
            #graficar_datos()
        elif opcion == '4':#Terminar con el juego
            print("La aventura ha terminado....\n Gracias por jugar. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")


menu_principal()

def graficar_datos():
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