import random

liste = []
toplam = 0
for i in range(0,20):
    liste.append(random.randint(1,25))
    toplam += liste[i]
    print("Eklenen eleman=",liste[i]," Liste eleman sayisi=",i+1," Toplam=",toplam,sep='',end='\n')
    if toplam >= 100:
        print("\nListenin ",i + 1,".elemani olan ",liste[i]," eklendikten sonra, toplam 100'u gecmistir.",sep='')
        break
