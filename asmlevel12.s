.section .text
.global _start
_start:
    movabs $0xdeadbeef00001337, %rax
    mov %rax, (%rdi)
    movabs $0xc0ffee0000, %rax
    mov %rax, (%rsi)

