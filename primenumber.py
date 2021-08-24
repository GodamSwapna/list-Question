n=int(input("enter a number:"))
counter=0
i=1
while i<=n:
    if n%i==0:
        counter=counter+n
        print(counter)
    i=i+1