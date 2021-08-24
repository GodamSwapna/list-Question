r=0
while r<=6:
    c=0
    while c<=4:
        if (c==0) or ((r==3 or r==0) and (c!=4)) or((c==4) and (r!=0 and r!=3 and r!=4 and r!=5 and r!=6)) or ((r==4) and (c!=1 and c!=3 and c!=4)) or ((r==5) and (c!=1 and c!=2 and c!=4)) or ((r==6) and (c!=1 and c!=2 and c!=3)):
            print("*",end=" ")
        else:
            print(end="  ")
        c+=1
    print()
    r+=1