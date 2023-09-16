import base64

# Known plaintext (b64) - this is the secret ciphertext you copied from the challenge
plaintext_b64 = "2FuY6Wnx6VhRFDoZBzfDJ+laMAEYeIMm60VnqhekD9dLA7N+OFd+oZtHzX60jLpWp8rqbGgc2urzcg=="

# Ciphertext (b64) - this is the corresponding ciphertext you copied from the challenge
ciphertext_b64 = "cHduLmNvbGxlZ2V7TU52eUFkS1l0Y3pYbjVOWE9EUUhvTE96b0xSLmRWek56TURMeUFUTXlNeld9Cg=="

# Secret ciphertext (b64) - this is the secret ciphertext you want to decrypt
secret_ciphertext_b64 = "2FuY6Wnx6VhRFDoZBzfDJ+laMAEYeIMm60VnqhekD9dLA7N+OFd+oZtHzX60jLpWp8rqbGgc2urzcg==" # replace with the correct value

# Decode the base64 values
plaintext = base64.b64decode(plaintext_b64)
ciphertext = base64.b64decode(ciphertext_b64)
secret_ciphertext = base64.b64decode(secret_ciphertext_b64)

# Find the key by XORing the known plaintext with its corresponding ciphertext
key = bytes([p ^ c for p, c in zip(plaintext, ciphertext)])

# Decrypt the secret ciphertext using the key
decrypted_secret = bytes([sc ^ k for sc, k in zip(secret_ciphertext, key)])

# Print the decrypted secret
print(decrypted_secret.decode('ascii'))
