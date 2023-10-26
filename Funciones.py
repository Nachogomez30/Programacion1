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

