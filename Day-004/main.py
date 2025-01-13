#Rock Paper Scissors 0 For Rock 1 for Paper 2 For Scissors
import random
while True:
    ch_your=int(input('Enter Your Choice:'))
    ch_comp=random.randint(0,2)

    if((ch_your==0 and ch_comp==0) or (ch_your==1 and ch_comp==1) or (ch_your==2 and ch_comp==2) ):
        print("Draw")
        print(ch_comp)
        print("\N{slightly smiling face}")

    elif ch_your==0 and ch_comp==1:
        print("You lose")
        print(ch_comp)
        print("\N{winking face}")

    elif ch_your==0 and ch_comp==2:
        print("You Win")
        print(ch_comp)
        print("\N{grinning face}")
        break

    elif ch_your==1 and ch_comp==0:
        print("You Win")
        print(ch_comp)
        print("\N{grinning face}")
        break

    elif ch_your==1 and ch_comp==2:
        print("You loose")
        print(ch_comp)
        print("\N{winking face}")

    elif ch_your==2 and ch_comp==0:
        print("You loose")
        print(ch_comp)
        print("\N{winking face}")


    elif ch_your==2 and ch_comp==1:
        print("You Win")
        print(ch_comp)
        print("\N{grinning face}")
        break
    else:
        print("Its an invalid choice you idiot")
        # grinning face
        print("\N{grinning face}")
        # slightly smiling face
        print("\N{slightly smiling face}")
        # winking face
        print("\N{winking face}")