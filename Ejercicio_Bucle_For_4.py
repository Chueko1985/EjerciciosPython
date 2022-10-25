"""
un grupo de amigos decide organizar un juego de estrategia, por lo cual forman dos
equipos de 6 integrantes cada uno, donde un integrante de cada equipo es del "Jefe" y
los otros 5 son sus "oficiales". Le regla mas importante del juego es que solo se
comunicaran mediante un canal comun, por l oque deben buscar la forma de ocultar el
contenido de sus mensajes. Uno de los equipos decide utilizar un metodo antigu de
encriptacion llamado "la cifra del cesar" que consiste en correr cada letra del
mensaje -considerendo la posicion de cada uno en el alfabeto- un determinada cantidad
de lugares. Ejemplo: si el corrimiento de dos 2 lugares la palabra "ATAQUE" se
transforma en "CVCSWG".
cada dia el jefe del equipo debe enviar un mensaje a cada uno de sus oficiales.
Escribir un programa que permita encriptar los 5 mensajes. El corrimiento
(cantidad de lugares que se correrean las letras) sera dado por el usuario antes de
comenzar a encriptar. Los 5 mensajes usaran el mismo corrimiento. 
Nota: si el alfabeto termina antes de poder correr la cantidad de lugares necesario,
se vuelve a comenzar desde la letra A. Ejemplo: la palagra "EXTRA" corrida 3 lugares
se convierte en "HAWUD". Utilizando el alfabeto español, de 27 letras, el siguiente
calculo matematico permite volver a comenzar por el principio de una vez que ese lleego a
la z: (indice de la letra correr+corrimiento)%27
Solo se encriptaran las letras de los mensajes, dejando el resto de caracteres sin modificacion.
"""
alfabeto="abcdefghijklmnñopqrstuvwxyz"
corrimiento=int(input("Ingrese el corrimiento: "))
for i in range(5):
    mensaje = input("ingrese el msj a encriptar: ")
    encriptado = ""
    for caracter in mensaje:
        if caracter.lower() in alfabeto:
            indice=alfabeto.find(caracter.lower())
            indice = (indice+corrimiento)%27
            encriptado = encriptado +alfabeto[indice]
        else:
            encriptado = encriptado + caracter
    print(encriptado)