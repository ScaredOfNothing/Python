from operator import length_hint
import string
import secrets
import random

chars = string.punctuation + string.digits + string.ascii_letters
chars = list(chars)
key = chars.copy()

random.shuffle(key)

# encryption
plain_text = input("Enter a message to encrypt: ")
cipher_text = ""

for letter in plain_text:
    if letter in chars:
        index = chars.index(letter)
        cipher_text += key[index]

print(f"original_message: {plain_text}")
print(f"encrypted_message: {cipher_text}")

# decryption
cipher_text = input("Enter a message to decrypt: ")
plain_text = ""

for letter in cipher_text:
    if letter in key:
        index = key.index(letter)
        plain_text += chars[index]

print(f"encrypted_message: {cipher_text}")
print(f"original_message: {plain_text}")

