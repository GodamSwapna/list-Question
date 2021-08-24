n1=int(input("enter a number:"))
n2=int(input("enter a number:"))
if n1>n2:
    n=n1-n2
else:
    n=n2-n1
while True:
    if n1%n==0 and n2%n==0:
        print(n)
        break
    n=n+1