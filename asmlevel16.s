.section .text
.global _start
_start:
    mov (%rsp), %rax      # load Quad Word D
    add 0x8(%rsp), %rax   # add Quad Word C
    add 0x10(%rsp), %rax  # add Quad Word B
    add 0x18(%rsp), %rax  # add Quad Word A
    shr $2, %rax          # divide sum by 4
    sub $8, %rsp          # move rsp to make room for the average
    mov %rax, (%rsp)      # store the average
