
#EJERCICIO 1:
alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "Ñ", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

phrases = []

displacement = int(input("Ingrese el número de letras que quiera desplazar: "))

for i in range(5):
    phrase = input(f"Ingrese la frase {i+1}: ")
    encrypted_phrase = ""
    for char in phrase:
        char = char.upper()
        if char in alphabet:
            index_message = (alphabet.index(char) + displacement) % 27
            encrypted_phrase += alphabet[index_message]
        else:
            encrypted_phrase += char
    phrases.append(encrypted_phrase)

print("Frases encriptadas:")
for i in phrases:
    print(i)

##########################################################

#EJERCICIO 2:
total_pair = 0
total_odd = 0

while True:
    number = int(input("Ingrese un numero positivo, si desea terminar ingrese el 0: "))

    if number == 0:
        break
    elif number < 0:
        continue
    else:
        pair = 0
        odd = 0
        temp_number = number
        
        while temp_number > 0:
            digit = temp_number%10
            if digit%2 == 0 and digit != 0:
                pair += 1
            elif digit != 0:
                odd += 1
            temp_number //= 10
        print(f"Numero: {number} contiene {pair} nºpares y {odd} nº impares.")
    
        total_pair += pair
        total_odd += odd

print(f"Numeros pares totales: {total_pair}. Numero total de impares: {total_odd}.")
