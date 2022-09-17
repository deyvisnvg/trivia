import random

BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
RESET = '\033[39m'

bienvenida = YELLOW + '''
======================================================================================================================
                         ____  _                           _     _                           _ 
                        |  _ \(_)                         (_)   | |                         (_)
                        | |_) |_  ___ _ ____   _____ _ __  _  __| | ___     __ _   _ __ ___  _ 
                        |  _ <| |/ _ \ '_ \ \ / / _ \ '_ \| |/ _` |/ _ \   / _` | | '_ ` _ \| |
                        | |_) | |  __/ | | \ V /  __/ | | | | (_| | (_) | | (_| | | | | | | | |
                        |____/|_|\___|_| |_|\_/ \___|_| |_|_|\__,_|\___/   \__,_| |_| |_| |_|_|

  _______   _       _                   _                 _____                            _             _   __        
 |__   __| (_)     (_)                 | |               / ____|                          | |           (_) /_/        
    | |_ __ ___   ___  __ _   ___  ___ | |__  _ __ ___  | |     ___  _ __ ___  _ __  _   _| |_ __ _  ___ _  ___  _ __  
    | | '__| \ \ / / |/ _` | / __|/ _ \| '_ \| '__/ _ \ | |    / _ \| '_ ` _ \| '_ \| | | | __/ _` |/ __| |/ _ \| '_ \ 
    | | |  | |\ V /| | (_| | \__ \ (_) | |_) | | |  __/ | |___| (_) | | | | | | |_) | |_| | || (_| | (__| | (_) | | | |
    |_|_|  |_| \_/ |_|\__,_| |___/\___/|_.__/|_|  \___|  \_____\___/|_| |_| |_| .__/ \__,_|\__\__,_|\___|_|\___/|_| |_|
                                                                              | |                                      
                                                                              |_|                                      
=======================================================================================================================
''' + WHITE


# Variable
continuar = True
puntaje = random.randint(0, 10)
correctas = 0

# Lo primero es mostrar en pantalla el texto de bienvenida para quien juegue tu trivia
print(bienvenida)
print("Pondremos a prueba tus conocimientos")
print("Comenzarás con: ", puntaje, " puntos")

# Personalizar Trivia:
nombreJugador = input("Ingresa tu nombre: " + BLUE)

# Es importante dar instrucciones sobre cómo jugar:
print(WHITE +"\nHola {} Responde las siguientes preguntas escribiendo la letra de la alternativa y presionando 'Enter' para enviar tu respuesta:\n".format(nombreJugador))

# OJO, el \n al final de la línea 6 es para dar un "salto de línea"

def validarRespuesta(respuesta):
    while respuesta not in ("a", "b", "c", "d", "x"):
        respuesta = input(WHITE + "Debes responder a, b, c ó d. Ingresa nuevamente tu respuesta: "  + BLUE)

    return respuesta

# Mensaje Secreto
def mensajeSecreto(numPregunta, respuesta, mensajeSecret):
    if numPregunta == "1":
        while respuesta == "x":
            print(MAGENTA + mensajeSecret + WHITE)
            respuesta = validarRespuesta(input("\nTu respuesta: " + BLUE))
    if numPregunta == "2":
        while respuesta == "x":
            print(MAGENTA + mensajeSecret + WHITE)
            respuesta = validarRespuesta(input("\nTu respuesta: " + BLUE))
    if numPregunta == "3":
        while respuesta == "x":
            print(MAGENTA + mensajeSecret + WHITE)
            respuesta = validarRespuesta(input("\nTu respuesta: " + BLUE))

    return respuesta


def evaluarRespuesta(numPregunta, respuesta, puntaje, mensajeCorrecto, mensajeIncorrecto, correctas):
    if numPregunta == "1":
        if respuesta == "b":
            puntaje += random.randint(8, 10)
            correctas += 1
            print(WHITE + mensajeCorrecto)
            print(GREEN + "\nHasta ahora has conseguido ", puntaje, " puntos." + WHITE)
        else:
            puntaje -= 5
            print(WHITE + mensajeIncorrecto)
            print(GREEN + "\nTu puntaje hasta ahora es de ", puntaje, " puntos." + WHITE)

    if numPregunta == "2":
        if respuesta == "c":
            puntaje += random.randint(4, 6)
            correctas += 1
            print(WHITE + mensajeCorrecto)
            print(GREEN + "\nHasta ahora has conseguido ", puntaje, " puntos." + WHITE)
        else:
            puntaje -= 5
            print(WHITE + mensajeIncorrecto)
            print(GREEN + "\nTu puntaje hasta ahora es de ", puntaje, " puntos." + WHITE)
        
    if numPregunta == "3":
        if respuesta == "a":
            puntaje += random.randint(4, 6)
            correctas += 1
            if correctas == 3:
                print(WHITE + mensajeCorrecto)
                print(GREEN + "Hasta ahora has conseguido ", puntaje, " puntos." + WHITE)
            else:
                print(WHITE + "\nHas hecho hasta lo imposible para responder a todas las preguntas, eso merece ser reconocido, Felicidades")
        else:
            puntaje -= 5
            print(WHITE + mensajeIncorrecto)
            print(GREEN + "Tu puntaje hasta ahora es de ", puntaje, " puntos." + WHITE)
    
    return {
        "puntaje": puntaje,
        "correctas": correctas
    }

while continuar:
    # Pregunta 1
    print("1) ¿Quién fue el creador de windows?")
    print("   a) Linus Torvalds")
    print("   b) Bill Gates")
    print("   c) Mark Zuckerberg")
    print("   d) Dennis Ritchie")

    # Almacenamos la respuesta del usuario en la variable "respuesta_1"
    numPregunta_1 = "1"
    mensajeSecret_1 = "Mensaje secreto: Jovenes apasionados de la tecnología, crean el 4 de abril una pequeña compañía llamada Microsoft"
    mensajeCorrecto_1 = "\nFelicidades!!!, eres un genio, se ve que sabes mucho de este tema, continúa retandote respondiendo las siguientes preguntas."
    mensajeIncorrecto_1 = "\nOOHH! Fallaste, has perdido 5 puntos, la Respuesta es Bill Gates.\nPero puedes seguir retandote con las siguientes interrogantes, Suerte!!!"

    respuesta_1 = input("\nTu respuesta: " + BLUE)
    respuesta_1 = validarRespuesta(respuesta_1)
    respuesta_1 = mensajeSecreto(numPregunta_1, respuesta_1, mensajeSecret_1)
    result = evaluarRespuesta(numPregunta_1, respuesta_1, puntaje, mensajeCorrecto_1, mensajeIncorrecto_1, correctas)
    puntaje = result["puntaje"]
    correctas = result["correctas"]
        
    # Pregunta 2
    print("\n2) ¿Que significan las siglas CPU?")
    print("   a) Consejo de Poetas Unidos")
    print("   b) Unidad Central Personal")
    print("   c) Unidad Central de Procesamiento")
    print("   d) Central Para Unir")

    # Almacenamos la respuesta del usuario en la variable "respuesta_2"
    numPregunta_2 = "2"
    mensajeSecret_2 = "Mensaje secreto: Es la parte de una computadora en la que se encuentran los elementos que sirven para procesar datos "
    mensajeCorrecto_2 = "\nFelicidades!!!, eres un genio, se ve que sabes mucho de este tema, continúa retandote respondiendo las siguientes preguntas."
    mensajeIncorrecto_2 = "\nOOHH! Fallaste, has perdido 5 puntos, la Respuesta es Unidad Central de Procesamiento.\nPero puedes seguir retandote con las siguientes interrogantes, Suerte!!!"
    
    respuesta_2 = input("\nTu respuesta: " + BLUE)
    respuesta_2 = validarRespuesta(respuesta_2)
    respuesta_2 = mensajeSecreto(numPregunta_2, respuesta_2, mensajeSecret_2)
    result = evaluarRespuesta(numPregunta_2, respuesta_2, puntaje, mensajeCorrecto_2, mensajeIncorrecto_2, correctas)
    puntaje = result["puntaje"]
    correctas = result["correctas"]

    # Pregunta 3
    print("\n3) ¿Cual es el sistema de numeración que sólo utiliza dos dígitos, 0 y 1?")
    print("   a) Binario")
    print("   b) Unitario")
    print("   c) Calculadora")
    print("   d) Terciario")

    # Almacenamos la respuesta del usuario en la variable "respuesta_3"
    numPregunta_3 = "3"
    mensajeSecret_3 = "Mensaje secreto: Conocido también como el sistema digital. También llamado sistema diádico en ciencias de la computación"
    mensajeCorrecto_3 = "\nFelicidades!!!, eres completamente un genio, has logrado responder a todas las preguntas."
    mensajeIncorrecto_3 = "\nOOHH! Fallaste, has perdido 5 puntos, la Respuesta es Binario.\nHas hecho hasta lo imposible para responder a todas las preguntas, eso merece ser reconocido, Felicidades"
    
    respuesta_3 = input("\nTu respuesta: " + BLUE)
    respuesta_3 = validarRespuesta(respuesta_3)
    respuesta_3 = mensajeSecreto(numPregunta_3, respuesta_3, mensajeSecret_3)
    result = evaluarRespuesta(numPregunta_3, respuesta_3, puntaje, mensajeCorrecto_3, mensajeIncorrecto_3, correctas)
    puntaje = result["puntaje"]
    correctas = result["correctas"]

    print(GREEN + "\nGracias ", nombreJugador, " alcanzaste ", puntaje, " puntos")
    respContinuar = input(WHITE + "\n¿Desea volver a Evaluarse?, Responde (y ó n): " + BLUE).upper()

    while respContinuar not in ("Y", "N"):
        respContinuar = input(WHITE + "Debes responder y, n, Y ó N. Ingresa nuevamente tu respuesta: " + BLUE).upper()

    if respContinuar == "Y":
        continuar = True
        puntaje = random.randint(0, 10)
        correctas = 0
        print("\n--------------------------------------------------------\n")
        print(WHITE + "Comenzarás con: ", puntaje, " puntos\n")
    else:
        continuar = False
        print(GREEN + "\nGracias ", nombreJugador,
              " por jugar mi Trivia, alcanzaste ", puntaje, " puntos")
