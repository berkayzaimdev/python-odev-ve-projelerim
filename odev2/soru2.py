Liste=[1,2,3,3,4,6,8,9,8,1,2,5,4,3]
length=0
for i in Liste:#len() kullanmadan listenin uzunluğunu bulduk
    length+=1
print(Liste)
for i in range(length):
    if Liste[i] is not None:
        count=1
        for j in range(i,length):
            if Liste[i] is Liste[j] and i is not j:
                Liste[j]=None#birden fazla olan değer varsa o indise null atadık
                count+=1
        if count != 1:
            print("\nSilmeden önce",Liste[i],"elemanından",count,"adet bulunuyordu.")
            print(Liste)
Liste = [x for x in Liste if x is not None] #list comprehension yaptık ve null değerleri listeden attık
print("\nListenin son hali =",Liste)
