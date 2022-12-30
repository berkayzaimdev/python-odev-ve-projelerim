yazi=["Ahmet","altı","yaşında","zeynep","dört","yaşında","esra","iki","yaşında","ayşe","bir","yaşında"]
rakam={"bir":1,"iki":2,"dört":4,"altı":6}
for x in yazi:
    print(rakam[x] if x in rakam.keys() else x,end=' ')