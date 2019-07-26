#! /usr/bin/python3
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
alphabet = alphabet.lower()
secret = 'snitch'
word = "thepackagehasbeendelivered"

def getMatrix(): 
    mtx = {}
    count = 0
    alphabetLen = len(alphabet)
    alphabetList = list(alphabet)
    for letter in alphabet:
        mtx.update({ letter : alphabetList[count:alphabetLen] + alphabetList[:count] })
        count += 1
    return mtx

def addPadding(word, size):
    multiplier = round(size / len(word)) + 1
    new_word = word * multiplier
    return new_word[:size]

def encrypt(word, secret):
    mtx = getMatrix()
    encryption = ''
    count = 0
    for letter in word:
        encryption += mtx[letter][alphabet.index(secret[count])]
        count += 1
    return encryption


message = input('Digite uma mensagem: ').lower()
secretPadding = addPadding(secret, len(message))
print(encrypt(message, secretPadding))