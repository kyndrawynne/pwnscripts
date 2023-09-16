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

    # read data from client into buffer
    sub rsp, 1024
    mov rdi, qword ptr [rsp + 1024] # load the saved client fd
    mov rsi, rsp
    mov rdx, 1024
    mov rax, 0 # sys_read
    syscall

    # Call Python script using execve to parse the HTTP request
    lea rdi, [python_path]
    lea rsi, [python_args]
    xor rdx, rdx
    mov rax, 59  # sys_execve
    syscall

    # Read the file path from standard output (which was duplicated from the client socket)
    mov rdi, 0   # standard input
    lea rsi, [file_path_buffer]
    mov rdx, 256 # buffer size
    mov rax, 0   # sys_read
    syscall

    # Open the file
    lea rdi, [file_path_buffer]
    xor rsi, rsi # O_RDONLY
    mov rax, 2   # sys_open
    syscall

    # Check if file opened successfully
    test rax, rax
    js file_not_found

    # Read the file's contents
    mov rdi, rax # file descriptor
    lea rsi, [file_content_buffer]
    mov rdx, 1024# buffer size
    mov rax, 0   # sys_read
    syscall

    # Send the HTTP response header
    lea rsi, [http_header]
    mov rdx, 19  # length of "HTTP/1.0 200 OK\r\n\r\n"
    mov rax, 1   # sys_write
    syscall

    # Send the file's contents
    lea rsi, [file_content_buffer]
    mov rax, 1   # sys_write
    syscall

    # Exit
    mov rdi, 0
    mov rax, 60  # SYS_exit
    syscall

file_not_found:
    # Handle file not found error (send 404 response)

.section .data
python_path:
    .asciz "/usr/bin/python3"

python_script:
    .asciz "/home/hacker/weblvl7.py"

python_args:
    .quad python_path
    .quad python_script
    .quad 0

file_path_buffer:
    .zero 256

file_content_buffer:
    .zero 1024

http_header:
    .asciz "HTTP/1.0 200 OK\r\n\r\n"
