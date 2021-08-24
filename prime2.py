nbr=int(input("enter a number:"))
i=1
counter=0
while i<=nbr:
    if nbr%i==0:
        counter=counter+1
    i=i+1
if counter==2:
    print(" it is a prime number")
else:
    print("not prime number")

print("program finish")