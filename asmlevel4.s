.global _start
_start:
    mov %rdi, %rbx
    mov %rbx, %rax
    xor %rdx, %rdx
    div %rsi

