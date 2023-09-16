from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.asymmetric.padding import PKCS1v15
from cryptography.hazmat.primitives import hashes

def generate_valid_rsa_key():
    while True:
        private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=1024,
            backend=default_backend()
        )
        
        public_key = private_key.public_key()
        n = public_key.public_numbers().n
        e = public_key.public_numbers().e

        if 2**512 < n < 2**1024:
            return private_key, e, n

def decrypt_challenge(private_key, challenge):
    plaintext = pow(challenge, private_key.private_numbers().d, private_key.public_key().public_numbers().n)
    return plaintext

if __name__ == "__main__":
    private_key, e, n = generate_valid_rsa_key()
    print(f"Generated RSA Parameters:\n e = {e}\n n = {n}")

    # This is a placeholder challenge, replace it with your challenge
    challenge = int("0xe75f62d5e3db145a752b43df9bbc223f0794fe5f233555efffa70a9ed3550ca1c5eb6ac1501079710711cb82ee75d0d86a3d6ad0e7ac18dbb81ba6708cb90c8e", 16)

#    response = decrypt_challenge(private_key, challenge)
#    print(f"Decrypted Challenge (Response): {hex(response)}")


