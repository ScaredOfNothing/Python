
from operator import length_hint
import string
import secrets

"""
chars = string.punctuation + string.digits + string.ascii_letters
chars = list(chars)
key = chars.copy()

random.shuffle(key)

#print(f"chars: {chars}")
#print(f"key: {key}")

#encryption

plain_text = input("Enter a message to encrypt: ")
cipher_text = ""

for letter in plain_text:
    index = chars.index(letter)
    cipher_text += key[index]

print(f"original_message: {plain_text}")
print(f"encrypted_message: {cipher_text}")

#dencryption

cipher_text = input("Enter a message to dencrypt: ")
plain_text = ""

for letter in cipher_text:
    index = key.index(letter)
    plain_text += chars[index]


print(f"encrypted_message: {cipher_text}")
print(f"original_message: {plain_text}")
"""


"""
dupxo = "dupxo"

random_choice = secrets.choice([dupxo, 11, 111])

print(random_choice)
"""
"""
#Passowrd generator
def generate_password(lenght: int):
    chars = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
    password = ''.join(secrets.choice(chars) for _ in range(lenght))
    
    
    print("Generated password: ", password)

generate_password(60)
"""

random = secrets.randbits(16)


print(random)