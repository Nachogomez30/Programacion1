#    -Parcial Nº1-
# Alumno: Ignacio Gómez Garcia
# Comision: A

# Iniacializacion de variables
pair_numbers = 0
odd_numbers = 0
aux = 0
vowels = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}

# Se le pide al usuario su nombre
user_name = input("Ingrese su nombre: ")
user_name = user_name.title()

# Menú y elección de opcion
while True:
    print("\n--------------------------------")
    print("1) - Juego de números")
    print("2) - Juego de palabras")
    print("3) - Salir")
    print("--------------------------------")
    option = int(input("Ingrese '1' o '2' o '3' para elegir una opcion: "))
    
    if option != 1 and option != 2 and option != 3:
        print(f"{user_name} has ingresado una opcion incorrecta.")
    else:
        break

# Juego de Números
if option==1:
    print(f"\n{user_name} has elegido el 'Juego de números'. \nDebe ingresar numeros enteros, si deseas terminar ingresa un '0'.\n")
    
    # Se ingresa un numero hasta que que se ingrese '0'
    while True:
        game_1 = int(input(f"{user_name} ingresa un numero entero: "))
        if game_1==0:
            break
        elif game_1%2==0 and game_1>pair_numbers:
            pair_numbers = game_1
        elif game_1%2 != 0:
            odd_numbers += game_1
            aux+=1
    
    # Promedio de numeros impares
    odd_numbers=odd_numbers/aux
    
    print(f"\nEl mayor número par es: {pair_numbers} \nEl promedio de los números impares es: {odd_numbers}")

# Juego de Palabras
elif option==2:
    print(f"\n{user_name} has elegido el 'Juego de palabras'.\nDebe ingresar una frase.\n")
    
    phrase = input("Ingrse una frase: ")
    
    # Se valida cuantas vocales hay de cada una
    for letter in phrase.lower():
        if letter in vowels:
            vowels[letter] += 1

    for vowel, cant in vowels.items():
        print(f"La vocal '{vowel}' aparece {cant} veces en la frase.")

# Opcion Salida
else:
    print(f"\n¡Hasta luego {user_name}!")