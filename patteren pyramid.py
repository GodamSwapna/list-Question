n=int(input("enter a number:"))
r=0
while r<n:
    s=n-r-1
    while s>0:
        print(end=" ")
        s-=1
    st=r+1
    while st>0:
        print("*",end="")
        st=st-1
    print()
    r+=1

# n=int(input("enter a number:"))
# r=0
# while r<=n:
#     s=r
#     while s>0:
#         print("",end="")
#         s-=1
#     st=1
#     while st<=n:
#         print("*",end="")
#         st+=1
#     print()
#     r+=1