s="the quick brown fox jumped over the lazy dog. the dog slept over the verandah."
sb="over"
n=s.split()
i=0
ms=[]
st=" "
while i<len(n):
    if n[i]!=sb:
        ms.append(n[i])
    i+=1
st=st.join(ms)
print(st)

