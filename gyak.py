"""
#1.

lista = []
for x in range(1,4,1):
    szam = int(input("Kérem a számot: "))
    lista.append(szam)
    
legkis = min(lista)
print("A lista legkisebb száma:",legkis)


#2.
szam1 = int(input("Kérem az első számot: "))
szam2 = int(input("Kérem a második számot: "))
szam3 = int(input("Kérem a harmadik számot: "))
if szam1 == szam2 == szam3:
    print("Ez három érték egyenlő.")
else:
    print("Ez három érték különböző.")


  
#3.
pont = int(input("Mi a dolgozatra kapott pontszám? "))
if pont<50:
    print("A dolgozatra kapott érdemjegy: 1")
if 50<=pont<60:
    print("A dolgozatra kapott érdemjegy: 2")
if 60<=pont<70:
    print("A dolgozatra kapott érdemjegy: 3")
if 70<=pont<85:
    print("A dolgozatra kapott érdemjegy: 4")
if pont>=85:
    print("A dolgozatra kapott érdemjegy: 5")

#4.
oszthato = False
szam = int(input("Kérem a számot: "))
if szam %3 ==0 or szam %5 ==0:
    oszthato = True
    
if oszthato:
    print("A szám osztható 3-mal vagy 5-tel.")
else:
    print("A szám NEM osztható 3-mal vagy 5-tel.")


#5
szam1 = int(input("Kérem az első számot: "))
szam2 = int(input("Kérem a második számot: "))
szam3 = int(input("Kérem a harmadik számot: "))

if szam1 + szam2 == szam3 or szam2 + szam3 ==szam1 or szam1 + szam3 == szam2:
    print("Valamelyik két szám összege egyenlő a harmadik számmal.")
else:
    print("Valamelyik két szám összege NEM egyenlő a harmadik számmal.")


#6.
szam1 = int(input("Kérem az első számot: "))
szam2 = int(input("Kérem a második számot: "))
szam3 = int(input("Kérem a harmadik számot: "))

if szam1 %2 ==0 and szam2 %2 ==0 and szam3 %2 ==0:
    print("Mind a három szám páros.")
else:
    print("NEM páros mind a három szám.")
    


#7.
x = int(input("Adj meg egy pozitív számot: "))
while x > 1:
    x-=1
    if x %3 ==0:
        print(x)


#8.
A = float(input("Kérem a számot: "))
K = int(input("Kérem a másik számot: "))
print(A**K)

#9.
szam = int(input("Kérek egy 20-tól nem nagyobb számot: "))
szokoz = szam*" "
print(szokoz,"START")

#12.
szam1 = float(input("Kérem az első számot: "))
szam2 = float(input("Kérem a második számot: "))
x = 0
while szam1<szam2:
    szam1+=1
    print(szam1)

while szam2<szam1:
    szam2+=1
    print(szam2)


#13.
szam1 = int(input("Kérem az első számot: "))
szam2 = int(input("Kérem a második számot: "))
x = 0
while szam1<szam2:
    szam1+=1
    if szam1 %2 ==0:
        print(szam1)

while szam2<szam1:
    szam2+=1
    if szam2 %2 ==0:
        print(szam2)


#27.
lista = [20,100,2,23,4]
sorrend = lista.sort()
csökkeno = lista.reverse()
print(lista)
"""
