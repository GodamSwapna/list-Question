r=0
while r<=5:
    s=6-r-1
    while s>0:
        print("",end="")
        s-=1
    k=65
    num=r+1
    while num>0:
        print(chr(k),end="")
        num-=1
        k+=1
    print()
    r+=1
    l=65
    nm=r+1
    while nm>0:
        print(chr(l+r),end="")
        nm-=1
        l=l-1
    print()
    r+=1