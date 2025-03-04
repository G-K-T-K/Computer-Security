#ENCRYPTION

from math import sqrt
import numpy as np

Key  =  input("Enter the key: ")
word = input("Enter the word: ")

Key = Key.lower()
word = word.lower()

key_s = int(sqrt(len(Key)))

while key_s * key_s < len(Key):
    Key += 'a'  
while len(word) % key_s != 0:
    word += 'a'

KM = np.array([[ord(Key[a*key_s + b]) - ord("a") for b in range(key_s)] for a in range(key_s)])

words = np.array([[ord(b) - ord('a') for b in word[a:a+key_s]] for a in range(0, len(word), key_s)])

en = []
for a in words:
    en.append(np.mod((KM @ a), 26).flatten().tolist())
enW = ""
for a in en:
    for b in a:
        enW += chr(ord('a')+b) 

print(enW)

#DECRYPTION

from math import sqrt
import numpy as np

Key = input("Enter the key: ")
encrypted_word = input("Enter the encrypted word: ")

Key = Key.lower()
encrypted_word = encrypted_word.lower()

key_s = int(sqrt(len(Key)))

while key_s * key_s < len(Key):
    Key += 'a'
while len(encrypted_word) % key_s != 0:
    encrypted_word += 'a'

# Generate Key Matrix
KM = np.array([[ord(Key[a*key_s + b]) - ord("a") for b in range(key_s)] for a in range(key_s)])

# Compute the Inverse of Key Matrix
det = int(np.round(np.linalg.det(KM)))  # Determinant of the matrix
det_inv = pow(det, -1, 26)  # Modular inverse of determinant mod 26

adjugate = np.round(det * np.linalg.inv(KM)).astype(int)  # Adjugate matrix
KM_inv = (det_inv * adjugate) % 26  # Modular inverse of the key matrix

# Convert encrypted text to matrix form
words = np.array([[ord(b) - ord('a') for b in encrypted_word[a:a+key_s]] for a in range(0, len(encrypted_word), key_s)])

# Decryption process
decrypted_text = []
for a in words:
    decrypted_text.append(np.mod((KM_inv @ a), 26).flatten().tolist())

# Convert numbers back to characters
decrypted_word = ""
for a in decrypted_text:
    for b in a:
        decrypted_word += chr(ord('a') + b)

print("Decrypted word:", decrypted_word)