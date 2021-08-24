s = "the quick brown fox jumped over the lazy dog. the dog slept over the verandah."
sb="over"
n=s.split()
i=0
sum="  "
while i<len(n):
    if n[i]!=sb:
        sum=sum+n[i]
    i+=1
print(sum,end=" ")
    
