n=int(input("enter a number:"))
sum=0
i=1
while i<n:
    if n%i==0:
        sum=sum+i
    i=i+1
if n==sum:
    print(n,"is perfect number")
else:
    print(n,"is not perfect number")