r=0
while r<=7:
    c=0
    while c<=4:
        if (c==0) or (c==4) or ((r==2) and (c!=2)) or((r==3) and (c!=1 and c!=3)):
            print("*",end=" ")
        else:
            print(end="  ")
        c+=1
    print()
    r+=1