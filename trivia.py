import random

# Variable
continuar = True
puntaje = random.randint(0, 10)
correctas = 0

# Lo primero es mostrar en pantalla el texto de bienvenida para quien juegue tu trivia
print("Bienvenido a mi trivia sobre computación")
print("Pondremos a prueba tus conocimientos")
print("Comenzarás con: ", puntaje, " puntos")

#Personalizar Trivia:
nombreJugador = input("Ingresa tu nombre: ")

# Es importante dar instrucciones sobre cómo jugar:
print("\nHola {} Responde las siguientes preguntas escribiendo la letra de la alternativa y presionando 'Enter' para enviar tu respuesta:\n".format(nombreJugador))

# OJO, el \n al final de la línea 6 es para dar un "salto de línea"

def evaluarRespuesta(respuesta):
  while respuesta not in ("a", "b", "c", "d", "x"):
    respuesta = input("Debes responder a, b, c ó d. Ingresa nuevamente tu respuesta: ")

  return respuesta

while continuar:
  # Pregunta 1
  print("1) ¿Quién fue el creador de windows?")
  print("   a) Linus Torvalds")
  print("   b) Bill Gates")
  print("   c) Mark Zuckerberg")
  print("   d) Dennis Ritchie")

  # Almacenamos la respuesta del usuario en la variable "respuesta_1"
  respuesta_1 = input("\nTu respuesta: ")
  respEvaluada1 = evaluarRespuesta(respuesta_1)

  # Mensaje Secreto
  while respEvaluada1 == "x":
    print("Mensaje secreto: Jovenes apasionados de la tecnología, crean el 4 de abril una pequeña compañía llamada Microsoft")
    respEvaluada1 = evaluarRespuesta(input("\nTu respuesta: "))
  #Evaluamos respuesta 1
  if respEvaluada1 == "b":
    puntaje += random.randint(8, 10)
    correctas += 1
    print("\nFelicidades!!!, eres un genio, hasta ahora has conseguido ", puntaje," puntos, se ve que sabes mucho de este tema, continúa retandote respondiendo las siguientes preguntas.")
  else:
    puntaje -= 5
    print("\nOOHH! Fallaste, has perdido 5 puntos")
    print("\nTu puntaje total es de ", puntaje,", la Respuesta es Bill Gates, pero puedes seguir retandote con las siguientes interrogantes, Suerte!!!")
  

  # Pregunta 2
  print("\n2) ¿Que significan las siglas CPU?")
  print("   a) Consejo de Poetas Unidos")
  print("   b) Unidad Central Personal")
  print("   c) Unidad Central de Procesamiento")
  print("   d) Central Para Unir")

  # Almacenamos la respuesta del usuario en la variable "respuesta_2"
  respuesta_2 = input("\nTu respuesta: ")
  respEvaluada2 = evaluarRespuesta(respuesta_2)

  # Mensaje Secreto
  while respEvaluada2 == "x":
    print("Mensaje secreto: Es la parte de una computadora en la que se encuentran los elementos que sirven para procesar datos ")
    respEvaluada2 = evaluarRespuesta(input("\nTu respuesta: "))
  # Evaluamos respuesta 2
  if respEvaluada2 == "c":
    puntaje += random.randint(4, 6)
    correctas += 1
    print("\nFelicidades!!!, eres un genio, hasta ahora has conseguido ", puntaje," puntos, se ve que sabes mucho de este tema, continúa retandote respondiendo las siguientes preguntas.")
  else:
    puntaje -= 5
    print("\nOOHH! Fallaste, has perdido 5 puntos")
    print("\nTu puntaje total es de ", puntaje,", la Respuesta es Unidad Central de Procesamiento, pero puedes seguir retandote con las siguientes interrogantes, Suerte!!!")

  # Pregunta 3
  print("\n3) ¿Cual es el sistema de numeración que sólo utiliza dos dígitos, 0 y 1?"
  )
  print("   a) Binario")
  print("   b) Unitario")
  print("   c) Calculadora")
  print("   d) Terciario")

  # Almacenamos la respuesta del usuario en la variable "respuesta_3"
  respuesta_3 = input("\nTu respuesta: ")
  respEvaluada3 = evaluarRespuesta(respuesta_3)

  # Mensaje Secreto
  while respEvaluada3 == "x":
    print("Mensaje secreto: Conocido también como el sistema digital. También llamado sistema diádico en ciencias de la computación")
    respEvaluada3 = evaluarRespuesta(input("\nTu respuesta: "))
  #Evaluamos respuesta 3
  if respEvaluada3 == "a":
    puntaje += random.randint(8, 10)
    correctas += 1
    if correctas == 3:
      print("\nFelicidades!!!, eres completamente un genio, has logrado responder a todas las preguntas.")
    else:
      print("\nHas hecho hasta lo imposible para responder a todas las preguntas, eso merece ser reconocido, Felicidades")
  else:
    puntaje -= 5
    print("\nOOHH! Fallaste, has perdido 5 puntos")
    print("\nLa Respuesta es Binario, Si deseas puedes volver a realizar la evaluación")

  print("\nGracias ", nombreJugador, " alcanzaste ", puntaje, " puntos")
  respContinuar = input("\n¿Desea Volver a Evaluarse?, Responde (S ó N): ")

  if respContinuar.upper() == "S":
    continuar = True
    puntaje = random.randint(0, 10)
    correctas = 0
    print("\n--------------------------------------------------------\n")
  else:
    continuar = False
    print("\nGracias ", nombreJugador, " por jugar mi Trivia, alcanzaste ", puntaje, " puntos")