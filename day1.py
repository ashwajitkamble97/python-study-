# print('king of the pirate!!!')
#
# #####
# print('hello world')
# ###########
#
# ##### variable####
#
# name =  "ashwajit" #string
# n=313  #interger
# f= 3.56 # float
# is_lalid = True # boolean
# list = [1,2,'ace', 3.5] # list or array
#
# a,b,c = 2,48,'king' #multiple assinments
#
# print(a);
# print(list)
# print(a+b-n)
# ######## input####
# name = input("enter you name:-")
# print("hello", name)
#
# ######### conditionlan statement#######
# x= int(input("enter Any number:-"));
#
# if x>10:
#     print("entered number is greter than 10")
# elif x==10:
#     print("entered number is exactly 10")
# else:
#     print("entered number is smaller than 10")



##################################################################################

#########LOOOPS#########
# i=0
# while i<=10:
#     print(i)
#     i+=1

#####for loop

# for n in range(1,100):
#     print(n)
#
# Looping over collections
# fruits = ["apple", "banana"]
# for fruit in fruits:
#     print(fruit)

#####
# # Break and continue
# for num in range(1, 10):
#     if num == 5:
#         break  # Exit the loop
#     if num % 2 == 0:
#         continue  # Skip even numbers
#     print(num)

#####functions
# for num in range(1, 10):
#     if num == 5:
#         break  # Exit the loop
#     if num % 2 == 0:
#         continue  # Skip even numbers
#     print(num)

# def greet(name):
#     return f"hello, {name}"
#
# print(greet("ace"))
a = int(input("enter any number 1:-"))
b = int(input("enter any number 2:-"))

def sum(a,b):
    return f"addition:-{a+b}"
print(sum(a,b))

###########################
#lists
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")  # Add item
fruits.pop()             # Remove last item
print(fruits[0])         # Access first item

#Dictionaries
person = {"name": "Alice", "age": 25}
print(person["name"])  # Access value
person["age"] = 26     # Update value

#####
##tuples
coordinates = (10, 20)
print(coordinates[0])  # Access first value

#sets

unique_numbers = {1, 2, 3, 3}
unique_numbers.add(4)  # Add item
unique_numbers.remove(2)  # Remove item

#7. Classes and Objects
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hi, I'm {self.name}!"

# Creating an object
p = Person("Alice", 30)
print(p.greet())

##################
#exception handling

try:
    result = 10 / 0
except ZeroDivisionError as e:
    print("Error:", e)
else:
    print("Division successful")
finally:
    print("Execution complete")


###################################
#file operations

# Writing to a file
with open("example.txt", "w") as file:
    file.write("Hello, file!")

# Reading from a file
with open("example.txt", "r") as file:
    content = file.read()
    print(content)

#### python modules

# Importing a module
import math
print(math.sqrt(16))  # Square root

# Import specific function
from math import pow
print(pow(2, 3))  # 2^3

# Custom modules
# Save `my_module.py` with a function, then:
import my_module
my_module.some_function()


##############################
#list comprihensations
# Create a list of squares
squares = [x**2 for x in range(10)]

######################################

#lambda functions
# Anonymous function
square = lambda x: x**2
print(square(5))

######################################
# decoretors
def decorator(func):
    def wrapper():
        print("Before function call")
        func()
        print("After function call")
    return wrapper

@decorator
def say_hello():
    print("Hello!")

say_hello()

#########
#importing libraries

import numpy as np
array = np.array([1, 2, 3])
print(array)

########################
#Basic Syntax Rules
######Indentation: Use 4 spaces for blocks.
######Comments: Use # for single-line and triple quotes for multi-line comments

# This is a comment
"""
This is a
multi-line comment
"""
##Docstrings: For documentation within functions/classes:
def greet():
    """This function greets the user."""
    print("Hello!")

##############################################################


