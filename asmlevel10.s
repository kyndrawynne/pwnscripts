movabs $0x404000, %rbx
mov (%rbx), %rax
mov %rax, %rdx
addq $0x1337, %rdx
mov %rdx, (%rbx)
