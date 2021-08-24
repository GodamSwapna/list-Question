n=[50,40,23,70,56,12,5,10,7]
i=0
max=0
s_m=0
third_m=0
while i<len(n):
    if n[i]>max:
        s_m=max
        max=n[i]
    elif n[i]>s_m:
        third_m=s_m
        s_m=n[i]
    elif n[i]>third_m:
        third_m=n[i]
    i+=1
print(third_m)