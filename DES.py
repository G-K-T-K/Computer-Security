from Crypto.Cipher import DES
import binascii

# Function to pad data to be multiple of 8 bytes (DES block size)
def pad(text):
    while len(text) % 8 != 0:
        text += ' '
    return text

# DES Encryption
def des_encrypt(plaintext, key):
    cipher = DES.new(key.encode(), DES.MODE_ECB)  # Create cipher object
    padded_text = pad(plaintext)  # Pad the text
    encrypted_text = cipher.encrypt(padded_text.encode())  # Encrypt
    return binascii.hexlify(encrypted_text).decode()  # Convert to hex

# DES Decryption
def des_decrypt(ciphertext, key):
    cipher = DES.new(key.encode(), DES.MODE_ECB)  # Create cipher object
    decrypted_text = cipher.decrypt(binascii.unhexlify(ciphertext))  # Decrypt
    return decrypted_text.decode().strip()  # Remove padding

# Input
key = input("Enter an 8-character key: ")[:8]  # DES requires 8-byte key
plaintext = input("Enter the text to encrypt: ")

# Encryption
ciphertext = des_encrypt(plaintext, key)
print("Encrypted Text:", ciphertext)

# Decryption
decrypted_text = des_decrypt(ciphertext, key)
print("Decrypted Text:", decrypted_text)