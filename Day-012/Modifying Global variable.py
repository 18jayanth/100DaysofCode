a=12
'''
def modify():
    a+=10
    #print(a) local variable 'a' referenced before assignment
modify()
print(a) #10

We cannot modify or use global variables directly inside our function
'''
def modify():
    global a
    a+=10 #22
    print(a)
modify()
print(a) #22
'''we can use global instead to modify'''


#we can modify 
a=10
def modify(b):
    print("Inside Function",a) #10
    return b+1
a=modify(a) #Inside Function 10
print("Outside Function",a) #Outside Function 11
a=modify(a) #Inside Function 11
print("Outside Function",a) #Outside Function 12
a=modify(a) #Inside Function 12
print("Outside Function",a) #Outside Function 13
a=modify(a) #Inside Function 13

print("Outside Function",a) #Outside Function 14

