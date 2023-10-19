# TPNº4
# Alumno: Ignacio Gómez

# Ejercicio 1:
word = input("Ingrese una palabra: ")
for i in range(10):
    print(word)

# Ejercicio 2:
age = int(input("Ingrese su edad: "))
for year in range(1, age + 1):
    print("Ha cumplido", year, "años.")

# Ejercicio 3:
n = int(input("Ingrese un número entero positivo: "))
for i in range(1, n + 1, 2):
    if i != 1:
        print(",", end=" ")
    print(i, end=" ")

# Ejercicio 4:
n = int(input("Ingrese un número entero positivo: "))
countdown = []
for i in range(n, -1, -1):
    countdown.append(str(i))
countdown_str = " ".join(countdown)
print(countdown_str)

# Ejercicio 5:
investment = float(input("Ingrese la cantidad a invertir: "))
interest_rate = float(input("Ingrese el interes anual (en decimal): "))
years = int(input("Ingrese el numero de años: "))
for year in range(1, years + 1):
    investment += investment * interest_rate
    print(f"Año {year}: ${investment:.2f}")

# Ejercicio 6:
height = int(input("Ingrese la altura del triangulo: "))
for i in range(1, height + 1):
    for j in range(i):
        print("*", end="")
    print()

# Ejercicio 7:
for i in range(1, 11):
    for j in range(1, 11):
        print(f"{i} x {j} = {i * j}")
    print()

# Ejercicio 8:
n = int(input("Ingrese un numero entero: "))
for i in range(1, n + 1, 2):
    for j in range(i, 0, -2):
        print(j, end=" ")
    print()

# Ejercicio 9:
password = "contraseña"
while True:
    user_password = input("Introduzca la contraseña: ")
    if user_password == password:
        print("¡Contraseña correcta!")
        break
    else:
        print("Contraseña incorrecta. Inténtelo de nuevo.")

# Ejercicio 10:
number = int(input("Ingrese un número entero: "))

if number <= 1:
    is_prime = False
else:
    is_prime = True
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            is_prime = False
            break

if is_prime:
    print(f"El numero {number} es un número primo.")
else:
    print(f"El numero {number} no es un número primo.")


# Ejercicio 11:
word = input("Ingrese una palabra: ")
for letter in reversed(word):
    print(letter)

# Ejercicio 12:
phrase = input("Ingrese una frase: ")
letter = input("ingrese una letra: ")
count = phrase.count(letter)
print(f"La letra '{letter}' aparece {count} veces en la frase.")

# Ejercicio 13:
while True:
    user_input = input("Ingrese lo que desee (o 'salir' para salir): ")
    if user_input == "salir":
        break
    print(user_input)

# Ejercicio 14:
start = int(input("Ingrese el primer entero: "))
end = int(input("Ingrese el segundo entero: "))
print("Numeros pares:")
for num in range(start, end + 1):
    if num % 2 == 0:
        print(num)
print("Numeros impares:")
for num in range(start, end + 1):
    if num % 2 != 0:
        print(num)

# Ejercicio 15:
number = int(input("Ingrese un numero entero positivo mayor a 0: "))
print("Divisores:")
for i in range(1, number + 1):
    if number % i == 0:
        print(i)

# Ejercicio 16:
num_count = int(input("Cuantos numeros va a ingresar? "))
negative_count = 0
for i in range(num_count):
    num = int(input("ingrese un numero: "))
    if num < 0:
        negative_count += 1
print(f"Usted ingreso {negative_count} numeros negativos.")

# Ejercicio 17:
phrase = input("Ingrese una frase: ").lower()
vowels = "aeiou"
unique_vowels = ""
for char in phrase:
    if char in vowels and char not in unique_vowels:
        unique_vowels += char
print("Vocales unicas en la oracion:", unique_vowels)

# Ejercicio 18:
fibonacci = [0, 1]
for i in range(8):
    next_num = fibonacci[-1] + fibonacci[-2]
    fibonacci.append(next_num)

fibonacci_str = ""
for num in fibonacci:
    fibonacci_str += str(num) + ", "

print("Los primeros 10 numeros de la secuencia de Fibonacci son: " + fibonacci_str)

# Ejercicio 19:
goal = float(input("Ingrese la meta de ahorro: "))
total_savings = 0
while total_savings < goal:
    savings = float(input("Ingrese el monto a ahorrar (valor positivo): "))
    if savings <= 0:
        print("La cantidad debe ser positiva.")
        continue
    total_savings += savings
print("¡Meta alcanzada!")

# Ejercicio 20:
sum_total = 0
while True:
    num = int(input("Ingrese un numero (0 para salir): "))
    if num == 0:
        break
    sum_total += num
print("La suma de todos los numeros ingresados es:", sum_total)

# Ejercicio 21:
max_number = 0
while True:
    num = int(input("Ingrese un numero positivo (0 para salir): "))
    if num == 0:
        break
    if num > max_number:
        max_number = num
print("El número más grande ingresado es:", max_number)

# Ejercicio 22:
even_count = 0
while True:
    num = int(input("Ingrese un número entero positivo (-1 para salir): "))
    if num == -1:
        break
    digit_sum = sum(int(digit) for digit in str(num))
    print(f"La suma de los dígitos en {num} es {digit_sum}.")
    if num % 2 == 0:
        even_count += 1
print(f"Ingresó {even_count} numeros positivos.")

# Ejercicio 23 y 24:
total_cost = 0
while True:
    purchase = float(input("Ingrese el monto de la compra (0 para finalizar): "))
    if purchase < 0:
        print("El importe de la compra no puede ser negativo..")
        continue
    if purchase == 0:
        break
    total_cost += purchase
if total_cost > 1000:
    total_cost -= total_cost * 0.1
print(f"Costo total a pagar: {total_cost}")

# Ejercicio 25:
num = int(input("Introduzca un numero entero positivo: "))
factorial = 1
for i in range(1, num + 1):
    factorial *= i
print(f"El factorial de {num} es {factorial}")
