section .text
global _start

_start:
    ; Save the current stack pointer into RDI
    mov rdi, rsp

    ; Null-terminate the string
    xor rax, rax
    push rax

    ; Push "/bin/sh" onto the stack
    push 0x68732f2f
    push 0x6e69622f

    ; Move the address of "/bin/sh" (top of the stack) into RSI
    mov rsi, rsp

    ; Null-terminate the arguments array
    xor rdx, rdx

    ; Call execve("/bin/sh", ["/bin/sh", NULL], NULL)
    mov al, 0x3b
    syscall
    