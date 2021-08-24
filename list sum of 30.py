number = 30
n = [10, 11, 12, 13, 14, 17, 18, 19] 
i=0
N=30
while i<len(n):
    j=0
    while j<=i:
        if n[i]+n[j]==30:
            print([n[i],n[j]],end="")
        j+=1
    i+=1

