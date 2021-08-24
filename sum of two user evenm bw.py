n1=int(input("enter a number:"))
n2=int(input("enter a number:"))
i=n1
sum=0
while i<=n2:
    if i%2==0:
        sum=sum+i
    i=i+1
print(sum)