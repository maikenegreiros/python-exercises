#! /usr/bin/python3
import random
print("******Advinhe a palavra******")

words = [
    'tagamandapio',
    'casa',
    'escola',
    'trem',
    'telefone',
    'celular',
    'orelha',
    'chicote',
    'paralelepipedo',
    'inconstitucionalicimamente'
]
attempts = 4
word = words[random.randrange(0,len(words))].upper()
board = {}

def isASingleLetter(letter):
    return len(letter) == 1

def getLettersPositions(letter):
    positions = []
    count = 0
    for l in word:
        if l == letter:
            positions.append(count)
        count += 1
    return positions

def initializeBoard():
    for i in range(len(word)):
        board[i] = "__"

def fillBoard(letter, positions):
    for i in positions:
        board[i] = letter

def displayBoard():
    print('', end="\n\n")
    for i in board:
        print(board[i], end=" ")
    print('', end="\n\n")

def hasWin():
    return list(word) == list(board.values())

initializeBoard()
displayBoard()

while (attempts and not hasWin()):
    guess = input("Digite uma letra: ").upper()
    if (not isASingleLetter(guess)):
        print("Você deve digitar apenas uma letra")
        continue

    if (not(guess in word)):
        attempts -= 1
        print("Essa letra não existe. Lhe restam {} tentativas".format(attempts))
    else:
        fillBoard(guess, getLettersPositions(guess))

    displayBoard()
    
    
if(hasWin()): print("-------Você venceu!-------")
elif(not attempts): print("-------Você perdeu!-------")