from Crypto.PublicKey import RSA
from Crypto.Hash import SHA256
import json
import base64

# Decoding and extraction script
def get_root_n(encoded_str):
    decoded_str = base64.b64decode(encoded_str).decode('utf-8')
    decoded_json = json.loads(decoded_str)
    return decoded_json["key"]["n"]

base64_str = "eyJuYW1lIjogInJvb3QiLCAia2V5IjogeyJlIjogNjU1MzcsICJuIjogMjI1MTY1MDI5NTI4NzI2MjA2MDEzNTAzNzQwMzgwNTgyOTQ4OTk0MzIwNTk0MzMxMzc2NjM3OTcxMzkzODUwMTU1OTQ0MzE2NjA0NDI4MTUyMDg5OTI1NTAxMDc4MjYxMTc2NTAzNDYxNDI0NzUwODYxMTU1NDM1NjQ3OTI4NTMwODgzMDI0NjY3Nzk1MTc4MzM5NjYwMzE0MTAzODU3OTk3MTI0ODA0Njc4MTcwMjE2MDA4MjY5MzczMjM1MTY0MjUyOTQ4MDkxMjY4NjM1MjE3NjQxMzEwMjg1OTEyMzU3MDYyMTU4MDI2MjM5NTA5NDg1Mzc0MTA0NzA3NTc2OTI2NzE3NzMxODM1MTIxOTg0NDcxODMzNzE2NzE2OTYyMjg4MzcwOTY2MjY1MTQ3MDM0MTg3NDUzNzE0MTg4MTg4MjU0MDIzNjMxNzM5MzY4NDUzNTExMDM0NDA2NTAzMTc0ODE5MzIxNDQ2NDUzMjY5OTQzMjA5MDkyOTgzOTYxNzM1Njc5MzI4MjY4Mjk1NDg0NjQzOTMzMzQyMzk3NzY5Nzc3NzU5NTY3MjUxOTA5NTg5MjA4MjUzMzYzMjgzNTAxNTA1MjEyOTA5MjkwNDM4NjI2OTkxMjE4MzE0NzcyNzA3NDk4NTAwMTcxMjIyMzQxODE5NDY0MDkyMzUzMTQ4ODU3MzQyNjc0OTg2ODg5Mjk3MDAyMjQyNDM2NzkxODc3NDU5MTg3NzE0MDYxMDY0MTE4OTk3MTAzMDcxNDE5NzkwNjU2MjU0NzQzMDg3MjMyMjI5MDk3NzQ5MjEzOTkwNTk1NTQ3MTN9LCAic2lnbmVyIjogInJvb3QifQ=="
root_n = get_root_n(base64_str)

# Certificate creation script
def create_user_cert(root_d, root_n):
    user_key_e = 65537
    user_key_n = 2**513  
    user_cert = {
        "name": "user",
        "key": {
            "e": user_key_e,
            "n": user_key_n
        },
        "signer": "root"
    }
    user_cert_data = json.dumps(user_cert).encode()
    user_cert_hash = SHA256.new(user_cert_data).digest()
    user_cert_signature = pow(int.from_bytes(user_cert_hash, "little"), root_d, root_n).to_bytes(256, "little")
    return base64.b64encode(user_cert_data).decode(), base64.b64encode(user_cert_signature).decode()

root_d = 0x37d58d0e679de5cf746ca10c1df16dea20e63fc10753f92eaf30a9704f1fe286f01c4c9bd6b460c5f9f0dbdf432f5b07a4005352a90089b48165d8549c5a2169efe0c9313a21d1c6ad9ec78bc0e08dbc5cb968d679518c22167bd3a933aef6e37bcd3da64b7cca31cf96a3fb48ce4e743065965d72956509c0d708d197fc257d5e03f5a1920bb0f32221f5d436a9f311b8988df25526d1d40dac2f981ffb3e95b6c1f9b4b243192fe4de58fb3a91c6064fb920c7ed9cc45ec86b087fcb1e1811940352f097c886d644394bf0ef19aca78d12125b5a28a3d923854d2d8866e34911e212a88506ec1fd544c38c6203205e6d779bf2f1c8026dc31a0d44adcd6301
user_cert_data, user_cert_signature = create_user_cert(root_d, root_n)

print("User Certificate (b64):", user_cert_data)
print("User Certificate Signature (b64):", user_cert_signature)
