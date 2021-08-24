i=1
while i<=500:
    j=1
    sum=0
    while j<i:
        if i%j==0:
           sum=sum+j
        j=j+1
    if i==sum:
        print(i)
    i=i+1
