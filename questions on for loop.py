for i in range(5):
    print(i)

for i in (1,2,3,4):
    print(i)


print("*3")
for i in (2,3,4):
    print("i")
print("*4")
for i in (4,3,2,1,0):
    print(i, end=" ")

print("*5")
for i in range(10):
    if(i%2!=0):
        print("Hello",i)

print("*6")
for i in range(10,2,-2):
    print(i, "Hello")

print("*7")
str = "Python Output based Questions"
word=str.split()
for i in word:
    print(i)

print("*8")
for i in range(7,10):
    print("Python Output based Questions")
print("Python Output based Questions")
print("*9")
for i in range(7,-2,-9):
    for j in range(i):
        print(j)
print("*10")
i="9"
for k in i:
    print(k)
print("*11")
for i in range(1,8):
    print(i)
    i+=2
print("*12")
for i in range(4,7):
    i=i+3
    print("Hello")
print("*13")
for i in range(4,7):
    i=i+3
    print("Hello",i) 
# i=65
# while i<=70:
#     j=i
#     while j<=70:
#         print(chr(j),end="")
#         j+=1
#     print()
#     i+=1  
print("*14")
i=4
while(i<10):
    i=i+3
    print(i)
print("*15")
for i in range(20):
    if i//4==0:
        print(i)
print("*16")
x=1234
while x%10:
    x=x//10
    print(x)
print("*17")
for i in 1,2,3:
    print(i*i)
print("*18")
for i in 2,4,6:
    print("H"*i)
print("*19")
p=10
q=20
p=p*q//4
q=p+q**3
print(p,q)
print("*20")
n=11
for i in range(2,n//2):
    if n%i!=0:
        print("Python Output based Questions")
        break
    else:
        print("Bye")
print("*21")

n=20
for i in range(2,n//4):
    if n%i==0:
        print("Python Output based Questions")
    else:
        print("Bye")
print("*22")
for i in "123":
    print(i)
print("*23")
for i in [10,20,30]:
    print("Hello",i)
print("*24")
x=2
for i in range(x**2,x,-1):
    print(x)
print("*25")

x=10
for i in range(x):
    if x==5:
        break
        print("H")
print(x)
x=6
for i in range(x):
    if x==5:
        break
    print("H")
print(x)



















