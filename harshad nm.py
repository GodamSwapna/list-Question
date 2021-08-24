num=int(input("enter any number:"))
rem=0
sum=0
n=num
while num>0:
    rem=num%10
    sum=rem+sum
    num=num//10
if n%sum==0:
    print(n,"is a harshad number")
else:
    print(n,"is not harshad number")