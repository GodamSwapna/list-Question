n=int(input("enter a number:"))
num=n
sum=0
while n>0:
    i=1
    fact=1
    rem=n%10
    while i<=rem:
        fact=fact*i
        i=i+1
    sum=sum+fact
    n=n//10
if sum==num:
    print("Given number is a strong number")
else:
    print("given number is not strong number")
    

