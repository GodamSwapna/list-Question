n=int(input("enter a number:"))
rev=0
num=n
while n!=0:
    rem=n%10
    rev=(rev*10)+rem
    n=n//10
print("you are input is",rev)
if num==rev:
    print(rev,"is polynrom")
else:
    print(rev,"is not polyndrom")