from NivelAcademico import NivelAcademico

with open('trama_historia\ejercicio1.txt', 'r', encoding='UTF-8') as archivo_eje1:
    print(archivo_eje1.read())

with open('trama_historia\ejercicio3.txt', 'r', encoding='UTF-8') as archivo_eje3:
            print(archivo_eje3.read())


archivo = NivelAcademico("asda", 1)
archivo.leer_archivo('trama_historia\desafiofinal.txt')
print(archivo)