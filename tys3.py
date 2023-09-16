import base64

# Given RSA parameters
e = 0x10001
n = 0xa8b99ec36a68336cb4fbac235a48d3b8c764ab8f215173d23fa9bcaf6ec11213a8ce08e2806bd40aa0c9daf35e12d78ebb86366475680c60cd125988831b193a1180c8ef70905480f21dad5c2306eb60c73a53c44312f2baf0cf5dd48dcd117287bfaf4ed3890c7adc8136f9b08158e2208d50262bd5d6b1ade2b86362de2021
d = 0xb4cb8764482f3f6d75ae0fd29d352360b40f74a9c1cd0c1dfdc07e7f6d7b95aa4e8d23085d7f7ef42587b51e6829878476b1cbe8434bf5e7528a369b255f727225b6af5ca7072acd027a19ea17d5bd25624a3947fcd956c11a97cc3707e32c2cb75c2aaf30089e3270327a9fb08a9eac83e5466f6ebe1d2ad5125efb71aad9

# Decryption
ciphertext_b64 = "NLWFPYBfdl28jBYZm9ouVUTVmtpMu+d5VXZnEJqOJv1NYZEDOkZd1N/5y22h6I9vep2GRdaLK3N0BTo6U29zLDtTZHWQyMqCROac6WIp+8tpn13FtjNhNdRZFdF+OINmnrzmPAdnOgErDDnB/XRz3CR1uRNZ8ATV+zjgSqazDn8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA=="
ciphertext_bytes = base64.b64decode(ciphertext_b64)

ciphertext_integer = int.from_bytes(ciphertext_bytes, byteorder='big')

# Manually perform RSA decryption operation
decrypted_integer = pow(ciphertext_integer, d, n)

decrypted_bytes = decrypted_integer.to_bytes((decrypted_integer.bit_length() + 7) // 8, byteorder='big')
print("Decrypted message:", decrypted_bytes)
try:
    print("Decrypted message as text:", decrypted_bytes.decode('utf-8'))
except UnicodeDecodeError:
    print("The decrypted bytes do not appear to be a valid UTF-8 string.")

