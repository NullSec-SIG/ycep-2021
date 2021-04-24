import random
a = random.randint(250,300)
b =random.randint(250,300)
a1 =random.randint(250,300)
b1 = random.randint(250,300)
m = a*b-1
e =a1*m + a
d = b1*m+b
n =((e*d)-1)/m
pt = random.randint(1,n-1)
ct = ((pt * e) % n) 
