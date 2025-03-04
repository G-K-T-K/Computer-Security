from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import binascii

# Generate RSA Key Pair
key = RSA.generate(2048)
private_key = key.export_key()
public_key = key.publickey().export_key()

# Save the keys
with open("private.pem", "wb") as priv_file:
    priv_file.write(private_key)

with open("public.pem", "wb") as pub_file:
    pub_file.write(public_key)

# Load Public Key for Encryption
def load_public_key():
    with open("public.pem", "rb") as pub_file:
        return RSA.import_key(pub_file.read())

# Load Private Key for Decryption
def load_private_key():
    with open("private.pem", "rb") as priv_file:
        return RSA.import_key(priv_file.read())

# RSA Encryption
def rsa_encrypt(plaintext):
    public_key = load_public_key()
    cipher = PKCS1_OAEP.new(public_key)
    encrypted_text = cipher.encrypt(plaintext.encode())
    return binascii.hexlify(encrypted_text).decode()

# RSA Decryption
def rsa_decrypt(ciphertext):
    private_key = load_private_key()
    cipher = PKCS1_OAEP.new(private_key)
    decrypted_text = cipher.decrypt(binascii.unhexlify(ciphertext))
    return decrypted_text.decode()

# Input
plaintext = input("Enter the text to encrypt: ")

# Encryption
ciphertext = rsa_encrypt(plaintext)
print("Encrypted Text:", ciphertext)

# Decryption
decrypted_text = rsa_decrypt(ciphertext)
print("Decrypted Text:", decrypted_text)