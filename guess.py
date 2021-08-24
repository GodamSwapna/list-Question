number=int(input("enter a number:"))
i=1
while i<=5:
    n=int(input("enter you are guessing number45 number:"))
    i+=1
    if n>number:
        print("you are guessing number greater than num")
    elif n<number:
        print("you are guessing number less than num")
    elif n==number:
        print("your answer is crrect")
        print("thankyou")
    elif i==5:
        print("sorry you are choice is over plseas stop ")
        break
print("you are choice is over")
                


