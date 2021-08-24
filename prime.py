i=2
while i<=100:
    j=1
    cf=0
    sum=0
    while j<=i:
        if i%j==0:
            cf=cf+1
            sum=sum+i
        j=j+1
    if cf==2:
        print(i,"prime number")
    i=i+1        
print(sum)   
    