from base64 import b64encode, b64decode

block_size = 16  # Likely block size for AES
secret_ciphertext_b64 = "0I4jKaNzJgMf4BJpe1y3Zjzm9aoBdvOE3tvAK6adxvC8NvsUxJ5UlvGwnMGeMagsVPza/zRgp8us56S/Gigo5Q=="
plaintext_prefix_b64 = "0I4jKaNzJgMf4BJpe1y3Zjzm9aoBdvOE3tvAK6adxvC8NvsUxJ5UlvGwnMGeMagsVPza/zRgp8us56S/Gigo5Q=="
ciphertext_b64 = "1XjIj313rDXdLG+/+fDeVBJOsaB2uE3ADIBQmyZkoqomG/0BM952JDUU9rUVxzzE08XR2Sn+J2b0JP7kKY7mt9COIymjcyYDH+ASaXtct2Y85vWqAXbzhN7bwCumncbwvDb7FMSeVJbxsJzBnjGoLFT82v80YKfLrOekvxooKOU="

# Function to simulate interacting with the challenge
def encrypt_with_secret(plaintext_prefix_b64):
    # Here you would send plaintext_prefix_b64 to the challenge and retrieve the corresponding ciphertext
    # For example:
    ciphertext_b64 = challenge.encrypt(plaintext_prefix_b64)
    pass

# Start with an empty secret
decrypted_secret = ""

# Iterate through each block of the secret
for block_idx in range(0, len(b64decode(secret_ciphertext_b64)), block_size):
    # Discover each byte in the block
    for byte_idx in range(block_size):
        prefix = 'A' * (block_size - 1 - byte_idx)
        target_ciphertext_b64 = encrypt_with_secret(b64encode(prefix.encode() + decrypted_secret[block_idx:block_idx+byte_idx].encode()))

        # Brute force the next byte
        for b in range(256):
            test_prefix = prefix + decrypted_secret[block_idx:block_idx+byte_idx] + chr(b)
            test_ciphertext_b64 = encrypt_with_secret(b64encode(test_prefix.encode()))

            if test_ciphertext_b64[:block_size] == target_ciphertext_b64[:block_size]:
                decrypted_secret += chr(b)
                break

print("Decrypted Secret:", decrypted_secret)
