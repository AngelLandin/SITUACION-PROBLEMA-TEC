#Estructura base
import random
import statistics
import emoji

class Primaria():
    

    def español_primaria(): #funcion de 2 juegos de español para niños de 1° a 3° de primaria
        while True:
            print("------Comencemos con Español-------")
            print("°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°")
            
            print("~~~~~~Silabas SIMPLES~~~~~~") #primera actividad aplicando primero la teoría
            print("¿Que son? \n Las sílabas simples son aquellas que están formadas por una sola vocal o por la combinación de una consonante y una vocal. \n NOTA: una sílaba simple puede tener como máximo dos letras")
            
            aciertos_1=0  #contador inicial donde se registra que lleve 5 palabras
            print("Ejercicio 1: \n Escibre 5 palabras que tengan dos Silabas simples")
            for i in range(5): #El rango en que se ejecuta el código
                sil= str(input("Palabra: ")) #variable que recibe la palabra dada por el usuario
                sila=len(str(sil))
                if sila <= 4: #condicional sobre el cumplimiento de los requisitos de las instrucciones.
                    print("Correcto")
                    aciertos_1+=1 #agregar un acierto si la respuesta que se evaluo primero es correcta.
                else:
                    print("Algo esta mal, son solo dos silabas?") #retroalimentación
                    
            print("Lograste",aciertos_1," palabras")  #mostrar los aciertos
            print("--------------Siguiente Actividad------------- ")
            print("Deseas continuar continuar \n -Si  -No ")
            usuario=input("Opcion: ")   #variable que recibe la opcion de desear continuar.
            if usuario == "no" or usuario== "No":
                break
            #evaluar la respuesta y continuando con el juego, para esta condición el ciclo se rompe y regresa al menu de primaria
            else: 
                print("Perfecto!, continuemos...")
                
                print("°°°°Completa la palabra°°°°")
                print("Completa la palabra \n NOTA: Si son +2 letras colocalas en orden y separadas por un espacio") #Instrucciones para ejecutar el código
                acierto_2=0

                print("Pelí_ula")
                p1= str(input("que letra falta_ : ")) #variable con la letra que falta
                if p1=="c":
                    print("Correcto:Película")
                    acierto_2+=1
                else:
                    print("Incorrecto, intenta con otra")
                    
                print("S_lla")
                p2= str(input("que letra falta_ : "))
                if p2=="i":
                    print("Correcto:Silla")
                    acierto_2+=1
                else:
                    print("Incorrecto, intenta con otra")
                    
                print("Mon_da")
                p3= str(input("que letra falta_ : "))
                if p3=="e":
                    print("Correcto:Moneda")
                    acierto_2+=1
                else:
                    print("Incorrecto, intenta con otra")

                        
                print("To_lla")
                p4= str(input("que letra falta_ : "))
                if p4=="a":
                    print("Correcto:Toalla")
                    acierto_2+=1
                else:
                    print("Incorrecto, intenta con otra")

                print("Nar_anj_")
                p5= str(input("que letra falta_ : "))
                if p5=="a a":
                    print("Correcto:Naranja")
                    acierto_2+=1
                else:
                    print("Incorrecto, intenta con otra")

                print("T_lef_no")
                p6= str(input("que letra falta_ : "))
                if p6=="e o":
                    print("Correcto:Telefono")
                    acierto_2+=1
                else:
                    print("Incorrecto, intenta con otra")

                print("C_m_da")
                p7= str(input("que letra falta_ : "))
                if p7=="o i":
                    print("Correcto:Comida")
                    acierto_2+=1
                else:
                    print("Incorrecto, intenta con otra")
                    
                print("Es_al_ra")
                p8= str(input("que letra falta_ : "))
                if p8=="c e":
                    print("Correcto:Escalera")
                    acierto_2+=1
                else:
                    print("Incorrecto, intenta con otra")
                    
                print("_migo")
                p9= str(input("que letra falta_ : "))
                if p9=="A" or p9=="a":
                    print("Correcto:Amigo")
                    acierto_2+=1
                else:
                    print("Incorrecto, intenta con otra")
                    
                print("M_ri_os_")
                p10= str(input("que letra falta_ : "))
                if p10=="a p a":
                    print("Correcto:Mariposa")
                    acierto_2+=1
                else:
                    print("Incorrecto, intenta con otra")
                print("\n Obtuviste",acierto_2,"/10")
                break #termino de actividades de español con un recuento de los aciertos
            
    def matematicas_primaria(): #función principal de los juego de matematicas en nivel básico de primaria"
        while True:
            print("--------Sigamos con Matemáticas-------- \n°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°")
            print("~~~~~~Cuenta los elementos~~~~~~~")#el usuario debe contar los cohetes que se despliegan en un cuadrado
            print("Cuenta los (🚀) que tiene el cuadrado")
            acierto=0 #contador incial de aciertos
            for m in range(3): #el numero de veces que se despliega un cuadrado diferentes
                
                while True: #ciclo para lograr el objetivo 3 veces
                    n= random.randint(2,5)
                    for i in range(n):
                        print('🚀 ' * n)
                
                        cont= n*n 
                    res=(int(input("Respuesta: ")))

                    if res== cont:
                        print("Correcto!") #evalua si es el numero de elementos y señala el acierto
                        
                        break 
                    else:
                        print("Incorrecto :( \n Vuelve a intentarlo")
                acierto= acierto+1
            print("Contaste correctamente tres figuras")
                
            print("--------------Siguiente Actividad------------- ") #opción de continuar con el juego en matematicas o terminar el juego
            print("Deseas continuar continuar \n -Si  -No ")
            usuario=input("Opcion: ") # variable para evaluar la opción del jugador
            if usuario == "no" or usuario== "No": #regresar al menu principal de primaria
                break
            
            elif usuario== "si" or "Si": #condición necesaria para continuar con la siguiente actividad
                print("Esa es la actitud!,sigamos avanzando...")
                
                print("~~~~ORDENA UNA LISTA~~~~~") #titulo de la actividad
                lista=[]  #lista declarada vacia que sera llenada por numeros aleatorios
                lista_orden=[] #lista para ser ordenada sin mostrar al usuario

                print("------Menor a mayor------")
                #print("Ordena las listas")
                acierto=0 #contador inicial
                while acierto<3:  #ciclo para que acierte en el acomodo de 3 listas
                    print("Ordena las lista")
                    for i in range(5):
                        lista.append(random.randint (1,10)) #genera un número aleatorio y lo agrega a la lista vacia

                    print(lista) #muestra de la lista que debe acomodar el usuario
                    for i in range (len(lista)):
                        #lista_orden=[]
                        lista_orden.append(int(input(" "))) # lista que declara el usuario y se insertan los valores a una vacia para ser analizada
                        
                    respuesta= sorted(lista)   #instrucción que ordena la lista
                    if lista_orden == respuesta:  #validación de listas para determinar si fue correcto o incorrecto
                        print(lista_orden)
                        print("Correcto!")
                        
                        acierto=acierto+1
                        lista.clear()
                        lista_orden.clear()   #limpia de listas para el ciclo pueda continuar con el ejercicio sin incrementar el numero de valores
                        
                    else:
                        print("Incorrecto")
                        print("La respuesta es: ",respuesta)
                        lista.clear()
                        lista_orden.clear()
                        
                print("Completaste 3 Listas correctamente! \n FELICIDADES!!") #mensaje de realización
                
                print("--------------Ultima Actividad------------- ") #señalamiento de numero de actividad
                print("Deseas continuar \n -Si  -No ")
                usuario=input("Opcion: ")
                if usuario == "no" or usuario== "No":
                    break
                
                else:
                    print("***Que numero falta en esta serie?***") #ejecución resultante mostrada para el jugador que desea seguir jugando
                    aciertos=0
                    for s in range(1,10,1): #para un juego de 10 ejercicios
                        lista=[] 
                        lista_usuario=[]
                        l= random.randint(10,20)
                        for i in range(1,l,random.randint(1,5)):
                            lista.append(i) #lista sin manipular datos
                            lista_usuario.append(i) #lista donde se remplaza un dato para colocar el numero que falta

                        r=random.randint(1,len(lista)-1)
                        lista[r]='_'  # cambia el valor de una numero en la lista, partiendo de un numero aleatorio dentro de la lista

                        print(lista)
                        n=int(input("num: "))
                        lista.pop(r) #borra el elemento en esa posición
                        lista.insert(r,n) #inserta el numero dadao por el usuario en la lista en la que se manipula sus respuestas

                        if lista == lista_usuario: #validación de orden
                            print("Correcto!!!")
                            aciertos+=1
                            
                        else:
                            print("Sigue intentanto")
                            
                    print("Obtuviste ",aciertos,"aciertos!!!") #aciertos totales que consiguió el usuario
                    
                    print()
                    print("Lo hiciste increible! \n Hemos terminado con los juegos, vuelve pronto....")
                    break #fin del ciclo de los 5 juegos de nivel basico en primaria
                

    def español_primaria_2(): #funcion que manda a llamar a todos los juegos relacionados a español de 4° a 6° de primaria
        while True: #ciclo que prmite seguir en esta sección
            print("~~~~~Bienvenido a la sección Español~~~~")#bienvenida a los que seleccionan este grado academico 
            print("--------Actividad 1--------")
            print("~~~~~~~ Comprensión Lectora ~~~~~~~~") #descripción de actividad
            print("Instrucciones: \n Lee las lecturas y selecciona la respuesta correcta: ")
            print("Lectura 1: \n Jorge  tiene una bicicleta nueva. La bicicleta puede ir muy rápido. Su bicicleta nueva es azul. Es una bicicleta grande. A Jorge le gusta montar en bicicleta con sus amigos. A él le gusta pasear en bicicleta por el parque. Jorge  guarda su bicicleta adentro por las noches. Jorge  cuida su bicicleta nueva.")
            print("Preguntas: \n 1.¿Dónde pone Jorge  la bicicleta por las noches? \n a)Afuera  b)Adentro  c)En la escuela")
            r1=str(input("Respuesta: ")) #variable de entrada con la respuesta del usuario
            if r1=="b" or r1=="B" or r1=="b)":
                print("Correcto") #validación de la respuesta
            else:
                print("Incorrecto")
            print("2. ¿Con quién le gusta a Jorge  pasear en bicicleta? \n a)Hermano  b)Madre  c)Amigos")
            r2=str(input("Respuesta: "))
            if r2=="c" or r2=="C" or r2=="c)":
                print("Correcto")
            else:
                print("Incorrecto")
            print("3. ¿Cómo crees tú que Jorge  se siente en relación a su bicicleta? \n a)No le gusta  b)Quiere una bicicleta roja  c)Le gusta su bicicleta nueva")
            r3=str(input("Respuesta: "))
            if r3=="c" or r3=="C" or r3=="c)":
                print("Correcto")
            else:
                print("Incorrecto")
                
                #segunda lectura de comprensión, preguntas separadas por saltos de linea (\n)
            print("Lectura 2: \n Un ratoncito y un gato eran amigos. Un día el ratoncito fue a ver al gato. El gato estaba en la cama enfermo. El ratoncito le preparo sopa al gato. Le leyó un cuento al gato. El gato se durmió. El ratoncito fregó el suelo y lavó la ropa. Finalmente, el gato se despertó. El gato se sentía mejor. El ratoncito y el gato jugaron un juego. ")
            print("Preguntas: \n 1.¿Por qué estaba el gato en la cama? \n a)Estaba enfermo  b)Tenía sueño  c)Quería jugar")
            r1=str(input("Respuesta: "))
            if r1=="a" or r1=="A" or r1=="a)":
                print("Correcto")
            else:
                print("Incorrecto")
            print("2. ¿Qué hizo el ratoncito después de preparar la sopa? \n a)Barrió el suelo  b)Lavó ropa  c)Le leyó un cuento")
            r2=str(input("Respuesta: "))
            if r2=="c" or r2=="C" or r2=="c)":
                print("Correcto")
            else:
                print("Incorrecto")
            print("3. ¿Qué es lo último que hicieron el ratoncito y el gato? \n a)Comieron sopa  b)Jugaron un juego  c)Fueron a la tienda")
            r3=str(input("Respuesta: "))
            if r3=="b" or r3=="B" or r3=="b)":
                print("Correcto")
            else:
                print("Incorrecto")
            #evalua cada inciso y recibe retroalimentación
                
            print("--------------Siguiente Actividad------------- ")
            
            print("Deseas continuar continuar \n -Si  -No ") #validar seguimiento en sección español
            usuario=input("Opcion: ")
            if usuario == "no" or usuario== "No": #redirecciona a otra sección
                break
            
            else:
                print("Estupendo!, sigamos avanzando")
                print()
                print("~~~~~~ADIVINANZAS~~~~~~~~") #titulo actividad
                print("Una adivinanza es un tipo de acertijo o enigma que se presenta generalmente en forma de rima.")
                print("Estas listo para intentar resolver algunas? \nMucha suerte!")
                print("1.- 'Blanca por dentro, verde por fuera. Si quieres que te lo diga, espera.' ")
                a1=str(input("Respuesta: "))
                print("2.- 'Trabajo con flores y el hombre disfruta el fruto de mis labores. ¿Quién soy?'")
                a2=str(input("Respuesta: "))
                print("3.- 'Siempre quieto y sin embargo nunca para de correr. ¿Qué es?' ")
                a3=str(input("Respuesta: "))
                print("4.- 'Tengo agujas y no sé coser, tengo números y no sé leer. ¿Qué soy?' ")
                a4=str(input("Respuesta: "))
                print("5.- 'Roja por fuera, blanca por dentro. ¿Qué es?' ")
                a5=str(input("Respuesta: "))
                print("6.* ' Vuelo de noche, duermo de día y nunca verás plumas en ala mía. ¿Quién soy?' ")
                a6=str(input("Respuesta: "))
                #se reciben 6 variables, cada una con las respuestas de las adivinanzas

                adivinanza_s=['La pera','El jardinero','El río','El reloj','La manzana','El murciélago']
                print("Compara tu respuesta con las soluciones",adivinanza_s) #se muestran los resultados esperados
                print("¿Cuantas pudiste adivinar?")  
                n=int(input("Aciertos: ")) #variable donde el usuario sea quien califique sus aciertos
                if n == 6:
                    print("FELICIDADES, lo hiciste perfecto!!")
                elif n>4 and n<6:
                    print("Buen puntaje, en la siguiente lo lograras!")
                else:
                    print("Las adivinanzas no son lo tuyo, pero sigue intentando!")
                    
                break #fin del ciclo de 2 juegos en el apartado de español
            
    def matematicas_primaria_2(): #funcion que maneja los juegos implementados para un nivel de primaria_2
        while True: #ciclo que condiciona como se reproduce los juegos
            print("------------Sigamos con Matemáticas--------------")
            
            print("~~~~~~Unidades de Medida~~~~~~~") #actividad de repaso
            print("MASA: \n Lo primero que debes de conocer es la equivalencia de las unidades de masa más comunes")
            print("Unidades de masa: \n Gramo (g): Es la unidad básica. \n Kilogramo (kg): 1 kilogramo = 1000 gramos. \n Miligramo (mg): 1 miligramo = 0.001 gramos")
            print("Ahora puedes convertir cantidades en distintas unidades. \n Ejercicios: ")
            
    #instrucciones de ayuda para quien le falle el concepto
            print("GRAMOS A KILOGRAMOS")
            aciertos_1=0
            while aciertos_1<3:
                num= random.randint(100,10000) #numero a convertir a kg
                print(num,"gramos a kg: ")
                s=float(input("Resultado= "))
                kg= num/1000
                if s==kg:
                    print("Muy bien!")
                    aciertos_1+=1
                else:
                    print("Sigue practicando ")
                    #validar parametros que los permitan avanzar a otro tipo de ejercicioa
            print("GRAMOS A MILIGRAMOS") #diferencia en la dinamica de la clase
            aciertos_2=0
            while aciertos_2<3:
                num= random.randint(1,50)
                print(num,"gramos a miligramos: ")
                s=float(input("Resultado= "))
                mg= num*1000 #formula necesaria paa comparar los resultados obtenidos con los esperados
                if s==mg:
                    print("Muy bien!")
                    aciertos_2+=1 #contador de todos los aciertos
                else:
                    print("Sigue practicando ")
                    
            print("--------------Siguiente Actividad------------- ")
            print("Deseas continuar continuar \n -Si  -No ")
            usuario=input("Opcion: ") #validar la opción que elige y ver que ocurre con las siguientea actividades
            if usuario == "no" or usuario== "No":
                break #ciclo que se rompe para volver al menu principal
            
            elif usuario== "si" or "Si":
                print("Esa es la actitud!,sigamos avanzando...")
            
                print("--------------Siguiente Actividad------------- ") #titulo de la página
                print("~~~~~~Porcentajes~~~~~~~")
                print("En esta sección aprenderas a calcular el porcentaje de una cantidad, estas listo?")
                print("Sigue los siguientes pasos y luego ponlo en práctica!")
                print("Procedimiento: \n 1.Multiplica la cantidad por el porcentaje \n 2.Divide el resultado entre 100:")
                print("Fácil, cierto? \n Ahora resuelve los siguientes ejercicios, deberas acertar 8 para obtener insignia de reconocimiento")

                acierto_3=0
                for i in range(10): #en un rango en el que puedan hacerlo hasta 10 veces
                    cantidad= random.randint(1,100) # cantidad a la que debe sacarse un porcentaje
                    porcentaje= random.randint(1,100) #porcentaje maximo de 100%
                    print("Calcula el", porcentaje," % de", cantidad, ":")
                    n=(float(input("n: "))) #variabel de respuesta usuario
                    calculo= (cantidad*porcentaje) / 100 #calculos para obtener el porcentaje que pedimos
                    if n==calculo:
                        print("Correcto")
                        acierto_3=acierto_3+1
                    else:
                        print("Incorrecto")
                    #validar cuantos ejercicios de 10 fueron correctos"
                print("Obtuviste",acierto_3,"aciertos")
                if acierto_3>=8:
                    print("Lo conseguiste, eres increible con los porcentajes")
                
                else:
                    print("Te falta trabajar más")
                    #retroalimentación en basde a una puntuación
                
                
                
                    print("--------------Ultima Actividad------------- ")
                    print("Deseas continuar \n -Si  -No ")
                    usuario=input("Opcion: ")
                    if usuario == "no" or usuario== "No":
                        break #definir si seguir en este bloque, actividad
                
                    else:
                        print("~~~~~~Media, Mediana y Moda~~~~~~") #condición para terminar con esta actividad
                        aciertos=0
                        for i in range(3): #en un rango de 3 listas por jueo
                            print("En base a esta lista, responde lo siguiente")
                            numeros=[] #lista donde se incerta los valores a evaluar
                            for i in range(7):
                                numeros.append(random.randint(2,10))

                            print(numeros)#lista de los numeros en los que sacas esos parametros

                            #Media
                            media= float(input("Media: "))
                            med= statistics.mean(numeros) #funcion que nos permite sacar la media a traves de una funcion previamente establecida
                            redondear= round(med,2) #instruccion para redondear el resultado de los calculos
                            #print(redondear)
                            if media==med: #validar respuestas
                                print("Excelente!!, sigue avanzando...")
                                aciertos+=1
                            else:
                                print("Sigue intendo...")
                            #Mediana
                            mediana= int(input("Mediana: ")) #misma dinamica, direnete objetivo
                            mediana_s=statistics.median(numeros)
                            #print(mediana_s)
                            if mediana==mediana_s:
                                print("Correcto")
                                aciertos+=1
                            else:
                                print("Sigue intendo...")
                            #Moda
                            mod= int(input("Moda: ")) #ultima dinamica con un objetivo difrentes
                            moda= statistics.mode(numeros)
                            #print(moda)
                            if mod==moda:
                                print("Muy bien!!")
                                aciertos+=1
                            else:
                                print("Sigue intendo...")
                                
                        print("Aciertos: ",aciertos)
                        print("Terminamos Matemáticas, lo hiciste increible!!")
                        break #termino de la clase de matemáticas para niños de primaria
                                
    def nivel_1p(): #llama ambas funciones de las distintas materias
        español_primaria() #inicia con español
        print("Deseas continuar con la parte de matemáticas? \n -Si  -No")
        mat=input("Opción: ") #valida lo que el usuario desea continuar haciendo
        if mat=="Si" or mat=="si": #ciclo para llamar a la función si el usuario asi lo decide
            matematicas_primaria()
                        
    def nivel_2p():
        print("Listo para aprender?") #mensaje de animo
        español_primaria_2() #llamado de la primera seccion del juego en esta edad
        print("Aún hay mas por explorar!! \n Deseas continuar con la parte de matemáticas? \n -Si  -No")
        mat=input("Opción: ") #ingresa en una variable la opción a elegir
        if mat=="Si" or mat=="si":
            matematicas_primaria_2() #reproduce el codigo dodne se ve los juegos presentados
        
    def main_primaria(self):
        print("------Bienvenido al Nivel Primaria------") #menu principal de primaria 
        #print("Selecciona una opción: \n  1° a 3° grado (1) \n  4° a 6° grado (2) \n  Salir del juego(3)")
        while(True):
            print("~~~Menú principal~~~ \n Selecciona una opción: \n  1° a 3° grado (1) \n  4° a 6° grado (2) \n  Salir del juego(3)")
            nivel= int(input("Opción: ")) #selección de las opciones presentadas
            if nivel==1: #llamar a cada función por su nivel
                nivel_1p()
            elif nivel ==2: #validar el rumbo del juego dependiendo el nivel
                nivel_2p()
            elif nivel==3:
                print("Gracias por jugar!") #termina con la sección del juego de primaria y regresa al menu principal del juego
                break
            else:
                print("Elige una opción válida(1 o 2)") #valida que sea una opción que este incluida en el menu

    def __init__(self, nombre):
        self.nombre = nombre

                
