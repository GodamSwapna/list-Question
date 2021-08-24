# i=1
# str="godamswapna"
# while i<=len(str):
#     if str[i]=='m' or str[i]=='p':
#         i+=1
#         continue
#     print('current latter:',str[i])
#     i+=1



i=1
while i<=5:
    if i%2==0:
        j=0
        while j<=i:
            print(i+j,end="")
            j+=1
    else:
        j=1
        while j<=i:
            print(i-j,end="")
            j+=1
    print()
    i+=1
# i=5
# while i>0:
#     j=1
#     k=1
#     while j<=i:
#         print()
#         j+=1
#         k+=1
#     i+=1



