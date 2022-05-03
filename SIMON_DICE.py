import time
import os
import random

def borrarPantalla():
   if os.name == "posix":
       os.system ("clear")
   elif os.name == "ce" or os.name == "nt" or os.name == "dos":
       os.system ("cls")
borrarPantalla()

def apagar_tablero():
    global tabla
    tabla = [
            ["                ","                 "],
            ["|-------------| "," |-------------| "],
            ["|             | "," |             | "],
            ["|      1      | "," |      2      | "],
            ["|             | "," |             | "],
            ["|-------------| "," |-------------| "],
            ["                ","                 "],
            ["                ","                 "],
            ["|-------------| "," |-------------| "],
            ["|             | "," |             | "],
            ["|      3      | "," |      4      | "],
            ["|             | "," |             | "],
            ["|-------------| "," |-------------| "],
            ["                ","                 "],
        ]

apagar_tablero()
def tiempo(x):
    if x==1:
        time.sleep(0.7)
    if x==2:
        time.sleep(0.5)
    if x ==3:
        time.sleep(0.3)
    if x ==4:
        time.sleep(0.1)
    
def iluminar_cuadrado1():
    x = 0
    for i in tabla:
        x = x+1
        if x == 8:
            break
        else:
            i[0] = "\033[41m" + i[0] + "\033[0m"

def iluminar_cuadrado2():
    x = 0
    for i in tabla:
        x = x+1
        if x == 8:
            break
        else:
            i[1] = "\033[42m" + i[1] + "\033[0m"

def iluminar_cuadrado3():
    x = 0
    for i in tabla:
        x = x+1
        if x < 8:
            continue
        else:
            i[0] = "\033[44m" + i[0] + "\033[0m"

def iluminar_cuadrado4():
    x = 0
    for i in tabla:
        x = x+1
        if x < 8:
            continue
        else:
            i[1] = "\033[45m" + i[1] + "\033[0m"

def mostrar_tablero():
    for i in tabla:
        for x in i:
            print("\t",x,end="")
        print("")

print("""

                        Estas en el juego de Simon Dice
                        
                        Niveles de Dificultad:
                        1- Principiate
                        2- Profesional
                        3- Avanzado
                        4- Experto

                        
                        """)

dificultad = int(input("Elige el nivel de dificultad: "))
borrarPantalla()
def mostrar_pantalla():
    for i in tabla:
        for x in i:
            print("\t",x,end="")
        print("")
    tiempo(dificultad)
    borrarPantalla()
    apagar_tablero()


salir = False
contador = 0
numeros = ""

while salir == False:
    contador += 1
    aleatorio = random.randrange(1,5)
    aleatoriostr = str(aleatorio)
    numeros += aleatoriostr
    for i in numeros:
        if i == "1":
            iluminar_cuadrado1()
        if i == "2":
            iluminar_cuadrado2()
        if i == "3":
            iluminar_cuadrado3()
        if i == "4":
            iluminar_cuadrado4()
        mostrar_pantalla()
        mostrar_tablero()
        tiempo(dificultad)
        borrarPantalla()
    mostrar_tablero()
    adivinar = input("Dime la secuencia de numeros: ")
    if adivinar == numeros:
        print("Has acertado, ¡CONTINUA!")
        time.sleep(1)
        borrarPantalla()
        
    else:
        print("\n¡Has perdido!\n")
        if dificultad ==1:
            modo = "Principiante"
        elif dificultad ==2:
            modo = "Profesional"
        elif dificultad ==3:
            modo = "Avanzado"
        elif dificultad ==4:
            modo = "Extremo"

        print("Has llegado hasta el nivel",contador,"en modo",modo,"\n\n")
        salir = True