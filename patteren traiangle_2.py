r=0
while r<=5:
    c=0
    while c<=5:
        if (c==0) or ((r==1) and (c!=1 and c!=2 and c!=3 and c!=5)) or ((r==2) and (c!=1 and c!=2 and c!=4 and c!=5)) or ((r==3) and (c!=1 and c!=3 and c!=4 and c!=5)) or((r==4) and (c!=2 and c!=3 and c!=4 and c!=5)) or((r==5) and (c!=1 and c!=2 and c!=)):
            print("*",end="")
        else:
            print(end="")and 
        c+=1
    print()
    r+=1