# n=int(input("enter a numbet:"))
# i=1
# while i<=10:
#     j=1
#     while j<=n:
#         print(i*j)
#         j+=1
#     i+=1      

num=int(input("enter a number:"))
i=1
while num>0:
    if num%2==0:
        print(num)
    n=num+i
    if n%2!=0:
        print(n)
    num-=1
    i+=1