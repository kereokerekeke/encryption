from helpers import alphabet_position, rotate_character
from sys import argv, exit


def encrypt(text, key):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encryptedMessage = ''
    nextRot = 0
    for letter in text:
        if letter.lower() not in alphabet:
            encryptedMessage += letter
            continue
        if nextRot > (len(key) - 1):
            nextRot = 0
        encryptedMessage += rotate_character(letter,
                                             alphabet_position(key[nextRot]))
        nextRot += 1
    return encryptedMessage


def main():
    if not argv[1].isalpha():
        print('Letters only, please')
        exit()
    text = input('Type a message: ')
    print(encrypt(text, argv[1]))


if __name__ == '__main__':
    main()