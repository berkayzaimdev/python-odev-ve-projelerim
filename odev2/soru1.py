fiyat={"muz":4,"elma":2,"portakal":1.5,"armut":3}
stok={"muz":6,"elma":8,"portakal":32,"armut":15}
for i in range(1,4):
    print(i,".musteri\n---------",sep='')
    secim='E'
    tutar=0
    while secim=='E' and stok: #tüm meyveler tükendiğinde döngüden çık
        print("\nGüncel stok-fiyat bilgisi")
        for x,y in stok.items(): #.items ile hem key'e hem value'ya foreach ile eriştik x=key y=value
            print("{}:{} tane-{} TL".format(x,y,fiyat[x]),end='\n',sep='')
        meyve=input("\nLütfen almak istediğiniz meyveyi seçin:")
        if meyve not in stok:
            print("Lütfen geçerli bir meyve adı girin.")
            continue
        adet=int(input("Lütfen kaç tane almak istediğini seçin:"))
        if adet>stok[meyve]:
            print("Seçtiğiniz meyvede o adette yeterli stok bulunmamaktadır.")
        else:
            tutar+=adet*fiyat[meyve]
            print("Tutar =",adet*fiyat[meyve],"TL")
            stok[meyve]-=adet
            if stok[meyve]==0:
                print(meyve,"stoğu tükenmiştir.")
                del(stok[meyve],fiyat[meyve]) #Seçilen üründe stok biterse ürünü seçim listesinden kaldır
        secim=input("Siparişinizi sonlandırmak ya da devam etmek için bir seçim yapın = E/H  ")
    print("Ödenecek miktar =",tutar,"TL\n\n\n")
    if not stok:
        print("\nTüm meyvelerin stoğu tükenmiştir.")
        break