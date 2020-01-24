class Calisan:
    counter = 0
    toplam=[]
    def __init__(self,isim,soyisim,yas,maas,email): 
        self.isim = isim
        self.soyisim = soyisim
        self.maas = maas
        self.yas=yas
        self.email = isim+soyisim+"@sirket.com"
        Calisan.counter = Calisan.counter + 1
        Calisan.toplam.append(self)

def zam_yap(oran):
    toplammaas = 0
    for i in Calisan.toplam:
        toplammaas += i.maas
        i.maas = int(i.maas * ((100+oran)/100))
    maliyet=toplammaas*oran/100
    return maliyet
        


def maassirala():
    maassirala=[]
    for i in Calisan.toplam:
        maassirala.append(i.maas)
    maassirala.sort()
    return maassirala

def isimsirala():
    isimsirala=[]
    for i in Calisan.toplam:
        isimsirala.append(i.isim)
    isimsirala.sort()
    return isimsirala

def yassirala():
    yassirala=[]
    for i in Calisan.toplam:
        yassirala.append(i.yas)
    yassirala.sort()
    return yassirala

calisan1=Calisan("merve","gokcan",25,1400,26)

calisan2=Calisan("guldane","ozdemir",26,6000,26)

calisan3=Calisan("nermin","akarsu",24,1500,27)

calisan4=Calisan("hilal","altas",22,2500,30)

print("Maliyet",zam_yap(10))

print(isimsirala())
print(maassirala())
print(yassirala())





    