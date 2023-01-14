from tkinter.ttk import *
from tkinter import messagebox
from tkinter import *


class SButton(Button):
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


def total():
    sonuc=messagebox.askyesno("Çıkış Yap","Emin misiniz?")
    if sonuc:
        pencere.destroy()


def rezerve():
    sonuc=messagebox.askyesno("Çıkış Yap","Emin misiniz?")
    if sonuc:
        pencere.destroy()


def reset():
    sonuc=messagebox.askyesno("Çıkış Yap","Emin misiniz?")
    if sonuc:
        pencere.destroy()


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
    print(values[selected_value])


pencere = Tk()
pencere.title("Otel Rezervasyon")


frame_resim = Frame(pencere)
o0=PhotoImage(name="Temp",file="icons/temp.gif")
o1=PhotoImage(name="Bodrum",file="icons/bodrum.gif")
o2=PhotoImage(name="Çeşme",file="icons/çeşme.gif")
o3=PhotoImage(name="Marmaris",file="icons/marmaris.gif")
resim = Label(frame_resim,image=o0)
resim.pack()

i=0;

frame_secim =Frame(pencere)
label_soyad=Label(frame_secim,text="Ad:").grid(column=0,row=i)
text_ad=Text(frame_secim,width=15,height=1).grid(column=1,row=i,pady=5)
i+=1
label_soyad=Label(frame_secim,text="Soyad:").grid(column=0,row=i)
text_soyad=Text(frame_secim,width=15,height=1).grid(column=1,row=i,pady=5)
i+=1
label_adres=Label(frame_secim,text="Adres:").grid(column=0,row=i)
text_adres=Text(frame_secim,width=15,height=1).grid(column=1,row=i,pady=5)


rb = IntVar()
rb_buttons = [Radiobutton(frame_secim, text="Bodrum", variable=rb, value=5, command=resimDegis),
              Radiobutton(frame_secim, text="Çeşme", variable=rb, value=3, command=resimDegis),
              Radiobutton(frame_secim, text="Marmaris", variable=rb, value=1, command=resimDegis)]

for i, button in enumerate(rb_buttons):
    button.grid(column=0,row=i+3,columnspan=2)

i+=4
values = {"Seçiniz": -1, "Family": 0, "Deluxe": 1,"King Suit": 2}
cmb=Combobox(frame_secim, values=list(values.keys()),state="readonly")
cmb.current(0)


cmb.bind("<<ComboboxSelected>>", on_select)
cmb.grid(column=0,row=i,pady=5,padx=10)
icon=PhotoImage(file="icons/iseçiniz.png")
ico = Label(frame_secim,image=icon)
ico.grid(column=1,row=i,pady=5)


i+=1
label_adres=Label(frame_secim,text="Yetişkin sayısı:").grid(column=0,row=i)
text_adres=Text(frame_secim,width=15,height=1).grid(column=1,row=i,pady=5)
i+=1
label_adres=Label(frame_secim,text="Çocuk sayısı:").grid(column=0,row=i)
text_adres=Text(frame_secim,width=15,height=1).grid(column=1,row=i,pady=5)
i+=1
label_adres=Label(frame_secim,text="Kaç gece kalacaksınız?:").grid(column=0,row=i)
text_adres=Text(frame_secim,width=15,height=1).grid(column=1,row=i,pady=5)


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












'''rb=IntVar()
rb1=Radiobutton(frame_secim,text="Bodrum",variable=rb,value=5,command=resimDegis).grid(column=0,row=3,columnspan=2,sticky="W")
rb2=Radiobutton(frame_secim,text="Çeşme",variable=rb,value=3,command=resimDegis).grid(column=0,row=4,columnspan=2,sticky="W")
rb3=Radiobutton(frame_secim,text="Marmaris",variable=rb,value=1,command=resimDegis).grid(column=0,row=5,columnspan=2,sticky="W")
'''
'''
for i, button in enumerate(rb):
    button.grid(column=0,row=i+3,columnspan=2,sticky="W")
'''
'''
values = {"Seçiniz": -1, "Family": 0, "Deluxe": 1,"King Suit": 2}
cmb=Combobox(frame_secim, values=list(values.keys()),state="readonly")
cmb.current(0)
def on_select(event):
    print(values[cmb.get()])
cmb.bind("<<ComboboxSelected>>", on_select)
cmb.grid(column=0,row=6,columnspan=2)

'''



'''
class ImageCombobox(Combobox):
    def __init__(self, master=None, **kw):
        super().__init__(master, **kw)
        self.icons = {}

    def insert(self, index, item, icon=None):
        self.icons[item] = icon
        super().insert(index, item)

    def set(self, item):
        super().set(item)
        self.config(image=self.icons.get(item))

values = {"Seçiniz": -1, "Family": 0, "Deluxe": 1,"King Suit": 2}
cmb = ImageCombobox(frame_secim, values=list(values.keys()), state="readonly")
cmb.current(0)

cmb.insert(0, 'Seçiniz', PhotoImage(file=''))
cmb.insert(1, 'Family', PhotoImage(file='icons/family.png'))
cmb.insert(2, 'Deluxe', PhotoImage(file='icons/deluxe.png'))
cmb.insert(3, 'King Suit', PhotoImage(file='icons/kingsuit.png'))

def on_select(event):
    print(values[cmb.get()])

cmb.bind("<<ComboboxSelected>>", on_select)
cmb.grid(column=0,row=6,columnspan=2)
'''