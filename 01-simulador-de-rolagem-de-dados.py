#! /usr/bin/python3
import random

roll = True
min = 1
max = 6

def roll_dice():
    return random.randint(min, max) 
    
while (roll == True):
    actual_number = roll_dice()
    print("número:",actual_number)
    answer = input("Deseja rolar mais uma vez o dado?\n1 - Sim\n2 - Não\n")
    if (answer == '1'):
        roll = True
    elif (answer == '2'):
        roll = False
    else:
        print('Opção inválida')
