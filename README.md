#HCTF2013 FINAL Qoobee

##Qoobee

程序-214功能可以执行代码，需要构造全ascii的shellcode，字符串里要含有ymkelwin

exp: ymkelwin.py

##Qoobee2

功能1中输入name存在溢出
ret2libc
利用-214功能中的mmap开辟的可执行缓冲区执行shellcode

exp: name.py

##Qoobee3

打工输入指令过滤存在问题，可以写入栈内存
写入ROP链
ROP调用mmap read之后执行shellcode

exp: work.py

##Qoobee4

fun1的输入description栈溢出
先利用fun2的printf漏洞（见Qoobee6）读取canary
注意一次只读100 bytes，分两次执行

exp: description

##Qoobee5

比赛时候打游戏，利用printf漏洞刷钱。先升级，再游戏...全部跑完要5分钟……

比赛后面发现printf可以对age指定的任意内存写入……想想可以直接改等级然后打游戏会更快点……

exp: game.py

##Qoobee6

printf可以对age指定的任意地址写入
读plt获得printf函数的地址
通过给定libc.so偏移获取system地址
将system替换plt的mmap函数

exp: printf.py
