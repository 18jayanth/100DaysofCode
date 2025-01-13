import random
from logo import logo
print("Welcome to Number Guessing Game!")
print(logo)


print("The Numbers are in Between 1 to 100")
print("Which level of Game do you want?? 1)easy 2)hard")
num=random.randint(1,100)
var=input()
if var=="easy":
    chances=10
    while chances!=0:
        ch=int(input("Please Enter Your Choice:"))
        if ch>num:
            print("Your num is high please decrease!!")
            chances-=1
            print("No of Chances left!",chances)
        elif ch<num:
            print("Your num is low  please increase!!")
            chances-=1
            print("No of Chances left!", chances)
        else:
            chances-=1
            print("You Won!! with chances available",chances)
            break
    else:
        print("I am Sorry,You Lost the Game!!")
if var=="hard":
    chances=5
    while chances!=0:
        ch=int(input("Please Enter Your Choice:"))
        if ch>num:
            print("Your num is high please decrease!!")
            chances-=1
            print("No of Chances left!",chances)
        elif ch<num:
            print("Your num is low  please increase!!")
            chances-=1
            print("No of Chances left!", chances)
        else:
            chances-=1
            print("You Won!! with chances available",chances)
            break
    else:
        print("I am Sorry,You Lost the Game!!")



