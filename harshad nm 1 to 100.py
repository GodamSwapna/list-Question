i=1
while i<=200:
    num=i
    sum=0
    while num>0:
        rem=num%10
        sum=sum+rem
        num=num//10
    if i%sum==0:
        print(i,"is harshad number")
    i=i+1