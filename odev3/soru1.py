from tkinter.ttk import *
from tkinter import messagebox
from tkinter import *

toplam=0


class SButton(Button):
    def __init__(self,parent,*args,**kwargs):
        Button.__init__(self,parent,*args,**kwargs)
        self["bg"]="#1834F3"
        self["fg"]="white"
        self["font"]=("Verdana",10,"bold")
        self["width"]=20
        self["height"]=2
        self["borderwidth"] = 0
        self.bind("<Enter>",self.hover)
        self.bind("<Leave>",self.unhover)
    def hover(self,event):
        self.config(bg="#3371FF")
    def unhover(self,event):
        self.config(bg="#1834F3")


def total():
    mesaj = "Elde Edilen Toplam Gelir:"+str(toplam)+" bin TL"
    messagebox.showinfo("Toplam Gelir", mesaj)


def rezerve():
    hatalar=""
    if rb.get()==0:
        hatalar+="Lütfen konaklayacağınız yeri seçiniz!\n"
    if values[cmb.get()]==-1:
        hatalar+="Lütfen konaklama tipi seçiniz!\n"
    for text in frame_secim.winfo_children():
        if isinstance(text, Text):
            s = text.get(1.0, END)
            if s.strip() == "":
                hatalar+="Lütfen boş alan bırakmayınız!\n"
                break
    if not (text_yetiskin.get(1.0, END).rstrip().isdigit() and text_cocuk.get(1.0, END).rstrip().isdigit() and text_c.get(1.0, END).rstrip().isdigit()):
        hatalar+="Lütfen kişi ve konaklanacak gün bilgisini sayısal olarak giriniz!\n"
    if hatalar == "":
        global toplam
        sonuc = int(text_c.get(1.0, END)) * (rb.get()+values[cmb.get()]) * (2 * int(text_yetiskin.get(1.0, END)) + int(text_cocuk.get(1.0, END)) )
        toplam+=sonuc
        mesaj = "Gelir:" + str(sonuc) + " bin TL"
        messagebox.showinfo("Rezervasyon Başarılı", mesaj)
    else:
        messagebox.showwarning("Hata",hatalar.rstrip())


def reset():
    global toplam
    toplam=0
    ico.config(image=icon)
    resim.config(image=o0)
    cmb.set("Seçiniz")
    rb.set(0)
    for element in frame_secim.winfo_children():
        if isinstance(element, Text):
            element.delete(1.0, END)
    messagebox.showinfo("İşlem Başarılı","Tüm seçimleriniz sıfırlandı!")


def cikis():
    sonuc=messagebox.askyesno("Çıkış Yap","Emin misiniz?")
    if sonuc:
        pencere.destroy()


def resimDegis():
    selected = rb.get()
    for button in rb_buttons:
        if button['value'] == selected:
            p=PhotoImage(file='icons/' + button['text'].lower() + '.gif')
            resim.config(image=p)
            resim.image=p


def on_select(event):
    selected_value = cmb.get()
    p=PhotoImage(file='icons/i' + selected_value.lower().replace(" ","") + '.png')
    ico.config(image=p)
    ico.image = p


pencere = Tk()
pencere.title("Otel Rezervasyon")


frame_resim = Frame(pencere,pady=10,padx=10)
o0=PhotoImage(name="Temp",file="icons/temp.gif")
o1=PhotoImage(name="Bodrum",file="icons/bodrum.gif")
o2=PhotoImage(name="Çeşme",file="icons/çeşme.gif")
o3=PhotoImage(name="Marmaris",file="icons/marmaris.gif")
resim = Label(frame_resim,image=o0)
resim.pack()


i=0;
frame_secim =Frame(pencere,pady=10,padx=10)
label_soyad=Label(frame_secim,text="Ad:",font="Verdana 9").grid(column=0,row=i)
text_ad=Text(frame_secim,width=15,height=1,font="Verdana 9").grid(column=1,row=i,pady=5)
i+=1
label_soyad=Label(frame_secim,text="Soyad:",font="Verdana 9").grid(column=0,row=i)
text_soyad=Text(frame_secim,width=15,height=1,font="Verdana 9").grid(column=1,row=i,pady=5)
i+=1
label_adres=Label(frame_secim,text="Adres:",font="Verdana 9").grid(column=0,row=i)
text_adres=Text(frame_secim,width=15,height=1,font="Verdana 9").grid(column=1,row=i,pady=5)


rb = IntVar()
rb_buttons = [Radiobutton(frame_secim, text="Bodrum", variable=rb, value=5, command=resimDegis,font="Verdana 9"),
              Radiobutton(frame_secim, text="Çeşme", variable=rb, value=3, command=resimDegis,font="Verdana 9"),
              Radiobutton(frame_secim, text="Marmaris", variable=rb, value=1, command=resimDegis,font="Verdana 9")]

for i, button in enumerate(rb_buttons):
    button.grid(column=0,row=i+3,columnspan=2)

i+=4
values = {"Seçiniz": -1, "Family": 0, "Deluxe": 1,"King Suit": 2}
cmb=Combobox(frame_secim, values=list(values.keys()),state="readonly",font="Verdana 9")
cmb.current(0)


cmb.bind("<<ComboboxSelected>>", on_select)
cmb.grid(column=0,row=i,pady=5,padx=10)
icon=PhotoImage(file="icons/iseçiniz.png")
ico = Label(frame_secim,image=icon)
ico.grid(column=1,row=i,pady=5)


i+=1
label_yetiskin=Label(frame_secim,text="Yetişkin sayısı:",font="Verdana 9").grid(column=0,row=i)
text_yetiskin=Text(frame_secim,width=15,height=1,font="Verdana 9")
text_yetiskin.grid(column=1,row=i,pady=5)
i+=1
label_cocuk=Label(frame_secim,text="Çocuk sayısı:",font="Verdana 9").grid(column=0,row=i)
text_cocuk=Text(frame_secim,width=15,height=1,font="Verdana 9")
text_cocuk.grid(column=1,row=i,pady=5)
i+=1
label_c=Label(frame_secim,text="Kaç gece kalacaksınız?:",font="Verdana 9").grid(column=0,row=i)
text_c=Text(frame_secim,width=15,height=1,font="Verdana 9")
text_c.grid(column=1,row=i,pady=5)


i+=1
b1=SButton(frame_secim,text="TOTAL",command=total).grid(columnspan=2,row=i,pady=5)
i+=1
b2=SButton(frame_secim,text="RESERVATION",command=rezerve).grid(columnspan=2,row=i,pady=5)
i+=1
b3=SButton(frame_secim,text="RESET",command=reset).grid(columnspan=2,row=i,pady=5)
i+=1
b4=Button(frame_secim,text="ÇIKIŞ",background="#E33437",borderwidth=0,width=20,height=2,fg="white",font=("Verdana",10,"bold"),command=cikis).grid(columnspan=2,row=i,pady=5)


frame_resim.grid(row=0,column=0)
frame_secim.grid(row=0,column=1)
pencere.mainloop()