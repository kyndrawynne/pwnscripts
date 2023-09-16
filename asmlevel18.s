.global _start

.section .text
_start:
  cmpl $0x7f454c46, (%rdi)  # Compare dword at rdi with 0x7f454c46
  je ELF_case               # Jump to ELF_case if equal
  cmpl $0x00005A4D, (%rdi)  # Compare dword at rdi with 0x00005A4D
  je MZ_case                # Jump to MZ_case if equal

  # Else case
  movl 4(%rdi), %eax        # Move dword at rdi+4 into eax
  imull 8(%rdi), %eax       # Multiply eax by dword at rdi+8
  imull 12(%rdi), %eax      # Multiply eax by dword at rdi+12
  jmp end                   # Jump to end

ELF_case:
  movl 4(%rdi), %eax        # Move dword at rdi+4 into eax
  addl 8(%rdi), %eax        # Add dword at rdi+8 to eax
  addl 12(%rdi), %eax       # Add dword at rdi+12 to eax
  jmp end                   # Jump to end

MZ_case:
  movl 4(%rdi), %eax        # Move dword at rdi+4 into eax
  subl 8(%rdi), %eax        # Subtract dword at rdi+8 from eax
  subl 12(%rdi), %eax       # Subtract dword at rdi+12 from eax
  # Fall through to end

end:
  # End of the program
