liste = []
x = int(input("Bir sayi giriniz."))
liste.append(x)
while len(liste) < 10:
    x = int(input("Bir sayi giriniz."))
    if x > liste[len(liste)-1]:
        liste.append(x)
liste.reverse()
print("Listenin ters cevrilmis hali =", liste)
