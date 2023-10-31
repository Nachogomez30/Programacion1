
#TPNº5
# Alumno: Ignacio Gómez

import Funciones
Funciones.clear_terminal()

print("TRABAJO PRACTICO Nº5")

while True:
    option = int(input("Ingrese el numero del ejercicio (1 - 17): "))
    if option>=1 and option<=17:
        print("\n~ Ejercicio",option,"~\n")

# Ejercicio 1:
        if option == 1:
            dni= input("Ingrese su DNI (de 7 a 8 digitos): ")
            if Funciones.validation_dni(dni):
                print("Su DNI es valido.")
            else:
                print("No ha ingresado un valor valido.")

#Ejercico 2:
        elif option == 2:
            word = input("Ingrese una cadena: ")
            print("La longitud de la ulitma palabra de la cadena es:",Funciones.length_word(word))

#Ejercicio 3
        elif option == 3:
            while True:
                name = input("Ingrese el nombre completo del socio (o un nombre vacío para finalizar): ")
                if name == "" or name == " ":
                    break
                while True:
                    dni = (input("Ingrese el dni de la persona (de 7 a 8 digitos): "))
                    if Funciones.validation_dni(dni):
                        break
                identifier = (Funciones.id_club(name,dni))
                print("\nID ->",identifier)
    else:
        break