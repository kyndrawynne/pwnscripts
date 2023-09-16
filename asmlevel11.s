.section .text
.global _start
_start:
    movabs $0x404000, %rbp

    movb (%rbp), %al
    movw (%rbp), %bx
    movl (%rbp), %ecx
    movq (%rbp), %rdx

