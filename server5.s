.intel_syntax noprefix
.globl _start

.section .text

_start:
    # Create a socket
    mov rax, 0x29
    mov rdi, 2     # AF_INET (IPv4)
    mov rsi, 1     # SOCK_STREAM (TCP)
    mov rdx, 0     # Protocol (default for TCP)
    syscall

    # Save the returned socket descriptor
    mov rdi, rax

    # Bind the socket to an address (port 80)
    mov rax, 0x31
    lea rsi, [rip+sockaddr]
    mov rdx, 16
    syscall

    # Listen on the socket
    mov rax, 0x32  # SYS_listen
    xor rsi, rsi  # Backlog of 0 connections
    syscall

    # Accept a connection
    mov rax, 0x2b # SYS_accept
    xor rsi, rsi  # No specific address
    xor rdx, rdx  # No address length
    syscall

    # Exit
    mov rdi, 0
    mov rax, 60
    syscall

.section .data
sockaddr:
.2byte 2      # sin_family = AF_INET
.2byte 0x5000 # sin_port = 80 (big-endian)
.4byte 0      # sin_addr = INADDR_ANY
.8byte 0      # Padding
