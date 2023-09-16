from Crypto.PublicKey import RSA
from Crypto.Hash import SHA256
import json
import base64

def create_user_cert(root_d, root_n, byte_order):
    # User key
    user_key_e = 65537
    user_key_n = 2**513  # A value between 2**512 and 2**1024
    
    # User certificate
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

    # Sign the user cert using the root private key
    user_cert_signature = pow(int.from_bytes(user_cert_hash, byte_order), root_d, root_n).to_bytes(256, byte_order)

    return base64.b64encode(user_cert_data).decode(), base64.b64encode(user_cert_signature).decode()

root_d = 0x6cb50a67aaf4d0fe20247799af7243ce8cd8d66d05f803942a160f165af6811834ac9a6cfadb3751cafbc6fba0823ebd00209856b15af7155795c93318b95d8c1375d643c791e4ece0e6889dfd42602e8e414e2cbf7020f37d1456f980d8e659e0d3132fa125cb3a83795003cfea26640d955d02f724e9c778b1df111a8c9fc44d653ff7d1eab2e9ece5ed672f21d5e03d856a016f48963652c20139b62720d72c5c87d48020edcca71e3e9835ed1790cd15bc291cb17fbfaf3ba38e315e4db5a0f1b3ae624ec1848f20d8b5b922be78e7f7fb48897cfe3791e810f82d5e84d102fbb74536c00a25f1d19737c99497672292304dbe807e633b273d108f4c225
root_cert_b64 = "eyJuYW1lIjogInJvb3QiLCAia2V5IjogeyJlIjogNjU1MzcsICJuIjogMjc2MTAzMjczNjY1MjM4NzkyMTE1NDY5OTE2OTA0NTQwOTAxNjY1Mzg1OTk0Nzg0ODc1NjAwNTYzMjEyNDI0MDUxMTYyOTMyMjYzMDI0MTM5MDQ5OTU1NDk2MjA1ODY4ODg1MTEyMzY4Mjc0NDMyOTM3MDU2MzYxNTk0MTU3MjIxMDU1MjEyNDUxNDI1MDQ1NDMxODc1MzQxMTI5NDc5NTAxODgxNTQzNjU4MjA1MzMzNjYwNTcxNDAzMjQzNTg2OTYzNTY3NDI1MjgwNjc2NDAzOTI1MDc2Nzc4Njc2NDk0NTYwMzk3MzU4NjA5OTgzNDAxMDI3NzM0Nzg5OTc0NjkyNTcwMzQ2NTgwMDc3MTkzOTU0NzgwODAyMjY2MTgzNjg4NDg0NjM0Mjg3OTE5MTUxNDA4OTI5MjUxNzAyNTEzMDg3ODMyNzczMTQ3NzkzNzQ0ODIyMDMyNTA1MDMyOTU3OTI4NTk2ODgwMjk3OTE0Nzg4ODg4NDMwOTEyNjY0OTU4MjEyNjY2NTQwODg2NzUyMjcxODYxMTY4NTI5OTUxMDQ5MDkwNTM4MTM3OTE0NTEzMDQ0NDIwMjg3ODkwMjA3MTU4MTI5MDcxMTYxNzYyMTkzMDg3OTc1NjQzNzU1NjkyNzA0MDg1ODczNDU5ODY5MDIyOTg3MTg3NzAzMjc1MjcxMzAzNjc2MDAwMzUwMjY0NjAxMTk0NzM5OTUzMjAyNDc0NDA4NTg5NzAzNTk2NjY1NDE0NTc2MDUwMjMyMjU0MjQxOTA3NjAyNjI2MDk2MzUyMDM0NTc5MDEzNzI5MjgzODc4ODd9LCAic2lnbmVyIjogInJvb3QifQ=="
root_cert_signature_b64 = "n2Ez/WKDRcwx9BM0pq7kueILS+h97D0nnGi/raVmdzbe/jt8C6LU8/JyeqrL05xgwug1jB2PX6tk3CbRmlmydi3y7oX+mwqc/1cyqrF5aQ4PWu36VexXslZm6TTkb7sXHp1+zADFX7i0vFLYk02W8ORtpBEDEZlsitIFd1mya0M4SGgTfvskiyTjeEOaeJ5WqKxaasviNG7PbzOqr+N/syYgAZdeYvsfO0Ca1lHIlKx8+4rdZShLa8Rw/unUnZe/PJbAzN+qPtewlTr45eKcTXGCoGhbC54VhUSYFncdwogIQLIL3l1BNW0Ft6dIqVheOnL/1BEKpC/2a5eQTvTDMw=="

# Extracting root_n from the root certificate
root_cert_decoded = json.loads(base64.b64decode(root_cert_b64).decode())
root_n = root_cert_decoded['key']['n']

for order in ["big", "little"]:
    user_cert_b64, user_signature_b64 = create_user_cert(root_d, root_n, order)
    print(f"\nByte Order: {order.capitalize()}")
    print(f"User certificate (b64): {user_cert_b64}")
    print(f"User certificate signature (b64): {user_signature_b64}")

