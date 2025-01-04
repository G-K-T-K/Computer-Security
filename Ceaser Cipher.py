user_input = input("Enter a word: ")
k = int(input("Constant: "))
user_input = user_input.upper()
encrypted_word = ""

for letter in user_input:
    ascii_value = ord(letter)
    new_ascii_value = (ascii_value - 65 + k) % 26 + 65
    encrypted_word += chr(new_ascii_value)

print("Encrypted word:", encrypted_word)