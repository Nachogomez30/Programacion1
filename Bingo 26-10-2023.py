import time
import random
from Funciones import *

print("\n-BINGO-")
print("-----------------------------")

card = [[]*5 for _ in range(5)]

for i in range(5):
    print("Línea",i+1)
    for j in range(5):        
        while True:
            condition = True
            
            num = int(input("Ingrese un valor para el cartón: "))        
            if num<1 or num>75:                
                print("El número no se encuentra dentro del rango, intente de nuevo")
                continue
            
            for k in range(5):
                num = str(num)
                if num in card[k]:
                    print("El número ya fue ingresado")
                    condition = False
            
            if condition==False:
                continue
            else:
                break                                
                    
        card[i].append(str(num))
show_card(card)

balls = []
for i in range(1,75):
    balls.append(str(i))


bingo = False
while bingo==False:
    clear_terminal()
    show_card(card)
    ball_number = str(random.choice(balls))
    balls.remove(ball_number)
    
    print("El número que salio es:",ball_number)
    
    for i in range(5):
        for j in range(5):
            if ball_number==card[i][j]:
                card[i][j] = "-"

    for i in range(5):        
        if card[i][0]=="-" and card[i][1]=="-" and card[i][2]=="-" and card[i][3]=="-" and card[i][4]=="-":
            print("BINGO! Se completó la fila",(i+1),"\n")
            bingo = True
            break

    for j in range(5):        
        if card[0][j]=="-" and card[1][j]=="-" and card[2][j]=="-" and card[3][j]=="-" and card[4][j]=="-":
            print("BINGO! Se completó la columna",(j+1),"\n")
            bingo = True
            break

    for i in range(5):        
            if card[i][i]=="-":
                diagonal = True
            else: 
                diagonal = False
                break    
        
    for i in range(5):
        if card[i][4-i]=="-":
            diagonal = True
        else:
            diagonal = False
            break
            
    if diagonal==True:
        print("BINGO! Se completó la diagonal\n")
        bingo = True
    
    time.sleep(1)



