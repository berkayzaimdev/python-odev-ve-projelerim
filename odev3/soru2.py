class Araba:
    arabalar = []
    next_id=1


    def __init__(self, marka="", hiz=0, fiyat=0, renk=""):
        self.marka = marka
        self.hiz = hiz
        self.fiyat = fiyat
        self.renk = renk
        self.id=Araba.next_id
        self.__class__.arabalar.append(self)
        Araba.next_id+=1


def goster():
    if not Araba.arabalar:
        print("Araba bilgisi bulunmuyor!")
    else:
        for car in Araba.arabalar:
            print("*"*30)
            print((("ID -> " + str(car.id)).center(28, " ")).rjust(29, "*").ljust(30, "*"))
            print((("Marka -> "+car.marka).center(28," ")).rjust(29,"*").ljust(30,"*"))
            print((("Hız -> "+str(car.hiz)+" km/h").center(28," ").rjust(29,"*").ljust(30,"*")))
            print((("Fiyat -> "+str("{:,.0f} TL".format(car.fiyat))).center(28," ").rjust(29,"*").ljust(30,"*")))
            print((("Renk -> "+car.renk).center(28," ").rjust(29,"*").ljust(30,"*")))
            print("*"*30)
            print("\n\n")


def ekle():
    marka = input("Marka giriniz:")
    hiz = int(input("Hız giriniz:"))
    fiyat = int(input("Fiyat giriniz:"))
    renk = input("Renk giriniz:")
    Araba(marka,hiz,fiyat,renk)
    print("Araç başarıyla eklendi!")


def sil():
    goster()
    id=int(input("Silmek istediğiniz aracın ID'sini giriniz: "))
    for a in Araba.arabalar:
        if a.id == id:
            Araba.arabalar.remove(a)
            del a
            print("Araç başarıyla silindi!")
            return
    print("Girdiğiniz ID'li bir araba bulunmuyor!")


def guncelle():
    goster()
    id = int(input("Güncellemek istediğiniz aracın ID'sini giriniz: "))
    for a in Araba.arabalar:
        if a.id == id:
            marka = input("Marka giriniz:")
            hiz = int(input("Hız giriniz:"))
            fiyat = int(input("Fiyat giriniz:"))
            renk = input("Renk giriniz:")
            a.marka = marka
            a.hiz = hiz
            a.fiyat = fiyat
            a.renk = renk
            print("Araç başarıyla güncellendi!")
            return
    print("Girdiğiniz ID'li bir araba bulunmuyor!")


a1 = Araba()
a2 = Araba("Volvo", 220, 900000, "Kırmızı")
a3 = Araba("Tesla", 200, 1200000, "Siyah")
a4 = Araba()
a5 = Araba("BMW", 240, 1450000, "Lacivert")

sil()
guncelle()
goster()
ekle()
goster()