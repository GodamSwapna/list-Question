i=5
m=1
while i>0:
    j=0
    k=5
    while j<i:
        print(k,end="")
        j+=1
        k-=1
    l=0
    while l<i:
        print(l+m,end="")
        l+=1
    print()
    i-=1
    m+=1