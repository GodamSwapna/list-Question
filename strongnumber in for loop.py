n=int(input("enter a number:"))
sum=0
num=n
while n>0:
    fact=1
    rem=num%10
    for i in range(1,rem+1):
        fact=fact*i
    print("factorial%d=%d"%(rem,fact))
    sum=sum+fact
    num=num//10
print("sum of factorial%d=%d"%(sum,num))
if sum==num:
    print("given number is strong number")    
else:
    print("given number is not strong number")