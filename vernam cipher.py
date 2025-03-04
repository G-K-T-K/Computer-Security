def generateKey(text, key):
    key = list(key)
    if len(text) == len(key):
        return key
    else:
        for i in range(len(text) - len(key)):
            key.append(key[i % len(key)])
    return "".join(key)

def stringEncryption(text, key):
    key = generateKey(text, key)
    cipherText = ""

    for i in range(len(text)):
        shift = (ord(text[i]) - ord('A') + ord(key[i]) - ord('A')) % 26
        cipherText += chr(shift + ord('A'))

    return cipherText

def stringDecryption(cipherText, key):
    key = generateKey(cipherText, key)
    plainText = ""

    for i in range(len(cipherText)):
        shift = (ord(cipherText[i]) - ord('A') - (ord(key[i]) - ord('A'))) % 26
        plainText += chr(shift + ord('A'))

    return plainText

# Taking input
plainText = input("Enter the text: ").upper()
key = input("Enter the key: ").upper()

# Encryption
encryptedText = stringEncryption(plainText, key)
print("Cipher Text -", encryptedText)

# Decryption
decryptedText = stringDecryption(encryptedText, key)
print("Decrypted Text -", decryptedText)