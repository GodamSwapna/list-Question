n=int(input("enter a number:"))
i=1
count=0
while n>=0:
    j=2
    c=0
    # sum=0
    while j<=i:
        if i%j==0:
            c=c+1
            # sum=sum+i
        j=j+1
    if c==1:
        # print(i,"prime number")
        if count==n:
            print(i)
        count+=1
        # break
    i=i+1