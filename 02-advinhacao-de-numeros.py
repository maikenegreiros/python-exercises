#! /usr/bin/python3
import random

min = 1
max = 100
secret_number = random.randint(min, max)
guess = None

def nailed_it(guess):
    return secret_number == guess

def isNumber(number):
    try:
        int(number)
    except:
        return False
    return True

def getHint(guess):
    if (guess < secret_number):
        return "Tente um número maior"
    elif (guess > secret_number):
        return "Tente um número menor"

print("*******Jogo da Advinhação*******\n")

while (True):
    guess = input("Dê seu chute: ")
    if (not isNumber(guess)):
        print("Seu papite não é um número inteiro válido")
        continue

    guess = int(guess)
    if (nailed_it(guess)): break
    print(getHint(guess))


print("\n-------Você acertou. Parabéns!-------")