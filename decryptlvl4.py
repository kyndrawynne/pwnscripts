from Crypto.Cipher import AES
import base64

def decrypt_ecb(ciphertext_b64, key_b64):
    key = base64.b64decode(key_b64)
    ciphertext = base64.b64decode(ciphertext_b64)

    cipher = AES.new(key, AES.MODE_ECB)
    plaintext = cipher.decrypt(ciphertext)

    # Removing padding
    padding_length = plaintext[-1]
    plaintext = plaintext[:-padding_length]

    return plaintext.decode('utf-8')

key_b64 = "Qd11KhiisBLWuO6mxCZrNQ=="
secret_ciphertext_b64 = "2RkDplOTgtttPxjvs4B+VJtOteWtveHUimYwwvA+hk9FSRjI8PZmjEPeBlGkizJLoLcDTkCK7tvkp7we5SRqLA=="

decrypted_secret = decrypt_ecb(secret_ciphertext_b64, key_b64)
print("Decrypted Secret:", decrypted_secret)
