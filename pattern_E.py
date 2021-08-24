r=0
while r<=6:
    c=0
    while c<=4:
        if (c==0) or(r==0) or (r==6) or((r==3) and(c!=4)):
            print("*",end="")
        else:
            print(end="")
        c+=1
    print()
    r+=1