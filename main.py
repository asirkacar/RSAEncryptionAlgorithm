import decimal

import math
import random
a=0
b=0
while(a==0):
    x = random.randint(50,1000)
    sayac = 0
    for i in range(2,x):
        if (x % i) == 0:
            sayac = sayac + 1
            break
    if sayac == 0:
        p = x
        a = 1
while(b == 0):
    y = random.randint(50, 1000)
    sayac = 0
    for i in range(2 , y):
        if (y % i) == 0:
            sayac = sayac + 1
            break
    if sayac == 0:
        q=y
        b=1
n=p*q
totien_n=(q-1)*(p-1)

c=0
while (c == 0):
    z = random.randint(2, totien_n)
    if math.gcd(totien_n,z) == 1:
        e = z
        c = 1
    else:
        continue
f = 0
sayac_k = 0
while (f == 0):
    if (1+(sayac_k*totien_n)) % e == 0:
        d = (1 + (sayac_k * totien_n)) / e
        f = 1
    else:
        sayac_k = sayac_k + 1

giris = input("giriş")
word = []
asc = []
newPswArry = []
answrPswrd = []
asnwrPswrdAsc = []
for i in range(len(giris)):
    word.append(giris[i])
for i in range(len(word)):
    asc.append(ord(word[i]))

for i in range(len(asc)):
    newPswArry.append((asc[i]**e)%n)

decimal.getcontext().prec = 100000000000000000
l = decimal.Decimal(0)
for i in range(len(newPswArry)):
    answrPswrd.append((decimal.Decimal(newPswArry[i]) ** decimal.Decimal(d)) % decimal.Decimal(n))
for i in range(len(answrPswrd)):
    asnwrPswrdAsc.append(chr(int(answrPswrd[i])))


"""-----------------------ASALLIK KONTROL-----------------"""
print("sayip:",p)
print("sayiq:",q)
print("n sayısı:",n)
print("totien",totien_n)
print("e sayısı",e)
print("d sayısı", d)
print("dizi kelimeler:",word)
print("dizi ascii:",asc)
print("sifreli dizi:",newPswArry)
print("sifre cozulu:", answrPswrd)
print("cözülü hali:",asnwrPswrdAsc)
print("sifre:")
print("".join([str(i) for i in newPswArry]))
print("cözülmüs hali:")
print("".join([str(i) for i in asnwrPswrdAsc]))

"""------------------------------ASALLIK KONTROL---------------------------"""
sayac_a = 0
sayac_b = 0
for i in range(2, p):
    if p % i == 0:
        sayac_a = sayac_a + 1
        break
if sayac_a == 0:
    print("---------------sayı asal:", p)
else:
    print("---------------sayı asal değil", p)

for i in range(2, q):
    if q % i == 0:
        sayac_b = sayac_b + 1
        break
if sayac_b == 0:
    print("---------------sayı asal:", q)
else:
    print("---------------sayı asal değil:", q)

"""------------------------------ASALLIK KONTROL---------------------------"""




















"""
y=[]
k=[]
t=[]
password_create=input("giris:")

for i in range(len(password_create)):
    y.append(int(ord(password_create[i])))
print("ascii",y)
for i in range(len(y)):
    k.append(y[i]**2)

print("son hali:", k)
for i in range(len(k)):
    c=k[i]
    c=str(c)
    for j in range((len(c))):
        a=c[j]
        a=int(a)
        t.append(chr(a))



#password_solved=input("giris:")"""





