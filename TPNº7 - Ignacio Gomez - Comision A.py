
#TPNº7
# Alumno: Ignacio Gómez

import Funciones
Funciones.clear_terminal()

print("TRABAJO PRACTICO Nº7")

while True:
    option = int(input("Ingrese el numero del ejercicio (1 - 8): "))
    if option>=1 and option<=8:
        print("\n~ Ejercicio",option,"~\n")
        
        # Ejercicio 1:
        if option == 1:
            numbers = [5, 2, 9, 1, 5, 6]
            Funciones.bubble_sort(numbers)
            print("Lista ordenada:", numbers)

        
        # Ejercicio 2:
        elif option == 2:
            words = ["manzana", "banana", "camion", "hola", "apego"]
            Funciones.selection_sort(words,key=None)
            print("Lista ordenada alfabéticamente:", words)
        
        # Ejercicio 3:
        elif option == 3:
            books = [
            {"titulo": "Libro 1", "autor": "Autor 1", "anio": 2000},
            {"titulo": "Libro 2", "autor": "Autor 2", "anio": 1998},
            {"titulo": "Libro 3", "autor": "Autor 3", "anio": 2010}
            ]
            key = input("Ingrese la clave (titulo, autor o anio): ").lower()
            sorted_books = Funciones.selection_sort(books,key)
            for book in sorted_books:
                print("Titulo:", book["titulo"], "autor:", book["Autor"], "anio:", book["Anio"])
        
    else:
        break