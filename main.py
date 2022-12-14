import os
import random
import time

#CODIGOS DE COLORES

NEGRO = '\033[30m'
ROJO = '\033[31m'
VERDE = '\033[32m'
AMARILLO = '\033[33m'
AZUL = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
BLANCO = '\033[37m'
RESET = '\033[39m'
print(CYAN + "bienvenido a mi trivia sobre el espacio".replace("b", "B"))
nombre = input("Ingresa tu nombre:" + RESET)
print(CYAN + "\n Hola", nombre, "Responder las siguientes preguntas" + RESET)
print(
    CYAN +
    "En este apartado podrás ver 4 preguntas a las cuales tu tendras que responder cual crees que es la respuesta correcta\n"
    + RESET)
print(
    ROJO +
    "He ocultado la respuesta en una de las 4 preguntas, solo es cuestion de pedir `ayuda`"
    .upper() + RESET)
iniciartrivia = True
Intento = 0
lista1 = []

while iniciartrivia == True:
    Intento += 1
    perdidas=0
    ganancias=0
    print("\nIntento numero:", Intento)
    puntaje = random.randint(1, 11)
    print(AZUL + "\nTienes", puntaje, "puntos para empezar\n" + RESET)
    print(CYAN + "Mucha suerte y que empieze la trivia:\n" + RESET)
    for cuenta in range(0, 6, +1):
        print(cuenta)
        time.sleep(1)

        #PREGUNTA1

    print("\n1) Cuantos planetas orbitan en el Sistema Solar? ")
    print(MAGENTA + "\na) 6" + RESET)
    print(MAGENTA + "b) 7" + RESET)
    print(MAGENTA + "c) 8" + RESET)
    print(MAGENTA + "d) 10" + RESET)

    respuestacorrecta = input("\nTu respuesta:")

    #Esquivar estas letras

    while respuestacorrecta not in ("a", "b", "c", "d", "A", "B", "C", "D"):
        respuestacorrecta = input(
            "Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")
    respuestacorrecta = respuestacorrecta.lower()
    if respuestacorrecta == "a":
        aleatorio = random.randint(1, 11)
        perdidas = perdidas+aleatorio
        puntaje = puntaje - aleatorio
        print(ROJO + "\nIncorrecto!", "Tu puntaje a disminuido en", aleatorio,
              "puntos\n\n", nombre,
              " Debes estudiar más sobre el Espacio\n" + RESET)
        print("Tu puntaje actual es de", puntaje, "puntos\n")
    elif respuestacorrecta == "b":
        aleatorio = random.randint(1, 11)
        puntaje = puntaje - aleatorio
        perdidas = perdidas+aleatorio
        print(ROJO + "\nIncorrecto!", "Tu puntaje a disminuido en", aleatorio,
              "puntos\n\n", nombre,
              " Debes estudiar más sobre el Espacio\n" + RESET)
        print("Tu puntaje actual es de", puntaje, "puntos\n")

    elif respuestacorrecta == "c":
        aleatorio = random.randint(5, 11)
        puntaje = puntaje + aleatorio
        ganancias = ganancias+aleatorio
        print(VERDE + "\nMuy bien".upper(), nombre,
              "!\n \nTu puntaje a aumentado en", aleatorio, "puntos" + RESET)
        print(AZUL + "\nTu puntaje actual es de", puntaje, "puntos\n" + RESET)
    else:
        aleatorio = random.randint(1, 11)
        puntaje = puntaje - aleatorio
        perdidas = perdidas+aleatorio
        print(ROJO + "\nIncorrecto!", "Tu puntaje a disminuido en", aleatorio,
              "puntos\n\n", nombre, "Te pasaste de alternativa\n" + RESET)
        print("Tu puntaje actual es de", puntaje, "puntos\n")

    #PREGUNTA2

    time.sleep(3)
    print("2) Cual fue el primer hombre en pisar la Luna?")
    print(MAGENTA + "\na) Franklink Chang Diaz" + RESET)
    print(MAGENTA + "b) Yuri Gagarin" + RESET)
    print(MAGENTA + "c) Pedro Duque" + RESET)
    print(MAGENTA + "d) Neil Alden Armstrong" + RESET)

    respuestacorrecta = input("\nTu respuesta:")

    while respuestacorrecta not in ("a", "b", "c", "d", "A", "B", "C", "D",
                                    "ayuda"):
        respuestacorrecta = input(
            "Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")
    respuestacorrecta = respuestacorrecta.lower()

    if respuestacorrecta == "a":
        aleatorio = random.randint(1, 11)
        puntaje = puntaje - aleatorio
        perdidas = perdidas+aleatorio
        print(ROJO + "\nIncorrecto!", "Tu puntaje a disminuido en", aleatorio,
              "puntos\n\n", nombre,
              "Debes estudiar mas sobre el Espacio\n" + RESET)
        print("Tu puntaje actual es de", puntaje, "puntos\n")

    elif respuestacorrecta == "b":
        aleatorio = random.randint(1, 11)
        puntaje = puntaje - aleatorio
        perdidas = perdidas+aleatorio
        print(ROJO + "\nIncorrecto!", "Tu puntaje a disminuido en", aleatorio,
              "puntos\n\n", nombre,
              "Sigue intentando te faltan pocas alternativas\n" + RESET)
        print("Tu puntaje actual es de", puntaje, "puntos\n")

    elif respuestacorrecta == "d":
        aleatorio = random.randint(5, 11)
        puntaje = puntaje + aleatorio
        ganancias = ganancias+aleatorio
        print(VERDE + "\nMuy bien".upper(), nombre,
              "!\n \nTu puntaje a aumentado en", aleatorio, "puntos" + RESET)
        print(AZUL + "\nTu puntaje actual es de", puntaje, "puntos\n" + RESET)

    elif respuestacorrecta == "ayuda":  #respuesta comodin
        print(
            AMARILLO +
            "\nEsta es una respuesta secreta, automaticamente te dare un puntaje aleatorio entre 20 y 100, cruza los dedos"
            + RESET)
        puntaje += random.randint(20, 101)
        print(AZUL + "\nTu puntaje es de", puntaje, "puntos\n" + RESET)
    else:
        aleatorio = random.randint(1, 11)
        puntaje = puntaje - aleatorio
        perdidas = perdidas+aleatorio
        print(ROJO + "\nIncorrecto!", "Tu puntaje a disminuido en", aleatorio,
              "puntos\n\n", nombre, "Te pasaste de alternativa\n" + RESET)
        print("Tu puntaje actual es de", puntaje, "puntos\n")

        #PREGUNTA3

    time.sleep(3)
    print("3) Cuantas lunas tiene el planeta Venus?")
    print(MAGENTA + "\na) 3" + RESET)
    print(MAGENTA + "b) 0" + RESET)
    print(MAGENTA + "c) 5" + RESET)
    print(MAGENTA + "d) 1" + RESET)

    respuestacorrecta = input("\nTu respuesta:")

    while respuestacorrecta not in ("a", "b", "c", "d", "A", "B", "C",
                                    "D"):  #inicio de while
        respuestacorrecta = input(
            "Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")
    respuestacorrecta = respuestacorrecta.lower()

    if respuestacorrecta == "a":
        aleatorio = random.randint(1, 11)
        puntaje = puntaje - aleatorio
        perdidas = perdidas+aleatorio
        print(ROJO + "\nIncorrecto!", "Tu puntaje a disminuido en", aleatorio,
              "puntos\n\n", nombre,
              "Debes estudiar mas sobre el Espacio\n" + RESET)
        print("Tu puntaje actual es de", puntaje, "puntos\n")

    elif respuestacorrecta == "c":
        aleatorio = random.randint(1, 11)
        puntaje = puntaje - aleatorio
        perdidas = perdidas+aleatorio
        print(ROJO + "\nIncorrecto!", "Tu puntaje a disminuido en", aleatorio,
              "puntos\n\n", nombre,
              "Sigue intentando te faltan pocas alternativas\n" + RESET)
        print("Tu puntaje actual es de", puntaje, "puntos\n")

    elif respuestacorrecta == "b":
        aleatorio = random.randint(5, 11)
        puntaje = puntaje + aleatorio
        ganancias = ganancias+aleatorio
        print(VERDE + "\nMuy bien".upper(), nombre,
              "!\n \nTu puntaje a aumentado en", aleatorio, "puntos" + RESET)
        print(AZUL + "\nTu puntaje actual es de", puntaje, "puntos\n" + RESET)
    else:
        aleatorio = random.randint(1, 11)
        puntaje = puntaje - aleatorio
        perdidas = perdidas+aleatorio
        print(ROJO + "\nIncorrecto!", "Tu puntaje a disminuido en", aleatorio,
              "puntos\n\n", nombre, "Te pasaste de alternativa\n" + RESET)
        print("Tu puntaje actual es de", puntaje, "puntos\n")

        #PREGUNTA 4

    time.sleep(3)
    print("4) En que pais cayo el meteorito que mato a todos los dinosaurios?")
    print("\nA continuacion veras una pregunta IMPORTANTE, Si respondes correctamente tus puntos se veran multiplicados y si lamentablemente tu respuesta es erronea seras PERJUDICADO, ¡Ten Cuidado!")

    #OPCIONES DE PREGUNTA DIFICIL

    print(MAGENTA + "\na) Mexico" + RESET)
    print(MAGENTA + "b) Panama" + RESET)
    print(MAGENTA + "c) Peru" + RESET)
    print(MAGENTA + "d) Brasil" + RESET)

    respuestacorrecta = input("\nTu Respuesta:")

    while respuestacorrecta not in ("a", "b", "c", "d", "A", "B", "C", "D"):
        respuestacorrecta = input(
            "Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")
    respuestacorrecta = respuestacorrecta.lower()
    if respuestacorrecta == "a":
        print(VERDE + "\nMuy bien".upper() + RESET)
        print(VERDE + "\nEnhorabuena Tu puntaje a sido multiplicado por 2" +
              RESET)
        puntaje = puntaje * 2
    elif respuestacorrecta == "b":
        print("\nPanama no existia en ese tiempo, A ESTUDIAR")
        print(
            "\nQue mala suerte, Respuesta incorrecta, Tu puntaje sera dividido a la mitad"
        )
        puntaje = puntaje / 2
    elif respuestacorrecta == "c":
        print(
            "\nPeru no es la respuesta correcta, Lo unico bueno es su gastronomia y Machu Pichu"
        )
        print(
            "\nRecorcholis, Tu respuesta es erronea, a continuacion restaremos 2 puntos"
        )
        puntaje = puntaje - 2
    else:
        print(
            "\nBrasil en ese tiempo ya tenia 3 mundiales sin que exista el mundial, solo por eso te dare 2 puntos, continue tentando meu amigo"
        )
        print(
            "\nTuviste suerte, es mala respuesta pero por solidaridad mia te regalare 2 puntos, pero solo por esta vez"
        )
        puntaje = puntaje + 2
    print("\nGracias", nombre, "Tu puntaje en esta Trivia es de", puntaje,
          "puntos")
    print(VERDE + "\nDeseas continuar la trivia nuevamente?" + RESET)
    repetirtrivia = input(
        VERDE +
        "\nResponder con un si, si deseas repetir la trivia, o cualquier tecla si deseas terminarla:"
        + RESET).lower()
    
    lista1.append(puntaje)
    if repetirtrivia == "si":
        print("\nGENIAL! Intentemoslo otra vez", nombre)
        iniciartrivia = True
        print("\nEstos fueron tus puntos perdidos:",perdidas)
        print("\nEstos fueron tus puntos ganados:",ganancias)
        time.sleep(7)
        os.system("clear")
    else:  #DESPEDIDA DE MI TRIVIA
        print(VERDE + "\nEspero te haya gustado mi Trivia", nombre,
              "Vuelve pronto" + RESET)
        iniciartrivia = False
        print(VERDE + "\nRecord de Puntajes de Mi Trivia:" +
              RESET)  #RECORD DE PUNTAJE
        for number in range(0, Intento, 1):
            print(lista1[number])
