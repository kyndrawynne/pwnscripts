from pwn import *
from base64 import b64encode, b64decode

p = process("/challenge/run")

p.recvuntil(b"secret ciphertext (b64): ")
secret_cipher = b64decode(p.recvuntil(b"\n", drop=True))

flag = b""

# For each block of the flag
for block in range(4):  # Change 3 to 4 or higher to extract more blocks
    # For each byte in the block
    for i in range(15, -1, -1):
        p.sendline(b64encode(b"a" * i))
        p.recvuntil(b"ciphertext (b64): ")
        cipher = b64decode(p.recvuntil(b"\n", drop=True))

        # Guess each possible byte value
        for j in range(0, 256):
            p.sendline(b64encode(b"a" * i + flag + bytes([j])))
            p.recvuntil(b"ciphertext (b64): ")
            temp_cipher = b64decode(p.recvuntil(b"\n", drop=True))
            if temp_cipher[block*16:(block+1)*16] == cipher[block*16:(block+1)*16]:
                flag += bytes([j])
                print(flag)
                break

print("Final flag:", flag)
