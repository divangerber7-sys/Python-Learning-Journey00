#   Encryption/Substitution Cipher in Python
#   Simple substitution cipher using shuffled characters

import random
import string

# Build character set (letters, digits, punctuation, and space)
chars = " " + string.ascii_letters + string.digits + string.punctuation
chars = list(chars)
key = chars.copy()

# Shuffle to create substitution key
random.shuffle(key)

# 🔒 ENCRYPTION
plain_text = input("Aloha!\nPlease enter a message you would like to encrypt:\n")
cipher_text = ""

for letter in plain_text:
    index = chars.index(letter)
    cipher_text += key[index]

print(f"\nThe original message is  : {plain_text}")
print(f"The encrypted message is : {cipher_text}")

# 🔓 DECRYPTION
cipher_text = input("\nPlease enter the encrypted message you would like to decrypt:\n")
plain_text = ""

for letter in cipher_text:
    index = key.index(letter)
    plain_text += chars[index]

print(f"\nThe encrypted message is : {cipher_text}")
print(f"The original message is  : {plain_text}")
print("Mahalo 🌺")
