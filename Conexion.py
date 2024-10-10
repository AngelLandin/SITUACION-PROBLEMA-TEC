import matplotlib.pyplot as plt
from pool_de_conexiones import Conexion
from logger_base import log
import numpy as np

class CursorDelPool:
    def __init__(self):
        self._conexion = None
        self._cursor = None

    def __enter__(self):
        log.debug('Inicio del método with __enter__')
        self._conexion = Conexion.obtenerConexion()
        self._cursor = self._conexion.cursor()
        return self._cursor

    def __exit__(self, tipo_excepcion, value_excepcion, detalle_excepcion):
        if value_excepcion:
            self._conexion.rollback()
            log.error(f'Ocurrió una excepción, se hizo rollback: {tipo_excepcion} {value_excepcion} {detalle_excepcion}')
        else:
            self._conexion.commit()
        self._cursor.close()
        Conexion.liberarConexion(self._conexion)

if __name__ == '__main__':
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
