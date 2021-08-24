r=0
while r<=7:
    c=0
    while c<=4:
        if (c==3) or (r==0):
            print("*",end="  ")
        else:
            print(end="  ")
        c+=1
    print()
    r+=1