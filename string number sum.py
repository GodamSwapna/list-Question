i=0
sum=0
while i<2:
    input1=input("enter you numeral in words('one/two/three'):")
    num=input1.split()
    j=0
    str1=""
    while j<len(num):
        if num[j]=="zero":
            str1+=str(0)
        elif num[j]=="one":
            str1+=str(1)
        elif num[j]=="two":
            str1+=str(2)
        elif num[j]=="three":
            str1+=str(3)
        elif num[j]=="four":
            str1+=str(4)
        elif num[j]=="five":
            str1+=str(5)
        elif num[j]=="six":
            str1+=str(6)
        elif num[j]=="seven":
            str1+=str(7)
        elif num[j]=="eight":
            str1+=str(8)
        elif num[j]=="nine":
            str1+=str(9)
        j+=1
    sum+=int(str1)
    i+=1
print(sum)