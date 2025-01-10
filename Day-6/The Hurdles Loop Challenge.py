//In This Challenge the flag is at a specific position , the robot needs to reach it ,doing the same repeared steps , which can be organised with functions and for loop without rewriting the same code
def turn_right():
    turn_left()
    turn_left()
    turn_left()
def movement():
    
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
    
for i in range(0,6):
    movement()

         
    
