
#TPNº6
# Alumno: Ignacio Gómez

import Funciones
Funciones.clear_terminal()

print("TRABAJO PRACTICO Nº6")

while True:
    option = int(input("Ingrese el numero del ejercicio (1 - 13): "))
    if option>=1 and option<=13:
        print("\n~ Ejercicio",option,"~\n")
        
        # Ejercicio 1:
        if option == 1:
            numbers=[]
            while True:
                number = int(input("Ingrese un numero: "))
                if number == 0:
                    break
                numbers.append(number)
        
        # Ejercicio 2:
        elif option == 2:
            delet_number = int(input(" Ingrese el numero que desea eliminar: "))
            if delet_number in numbers:
                numbers.remove(delet_number)
                print("El numero",delet_number," fue eliminado-")
            else:
                print("El numero ingresado no se encuentra.")
        
        # Ejercicio 3:
        elif option == 3:
            sum_numbers = sum(numbers)
            print("La sumatoria de los números en la lista es:",sum_numbers,".")
    else:
        break