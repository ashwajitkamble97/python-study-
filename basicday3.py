# 6. Dictionaries
#     51. Write a program to create a dictionary and print its keys and values.
# my_direct = {
#     "name"    :"Ashwajit",
#     "age"     : 26,
#     "address" : "Nagpur",
# }

# print("keys: ")
# for key in my_direct.keys():
#     print(key)

# print("values : ")
# for value in my_direct.values():
#     print(value)

# print("Boths : ")
# for key,value in my_direct.items():
#     print(f"{key}: {value}")
#===============================================================================
#     52. Write a program to add an item to a dictionary.
# my_direct = {
#     "name"    :"Ashwajit",
#     "age"     : 26,
#     "address" : "Nagpur",
# }

# print(f"origionl dictionary: {my_direct}")
# my_direct['contact'] = 9403904296

# print(f"Updated dictionary: {my_direct}")

#===============================================================================
#     53. Write a program to update the value of a key in a dictionary.
# my_direct = {
#     "name"    :"Ashwajit",
#     "age"     : 26,
#     "address" : "Nagpur",
# }

# print(f"origionl dictionary: {my_direct}")
# my_direct['address'] = "United Town of maharashtra"

# print(f"Updated dictionary: {my_direct}")
#===============================================================================

#     54. Write a program to check if a key exists in a dictionary.
# my_direct = {
#     "name"    :"Ashwajit",
#     "age"     : 26,
#     "address" : "Nagpur",
# }
# if "age" in my_direct:
#     print("Key exists")
# else:
#     print("Key does not exist")
#===============================================================================

#     55. Write a program to merge two dictionaries.
# my_direct = {
#     "name"    :"Ashwajit",
#     "age"     : 26,
#     "address" : "Nagpur",
# }

# my_direct2 = {
#     "car"       :"lykan Hyper sports",
#     "color"     : "matt red",
# }
# new_direct = my_direct.copy()
# new_direct.update(my_direct2)
# print(f"Marged directory : {new_direct}")
#===============================================================================

#     56. Write a program to find the sum of all values in a dictionary.
# my_derect = {
#     "ashwajit"  : 5.9 ,
#     "rohit"     : 9.8 ,
#     "pratik"    : 1.6 ,
#     "rupam"     : 1.1 ,
#     "sachin"    : 1.5 ,
# }
# total = sum(my_derect.values())
# print(f"Total wealth : ${total} trillion")

#===============================================================================

#     57. Write a program to sort a dictionary by its keys.
# my_derect = {
#     "ashwajit"  : 5.9 ,
#     "rohit"     : 9.8 ,
#     "pratik"    : 1.6 ,
#     "rupam"     : 1.1 ,
#     "sachin"    : 1.5 ,
# }
# sorted_dict = {key: my_derect[key] for key in sorted(my_derect.keys())}
# print(f"sorted directory : {sorted_dict}")
#===============================================================================

#     58. Write a program to remove a key-value pair from a dictionary.
# my_derect = {
#     "ashwajit"  : 5.9 ,
#     "rohit"     : 9.8 ,
#     "pratik"    : 1.6 ,
#     "rupam"     : 1.1 ,
#     "sachin"    : 1.5 ,
# }
# print(f"origional directory: {my_derect}")

# del(my_derect['rupam'])
# print(f"Updated directory: {my_derect}")

#===============================================================================

#     59. Write a program to invert keys and values in a dictionary.
# my_derect = {
#     "ashwajit"  : 5.9 ,
#     "rohit"     : 9.8 ,
#     "pratik"    : 1.6 ,
#     "rupam"     : 1.1 ,
#     "sachin"    : 1.5 ,
# }
# inverted_derect = {value : key for key , value in my_derect.items()}
# print(f"Inverted directory : {inverted_derect}")
#===============================================================================

#     60. Write a program to find the maximum and minimum values in a dictionary.
# my_derect = {
#     "ashwajit"  : 5.9 ,
#     "rohit"     : 9.8 ,
#     "pratik"    : 1.6 ,
#     "rupam"     : 1.1 ,
#     "sachin"    : 1.5 ,
# }
# max_val = max(my_derect.values())
# min_val = min(my_derect.values())
# print(f" mininimum wealth : {min_val}")
# print(f" Maximum wealth : {max_val}")

#===============================================================================


# 7. Tuples and Sets
#     61. Write a program to create and print a tuple.
# my_tuple = (1,2,3,"ashwajit",4,5,6)
# print(f"tuple : {my_tuple}")
#===============================================================================

#     62. Write a program to access elements of a tuple.
# my_tuple = (1,2,3,"ashwajit",4,5,6)
# print(f"tuple of 1st element : {my_tuple[0]}")
# print(f"tuple of Last element : {my_tuple[-1]}")
# print(f"tuple of 4th element : {my_tuple[3]}")
# print(f"tuple of 2nd last element : {my_tuple[-2]}")
#===============================================================================

#     63. Write a program to find the length of a tuple.
# my_tuple = (1,2,3,"ashwajit",4,5,6)
# length = len(my_tuple)
# print(f"legth of the tuple: {length}")
#===============================================================================

#     64. Write a program to find the largest and smallest elements in a tuple.
# my_tuple = (10, 45, 7, 89, "ashwajit", 56, 2.8, "ace", 5)
# numeric_values = tuple(x for x in my_tuple if isinstance(x, (int, float)))
# largest = max(numeric_values)
# smalest = min(numeric_values)
# print(f"max : {largest}")
# print(f"min : {smalest}")
#===============================================================================

#     65. Write a program to create a set and perform union, intersection, and difference operations.
# set_A = {1, 2, 3, 4, 5}
# set_B = {4, 5, 6, 7, 8}
# print(f"set A : {set_A}")
# print(f"set B : {set_B}")
# union_result  = set_A.union(set_B)
# print(f"union of set a & b : {union_result}")
# intersection_result = set_A.intersection(set_B)
# print(f"Intersection of set a & b : {intersection_result}")
# difference_result = set_A.difference(set_B)
# print(f"diffrence between set a & b : {difference_result}")
#===============================================================================

#     66. Write a program to check if an element exists in a set.
# set_A = {9,55,74,35,6,1,-4,-5}
# ele = -4
# if ele in set_A:
#     print(f"{ele} is exist")
# else:
#     print(f"{ele} is not exist")


#===============================================================================

#     67. Write a program to find the symmetric difference of two sets.
# set_A = {1, 2, 3, 4, 5}
# set_B = {4, 5, 6, 7, 8}
# result = set_A.symmetric_difference(set_B)
# print(f" symmetric diffrence between set A - set B : {result}")
#===============================================================================

#     68. Write a program to convert a list into a tuple.
# list_A = [1,5,7,"ace",-3, 9.88]
# tuple_A = tuple(list_A)
# set_A = set(list_A)
# print(f"list : {list_A}")
# print(f"tuple : {tuple_A}")
# print(f"set : {set_A}")
#===============================================================================

#     69. Write a program to count the occurrences of an element in a tuple.
# my_tuple = (10, 20, 30, 10, 40, 10, 50, 20, 10)
# count_ele = 10
# result = my_tuple.count(count_ele)
# print(f"element {count_ele} comes in tuple {result} Times")
#===============================================================================

#     70. Write a program to check if a tuple contains duplicates.
# my_tuple = (10,20,30,40,50, 80)
# my_set = set(my_tuple)
# if len(my_set) != len(my_tuple):
#     print("tuple have repeated vlues")
# else:
#     print("tuple not have repeated vlues")

#===============================================================================


# 8. File Handling
#     71. Write a program to read a file and print its contents.
# def read_file(file_name):
#     try:
#         with open(file_name,'r') as file:
#             contents = file.read()
#             print(f"content of file :{contents}")

#     except FileNotFoundError:
#         print(f"file {file_name} not found")
#     except Exception as e:
#         print(f"An error accur {e}")


# file_name = "example.txt"
# read_file(file_name)

#===============================================================================

#     72. Write a program to write data to a file.
# def write_file(file_name, data):
#     try:
#         with open(file_name,'w') as file:
#             contents = file.write(data)
#             print(f"content of file :{contents}")

#     except FileNotFoundError:
#         print(f"file {file_name} not found")
#     except Exception as e:
#         print(f"An error accur {e}")


# file_name = "example.txt"
# data = " It is not my dream to become king , its my brothers dream !"
# write_file(file_name,data)
#===============================================================================

#     73. Write a program to append data to a file.
# def append_file(file_name, data):
#     try:
#         with open(file_name,'a') as file:
#             contents = file.write(data)
#             file.write("\n")
#             print(f"content of file :{contents}")

#     except FileNotFoundError:
#         print(f"file {file_name} not found")
#     except Exception as e:
#         print(f"An error accur {e}")


# file_name = "example.txt"
# data = "Hello Everyone !"
# append_file(file_name,data)
#===============================================================================

#     74. Write a program to count the number of lines in a file.
# def count_line_in_file(file_name):
#     try:
#         with open(file_name, "r") as file:
#             count_line = sum(1 for line in file)
#         print(f"file {file_name} has {count_line} lines. ")
#     except FileExistsError:
#         print(f"file {file_name} not found")    
#     except Exception as e:
#         print(f"An error accur {e}")
# file_name = "example.txt"
# count_line_in_file(file_name)

#===============================================================================

#     75. Write a program to count the number of words in a file.
# def count_words(file_name):
#     try:
#         with open(file_name,'r') as file:
#             contents = file.read()
#             words = contents.split()
#             char_count = len(contents)
#             count_res = len(words)
#         print(f"file {file_name} have {count_res} words and {char_count} charactors")
#     except FileExistsError:
#         print(f"file {file_name} not found")    
#     except Exception as e:
#         print(f"An error accur {e}")

# file_name = "example.txt"
# count_words(file_name)

#===============================================================================

#     76. Write a program to count the number of characters in a file.
# def count_words(file_name):
#     try:
#         with open(file_name,'r') as file:
#             contents = file.read()
#             words = contents.split()
#             char_count = len(contents)
#             count_res = len(words)
#         print(f"file {file_name} have {count_res} words and {char_count} charactors")
#     except FileExistsError:
#         print(f"file {file_name} not found")    
#     except Exception as e:
#         print(f"An error accur {e}")

# file_name = "example.txt"
# count_words(file_name)
#===============================================================================

#     77. Write a program to copy the contents of one file to another.
# def copy_content(source_file,destination_file):
#     try :
#         with open(source_file,'r') as src:
#             contents = src.read()
#         with open(destination_file,'w') as dest:
#             res = dest.write(contents)
#         print(f"Contents of '{source_file}' successfully copied to '{destination_file}'.")
#     except FileNotFoundError:
#         print(f"The file '{source_file}' does not exist.")
#     except Exception as e:
#         print(f"An error occurred: {e}")
            
# source_file = "example.txt"
# destination_file = "destination.txt"
# copy_content(source_file,destination_file)

#===============================================================================

#     78. Write a program to find and replace text in a file.
# def find_and_replace(file_name, search_text, replace_text):
#     try:
#         # Open the file in read mode to read its content
#         with open(file_name, 'r') as file:
#             content = file.read()

#         # Replace the target text
#         updated_content = content.replace(search_text, replace_text)

#         # Open the file in write mode to overwrite with updated content
#         with open(file_name, 'w') as file:
#             file.write(updated_content)
        
#         print(f"Successfully replaced '{search_text}' with '{replace_text}' in '{file_name}'.")
#     except FileNotFoundError:
#         print(f"The file '{file_name}' does not exist.")
#     except Exception as e:
#         print(f"An error occurred: {e}")

# # Example usage
# file_name = 'example.txt'  # Replace with the actual file name
# search_text = 'Hello Everyone'   # Text to be replaced
# replace_text = 'Hello Everyone in the word'  # Replacement text
# find_and_replace(file_name, search_text, replace_text)

#===============================================================================

#     79. Write a program to check if a file exists.
# import os

# def check_file_exist(file_name):
#     if os.path.isfile(file_name):
#         print(f" file {file_name} is exist")
#     else:
#         print(f" file {file_name} is not exist")

# file_name = 'example.txt'
# check_file_exist(file_name)

#===============================================================================

#     80. Write a program to delete a file.
# import os
# def check_file_exist(file_name):
#     if os.path.isfile(file_name):
#         os.remove(file_name)
#         print(f" file {file_name} is deleted")
#     else:
#         print(f" file {file_name} is not exist")

# file_name = 'destination.txt'
# check_file_exist(file_name)
#===============================================================================

# 9. Functions
#     81. Write a function to calculate the factorial of a number.

# def foctorial_nub(num):
#     if num < 0:
#         res = "factorial of -ve number is not Possible"
#         return res
#     elif num == 1:
#         res = "factorial of 1 number is 1"
#         return res
#     else:
#         fact = 1
#         for i in range(1, (num+1)):
#             fact = fact * i
#         res = fact
#         return res
    
# num = int(input("Enter Number : "))
# result = foctorial_nub(num) 
# print(f" Factorial of number {num} is {result}")



#===============================================================================

#     82. Write a function to check if a number is prime.

# def is_prime(num):
#     if num < 2:
#         return False
    
#     for i in range(2, int(num ** 0.5) + 1):
#         if num % i == 0:
#             return False
#     return True

# num = int(input("Enter the number : "))

# if is_prime(num):
#     print(f"{num} is a prime number.")
# else:
#     print(f"{num} is not a prime number.")

#===============================================================================

#     83. Write a function to find the maximum of three numbers.

# def greter_num(num1,num2,num3):
#     if num1<=num2:
#         if num2<=num3:
#             res = f"{num3} is greter"
#         else:
#             res = f"{num2} is greter"
            
#     else:
#         if num1<=num3:
#             res = f"{num3} is greter"

#         else:
#             res = f"{num1} is greter"
    
#     return res


# num1 = int(input("Enter Num1: "))
# num2 = int(input("Enter Num2: "))
# num3 = int(input("Enter Num3: "))
# result = greter_num(num1,num2,num3)
# print(result)

#===============================================================================

#     84. Write a function to calculate the sum of all numbers in a list.
# def sum_of_list(res):
#     add = 0
#     for j in res:
#         add = add + j
#     return add


# a = int(input("Enter the number of elemets: "))
# res = []
# for i in range(a):
#     b = int(input(f"Enter number {i+1}: "))
#     res.append(b)

# print(f"list :{res}")
# result = sum_of_list(res)
# print(f"addition is {result}")

#===============================================================================

#     85. Write a function to reverse a string.
# def reverse_string(s):
#     reversed_str = ""
#     for char in s:
#         reversed_str = char + reversed_str 
#     return reversed_str

# input_string = input("Enter a string: ")
# reversed_string = reverse_string(input_string)
# print(f"Reversed string: {reversed_string}")

#===============================================================================

#     86. Write a function to check if a string is a palindrome.
# def is_palindrome(s):
#     for i in range(len(s) // 2):
#         if s[i] != s[-(i + 1)]:
#             return False
#     return True

# input_string = input("Enter a string: ")
# if is_palindrome(input_string):
#     print("The string is a palindrome.")
# else:
#     print("The string is not a palindrome.")

#===============================================================================

#     87. Write a function to find the GCD of two numbers.(grtetst comman diviser)

# def find_gsd(num1,num2):
#     while num2 :
#         num1 , num2 = num2 ,num1%num2
#     return num1

# num1 = int(input("enter num 1:"))
# num2 = int(input("enter num 2:"))
# print(find_gsd(num1, num2))
#===============================================================================

#     88. Write a function to calculate the power of a number.
# def find_power(a,b):
#     return(a**b)

# num1 = int(input("enter num 1:"))
# num2 = int(input("enter num 2:"))
# print(find_power(num1, num2))
#===============================================================================

#     89. Write a function to convert Celsius to Fahrenheit.
# def cel_to_fahr(a):
#     return (a *9/5) + 32 

# num1 = int(input("enter num 1:"))
# print(cel_to_fahr(num1))
#===============================================================================

#     90. Write a function to check if a number is an Armstrong number.
# def is_armstrong_number(num):
#     # Convert the number to a string to iterate over its digits
#     digits = str(num)
#     num_digits = len(digits)
#     # Calculate the sum of digits raised to the power of the number of digits
#     armstrong_sum = sum(int(digit) ** num_digits for digit in digits)
#     return armstrong_sum == num

# # Example usage
# number = 153
# if is_armstrong_number(number):
#     print(f"{number} is an Armstrong number.")
# else:
#     print(f"{number} is not an Armstrong number.")

#===============================================================================


# 10. Miscellaneous
#     91. Write a program to generate random numbers.
# import random

# print(random.randint(1, 1000))
#===============================================================================

#     92. Write a program to shuffle the elements of a list.
# import random
# arr = [1,2,3,4,5,6]
# random.shuffle(arr)
# print(arr)
#===============================================================================

#     93. Write a program to find the intersection of two arrays.
# def find_intersection(array1, array2):
#     # Use set intersection to find common elements
#     return list(set(array1) & set(array2))

# # Example usage
# array1 = [1, 2, 3, 4, 5]
# array2 = [4, 5, 6, 7, 8]

# intersection = find_intersection(array1, array2)
# print(f"Intersection of {array1} and {array2}: {intersection}")

#===============================================================================

#     94. Write a program to implement a simple banking system.
# class BankAccount:
#     def __init__(self, account_holder, balance=0):
#         self.account_holder = account_holder
#         self.balance = balance

#     def check_balance(self):
#         return f"Current balance: ${self.balance}"

#     def deposit(self, amount):
#         if amount > 0:
#             self.balance += amount
#             return f"Successfully deposited ${amount}. {self.check_balance()}"
#         return "Deposit amount must be greater than zero."

#     def withdraw(self, amount):
#         if amount <= 0:
#             return "Withdrawal amount must be greater than zero."
#         if amount > self.balance:
#             return "Insufficient funds."
#         self.balance -= amount
#         return f"Successfully withdrew ${amount}. {self.check_balance()}"

# # Example usage
# def main():
#     print("Welcome to the Simple Banking System!")
#     account = BankAccount("Ashwajit Kamble", 1000)

#     while True:
#         print("\nOptions:")
#         print("1. Check Balance")
#         print("2. Deposit Money")
#         print("3. Withdraw Money")
#         print("4. Exit")
#         choice = input("Choose an option: ")

#         if choice == "1":
#             print(account.check_balance())
#         elif choice == "2":
#             amount = float(input("Enter the amount to deposit: "))
#             print(account.deposit(amount))
#         elif choice == "3":
#             amount = float(input("Enter the amount to withdraw: "))
#             print(account.withdraw(amount))
#         elif choice == "4":
#             print("Thank you for banking with us!")
#             break
#         else:
#             print("Invalid choice. Please try again.")

# # Run the program
# if __name__ == "__main__":
#     main()

#===============================================================================

#     95. Write a program to create a calculator using functions.
#===============================================================================

#     96. Write a program to generate and validate OTPs.
#===============================================================================

#     97. Write a program to implement the binary search algorithm.
#===============================================================================

#     98. Write a program to convert a decimal number to binary.
#===============================================================================

#     99. Write a program to solve a quadratic equation.
#===============================================================================

#     100. Write a program to find the transpose of a matrix.
#===============================================================================

