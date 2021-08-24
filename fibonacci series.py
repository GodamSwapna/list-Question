n= int(input("Enter the terms "))
a = 0  
b = 1  
count = 0  
if (n<= 0):  
    print("Please enter a valid integer")  
elif (n== 1):  
    print("Fibonacci sequence upto",n)  
    print(a)  
else:  
    print("Fibonacci sequence:")  
    while (count < n) :  
        print(a, end = ' ')  
        c = a + b   
        a = b  
        b = c  
        count += 1