# TPNº3
# Alumno: Ignacio Gómez

# Ejercicio 1:
years = int(input("Ingrese hace cuantos años tiene su computadora: "))
if years <= 2:
    print("Su computadora es nueva.")
else:
    print("Su computadora es vieja.")

# Ejercicio 2:
years = int(input("Ingrese hace cuantos años tiene su computadora: "))
if years < 0:
    print("Error: ingresó un numero negativo.")
elif years <= 2:
    print("Su computadora es nueva.")
else:
    print("Su computadora es vieja.")

# Ejercicio 3:
name1 = input("Ingrese el nombre de la primera persona: ")
name2 = input("Ingrese el nombre de la segunda persona: ")
if name1[0] == name2[0]:
    print("Coincidencia")
else:
    print("No hay coincidencia")

# Ejercicio 4:
candidate = input("Ingrese el candidato a votar (A, B, y C): ")
if candidate == 'A':
    print("Usted votó por el partido Rojo.")
elif candidate == 'B':
    print("Usted votó por el partido Verde.")
elif candidate == 'C':
    print("Usted votó por el partido Azul.")
else:
    print("Opcion erronea.")

# Ejercicio 5:
letter = input("Ingrese una letra: ").lower()
if len(letter) == 1:
    if letter in 'aeiou':
        print("Es una vocal.")
    else:
        print("No es una vocal.")
else:
    print("Error: Debe ingresar solo un carater.")

# Ejercicio 6:
year = int(input("Ingrese un año: "))
if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print("El año",year,"es biciesto.")
else:
    print("El año",year,"no es biciesto.")

# Ejercicio 7:
num1 = float(input("Ingrese el primer numero: "))
num2 = float(input("Ingrese el segundo numero: "))
num3 = float(input("Ingrese el tercer numero: "))
min_number = min(num1, num2, num3)
print("El numero minimo es:", min_number)

# Ejercicio 8:
username = input("Ingrese su usuario: ")
password = input("Ingrese su contraseña: ")
if username == "Gwenevere" and password == "excalibur":
    print("Usuario y contraseña correctos. Puede ingresar a Camelot.")
else:
    print("Acceso denegado.")

# Ejercicio 9:
name = input("Ingrese su nombre: ")
gender = input("Ingrese su genero (M/F): ")
if (gender == 'F' and name[0] < 'M') or (gender == 'M' and name[0] > 'N'):
    print("Usted pertenece al grupo A.")
else:
    print("Usted pertenece al grupo B.")

# Ejercicio 10:
age = int(input("Ingrese su edad: "))
if age < 4:
    print("Usted puede ingresar gratis.")
elif 4 <= age <= 18:
    print("La entrada vale: $500.")
else:
    print("La entrada vale: $1000.")

# Ejercicio 11:
pizza_type = input("Usted quere una pizza vegetariana? (si/no): ").lower()

if pizza_type == "si":
    print("Ingredientes para la pizza vegetariana: Pimiento, Tofu")
else:
    print("Ingredientes para la pizza que no es vegetariana: Peperoni, Jamón, Salmón")

chosen_ingredient = input("Elija otro ingrediente (ademas de mozzarella y tomato): ").title()

if pizza_type == "si":
    print("Usted pidio una pizza vegetariana con mozzarella, tomato, y", chosen_ingredient)
else:
    print("Usted pidio una pizza que no es vegetariana con mozzarella, tomato, y", chosen_ingredient)

# Ejercicio 12:
current_year = int(input("Ingrese el año actual: "))
other_year = int(input("Ingrese otro año: "))
years_difference = abs(current_year - other_year)
print("Años de diferencia:", years_difference)

# Ejercicio 13:
num1 = int(input("Ingrese un numero entero positivo: "))
num2 = int(input("Ingrese otro numero entero positivo: "))

if num1 <= 0 or num2 <= 0:
    print("No ha ingresado un numero entero positivo")
elif num1 % num2 == 0 or num2 % num1 == 0:
    print("El numero mayor es multiplo del numero menor.")
else:
    print("El numero mayor no es multiplo del numero menor.")

# Ejercicio 14:
a = float(input("Ingrese el coeficiente 'a': "))
b = float(input("Ingrese el coeficiente 'b': "))

if a == 0:
    if b == 0:
        print("Infinitas soluciones.")
    else:
        print("No tiene solución.")
else:
    x = -b / a
    print("Solución:", x)

# Ejercicio 15:
choice = input("Ingrese (T) o (C) para calcular el area de un triangulo o un circulo: ").lower()

if choice == "t":
    base = float(input("Ingrese la base del triangulo: "))
    height = float(input("ingrese la altura del triangulo: "))
    area = 0.5 * base * height
    print("el area del triangulo es:", area)
elif choice == "c":
    radius = float(input("Ingrese el radio del circulo: "))
    area = 3.14159 * (radius ** 2)
    print("el area del circulo es:", area)

# Ejercicio 16:
a = float(input("Ingrese el valor 'a': "))
b = float(input("Ingrese el valor 'b': "))
operation = int(input("Elija una opcion (1: +, 2: *, 3: -, 4: /): "))

if operation == 1:
    result = a + b
elif operation == 2:
    result = a * b
elif operation == 3:
    result = a - b
elif operation == 4:
    if b != 0:
        result = a / b
    else:
        result = "La division por 0 no es posible."
else:
    result = "Error: no eligió una operación valida."

print("Resultado:", result)

# Ejercicio 17:
day = input("Ingrese un dia de la semana: ").lower()

if day == "lunes":
    print("Es Lunes de trabajo :(.")
elif day == "viernes":
    print("Es Viernes de fiesta :).")
elif day == "sabado" or day == "domingo":
    print("¡¡¡Es fin de semana!!!.")
else:
    print("Es un dia de la semana.")

# Ejercicio 18:
hours_worked = float(input("Ingrese el total de horas trabajadas en el mes: "))
hourly_rate = float(input("Ingrese el salario por hora: "))
minimum_hours = 48
overtime_rate = 1.1

if hours_worked >= minimum_hours:
    overtime_hours = hours_worked - minimum_hours
    overtime_pay = overtime_hours * hourly_rate * overtime_rate
    total_pay = minimum_hours * hourly_rate + overtime_pay
    print("Horas extas:", overtime_hours)
    print("Salario total:", total_pay)
else:
    total_pay = hours_worked * hourly_rate
    print("Salario total:", total_pay)

# Ejercicio 19:
pencil_quantity = int(input("Ingrese la canrtidad de lapices: "))
pencil_price = 60
discount_threshold = 1000
discount_percentage = 7

if pencil_quantity >= discount_threshold:
    total_cost = pencil_quantity * pencil_price * (1 - discount_percentage / 100)
else:
    total_cost = pencil_quantity * pencil_price

print("Costo total:", total_cost)

# Ejercicio 20:
grades = []
for i in range(4):
    grade = float(input(f"Ingrese la {i + 1}º nota: "))
    grades.append(grade)

average = sum(grades) / 4

if average >= 6:
    print("El estudiante aprobó.")
else:
    print("El estudiante no aprobó.")
