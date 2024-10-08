#Estructura base
import random
import statistics
def español_primaria():
    while True:
        print("------Comencemos con Español-------")
        print("°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°")
        
        print("~~~~~~Silabas SIMPLES~~~~~~")
        print("¿Que son? \n Las sílabas simples son aquellas que están formadas por una sola vocal o por la combinación de una consonante y una vocal. \n NOTA: una sílaba simple puede tener como máximo dos letras")
        
        aciertos_1=0
        print("Ejercicio 1: \n Escibre 5 palabras que tengan dos Silabas simples")
        for i in range(5):
            sil= str(input("Palabra: "))
            sila=len(str(sil))
            if sila <= 4:
                print("Correcto")
                aciertos_1+=1
            else:
                print("Algo esta mal, son solo dos silabas?")
        print("Lograste",aciertos_1," palabras")
        print("--------------Siguiente Actividad------------- ")
        print("Deseas continuar continuar \n -Si  -No ")
        usuario=input("Opcion: ")
        if usuario == "no" or usuario== "No":
            break
        
        else: 
            print("Perfecto!, continuemos...")
            
            print("°°°°Completa la palabra°°°°")
            print("Completa la palabra \n NOTA: Si son +2 letras colocalas en orden y separadas por un espacio")
            acierto_2=0

            print("Pelí_ula")
            p1= str(input("que letra falta_ : "))
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
            break
        
def matematicas_primaria():
    while True:
        print("--------Sigamos con Matemáticas-------- \n°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°")
        print("~~~~~~Cuenta los elementos~~~~~~~")
        print("Cuenta los (*) que tiene el cuadrado")
        acierto=0
        for m in range(3):
            
            while True:
                n= random.randint(2,5)
                for i in range(n):
                    print('* ' * n)
            
                    cont= n*n
                res=(int(input("Respuesta: ")))

                if res== cont:
                    print("Correcto!")
                    
                    break 
                else:
                    print("Incorrecto :( \n Vuelve a intentarlo")
            acierto= acierto+1
        print("Contaste correctamente tres figuras")
            
        print("--------------Siguiente Actividad------------- ")
        print("Deseas continuar continuar \n -Si  -No ")
        usuario=input("Opcion: ")
        if usuario == "no" or usuario== "No":
            break
        
        elif usuario== "si" or "Si":
            print("Esa es la actitud!,sigamos avanzando...")
            
            print("~~~~ORDENA UNA LISTA~~~~~")
            lista=[]
            lista_orden=[]

            print("------Menor a mayor------")
            #print("Ordena las listas")
            acierto=0
            while acierto<3:
                print("Ordena las lista")
                for i in range(5):
                    lista.append(random.randint (1,10))

                print(lista)
                for i in range (len(lista)):
                    #lista_orden=[]
                    lista_orden.append(int(input(" ")))
                    
                respuesta= sorted(lista)   
                if lista_orden == respuesta:
                    print(lista_orden)
                    print("Correcto!")
                    
                    acierto=acierto+1
                    lista.clear()
                    lista_orden.clear()
                    
                else:
                    print("Incorrecto")
                    print("La respuesta es: ",respuesta)
                    lista.clear()
                    lista_orden.clear()
                       
            print("Completaste 3 Listas correctamente! \n FELICIDADES!!")
            
            print("--------------Ultima Actividad------------- ")
            print("Deseas continuar \n -Si  -No ")
            usuario=input("Opcion: ")
            if usuario == "no" or usuario== "No":
                break
            
            else:
                print("***Que numero falta en esta serie?***")
                aciertos=0
                for s in range(1,10,1):
                    lista=[]
                    lista_usuario=[]
                    l= random.randint(10,20)
                    for i in range(1,l,random.randint(1,5)):
                        lista.append(i)
                        lista_usuario.append(i)

                    r=random.randint(1,len(lista)-1)
                    lista[r]='_'

                    print(lista)
                    n=int(input("num: "))
                    lista.pop(r)
                    lista.insert(r,n)

                    if lista == lista_usuario:
                        print("Correcto!!!")
                        aciertos+=1
                        
                    else:
                        print("Sigue intentanto")
                        
                print("Obtuviste ",aciertos,"aciertos!!!")
                
                print()
                print("Lo hiciste increible! \n Hemos terminado con los juegos, vuelve pronto....")
                break
            

def español_primaria_2():
    while True:
        print("~~~~~Bienvenido a la sección Español~~~~")
        print("--------Actividad 1--------")
        print("~~~~~~~ Comprensión Lectora ~~~~~~~~")
        print("Instrucciones: \n Lee las lecturas y selecciona la respuesta correcta: ")
        print("Lectura 1: \n Jorge  tiene una bicicleta nueva. La bicicleta puede ir muy rápido. Su bicicleta nueva es azul. Es una bicicleta grande. A Jorge le gusta montar en bicicleta con sus amigos. A él le gusta pasear en bicicleta por el parque. Jorge  guarda su bicicleta adentro por las noches. Jorge  cuida su bicicleta nueva.")
        print("Preguntas: \n 1.¿Dónde pone Jorge  la bicicleta por las noches? \n a)Afuera  b)Adentro  c)En la escuela")
        r1=str(input("Respuesta: "))
        if r1=="b" or r1=="B" or r1=="b)":
            print("Correcto")
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
        
            
        print("--------------Siguiente Actividad------------- ")
        
        print("Deseas continuar continuar \n -Si  -No ")
        usuario=input("Opcion: ")
        if usuario == "no" or usuario== "No":
            break
        
        else:
            print("Estupendo!, sigamos avanzando")
            print()
            print("~~~~~~ADIVINANZAS~~~~~~~~")
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

            adivinanza_s=['La pera','El jardinero','El río','El reloj','La manzana','El murciélago']
            print("Compara tu respuesta con las soluciones",adivinanza_s)
            print("¿Cuantas pudiste adivinar?")
            n=int(input("Aciertos: "))
            if n == 6:
                print("FELICIDADES, lo hiciste perfecto!!")
            elif n>4 and n<6:
                print("Buen puntaje, en la siguiente lo lograras!")
            else:
                print("Las adivinanzas no son lo tuyo, pero sigue intentando!")
                
            break
        
def matematicas_primaria_2():
    while True:
        print("------------Sigamos con Matemáticas--------------")
        
        print("~~~~~~Unidades de Medida~~~~~~~")
        print("MASA: \n Lo primero que debes de conocer es la equivalencia de las unidades de masa más comunes")
        print("Unidades de masa: \n Gramo (g): Es la unidad básica. \n Kilogramo (kg): 1 kilogramo = 1000 gramos. \n Miligramo (mg): 1 miligramo = 0.001 gramos")
        print("Ahora puedes convertir cantidades en distintas unidades. \n Ejercicios: ")

        print("GRAMOS A KILOGRAMOS")
        aciertos_1=0
        while aciertos_1<3:
            num= random.randint(100,10000)
            print(num,"gramos a kg: ")
            s=float(input("Resultado= "))
            kg= num/1000
            if s==kg:
                print("Muy bien!")
                aciertos_1+=1
            else:
                print("Sigue practicando ")
                
        print("GRAMOS A MILIGRAMOS")
        aciertos_2=0
        while aciertos_2<3:
            num= random.randint(1,50)
            print(num,"gramos a miligramos: ")
            s=float(input("Resultado= "))
            mg= num*1000
            if s==mg:
                print("Muy bien!")
                aciertos_2+=1
            else:
                print("Sigue practicando ")
                
        print("--------------Siguiente Actividad------------- ")
        print("Deseas continuar continuar \n -Si  -No ")
        usuario=input("Opcion: ")
        if usuario == "no" or usuario== "No":
            break
        
        elif usuario== "si" or "Si":
            print("Esa es la actitud!,sigamos avanzando...")
        
            print("--------------Siguiente Actividad------------- ")
            print("~~~~~~Porcentajes~~~~~~~")
            print("En esta sección aprenderas a calcular el porcentaje de una cantidad, estas listo?")
            print("Sigue los siguientes pasos y luego ponlo en práctica!")
            print("Procedimiento: \n 1.Multiplica la cantidad por el porcentaje \n 2.Divide el resultado entre 100:")
            print("Fácil, cierto? \n Ahora resuelve los siguientes ejercicios, deberas acertar 8 para obtener insignia de reconocimiento")

            acierto_3=0
            for i in range(10):
                cantidad= random.randint(1,100)
                porcentaje= random.randint(1,100)
                print("Calcula el", porcentaje," % de", cantidad, ":")
                n=(float(input("n: ")))
                calculo= (cantidad*porcentaje) / 100
                if n==calculo:
                    print("Correcto")
                    acierto_3=acierto_3+1
                else:
                    print("Incorrecto")
                
            print("Obtuviste",acierto_3,"aciertos")
            if acierto_3>=8:
                print("Lo conseguiste, eres increible con los porcentajes")
            
            else:
                print("Te falta trabajar más")
            
            
            
                print("--------------Ultima Actividad------------- ")
                print("Deseas continuar \n -Si  -No ")
                usuario=input("Opcion: ")
                if usuario == "no" or usuario== "No":
                    break
            
                else:
                    print("~~~~~~Media, Mediana y Moda~~~~~~")
                    aciertos=0
                    for i in range(3):
                        print("En base a esta lista, responde lo siguiente")
                        numeros=[]
                        for i in range(7):
                            numeros.append(random.randint(2,10))

                        print(numeros)

                        #Media
                        media= float(input("Media: "))
                        med= statistics.mean(numeros)
                        redondear= round(med,2)
                        #print(redondear)
                        if media==med:
                            print("Excelente!!, sigue avanzando...")
                            aciertos+=1
                        else:
                            print("Sigue intendo...")
                        #Mediana
                        mediana= int(input("Mediana: "))
                        mediana_s=statistics.median(numeros)
                        #print(mediana_s)
                        if mediana==mediana_s:
                            print("Correcto")
                            aciertos+=1
                        else:
                            print("Sigue intendo...")
                        #Moda
                        mod= int(input("Moda: "))
                        moda= statistics.mode(numeros)
                        #print(moda)
                        if mod==moda:
                            print("Muy bien!!")
                            aciertos+=1
                        else:
                            print("Sigue intendo...")
                            
                    print("Aciertos: ",aciertos)
                    print("Terminamos Matemáticas, lo hiciste increible!!")
                    break
                               
def nivel_1p():
    español_primaria()
    print("Deseas continuar con la parte de matemáticas? \n -Si  -No")
    mat=input("Opción: ")
    if mat=="Si" or mat=="si":
        matematicas_primaria()
                       
def nivel_2p():
    print("Listo para aprender?")
    español_primaria_2()
    print("Aún hay mas por explorar!! \n Deseas continuar con la parte de matemáticas? \n -Si  -No")
    mat=input("Opción: ")
    if mat=="Si" or mat=="si":
        matematicas_primaria_2()
    
def main_primaria():
    print("------Bienvenido al Nivel Primaria------")
    #print("Selecciona una opción: \n  1° a 3° grado (1) \n  4° a 6° grado (2) \n  Salir del juego(3)")
    while(True):
        print("~~~Menú principal~~~ \n Selecciona una opción: \n  1° a 3° grado (1) \n  4° a 6° grado (2) \n  Salir del juego(3)")
        nivel= int(input("Opción: "))
        if nivel==1:
            nivel_1p()
        elif nivel ==2:
            nivel_2p()
        elif nivel==3:
            print("Gracias por jugar!")
            break
        else:
            print("Elige una opción válida(1 o 2)")
            
main_primaria()