from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding

def get_private_exponent(e, n):
    # Since n is prime, phi(n) is n - 1
    phi = n - 1
    
    # Compute modular multiplicative inverse of e modulo phi(n)
    return pow(e, -1, phi)

def decrypt_challenge(d, n, challenge):
    return pow(challenge, d, n)

# Your values
e = 65537
n = 33226447894027101069403552416260060320816038941351630259773868929025567553699282122405061605679280424307316031499358671062522239605153675717414707880728359
challenge = 0xe75f62d5e3db145a752b43df9bbc223f0794fe5f233555efffa70a9ed3550ca1c5eb6ac1501079710711cb82ee75d0d86a3d6ad0e7ac18dbb81ba6708cb90c8e

d = get_private_exponent(e, n)
response = decrypt_challenge(d, n, challenge)

print(hex(response))

