from Crypto.Cipher import AES
import binascii

# Function to pad data to be multiple of 16 bytes (AES block size)
def pad(text):
    while len(text) % 16 != 0:
        text += ' '
    return text

# AES Encryption
def aes_encrypt(plaintext, key):
    cipher = AES.new(key.encode(), AES.MODE_ECB)  # Create cipher object
    padded_text = pad(plaintext)  # Pad the text
    encrypted_text = cipher.encrypt(padded_text.encode())  # Encrypt
    return binascii.hexlify(encrypted_text).decode()  # Convert to hex

# AES Decryption
def aes_decrypt(ciphertext, key):
    cipher = AES.new(key.encode(), AES.MODE_ECB)  # Create cipher object
    decrypted_text = cipher.decrypt(binascii.unhexlify(ciphertext))  # Decrypt
    return decrypted_text.decode().strip()  # Remove padding

# Input
key = input("Enter a 16-character key: ")[:16]  # AES requires 16-byte key
plaintext = input("Enter the text to encrypt: ")

# Encryption
ciphertext = aes_encrypt(plaintext, key)
print("Encrypted Text:", ciphertext)

# Decryption
decrypted_text = aes_decrypt(ciphertext, key)
print("Decrypted Text:", decrypted_text)