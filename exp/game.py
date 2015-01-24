#!/usr/bin/python2.7  
# -*- coding: utf-8 -*- 
'''
Created on 2014年11月29日

@author: yf
'''

from zio import *
import re
import time

io = zio('./qoobee4')#, print_write=False, print_read=False)
# io = zio(('10.11.12.13',1415), print_write=False, print_read=False)
lose_dic = ['scissor','rock','paper']
right_dic = ['paper', 'scissor','rock']
divset = [17, 16, 18, 19, 21, 22,23,24,25,26,27,28,29,30, 32 , 33 , 34  , 35 , 35  , 36 ,  37 , 38 , 39 , 40]
rightset = []
flag = ''


def losenum(modnum):
    return (modnum-1+3)%3

# def testdiv(modnum):
# #     while True:
#     io.read_until('Your Choice: ')
#     io.writeline('7')
#     io.read_until('Select one:')
#     io.writeline('%d' % losenum(modnum))
#     io.read_until('number(0-100)? ')
#     for i in divset:
#         io.writeline('%d' % i)
#         buf = io.read_until('\n')
#         if 'lose' in buf:
#             io.writeline('7')
#             io.read_until('Select one:')
#             io.writeline('%d' % losenum(modnum))
#             io.read_until('number(0-100)? ')
#         else:
#             print i
#     pass
pattern = re.compile(r'(\d+)!',re.M)

def checkround2():
    log('enter checkround')
    rst = {}
    io.read_until('Select one:')
    io.writeline('paper')
    buf = io.read_until('\n')
    if 'lose' in buf:
        log('lose')
        modnum = 2
        io.writeline('0')
        buf = io.read_until('Bye!')
        log(buf)
        divnum = int(pattern.findall(buf)[0])
        log('divnum:%d' % divnum)
    elif 'paper' in buf:
        log('tie')
        return '$'
        modnum = 1
        io.read_until('Select one: ')
        io.writeline('1234')
        io.read_until('number(0-100)? ')
        io.writeline('0')
        io.read_until('Your Choice: ')
        io.writeline('7')
        for i in rightset:
            log(i)
            log(right_dic[i])
            io.read_until('Select one:')
            io.writeline(right_dic[i])
        io.writeline('scissor')
        io.read_until('number(0-100)?')
        io.writeline('0')
        buf = io.read_until('\n')
        divnum = int(pattern.findall(buf)[0])
        log('divnum:%d' % divnum)
    elif 'rock' in buf:
        log('win')
        return '$'
        modnum = 0
        io.read_until('Select one: ')
        io.writeline('1234')
        io.read_until('number(0-100)? ')
        io.writeline('0')
        io.read_until('Your Choice: ')
        io.writeline('7')
        for i in rightset:
            log(i)
            log(right_dic[i])
            io.read_until('Select one:')
            io.writeline(right_dic[i])
        io.writeline('paper')
        io.read_until('number(0-100)?')
        io.writeline('0')
        buf = io.read_until('\n')
        divnum = int(pattern.findall(buf)[0])
        log('divnum:%d' % divnum)
    r = divnum*3 + modnum
    log ("char is %d,'%c'" % (r,chr(r)))
    rightset.append(modnum)
    log('out checkround')
    return chr(r)

def checkround3():
    log('enter checkround')
    rst = {}
    io.read_until('Select one:')
    io.writeline('scissor')
    buf = io.read_until('\n')
    if 'lose' in buf:
        log('lose')
        modnum = 0
        io.writeline('0')
        buf = io.read_until('Bye!')
        log(buf)
        divnum = int(pattern.findall(buf)[0])
        log('divnum:%d' % divnum)
    elif 'scissor' in buf:
        log('tie')
        return '$'
        modnum = 2
        io.read_until('Select one: ')
        io.writeline('1234')
        io.read_until('number(0-100)? ')
        io.writeline('0')
        io.read_until('Your Choice: ')
        io.writeline('7')
        for i in rightset:
            log(i)
            log(right_dic[i])
            io.read_until('Select one:')
            io.writeline(right_dic[i])
        io.writeline('scissor')
        io.read_until('number(0-100)?')
        io.writeline('0')
        buf = io.read_until('\n')
        divnum = int(pattern.findall(buf)[0])
        log('divnum:%d' % divnum)
    elif 'paper' in buf:
        log('win')
        return '$'
        modnum = 1
        io.read_until('Select one: ')
        io.writeline('1234')
        io.read_until('number(0-100)? ')
        io.writeline('0')
        io.read_until('Your Choice: ')
        io.writeline('7')
        for i in rightset:
            log(i)
            log(right_dic[i])
            io.read_until('Select one:')
            io.writeline(right_dic[i])
        io.writeline('paper')
        io.read_until('number(0-100)?')
        io.writeline('0')
        buf = io.read_until('\n')
        divnum = int(pattern.findall(buf)[0])
        log('divnum:%d' % divnum)
    r = divnum*3 + modnum
    log ("char is %d,'%c'" % (r,chr(r)))
    rightset.append(modnum)
    log('out checkround')
    return chr(r)

def forlast2():
    global flag
    log('last round')
    io.read_until('Your Choice: ')
    io.writeline('7')
    for i in rightset:
        log(i)
        log(right_dic[i])
        io.read_until('Select one:')
        io.writeline(right_dic[i])
    c = checkround3()
    if c:
        flag += c
    log('flag:%s' % flag)

def forlast():
    global flag
    log('last round')
    io.read_until('Your Choice: ')
    io.writeline('7')
    for i in rightset:
        log(i)
        log(right_dic[i])
        io.read_until('Select one:')
        io.writeline(right_dic[i])
    c = checkround2()
    if c=='$':
        forlast2()
    elif c:
        flag += c
    log('flag:%s' % flag)

def round():
    global flag
    for j in range(32):
        log('new round')
        io.read_until('Your Choice: ')
        io.writeline('7')
        for i in rightset:
            log(i)
            log(right_dic[i])
            io.read_until('Select one:')
            io.writeline(right_dic[i])
        c = checkround()
        if c=='$':
            forlast()
        elif c:
            flag += c
        log('flag:%s' % flag)

def checkround():
    log('enter checkround')
    rst = {}
    io.read_until('Select one:')
    io.writeline('rock')
    buf = io.read_until('\n')
    if 'lose' in buf:
        log('lose')
        modnum = 1
        io.writeline('0')
        buf = io.read_until('Bye!')
        log(buf)
        divnum = int(pattern.findall(buf)[0])
        log('divnum:%d' % divnum)
    elif 'rock' in buf:
        log('tie')
        modnum = 0
        if len(rightset)==31:
            return '$'
        io.read_until('Select one: ')
        io.writeline('1234')
        io.read_until('number(0-100)? ')
        io.writeline('0')
        io.read_until('Your Choice: ')
        io.writeline('7')
        for i in rightset:
            log(i)
            log(right_dic[i])
            io.read_until('Select one:')
            io.writeline(right_dic[i])
        io.writeline('scissor')
        io.read_until('number(0-100)?')
        io.writeline('0')
        buf = io.read_until('\n')
        divnum = int(pattern.findall(buf)[0])
        log('divnum:%d' % divnum)
    elif 'scissor' in buf:
        log('win')
        modnum = 2
        if len(rightset)==31:
            return '$'
        io.read_until('Select one: ')
        io.writeline('1234')
        io.read_until('number(0-100)? ')
        io.writeline('0')
        io.read_until('Your Choice: ')
        io.writeline('7')
        for i in rightset:
            log(i)
            log(right_dic[i])
            io.read_until('Select one:')
            io.writeline(right_dic[i])
        io.writeline('paper')
        io.read_until('number(0-100)?')
        io.writeline('0')
        buf = io.read_until('\n')
        divnum = int(pattern.findall(buf)[0])
        log('divnum:%d' % divnum)
    r = divnum*3 + modnum
    log ("char is %d,'%c'" % (r,chr(r)))
    rightset.append(modnum)
    log('out checkround')
    return chr(r)
#     testdiv(modnum)

def p7():
#     io.read_until('Your Choice: ')
#     io.writeline('1')
#     io.read_until('QooBee Name: ')
#     io.writeline('1')
#     io.read_until('QooBee Age: ')
#     io.writeline('1')
#     io.read_until('Description(30 bytes): ')
#     io.writeline('1')
    try:
        round()
    except TIMEOUT:
        print flag
#     print 'end'

def main():
    reg=re.compile(r'have (\d+) donuts')
    reg_level=re.compile(r'Exp: \d+\/(\d+)')
    time1 = time.time()
#     io = zio('./qoobee4')
    io.read_until('Choice:')
    io.writeline('1')
    io.read_until('Name:')
    io.writeline('1')
    io.read_until('Age:')
    io.writeline('1')
    io.read_until('(30 bytes):')
    io.writeline('%8888u%8888u%4u%4u%4u%4u%n')
    total=0
    Level=0
    io.read_until('Choice:')
    while Level<49:
        while total<1000:
            io.writeline('3')
            r = io.read_until('?')
            ind = r.index('Amount')
            Amount = int(r[ind+6:ind+8])
            io.writeline(str(Amount))
            total+=Amount
            r = io.read_until('Choice:')
            if 'Sorry' in r:
                total-=Amount
                io.writeline('2')
                io.read_until('Choice:')
        while total>0:
            if len(reg_level.findall(r))>0 and 500 == int(reg_level.findall(r)[0]):
                print reg_level.findall(r)
                Level=49
                break
            io.writeline('4')
            r = io.read_until('?')
            have=int(reg.findall(r)[0])
            if have>=9:
                have = 9
            total-=have
            io.writeline(str(have))
    time2=time.time()
    print time2-time1
    p7()
    f = open('flagset','a')
    f.write(flag+' '+time.strftime('%H:%M:%S',time.localtime(time.time()))+'\n')
    f.close()
    print 'thread over with flag:%s' % flag

if __name__ == '__main__':
    main()
