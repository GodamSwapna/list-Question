print("enter two number to calculate HCF")
a=int(input("enter a number: "))
b=int(input("enter a b number:"))
while a%b!=0:
    rem=a%b
    a=b
    b=rem
print("hcf of",b)
