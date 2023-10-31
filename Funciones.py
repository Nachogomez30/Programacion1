#SUMA DÍGITOS 
#Devuelve la suma de los dígitos de un número
def add_digits(number):
    sum = 0
    while number>10:
        sum += number%10                        
        number//= 10
    sum += number
    return sum         

#AHORCADO
#Verifica si las letras ingresadas por el usuario se encuentran en la palabra oculta
#La función devuelve una palabra con las letras que coinciden y guiones en los espacios restantes
def fill_word(characters,hidden_word):
    word = ""
    for j in range(len(hidden_word)):
        condition = False
        for i in characters:    
            if i == hidden_word[j]:
                word += i
                condition = True
        if condition == False:
            word += "_"
    return word

def validation(number, card):
    if number < 1 or number > 75:
        return False
    for x in card:
        if number in x:
            return False
    return True

# MOSTRAR CARTA DE BINGO:
def show_card(card):
    print("╔════════════════════════════════╗")
    for i in range(5):
        print(f"║","{:2s}     {:2s}     {:2s}     {:2s}     {:2s}".format(card[i][0],card[i][1],card[i][2],card[i][3],card[i][4]),"║")
    print("╚════════════════════════════════╝")
    
# BORRA LA TERMINAL
import os
def clear_terminal():
    os.system('clear' if os.name == 'posix' else 'cls')


# FUNCIONES DE TPNº5:
def validation_dni(dni):
    if len(str(dni)) >=7 and len(str(dni)) <=8:
        return True
    else:
        return False

def length_word(spaceses):
        spaceses=spaceses.strip()
        words=spaceses.split()
        if words:
            last_word=words[-1]
            return len(last_word)
        else:
            return 0

def id_club(name,dni):
    words = name.split()
    first_name = words[0]
    last_name = words[-1]
    three_digitd = dni[:3]
    identifier = first_name+str(len(last_name))+three_digitd
    return identifier

# FUNCIONES TPNº7
def bubble_sort(numbers):
    n = len(numbers)
    for i in range(n):
        for j in range(0, n - i - 1):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

def selection_sort(list, key):
    n = len(list)
    for i in range(n):
        idx = i
        for j in range(i + 1, n):
            if list[j][key] < list[idx][key]:
                idx = j
        list[i], list[idx] = list[idx], lit[i]

# FUNCIONES TPNº8
def count_digits(n):
    if n < 10:
        return 1
    else:
        return 1 + count_digits(n // 10)

def is_power_of(n, b):
    if n == 1:
        return True
    if n % b != 0 or n == 0:
        return False
    return is_power_of(n / b, b)

def positions_of(a, b):
    def find_positions(text, substring, index):
        if index + len(substring) > len(text):
            return []
        elif text[index:index + len(substring)] == substring:
            return [index] + find_positions(text, substring, index + 1)
        else:
            return find_positions(text, substring, index + 1)
    
    return find_positions(a, b, 0)