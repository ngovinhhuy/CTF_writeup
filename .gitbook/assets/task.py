from Crypto.Util.number import getPrime
import os
import math
flag = os.getenv("FLAG", "FakeCTF{warmup_a_frozen_cake}")
#print(flag)
m = int(flag.encode().hex(), 16)

p = getPrime(512)
q = getPrime(512)

n = p*q
a=pow(m, p, n)
b=pow(m, q, n)
c=pow(m, n, n)
print("n =", n)
print("a =", a)
print("b =",b)
print("c =", c)
print("m =", m)
print("A: ",a*b*pow(c,-1,n)%n)
