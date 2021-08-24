s="the quick brown fox jumped over the lazy dog. the dog slept over the verandah."
sb="over"
r="on"
n=s.split()
i=0
ns=[]
while i<len(n):
    if n[i]!=sb:
        ns.append(n[i])
    i+=1
ns=s.replace("over","on")
print(ns)