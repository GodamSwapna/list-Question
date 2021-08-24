r=0
while r<=5:
    c=0
    while c<=10:
        if ((c==0 or c==10) and (r!=0 and r!=1 and r!=2 and r!=3 and r!=4)) or ((c==1 or c==9) and (r!=0 and r!=1 and r!=2 and r!=3 and c==3)) or ((c==3 or c==7) and (r!=0 and r!=1 and r!=3 and r!=5)) or((c==4 or c==6) and (r!=0 and r!=2 and r!=4)) or ((c==5) and (r!=1 and r!=3 and r!=5)):
            print("*",end=" ")
        else:
            print(end="  ")
        c+=1
    print()
    r+=1