from tkinter import *
from tkinter import messagebox


def salonsifirla():
    return [[[[['-' for x in range(10)] for x in range(10)] for x in range(2)] for x in range(2)] for x in range(3)]


def cirosifirla():
    return [[0 for x in range(4)] for x in range(3)]


salon=salonsifirla()
ciro=cirosifirla()
filmindis=0


class FilmButonlari(Button):
    def __init__(self,parent,*args,**kwargs):
        Button.__init__(self,parent,*args,**kwargs)
        self["bg"]="#3b3b3b"
        self["fg"]="white"
        self["font"]=("Verdana",13,"bold")
        self["width"]=10
        self["height"]=2
        self["borderwidth"]=0
        self.bind("<Enter>",self.hover)
        self.bind("<Leave>",self.unhover)
    def hover(self,event):
        self.config(bg="#515151")
    def unhover(self,event):
        self.config(bg="#3b3b3b")


class SecimButonlari(Button):
    def __init__(self,parent,*args,**kwargs):
        Button.__init__(self,parent,*args,**kwargs)
        self["bg"]="#3700b3"
        self["fg"]="white"
        self["font"]=("Verdana",10,"bold")
        self["width"]=20
        self["height"]=2
        self["borderwidth"] = 0
        self.bind("<Enter>",self.hover)
        self.bind("<Leave>",self.unhover)
    def hover(self,event):
        self.config(bg="#6200ee")
    def unhover(self,event):
        self.config(bg="#3700b3")


class KategoriRB:
    def __init__(self, root, text,color,variable,value):
        self.radiobutton = Radiobutton(root,text=text, variable=variable, value=value)
        self.radiobutton.config(fg=color,font=("Helvecita", 13, "bold"))
        self.radiobutton.pack()


def rezervasyon():
    hatalar=""
    kat = rbk.get()
    try:
        if kat == 0:
            hatalar += "Lütfen kategori seçimi yapınız!\n"
        bilet = int(koltuk.get("1.0", END))
        if bilet > max or bilet < 1:
            hatalar += "Seçtiğiniz bilet sayısı belirtilen sınırlar içerisinde olmalıdır. Lütfen geçerli bir değer giriniz\n"
        satir = int((kat - 1) / 2)
        kat = 0 if kat % 2 != 0 else 1
        r = 0
        for i in salon[filmindis][satir][kat]:
            for j in i:
                if j == "X":
                    r += 1
        if bilet+r>100:
            hatalar+="Seçtiğiniz bilet sayısı, güncel kapasiteyi aşıyor! Lütfen geçerli bir değer giriniz."
    except ValueError:
        hatalar += "Lütfen sayısal bir değer giriniz!\n"
    if hatalar=="":
        fiyatmesaj=fiyatbul(indirimler, satir, kat, bilet)
        koltuklar = "Rezerve edilen koltuklar (Sıra-Koltuk): " if bilet > 1 else "Rezerve edilen koltuk (Sıra-Koltuk): "
        for i in range(len(salon[filmindis][satir][kat])):
            for j in range(len(salon[filmindis][satir][kat])):
                if salon[filmindis][satir][kat][i][j] == "X":
                    continue
                salon[filmindis][satir][kat][i][j] = "X"
                r += 1
                sira = str(1 + int((r - 1) / 10) + (satir * 10))
                x = 5 if (r - 1) % 10 < 5 else 11
                k = str(6 + (r - 1) % 10) if kat == 0 else str(x - (r - 1) % 10) if x==5 else str(x + (r - 1) % 10)
                koltuklar += sira + "-" + k + ", "
                bilet -= 1
                if bilet == 0:
                    break
            if bilet == 0:
                break
        messagebox.showinfo("Rezervasyonunuz Başarılı!", koltuklar.rstrip(", "))
        messagebox.showinfo("Fiyat Bilgisi",fiyatmesaj)
    else:
        messagebox.showerror("HATA", hatalar)


def fiyatbul(indirimler,satir,kat,bilet):
    indirim=0
    ciroindis=(satir*2)+kat
    for i in range(1,len(indirimler[ciroindis])-2,3):
        if bilet in range(int(indirimler[ciroindis][i]),int(indirimler[ciroindis][i+1])+1):
            indirim=int(indirimler[ciroindis][i+2])
            break
    toplam=bilet*float(indirimler[ciroindis][0])
    indirimlifiyat=toplam*(100-indirim)/100
    ciro[filmindis][(satir*2)+kat]+=indirimlifiyat
    return "\nBilet adedi:%d\nToplam tutar:%0.2f TL\nYapılan indirim:%0.2f TL\nNet tutar:%0.2f TL\n"%(bilet,toplam,toplam-indirimlifiyat,indirimlifiyat)


def salonguncelle():
    messagebox.showinfo("İşlem Başarılı","Salon Güncellendi!")
    salonyazdir()


def sifirla():
    global salon
    global ciro
    global filmindis
    salon=salonsifirla()
    ciro=cirosifirla()
    filmindis=0
    film.config(image=f1)
    salonyazdir()
    koltuk.delete(1.0,"end")
    messagebox.showinfo("İşlem Başarılı", "Yeni Etkinlik Açıldı!")


def salonyazdir():
    s0="\n"
    s1="\n"
    s2="\n"
    for k in range(len(salon[filmindis][0][0])):
        for m in salon[filmindis][0][1][k][4::-1]:
            s0 += m
        s0 += "\n"
        for m in salon[filmindis][0][0][k]:
            s1 += m
        s1 += "\n"
        for m in salon[filmindis][0][1][k][5:10]:
            s2 += m
        s2 += "\n"
    yazi00.config(text=s0)
    yazi01.config(text=s1)
    yazi02.config(text=s2)
    s0 = ""
    s1 = ""
    s2 = ""
    for k in range(len(salon[filmindis][1][0])):
        for m in salon[filmindis][1][1][k][4::-1]:
            s0 += m
        s0 += "\n"
        for m in range(len(salon[filmindis][1][0])):
            s1 += salon[filmindis][1][0][k][m]
        s1 += "\n"
        for m in salon[filmindis][1][1][k][5:10]:
            s2 += m
        s2 += "\n"
    yazi10.config(text=s0)
    yazi11.config(text=s1)
    yazi12.config(text=s2)


def toplamciro():
    total=""
    for i in range(len(salon[filmindis])):
        for j in range(len(salon[filmindis][i])):
           total+=str(1 + j + i * 2) + ".Kategori Ciro:" + str(ciro[filmindis][j + i * 2])+"\n"
    total+="Toplam Ciro:" + str(sum(ciro[filmindis]))
    messagebox.showinfo("Ciro Bilgisi",total)


def cikis():
    sonuc=messagebox.askyesno("Çıkış Yap","Emin misiniz?")
    if sonuc:
        pencere.destroy()


f = open("indirim.txt", "r")
max = int(f.readline().split("-")[1].replace("\n", ""))
indirimler = [[] for x in range(4)]
for line in f:
    if 'M' in line:
        line = line.replace('M', str(max))
    indirimler[int(line.split("-")[0]) - 1].extend(line.split("-")[1:])
f.close()


def filmdegis1():
    global filmindis
    filmindis = 0
    film.config(image=f1)
    salonyazdir()
    messagebox.showinfo("Vizyondaki Film",f1.name)


def filmdegis2():
    global filmindis
    filmindis = 1
    film.config(image=f2)
    salonyazdir()
    messagebox.showinfo("Vizyondaki Film", f2.name)


def filmdegis3():
    global filmindis
    filmindis = 2
    film.config(image=f3)
    salonyazdir()
    messagebox.showinfo("Vizyondaki Film", f3.name)


pencere=Tk()
pencere.title("Sinema BZ")


divyazi=Frame(pencere)


yazi00=Label(divyazi,font="Consolas 15 bold",fg="#4e4492")
yazi01=Label(divyazi,font="Consolas 15 bold",fg="#fc4909")
yazi02=Label(divyazi,font="Consolas 15 bold",fg="#4e4492")
yazi10=Label(divyazi,font="Consolas 15 bold",fg="#347284")
yazi11=Label(divyazi,font="Consolas 15 bold",fg="#461856")
yazi12=Label(divyazi,font="Consolas 15 bold",fg="#347284")
salonyazdir()
yazi00.grid(row=0,column=0)
yazi01.grid(row=0,column=1)
yazi02.grid(row=0,column=2)
yazi10.grid(row=1,column=0)
yazi11.grid(row=1,column=1)
yazi12.grid(row=1,column=2)

f1=PhotoImage(name="Yarının Sınırında",file="filmler/film1.gif")
f2=PhotoImage(name="Avengers: Infinity War",file="filmler/film2.gif")
f3=PhotoImage(name="Interstellar",file="filmler/film3.gif")
divfilm=Frame(pencere)
divbutton=Frame(divfilm,pady=5)
film=Label(divfilm,image=f1,width=404,height=600)
fb1=FilmButonlari(divbutton,text="FİLM 1",command=filmdegis1)
fb2=FilmButonlari(divbutton,text="FİLM 2",command=filmdegis2)
fb3=FilmButonlari(divbutton,text="FİLM 3",command=filmdegis3)
divfilm.grid(row=0,column=0,pady=5)
divbutton.pack(side=BOTTOM)
fb1.grid(row=0,column=0,padx=10)
fb2.grid(row=0,column=1,padx=5)
fb3.grid(row=0,column=2,padx=10)
film.pack(pady=5)

divsecim=Frame(pencere)
rbk=IntVar()
rbk1=KategoriRB(divsecim,text="1. Kategori",color="#fc4909",variable=rbk,value=1)
rbk2=KategoriRB(divsecim,text="2. Kategori",color="#4e4492",variable=rbk,value=2)
rbk3=KategoriRB(divsecim,text="3. Kategori",color="#461856",variable=rbk,value=3)
rbk4=KategoriRB(divsecim,text="4. Kategori",color="#347284",variable=rbk,value=4)
kmesaj=Label(divsecim,font=("Helvetica",12,"bold"),text="Koltuk Sayısı (1-"+str(max)+")",pady=2).pack(pady=0)
koltuk=Text(divsecim,width=5,height=1,font="Verdana 15")
koltuk.pack(pady=5)
b1=SecimButonlari(divsecim,text="REZERVASYON YAP",command=rezervasyon).pack(pady=5)
b2=SecimButonlari(divsecim,text="SALONU GÜNCELLE",command=salonguncelle).pack(pady=5)
b3=SecimButonlari(divsecim,text="YENİ ETKİNLİK",command=sifirla).pack(pady=5)
b4=SecimButonlari(divsecim,text="TOPLAM CİRO",command=toplamciro).pack(pady=5)
b5=Button(divsecim,text="ÇIKIŞ",borderwidth=0,background="#E33437",width=20,height=2,fg="white",font=("Verdana",10,"bold"),command=cikis).pack(pady=5)
divsecim.grid(row=0,column=2,padx=10)
divyazi.grid(row=0,column=1,padx=70)
pencere.mainloop()