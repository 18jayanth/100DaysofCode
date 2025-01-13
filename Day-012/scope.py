'''There is no block scope in Python
Which means we can still use variables that are declared in ifs and loops
'''

'''But it gives a warning because, if 'if' fails then print wont execute
so better declare and initialize before 'if' or'for' or 'while' '''


'''

age=11
if age>10:
    b=2
print(b) 2


But Python has Local and Global scope,
 we cant use variables
declared outside function'''


#but we cannot use global variables anywhere

a=10
def age():
    if age>10:
        b=2
#print(b)  #name 'b' is not defined
print(a) #10




