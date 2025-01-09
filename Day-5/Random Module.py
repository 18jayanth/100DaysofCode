'''
shuffle()
This method reorganizes the order of the items in a list.
It's an inbuilt method of the random module.
The syntax is random.shuffle(sequence).


choice()
This function selects a random element from a list.
The syntax is random.choice(items).
'''
import random

mylist = ["apple", "banana", "cherry"]
random.shuffle(mylist)
print(mylist)