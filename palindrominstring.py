chr=input("enter a character:")
output=""
i=len(chr)-1
while i>=0:
    output=output+chr[i]
    i=i-1
if chr==output:
    print(chr," is palindrom")
else:
    print(chr," is not palindrom")