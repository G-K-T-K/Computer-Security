#ENCRYPTION

import string

key = input("Enter the key: ").upper()
message = input("Enter the message: ").upper()

key = ''.join(sorted(set(key.replace("J", "I")), key=key.index))
alphabet = string.ascii_uppercase.replace('J', '')
table = key + ''.join([ch for ch in alphabet if ch not in key])
table = [table[i:i+5] for i in range(0, len(table), 5)]

message = message.replace("J", "I")
if len(message) % 2 != 0:
    message += 'X'
message_pairs = [message[i:i+2] for i in range(0, len(message), 2)]
for i in range(len(message_pairs)):
    if message_pairs[i][0] == message_pairs[i][1]:
        message_pairs[i] = message_pairs[i][0] + 'X'

encrypted_message = []
for a, b in message_pairs:
    r1, c1 = next((r, row.index(a)) for r, row in enumerate(table) if a in row)
    r2, c2 = next((r, row.index(b)) for r, row in enumerate(table) if b in row)
    
    if r1 == r2:
        encrypted_message.append(table[r1][(c1 + 1) % 5])
        encrypted_message.append(table[r2][(c2 + 1) % 5])
    elif c1 == c2:
        encrypted_message.append(table[(r1 + 1) % 5][c1])
        encrypted_message.append(table[(r2 + 1) % 5][c2])
    else:
        encrypted_message.append(table[r1][c2])
        encrypted_message.append(table[r2][c1])

print("Encrypted:", ''.join(encrypted_message))

#DECRYPTION

import string

key = input("Enter the key: ").upper()
encrypted_message = input("Enter the encrypted message: ").upper()

# Create Playfair Cipher table
key = ''.join(sorted(set(key.replace("J", "I")), key=key.index))
alphabet = string.ascii_uppercase.replace('J', '')
table = key + ''.join([ch for ch in alphabet if ch not in key])
table = [table[i:i+5] for i in range(0, len(table), 5)]

# Split message into pairs
message_pairs = [encrypted_message[i:i+2] for i in range(0, len(encrypted_message), 2)]

decrypted_message = []
for a, b in message_pairs:
    r1, c1 = next((r, row.index(a)) for r, row in enumerate(table) if a in row)
    r2, c2 = next((r, row.index(b)) for r, row in enumerate(table) if b in row)

    if r1 == r2:
        decrypted_message.append(table[r1][(c1 - 1) % 5])
        decrypted_message.append(table[r2][(c2 - 1) % 5])
    elif c1 == c2:
        decrypted_message.append(table[(r1 - 1) % 5][c1])
        decrypted_message.append(table[(r2 - 1) % 5][c2])
    else:
        decrypted_message.append(table[r1][c2])
        decrypted_message.append(table[r2][c1])

print("Decrypted:", ''.join(decrypted_message))