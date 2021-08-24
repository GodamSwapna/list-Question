i=1
while i<=100:
    num=i
    rev=0
    while num>0:
        rem=num%10
        rev=rev*10+rem
        num=num//10
    if i==rev:
        print(rev,"is palindrome number")
    i=i+1