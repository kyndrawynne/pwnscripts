.section .text
.global _start
_start:
    push %rdi        # Push rdi to the stack
    push %rsi        # Push rsi to the stack
    pop %rdi         # Pop the top value (which was rsi) from the stack to rdi
    pop %rsi         # Pop the next top value (which was rdi) from the stack to rsi
