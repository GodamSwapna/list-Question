r=0
while r<=4:
    c=0
    while c<=4:
        if ((c==0) and (r!=1 and r!=3)) or ((c==1) and (r!=0 and r!=2 and r!=4)) or((c==2) and (r!=0 and r!=1 and r!=3)) or ((c==3) and (r!=0 and r!=1 and r!=2 and r!=4)) or((c==4) and (r!=0 and r!=1 and r!=2 and r!=3)):
            print("1",end=" ")
        elif ((r==1) and (c!=1 and c!=2 and c!=3 and c!=4)) or ((r==2) and (c!=0 and c!=2 and c!=3 and c!=4)) or((r==3) and (c!=1 and c!=3 and c!=4)) or ((r==4) and (c!=0 and c!=2 and c!=4)):
            print("0",end=" ")
        c+=1
    print()
    r+=1     