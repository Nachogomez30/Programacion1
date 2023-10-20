import random
from Funciones import*

#Nombre del juego
print("\n~ AHORCADO ~")

#Creamos una lista de palabras para el juego
#Y asignamos de manera aleatoria una palabra de la lista a la variable 'hidden_word'
words = ["COMPUTADORA","PROGRAMA","INTERNET","SERVIDOR","IMPRESORA","PANTALLA","USUARIO","TECNOLOGIA","APLICACION","ARCHIVO","CONEXION","SISTEMA","DESARROLLO"]
hidden_word = random.choice(words)

#Inicializamos la variable 'number_of_attempts' que corresponde a la cantidad de intentos para los cuales la letra ingresada no se encontró en la palabra
#En la variable 'characters' se irán almacenando las letras que ingrese el usuario
number_of_attempts = 6
characters = ""

#Llamamos una primera vez a la función para asignarle a la variable word los espacios correspondientes a la palabra
word = fill_word(characters,hidden_word)

#Mostramos la cantidad de intentos disponibles
print("Cantidad de intentos disponibles:",number_of_attempts,)
print("------------------------------------------")

#Mientras el usuario no haya agotado todo sus intentos, se repite el procedimiento
while number_of_attempts>0:        
    #Solicitamos al usuario que ingrese una letra
    letter = input("Ingrese una letra: ").upper()
    
    #Validamos que el usuario ingrese un único caracter
    while len(letter)!=1:
        letter = input("Debe ingresar solo una letra, intente de nuevo: ")

    #Agregamos la letra ingresada a la variable 'characters'
    characters += letter

    #Si la palabra anterior no ha cambiado después de haber ingresado una letra nueva, significa que dicha letra no se encontraba en la palabra
    #Por lo tanto la cantidad de intentos disminuye en uno y mostramos un mensaje por pantalla
    if word == fill_word(characters,hidden_word):
        print("La letra no se encuentra en la palabra")                    
        number_of_attempts -=1
    
    #Llamamos a la función y mandamos como argumento la variable con las letras que ha ingresado el usuario y la palabra oculta
    #Asignamos el retorno de la función a la variable 'word' y la mostramos por pantalla
    word = fill_word(characters,hidden_word)
    print("\n  ",word)        
            
    #Si la variable 'word' es igual a 'hidden_word' significa que el usuario ha adivinado la palabra
    if word == hidden_word:
        #Mostramos un mensaje por pantalla con la cantidad de intentos restantes y mediante un 'break' damos por finalizado el ciclo 
        print("\nMuy bien! Adivinaste la palabra \nCantidad de intentos restantes:",number_of_attempts)
        break
    
    print("------------------------------------------")
    
#Por último, si el usuario agotó los intentos disponibles, mostramos un mensaje por pantalla
if number_of_attempts==0:
    print(f"Te has quedado sin intentos... \nLa palabra era: '{hidden_word}'")
print()