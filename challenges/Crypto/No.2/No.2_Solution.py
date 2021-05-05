def xor(a, b):
    res=[]
    i=0
    while i<len(a) or i<len(b):
        res.append(a[i%len(a)]^b[i%len(b)])
        i+=1
    return bytes(res)

for j in open("output.txt").read().strip().splitlines():
    k = bytes.fromhex(j)
    l = xor(k, xor(k[:1], b'H'))
    if l.startswith(b"HNF{"):
        print(l.decode())
