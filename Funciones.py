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