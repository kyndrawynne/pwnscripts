from Crypto.PublicKey import RSA
from Crypto.Util.number import long_to_bytes

def rsa_decrypt(d, n, challenge):
    # Convert the hex strings to integers
    d_int = int(d, 16)
    n_int = int(n, 16)
    challenge_int = int(challenge, 16)

    # Decrypt the challenge using the private key components (n, d)
    plaintext_int = pow(challenge_int, d_int, n_int)

    # Convert the plaintext to bytes and then to a hex string
    return long_to_bytes(plaintext_int).hex()

#YOU WILL NEED TO OPEN SEPERATE TERMINAL, CHANGE e,d,n, and challenge VALUES TO MAT>
# Example usage:
e = "10001"  # Public exponent (not needed for decryption, but included for complet>
d = "70308ce294930295dda8008abd49290e92f66767b5e29d3be549ad723b8c97139d664ccb31c36e>
n = "932e54c14352de87fc37a9d71da3c015f4187c9e501e456612998b585f44d34b79e961a3cadcae>
challenge = "3943d57657835df9df6351f3b2d9eaa6435ac730e2b5c0f8dd189777a4350724938032>

# Call the function with the provided values
response = rsa_decrypt(d, n, challenge)

print(f"The response is: {response}")
