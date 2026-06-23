# Assign multiple values to multiple variables
a,b,c = 4,5.50,"Hello, World!"
print(a)
print(b)
print(c)

# assign single value to multiple variables
a = b = c = 2.4
print(a)
print(b)
print(c)

#how memory is allocated to variables
a=10
a=20
print(a)
#memory is allocated to variable a only once, but the value of a is changed from 10 to 20.

#garbage collection in python
#Python has an inbuilt garbage collector, which recycles all the unused memory to make it available for heap storage area. 
#The garbage collector runs during program execution and is triggered when an object's reference count reaches zero. 
#This means that when there are no references to an object, it becomes eligible for garbage collection, and the memory occupied by that object can be reclaimed.