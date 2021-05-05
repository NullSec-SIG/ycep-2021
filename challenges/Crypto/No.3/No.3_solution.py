from pwn import xor

a = bytes.fromhex("37f17aef7304e649ab8d00fa6e3bee5870525b86b031f7a51997a40cd8070b00886ccc5f5d05535cf00a18f22448083cd90387f0d2ce37571280c3e44f4eb20fef7f677b9642b371")
b = bytes.fromhex("28da1cfc4041d61a8ff32ede68108f7f4b526bb9e1")

test = b"We have a East Coast, Singapore, we have a together, an East Coast plan."

key = xor(a, test)
print(xor(a, test))
print(xor(key, b))
