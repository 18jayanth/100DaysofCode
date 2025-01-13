# Random Module generates random Numbers
import random
import my_module
'''
#Random Numbers For Int
random_int=random.randint(1,10)
print(random_int) #1<=x<=10
# We can use Our own modules
print(my_module.myfavnum) # 3.14


#Random Numbers For Float
random_between_0and1=random.random()
print(random_between_0and1) # 0<=x<1
random_between_0and1=random.random()*10
random_float=random.#uniform(1,10)
print(random_float) 1<=x<=10
'''
choice=random.randint(0,1)
if choice==0:
    print("Head")
else:
    print("Tails")
