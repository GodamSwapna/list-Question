n=[23,14,56,12,19,9,15,25,31,42,43]
i=0
e_s=0
o_s=0
while i<len(n):
    if n[i]%2==0:
        
        e_s=e_s+n[i]
    else:
        o_s=o_s+n[i]
    i+=1
print(e_s,"is a even number")
print(o_s,"is a odd number")  