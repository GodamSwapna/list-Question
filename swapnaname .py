input=input("enter you are name:")
name=input.split()
print(name)
i=0
str1=""
while i<len(name):
    if name[i]==name[0]:
        str1+=name[i][0]
    else:
        str1=str1+"."+name[i]
    i+=1
print(str1)