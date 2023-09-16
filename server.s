.intel_syntax noprefix
.globl _start

.section .text

_start:
    mov rax, 41     
    mov rdi, 2      
    mov rsi, 1      
    mov rdx, 0      
    syscall
    mov rdi, rax    

    mov rax, 49     
    push 0x00000000 
    push 0x5000     
    push 2          
    mov rsi, rsp    
    mov rdx, 16     
    syscall

    mov rax, 50     
    mov rsi, rdi    
    xor rdx, rdx    
    syscall

    mov rax, 43     
    syscall
    mov r8, rax     

    mov rax, 0      
    lea rsi, [rsp-512] 
    mov rdx, 512    
    syscall

    mov rax, 2      
    xor rdx, rdx    
    syscall
    mov r9, rax     

    mov rax, 0      
    lea rsi, [rsp-512] 
    mov rdx, 512    
    syscall

    mov rax, 3      
    mov rdi, r9     
    syscall

    mov rax, 1      
    mov rdi, r8     
    lea rsi, [rel response_header]
    mov rdx, 19     
    syscall

    mov rax, 1      
    lea rsi, [rsp-512] 
    syscall

    mov rax, 3      
    mov rdi, r8     
    syscall

    mov rax, 60     
    xor rdi, rdi    
    syscall

.section .data
response_header:
    .asciz "HTTP/1.0 200 OK\r\n\r\n"

