import base64

# Load d and n
with open('private_d.txt', 'r') as f:
    d = int(f.read(), 16)

n = 0xc44da95ebaf53370ea729c493924e8856ec0773ab0cc4c10c4254950a065275f42ae800b7c5e327515e8d5b7317108ce2cab44c41cb2bafadd455cf280a6f40afa5ae059b7a6874bf9e03282079ee0df4b1e7696737173bf12acbc377d29abd977364eda900173606399c5833d34ccafa1722f4a373e6d04adb0ce3f8215df15  # Replace with the n you used earlier

# Decode the base64 ciphertext
ciphertext_b64 = "Pcfv0fRKByjorr3B+zcr3N6FpoEmmGvXbERKSSJX2EDhD7eCv+WcySDyZcrNKHoiSRn92pvdr8SnaDlwmq75zkgu24HUozbzJB4YQ6jZEy5ToapCArOhNkFXVg/HQUoWsNXXcwZs13NhZhYTbXnrvU0VC7CulkWEUlKuZa6dgUQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA=="
ciphertext_bytes = base64.b64decode(ciphertext_b64)

# Convert the bytes to an integer
ciphertext_int = int.from_bytes(ciphertext_bytes, "big")

# Decrypt using RSA formula
plaintext_int = pow(ciphertext_int, d, n)

# Convert the decrypted plaintext integer back into bytes
plaintext_bytes = plaintext_int.to_bytes((plaintext_int.bit_length() + 7) // 8, 'big')

print(plaintext_bytes)
decoded_string = plaintext_bytes.decode('ascii')
print(decoded_string)

