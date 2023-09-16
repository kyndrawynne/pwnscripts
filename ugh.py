from Crypto.PublicKey import RSA

key = RSA.generate(1024)

print("Public Key:")
print(f"e: {hex(key.e)}")
print(f"n: {hex(key.n)}")

print("Private Exponent:")
print(f"d: {hex(key.d)}")
