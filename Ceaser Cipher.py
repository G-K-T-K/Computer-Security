# ENCRYPTION

user_input = input("Enter a word: ")
k = int(input("Constant: "))
user_input = user_input.upper()
encrypted_word = ""

for letter in user_input:
    ascii_value = ord(letter)
    new_ascii_value = (ascii_value - 65 + k) % 26 + 65
    encrypted_word += chr(new_ascii_value)

print("Encrypted word:", encrypted_word)

#DECRYPTION

encrypted_word = input("Enter the encrypted word: ")
k = int(input("Constant: "))
decrypted_word = ""

for letter in encrypted_word:
    ascii_value = ord(letter)
    new_ascii_value = (ascii_value - 65 - k) % 26 + 65
    decrypted_word += chr(new_ascii_value)

print("Decrypted word:", decrypted_word)