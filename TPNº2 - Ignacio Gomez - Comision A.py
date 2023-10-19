# TPNº2
# Alumno: Ignacio Gómez

# Ejercicio 1:
base = float(int("Ingrese la base del rectangulo: "))
height = float(int("Ingrese la altura del rectangulo: "))
perimeter = base*2+height*2
area = base*height
print(f"El perimetro del rectangulo es: {perimeter} y el area es: {area}.")

# Ejercicio 2:
legs_1 = float(int("Ingrese el primer cateto: "))
legs_2 = float(int("Ingrese el segundo cateto: "))
hypotenuse = (legs_1**2+legs_2**2)**1/2
print(f"La hipotenusa del triangulo dado los catetos entregados por usted es: {hypotenuse}.")

# Ejercicio 3:
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
suma = num1 + num2
resta = num1 - num2
division = num1 / num2
multiplicacion = num1 * num2
print("Suma:", suma)
print("Resta:", resta)
print("División:", division)
print("Multiplicación:", multiplicacion)

# Ejercicio 4:
fahrenheit = int(input("Ingrese los grados en fahrenheit: "))
celsius = (fahrenheit-32)*5/9
print(f"Los grados fahrenheit a grados  celsius son: {celsius}")

# Ejercicio 5:

# Ejercicio 6:
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
num3 = float(input("Ingrese el tercer número: "))
media = (num1 + num2 + num3) / 3
print("La media de los tres números es:", media)

# Ejercicio 7:
minutes = int(input("Ingrese la cantidad de minutos: "))
hours = minutes // 60
remaining_minutes = minutes % 60
print(minutes, "minutos son", hours, "horas y", remaining_minutes, "minutos.")

# Ejercicio 8:
base_salary = float(input("Ingrese el sueldo base del vendedor: "))
sales = float(input("Ingrese el monto total de las ventas: "))
commission = 0.10 * sales
total_mes = base_salary + commission
print("El vendedor recibirá", commission, "por comisiones y un total de", total_mes, "en el mes.")

# Ejercicio 9:
total_purchase = float(input("Ingrese el total de la compra: "))
discount = 0.15 * total_purchase
total_to_pay = total_purchase - discount
print("El cliente deberá pagar", total_to_pay, "después del descuento del 15%.")

# Ejercicio 10:
partials = []
for i in range(1, 4):
    grade = float(input("Ingrese la calificación del parcial " + str(i) + ": "))
    partials.append(grade)

final_exam = float(input("Ingrese la calificación del examen final: "))
final_project = float(input("Ingrese la calificación del trabajo final: "))

average_partials = sum(partials) / len(partials)
final_grade = 0.55 * average_partials + 0.30 * final_exam + 0.15 * final_project

print("La calificación final en Algoritmos es:", final_grade)

# Ejercicio 11:
num1 = float(input("Ingrese el Primer numero: "))
num2 = float(input("Ingrese el Segundo numero: "))
distance = abs(num1 - num2)
print("La distancia entre los 2 numeros es:", distance)

# Ejercicio 12:
number = float(input("Ingrese un numero: "))
square_root = number ** (1/2)
cubic_root = number ** (1/3)
print("Raiz cuadrada:", square_root)
print("Raiz cubica:", cubic_root)

# Ejercicio 13:
two_digit_number = int(input("Ingrese un numero de 2 digitos: "))
tens_digit = two_digit_number // 10
units_digit = two_digit_number % 10
reversed_number = units_digit * 10 + tens_digit
print("Numero invertido:", reversed_number)

# Ejercicio 14:
A = float(input("Ingrese el valor de A: "))
B = float(input("Ingrese el valor de B: "))
A, B = B, A
print("A =", A)
print("B =", B)

# Ejercicio 15:
HH = int(input("Ingrese la hora de salida: "))
MM = int(input("Ingrese los minutos de salida: "))
SS = int(input("Ingrese los segundos de salida: "))
T = int(input("Ingrese el tiempo del viaje en segundos: "))
total_seconds = HH * 3600 + MM * 60 + SS + T
arrival_hour = str(total_seconds // 3600)
arrival_minute = str((total_seconds % 3600) // 60)
arrival_second = str(total_seconds % 60)

if arrival_hour < 10:
    arrival_hour = '0' + arrival_hour
if arrival_minute < 10:
    arrival_minute = '0' + arrival_minute
if arrival_second < 10:
    arrival_second = '0' + arrival_second

arrival_time = arrival_hour + ':' + arrival_minute + ':' + arrival_second
print("Horario de llegada: " + arrival_time)


# Ejercicio 16:
name = input("Ingrese su nombre: ")
last_name1 = input("Ingrese su primer apellido: ")
last_name2 = input("Ingrese su segundo apellido: ")
initials = name[0] + last_name1[0] + last_name2[0]
print("Iniciales:", initials)

# Ejercicio 17:
usuario = input("Ingrese su nombre: ")
print(f"Ahora estás en la matrix, {usuario}")

# Ejercicio 18:
cost = float(input("Ingrese el costo de la cena: "))
service_charge = cost * 0.062
tip = cost * 0.10
total_cost = cost + service_charge + tip
print("Monto final a pagar:", total_cost)

# Ejercicio 19:
day = int(input("Ingrese el dia de su nacimiento: "))
month = int(input("Ingrese el mes de su nacimiento: "))
year = int(input("Ingrese el año de su nacimiento: "))
print("Fecha de nacimiento:", "{:02d}/{:02d}/{:04d}".format(day, month, year))

# Ejercicio 20:
birthdate = input("Ingrese su fecha de nacimiento con el formato DDMMAAAA: ")
day = int(birthdate[:2])
month = int(birthdate[2:4])
year = int(birthdate[4:])
print("Fecha de nacimiento:", "{:02d}/{:02d}/{:04d}".format(day, month, year))

# Ejercicio 21:
km_per_liter = float(input("Ingrese los kilometros por litros de su moto: "))
tank_capacity = float(input("Ingrese la capacidad de su tanque: "))
total_distance = float(input("Ingrese la distancia que recorerá en kilometros: "))
tanks_needed = total_distance / (km_per_liter * tank_capacity)
print("El tanque necesita:", tanks_needed, "litros de combustible.")
