print("Welcome to Treasure Island Your mission is to find the treasure")
#0 for left 1 for right
choice1=int(input("Enter Your Choice Left(0) or Right(1)?"))
if choice1 != 0:
    print("Fall into a hole.Game Over.")
else:
    #wait =0 swim=1
    choice2 = int(input("Enter Your Choice Wait(0) or Swim(1)?"))
    if choice2 !=0:
        print("Attacked by trout. Game Over.")
    else:
        #Red=0,Yellow=1,Blue=2,or anything=3
        choice3=int(input("Which door? Red(0) or Yellow(1) or Blue(2) or anything else(3)"))
        if choice3==0:
            print("Burned by fire. Game Over")
        elif choice3==1:
            print("You Win!")
        elif choice3==2:
            print("Eaten by beasts. Game Over.")
        else:
            print("Game Over")




