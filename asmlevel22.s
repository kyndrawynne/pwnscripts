.section .text
.globl _start

_start:
    movq $0, %rax
    movq %rdi, %rsi
    cmpq $0, %rsi
    je done
loop:
    movb (%rsi), %bl
    cmpb $0, %bl
    je done
    cmpb $90, %bl
    jbe next
    pushq %rax
    pushq %rdi
    movb %bl, %dil
    movq $0x403000, %rcx
    call *%rcx
    popq %rdi
    popq %rax
    movb %al, (%rsi)
    addq $1, %rax
next:
    addq $1, %rsi
    jmp loop
done:
    ret
