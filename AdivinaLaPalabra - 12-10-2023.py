import random

#Creamos una lista con muchas palabras para el juego
words = ["ARBOL", "IMPRESO", "ORQUESTA", "BANCO", "PERSONAS", "CAMION", "MESA", "CENTRIFUGADO", "GATO", "PEZ", "MURCIELAGO", "MAR", "SEÑAL", "CAMPESINO", "CIELO", "AMIGO", "ENCHUFAR", "VOLANTE", "ARBUSTO", "SUBMARINO", "NEUMATICO"]

print("\n~ ADIVINE LA PALABRA ~")
print("-------------------------------------------------------------")

#Asignamos de manera aleatoria una palabra de la lista a la variable 'hidden_word'
#Inicializamos la variable 'number_of_attempts' la cual corresponde a la cantidad de intentos del usuario
hidden_word = random.choice(words)
number_of_attempts = 1

#Contamos la cantidad de letras de la palabra oculta y asignamos dicho valor a la variable 'word_length'
word_length = len(hidden_word)

#El ciclo se repite hasta que se realicen 10 intentos o bien hasta que el usuario adivine la palabra
print(f"Ingrese una palabra de {word_length} letras que no se repitan")
while number_of_attempts<=10:
    condition = False

    #Pedimos una palabra al usuario hasta que ingrese una palabra válida    
    while condition == False:
        attempt = input("   -> ").upper()
        
        #Corroboramos que la palabra ingresada tenga la misma cantidad de letras que la palabra oculta, de lo contrario, pedimos nuevamente la palabra al usuario        
        while len(attempt)!=word_length:
            print(f"La palabra no es de {word_length} letras")
            attempt = input("   -> ").upper()
            if len(attempt)==5:
                break
            
        #Corroboramos que la palabra ingresada no contenga letras repetidas    
        condition = True
        for i in range(word_length):
            for j in range(i+1,word_length):
                if attempt[i] == attempt[j]:
                    condition = False

        #Si es así, mostramos un mensaje por pantalla
        if condition==False:
            print("La palabra tiene letras repetidas")                    

    #Creamos una lista con los espacios para las letras de la palabra oculta
    x = []
    for i in range(word_length):
        x.append("_") 

    correct = 0
    regular = 0

    #Mostramos por pantalla el número de intentos y comparamos la palabra ingresada por el usuario con la palabra oculta
    #Repetimos este procedimiento para la cantidad de letras de la palabra ingresada
    print(f"\n-Intento N°{number_of_attempts} de 10-")
    for i in range(word_length):
        #Si la letra de la posición 'i' coincide con la letra de la palabra, agregamos dicha letra en la posición correspondiente en la lista
        if attempt[i] == hidden_word[i]:
            x[i] = attempt[i]
            correct +=1

        #Si la letra se encuentra en la palabra pero no coincide la posición, mostramos un mensaje por pantalla
        elif attempt[i] in hidden_word:   
            print(f"La letra '{attempt[i]}' se encuentra en la palabra pero no en esa posición")       
            regular +=1

    #Mostramos por pantalla la lista con las letras que se encuantran en la posición correcta
    for i in range(word_length):
        print(x[i], end = " ")        
    print("\n")

    #En el caso que no haya coincidido ninguna letra, avisamos al usuario
    if correct==0 and regular==0:
        print("No coincide ninguna letra")                    
    
    #Si la palabra ingresada es la palabra oculta, mostramos un mensaje por pantalla y salimos del ciclo
    if correct == word_length:        
        print("Muy bien! Adivinaste la palabra \nCantidad de intentos:",number_of_attempts)
        break

    #Aumentamos en uno la cantiadad de intentos realizados
    number_of_attempts +=1
    print("-------------------------------------------------------------")
    
#Si no se adivinó la palabra en los intentos disponibles, mostramos un mensaje por pantalla
if number_of_attempts==11:
    print("Te has quedado sin intentos…")
print()
