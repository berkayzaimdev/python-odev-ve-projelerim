for i in range(100,1000):
    birler=i%10
    onlar=int(i/10)
    yuzler=int(onlar/10)
    onlar %= 10
    if yuzler + birler > onlar:
        print(i)