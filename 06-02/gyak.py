#1. kérjünk be 5db számot és vizsgájuk meg hány db nagyobb mint 50
#2. függvény segítségével bekérünk 10 db egész számot amelyeket tárolunk listában
# a függvény adja vissza a legnagyobb és a legkisebb közötti különbségét
#3. olvassuk be a txt-t.
#a) hány diák szerepel
#b) Ádámnak mi a hobbija
#c) van-e olyan diák aki betöltötte a 30. évet ha igen ki ő?
#d) életkoruk átlaga 2 tizedes
#e) készíts egy olyan allomany.txt ahol a nevek csak a Diákok Hobbi

"""
#1.
db = 0
for x in range(1,6,1):
    szam = int(input("Kérem a számokat: "))
    if szam > 50:
        db+=1
        
if db > 0:
    print("Ennyi szám 50-től nagyobb:",db)
else:
    print("Nincs 50-től nagyobb szám.")


#2.
def fugg(nagy-kicsi):
    lista=[]
    for x in range(1,11,1):
        szam = int(input("Kérem a számokat: "))
        lista.append(szam)
        
    nagy=max(lista)
    kicsi=min(lista)
    kulonb=nagy-kicsi
    print("A legnagyobb és a legkisebb szám különbsége:",kulonb)
    
fugg()

"""
#3.
class Adat():
    def __init__(self,sor):
        egy=sor.rstrip("\n").split(";")
        self.nev=egy[0]
        self.kor=int(egy[1])
        self.hobbi=egy[2]
        
file=open("adatok.txt",encoding="utf-8")
be=file.readlines()
lista=[]
for x in be:
    lista.append(Adat(x))

#a)
nevek=[]
for x in lista:
    nevek.append(x.nev)

db=0
for x in nevek:
    db+=1
print("Ennyi diák van:",db)


#b)
kor_ossz=0
kor=[]
for x in lista:
    kor.append(x.kor)
    
for x in kor:
    kor_ossz+=x
    
kor_db=len(kor)
atlag=kor_ossz/kor_db
    
print("Életkoruk átlaga: {:.2f}".format(atlag))


#e)
ki = open("allomany.txt","w")
for x in lista:
    ki.write(x.nev+" " +x.hobbi+"\n") 
    
ki.close()
