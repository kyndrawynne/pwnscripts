.section .text
.global _start
_start:
    mov (%rdi), %rax         # Load the quad word at the address in rdi into rax
    mov 0x8(%rdi), %rbx      # Load the next quad word (8 bytes away) into rbx
    add %rbx, %rax           # Add the values in rax and rbx, storing the result in rax
    mov %rax, (%rsi)         # Store the result at the address in rsi
