.intel_syntax noprefix
.globl _start
.global header

.section .text

_start:

    # create socket
    mov rdi, 2  # AF_INET
    mov rsi, 1  # SOCK_STREAM
    mov rdx, 0  # IPPROTO_IP
    mov rax, 41 # sys_socket
    syscall
    push rax

    # create bind
    mov rdi, rax
    sub rsp, 16
    mov word ptr [rsp], 2 # sa_family
    mov word ptr [rsp+2], 0x5000 # sin_port
    mov dword ptr [rsp+4], 0 # sin_addr
    mov qword ptr [rsp+8], 0 # 8 zeros
    mov rsi, rsp
    mov rdx, 16
    mov rax, 49
    syscall
    add rsp, 16

    # listen
    mov rdi, qword ptr [rsp]
    xor rsi, rsi
    mov rax, 50
    syscall

    # accept
    mov rdi, qword ptr [rsp]
    xor rsi, rsi
    xor rdx, rdx
    mov rax, 43
    syscall
    push rax # save the new client fd onto the stack

    # read data from client
    sub rsp, 1024
    mov rdi, qword ptr [rsp + 1024] # load the saved client fd
    mov rsi, rsp
    mov rdx, 1024
    mov rax, 0 # sys_read
    syscall

    # write data to the client
    mov rdi, qword ptr [rsp + 1024] # load the saved client fd
    lea rsi, [header]
    mov rdx, 19
    mov rax, 1  # sys_write
    syscall

    # close the client fd
    mov rdi, qword ptr [rsp + 1024] # load the saved client fd
    mov rax, 3
    syscall

    # exit
    mov rdi, 0
    mov rax, 60     # SYS_exit
    syscall

.section .data
header:
      .string "HTTP/1.0 200 OK\r\n\r\n"

