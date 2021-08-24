print("well come to KBC program") 
q=[
    "How many continents are there?",              # pehla question
    "What is the capital of India?",            # doosra question
    "NG mei kaun se course padhaya jaata hai?"    # teesra question
]
o=[
    #pehle question ke liye options
    ["Four", "Nine", "Seven", "Eight"],
    #second question ke liye options
    ["Chandigarh", "Bhopal", "Chennai", "Delhi"],
    #third question ke liye options
    ["Software Engineering", "Counseling", "Tourism", "Agriculture"]
]
fifty=[["four","seven"],["bhopal","delhi"],["software engineering","tourism"]]
s=[3, 4, 1] 
a=[2,2,1]
i=0
c=0
while i<len(q):
    print("this is your quetion")
    print(i+1,q[i])
    print("select you are option")
    j=0
    while j<=len(o):
        print(j+1,o[i][j])
        j=j+1
    n=int(input("enter you are option:"))
    if n==s[i]:
        print("congration...")
    elif n==5050:
        k=0
        while k<len(fifty[i]):
            print(k+1,fifty[i][k])
            k+=1
        n1=int(input("enter you are option"))
        if n1==a[i]:
            print("congratulation...")
        else:
            print("you are answer is wrong")
            break
    else:
        print("you have one choice")
        n3=int(input("enter you are option:"))
        if n3==s[i]:
            print("congratulation...")
        else:
            print("you are choice is over")
            break
else:            
        print("you are answer is wrong")
    print()
    i+=1
print("go to the next quetion")