#TPNº8
# Alumno: Ignacio Gómez

import Funciones
Funciones.clear_terminal()

print("TRABAJO PRACTICO Nº8")

while True:
    option = int(input("Ingrese el numero del ejercicio (1 - 8): "))
    if option>=1 and option<=10:
        print("\n~ Ejercicio",option,"~\n")
        
        # Ejercicio 1:
        if option == 1:
            num = int(input("Ingrese un numero positivo: "))
            if num > 0:
                digits = Funciones.count_digits(num)
                print(f"El numero {num} tiene {digits} ddigitos.")
            else:
                print("No ha ingresado un numero positivo.")
        if option == 2:
            n = int(input("Ingrese un numero entero: "))
            b = int(input("Ingrese otro numero entero: "))
            if n >= 0 and b >= 2:
                if Funciones.is_power_of(n, b):
                    print(f"{n} es potencia de {b}.")
                else:
                    print(f"{n} no es potencia de {b}.")
            else:
                print("Ha ingresado un valor invalido.")
        if option == 3:
            a = input("Ingrese una cadena: ")
            b = input("Ingrese la subcadena: ")
            positions = Funciones.positions_of(a, b)
            if positions:
                print(f"La subcadena '{b}' Se encuentra en las posicions: {positions}")
            else:
                print(f"La subcadena '{b}' no se encuentra en el texto: '{a}'.")
    else:
        break