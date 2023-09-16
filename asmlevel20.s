movq $0, %rax    # xor rax,rax
movq $0, %rcx    # xor rcx,rcx
movq %rsi, %rbx  # mov rbx,rsi
loop:
subq $1, %rbx    # sub rbx,1
movq (%rdi,%rbx,8), %rcx  # mov rcx,[rdi+rbx*8]
addq %rcx, %rax  # add rax,rcx
cmpq $0, %rbx    # cmp rbx,0
jne loop         # jne loop
nop
cqto             # sign extend rax to rdx:rax for division
idivq %rsi       # div rsi
