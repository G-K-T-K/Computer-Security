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