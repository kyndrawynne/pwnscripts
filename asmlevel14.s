.section .text
.global _start
_start:
    pop %rax                # Pop the top value of the stack into rax
    sub %rdi, %rax          # Subtract the value in rdi from rax
    push %rax               # Push the result back onto the stack
