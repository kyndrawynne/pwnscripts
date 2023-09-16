.global _start

.section .text
_start:
  jmp bridge_end       # Relative jump to the label 'bridge_end'

  .rept 0x51          # Repeat NOP instruction 0x51 times
    nop
  .endr

bridge_end: 
  pop %rdi             # Take the top of stack into rdi
  mov $0x403000, %rax  # Move the address into rax
  jmp *%rax            # Jump to the address stored in rax
