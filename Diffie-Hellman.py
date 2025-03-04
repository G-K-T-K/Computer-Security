from Crypto.Util.number import getPrime
import random

# Generate a large prime number (p) and a base (g)
p = getPrime(64)  # 64-bit prime for simplicity
g = random.randint(2, p - 1)

print("Publicly Shared Values:")
print("Prime (p):", p)
print("Base (g):", g)

# Alice's Private Key
a = random.randint(2, p - 1)
A = pow(g, a, p)  # A = g^a mod p

# Bob's Private Key
b = random.randint(2, p - 1)
B = pow(g, b, p)  # B = g^b mod p

# Key Exchange
print("\nExchanging Keys...")
print("Alice sends:", A)
print("Bob sends:", B)

# Compute Shared Secret Key
alice_secret = pow(B, a, p)  # (B^a) mod p
bob_secret = pow(A, b, p)    # (A^b) mod p

print("\nShared Secret Computed by Alice:", alice_secret)
print("Shared Secret Computed by Bob:", bob_secret)

# Both Alice and Bob should have the same secret key
assert alice_secret == bob_secret, "Key Exchange Failed!"
print("\nDiffie-Hellman Key Exchange Successful!")