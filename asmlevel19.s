movq %rdi, %rax
andq $0xfffffffffffffffc, %rax
je normal
nop
jmp *(%rsi, %rax, 8)
nop
normal:
jmp *(%rsi, %rdi, 8)
nop

