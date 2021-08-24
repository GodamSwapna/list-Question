i=1
while i<=500:
    num=i
    sum=0
    while num>0:
        j=1
        fact=1
        rem=num%10
        while j<=rem:
            fact=fact*j
            j=j+1
        sum=sum+fact
        num=num//10
    if sum==i:
        print(i)
    i=i+1       

    


