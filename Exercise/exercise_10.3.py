import random
import string

char = ' ' + string.punctuation + string.digits + string.ascii_letters
char = list(char)
key = char.copy()
random.shuffle(key)


#encrypt
plain_text = input("Enter a message to encrypt: ")
cipher_text = ''

for letter in plain_text:
    index = char.index(letter)
    cipher_text += key[index]

print(f'Original Message: {plain_text}')
print(f'Encryptrd massage: {cipher_text}')

#decrypt
cipher_text = input("Enter a message to encrypt: ")
plain_text = ''

for letter in cipher_text:
    index = key.index(letter)
    plain_text += char[index]

print(f'Encryptrd Message: {cipher_text}')
print(f'Original massage: {plain_text}')