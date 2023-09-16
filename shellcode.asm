section .text
global _start

_start:
    ; Get the current stack pointer
    mov rdi, rsp

    ; Find the base address of the stack (16-byte aligned)
    and rdi, 0xFFFFFFFFFFFFFFF0

    ; Add an offset to the base address for the string "/bin/sh"
    add rdi, 16

    ; Null-terminate the string
    xor rax, rax
    mov [rdi], rax

    ; Move the string "/bin/sh" to rsi
    push rdi
    mov rsi, rsp

    ; Null-terminate the arguments array
    xor rdx, rdx

    ; Call execve("/bin/sh", ["/bin/sh", NULL], NULL)
    mov al, 0x3b
    syscall