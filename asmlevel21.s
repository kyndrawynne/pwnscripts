movq $0, %rax       # mov rax,0
cmpq $0, %rdi       # cmp rdi,0
je done             # je done
movq $-1, %rsi      # mov rsi,-1
loop:
addq $1, %rsi       # add rsi,1
movzbl (%rdi,%rsi), %eax  # movzx rax, byte ptr [rdi+rsi]
cmpq $0, %rax       # cmp rax,0
jne loop            # jne loop
movq %rsi, %rax     # mov rax,rsi
done:
