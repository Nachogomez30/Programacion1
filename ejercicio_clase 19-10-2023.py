import Funciones

count_number = 0

while True:
    number = int(input("Ingrese un número: "))
    if number != 0:
        count_number = count_number+number
        print(f"Suma: {Funciones.add_digits(number)}")
    else:
        break
print(f"\nLa suma total de todos los numeros es: {count_number}.\nLa suma de los digitos de ese numero es: {Funciones.add_digits(count_number)}.")