n=input("enter you are name:")
rev=" "
i=len(n)-1
while i>=0:
    rev=rev+n[i]
    i-=1
print(rev)