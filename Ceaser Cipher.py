user_input = input("enter a letter : ")
k = int(input("constant : "))
user_input = user_input.upper()
ascii_value = ord(user_input)
new_ascii_value = (ascii_value - 65 + k) % 26 + 65
print(chr(new_ascii_value))
