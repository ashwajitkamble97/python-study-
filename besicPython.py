
    # 1. Write a program to print "Hello, World!"
# print("Hello, World!")
#----------------------------------------------------------------------------------------------------------------------
    # 2. Write a program to accept user input and print it.
# a = str(input("Enter Any String:- "))
# print(a)
#----------------------------------------------------------------------------------------------------------
    # 3. Write a program to add two numbers.
# a= int(input("Enter 1st Number:-- "))
# b= int(input("Enter 2st Number:-- "))
# print("Addition of numbers:--" ,a+b)
# ------------------------------------------------------------------------------------------
    # 4. Write a program to calculate the square of a number.
# a= int(input("Enter 1st Number:-- "))
# print(a**2)
# ------------------------------------------------------------------------------------------
    # 5. Write a program to swap two variables.
# a= 27
# b=99
# print("Before swap a=",a,"b=",b)
# temp=a
# a=b
# b=temp
# print("After swap a=",a,"b=",b)
# ------------------------------------------------------------------------------------------
    # 6. Write a program to calculate the area of a circle.
# r= int(input("Enter Redius:-- "))
# print("Redius is",r)
# area = 3.14159*r**2
# print("Area of circle is",area)
# ------------------------------------------------------------------------------------------
    # 7. Write a program to check if a number is even or odd.
# num= int(input("Enter number:-- "))
# if num%2==0:
#     print(num,"is Even")
# else:
#     print(num,"is odd")
# ------------------------------------------------------------------------------------------
    # 8. Write a program to find the largest of three numbers.
# num1=int(input("Enter Num 1 :--"))
# num2=int(input("Enter Num 2 :--"))
# num3=int(input("Enter Num 3 :--"))

# if num1<num2:
#     if num2<num3:
#         print(num3,"is greter")
#     else:
#         print(num2,"is greter")
# else:
#     print(num1,"is greter")
# -------------------------------------------------------------------------------------------
    # 9. Write a program to calculate the factorial of a number.
# num = int(input("Enter any Number:-- "))
# fact = 1

# if num < 0:
#     print("number is negative ")
# elif num==0:
#     print("factorial of number",num," is 1")
# else:

#     for i in range(1, num+1):
#         fact = fact * i

# print("factorial of number",num,"is",fact)
# # -------------------------------------------------------------------------------------------
    # 10. Write a program to reverse a string.
# a = str(input("Enter String:-- "))
# string=""
# print("the String before reverse :-- ", a)

# for i in a:
#     string = i + string
    
# print("Reverse string :--- ",string)
# ---------------------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------
# 2. Control Flow
#     11. Write a program to check if a number is positive, negative, or zero.
# num = int(input("Enter Number:-- "))

# if num <0:
#     print("Entered Number is Negative")
# elif num == 0:
#     print("Entered Number is Zero")
# else:
#     print("Enterd Number Is Positive")
# -----------------------------------------------------------------------------------------------
#     12. Write a program to check if a year is a leap year.
# y = int(input("Enter Year:--"))

# if (y % 4 == 0 and y % 100 != 0) or (y % 400 ==0) :
#     print(f"{y} is Leap Year")
# else:
#     print(f"{y} is Not Leap Year")
# -----------------------------------------------------------------------------------------------
#     13. Write a program to find the largest of three numbers using nested if-else.
# num1 = int(input("Enter Num1: "))
# num2 = int(input("Enter Num2: "))
# num3 = int(input("Enter Num3: "))

# if num1<=num2:
#     if num2<=num3:
#         print(f"{num3} is greter")
#     else:
#         print(f"{num2} is greter")
# else:
#     if num1<=num3:
#         print(f"{num3} is greter")
#     else:
#         print(f"{num1} is greter")


# -----------------------------------------------------------------------------------------------

#     14. Write a program to print all even numbers in a range.
# numbers = list(map(int, input("Enter three numbers separated by spaces: ").split()))
# print(numbers)
# Program to print even, odd, and prime numbers in a range
# start = int(input("Enter the start of the range: "))
# end = int(input("Enter the end of the range: "))

# even_numbers = []
# odd_numbers = []
# prime_numbers = []

# for num in range(start, end + 1):
    
#     if num % 2 == 0:
#         even_numbers.append(num)
#     else:
#         odd_numbers.append(num)

#     if num > 1:  
#         is_prime = True
#         for i in range(2, num):
#             if num % i == 0:
#                 is_prime = False
#                 break
#         if is_prime:
#             prime_numbers.append(num)

# print(f"Even numbers: {even_numbers}")
# print(f"Odd numbers: {odd_numbers}")
# print(f"Prime numbers: {prime_numbers}")
# -----------------------------------------------------------------------------------------------

#     15. Write a program to print numbers divisible by 5 and 7 within a range.
# start = int(input("Enter the start of the range: "))
# end = int(input("Enter the end of the range: "))
# five = []
# seven = []
# none = []
# for i in range(start, end+1):
#     if i % 5 == 0:
#         five.append(i)

#     if i % 7 == 0:
#         seven.append(i)

#     if (i % 5 != 0) and (i % 7 != 0):
#         none.append(i)

# print(f"\n numbers is divisible by 5 :{five}")
# print(f"\n numbers is divisible by 7 :{seven}")
# print(f"\n numbers is Not divisible by 5 & 7 :{none}")


# -----------------------------------------------------------------------------------------------

#     16. Write a program to generate a multiplication table of a number.
# num = int(input("Enter the number : "))
# multi = int(input("Enter number upto the range: "))
# arr = []

# for i in range(1,multi +1 ):
#     if i % num == 0 :
#         arr.append(i)
# print(f"the multiple of {num} are {arr}")
# -----------------------------------------------------------------------------------------------

#     17. Write a program to print the Fibonacci series up to a given number.
# num = int(input("Enter the number : "))

# fibo = [0,1]

# for i in range(2,num):
#     fibo.append(fibo[i - 1] + fibo[i - 2])

# print(f"Fibonacci series up to a {num} number is {fibo}")
# -----------------------------------------------------------------------------------------------

#     18. Write a program to find the sum of all natural numbers up to a given number.
# add = 0
# num = int(input("Enter the number : "))
# for i in range(1,num+1):
#     add = add + i
# print(f"the sum of all natural numbers up to a {num} number is {add}")
# -----------------------------------------------------------------------------------------------

#     19. Write a program to check if a given character is a vowel or consonant.
# char =str(input("Enter any Character: "))
# vowel = "aeiouAEIOU"
# if len(char) < 2:
#     if char in vowel:
#         print(f"given character {char} is Vowel")
#     else:
#         print(f"given character {char} is consonant")
# else:
#     print(f"given character {char} Having greter legth !")
# -----------------------------------------------------------------------------------------------

#     20. Write a program to implement a simple calculator (addition, subtraction, multiplication, division).
# num1 = int(input("Enter the 1st number : "))
# num2 = int(input("Enter the 2nd number : "))
# print("addition = 1, subtraction = 2, multiplication = 3, division = 4")
# cal = int(input("Enter the Calculation number : "))
# if cal < 5:
#     if cal == 1:
#         print(f"Addition of {num1} and {num2} is {num1+num2}")
#     elif cal == 2:
#         print(f"Subtraction of {num1} and {num2} is {num1-num2}")
#     elif cal == 3:
#         print(f"Multiplication of {num1} and {num2} is {num1*num2}")
#     elif cal == 4:
#         print(f"division of {num1} and {num2} is {num1%num2}")
# else:
#     print(f"Entered the Calculation number {cal} is Invalid!")

# -----------------------------------------------------------------------------------------------
# 3. Loops
#     21. Write a program to print numbers from 1 to 10 using a for loop.
# for i in range(1,10 +1):
#     print(f"{i}\n")
# -----------------------------------------------------------------------------------------------

#     22. Write a program to print the first 10 natural numbers using a while loop.
# i=1
# while i <= 100:
#     print(f"{i}\n")
#     i+=1
# -----------------------------------------------------------------------------------------------

#     23. Write a program to print the sum of the first 10 natural numbers.
# total = 0
# for i in range(1,10+1):
#     total = total + i
# print(f"sum of first 10 natural numbers is {total}")
# -----------------------------------------------------------------------------------------------

#     24. Write a program to calculate the power of a number using a loop.
# num1 = int(input("Enter the number : "))
# power = int(input("Enter the Power of number : "))
# cal = 1
# for _ in range(power):
#     cal = cal*num1

# print(f"calculation of number {num1} to the power of {power} is {cal}")

# -----------------------------------------------------------------------------------------------

#     25. Write a program to print a pattern of stars (triangle, inverted triangle, etc.).
# num= int(input("Enter the number stars  : "))
# print("Right Angle triagle")
# for i in range(1,num+1):
#     print("* "*i)

# print("Inverted Right Angle triagle")

# for i in range(num,0,-1):
#     print("* "*i)

# print("triagle")
# for i in range(1,num+1):
#     print(" " * (num-i)+ " *" * i)
    
# print("Inverted triagle")
# for i in range(num,0,-1):
#     print(" " * (num-i)+ " *" * i)
# -----------------------------------------------------------------------------------------------

#     26. Write a program to check if a number is a prime number.
# num = int(input("Enter the number : "))

# def is_prime(num):
#     if num < 2:
#         return False
    
#     for i in range(2, int(num ** 0.5) + 1):
#         if num % i == 0:
#             return False
#     return True

# if is_prime(num):
#     print(f"{num} is a prime number.")
# else:
#     print(f"{num} is not a prime number.")


# -----------------------------------------------------------------------------------------------

#     27. Write a program to print all prime numbers in a range.
# def is_prime(number):
#     if number < 2:
#         return False
    
    
#     for i in range(2, int(number ** 0.5) + 1):
        
#         if number % i == 0:
#             return False
    
    
#     return True

# def list_primes_up_to(n):
#     prime_numbers = []
#     for num in range(2, n + 1):
#         if is_prime(num):
#             prime_numbers.append(num)
#     return prime_numbers

# # Example usage
# n = int(input("Enter a number: "))
# primes = list_primes_up_to(n)

# print(f"Prime numbers up to {n}: {primes}")
# # -----------------------------------------------------------------------------------------------

#     28. Write a program to print the factors of a number.
# n = int(input("Enter a number: "))
# print(f"the factors of a number {n} is ", end=" ")
# fact = []
# for i in range(1,n+1):
#     if n % i == 0 :
#         print(i,end=" ")
    
# -----------------------------------------------------------------------------------------------
#     29. Write a program to find the greatest common divisor (GCD) of two numbers.
# n1= int(input("Enter a 1st number: "))
# n2 = int(input("Enter a 2nd number: "))
# -----------------------------------------------------------------------------------------------
#     30. Write a program to find the least common multiple (LCM) of two numbers.
# n1= int(input("Enter a 1st number: "))
# n2 = int(input("Enter a 2nd number: "))
# -----------------------------------------------------------------------------------------------

