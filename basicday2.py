# 4. Strings
#     31. Write a program to count the number of vowels in a string.
# a = str(input("Enter Any String: "))
# vowels = "aeiouAEIOU"
# count =0
# for i in a:
#     if i in vowels:
#         count +=1
# print(f"The number of vowels in a string: ({count})")

#======================================================================================
#     32. Write a program to find the length of a string.
# a = str(input("Enter Any String: "))
# print(f"lengh of string: {len(a)}")
#======================================================================================

#     33. Write a program to check if a string is a palindrome.
# a = str(input("Enter Any String: "))
# string = ""
# for i in a:
#     string = i + string

# if a == string :
#     print(f"The string: {a} is palindrome")
# else:
#     print(f"The string: {a} is NOT palindrome")



#======================================================================================
#     34. Write a program to reverse a string.
# a = str(input("Enter Any String: "))
# string = ""
# for i in a:
#     string = i + string

# print(f"The everse string is {string}")
#======================================================================================

#     35. Write a program to count the number of words in a sentence.
# a = str(input("Enter Any Sentence: "))
# count = 0
# word = False
# for i in a:
#     if i == ' ':
#         count =count + 1
#         word = False
#     else:
#         word = True

# if word :
#     count = count + 1

# print(f"Number of word in the sentence is {count}")

#======================================================================================

#     36. Write a program to replace all vowels in a string with a specific character.
# a = str(input("Enter Any String : "))
# b = str(input("Enter Any Replacement Character : "))
# vowels = "aeiouAEIOU"
# rep = ''
# for i in a:
#     if i in vowels:
#         rep = rep + b
#     else:
#         rep = rep + i

# print(f"The enter string;{a} and replaced string : {rep}")


#======================================================================================

#     37. Write a program to find the frequency of each character in a string.
# a = str(input("Enter Any String : "))
# freq = {}
# for i in a:
#     if i in freq:
#         freq[i] = freq[i] + 1
#     else:
#          freq[i] = 1

# print(f"{freq}")


#======================================================================================

#     38. Write a program to remove all spaces from a string.
# a = str(input("Enter Any String : "))
# res = ""
# for i in a:
#     if i != ' ':
#         res = res + i

# print(f"{res}")


#======================================================================================

#     39. Write a program to convert a string to uppercase.
# a = str(input("Enter Any String: "))
# res = ''
# for i in a:
#     if 'a' <= i <= 'z':
#         # convert the charactor in AScII
#         res += chr(ord(i) - 32)
#     else:
#         res += i

# print(f"{res}")
#======================================================================================

#     40. Write a program to find all substrings of a string.
# a = str(input("Enter Any String: "))
# print(f"Entered string: {a}")
# for i in range(len(a)):
#     for j in range(i,len(a)):
#         res = ''
#         for k in range(i,j+1):
#             res = res + a[k]
#         print(f"substrings: {res}")

#======================================================================================

# 5. Lists
#     41. Write a program to create a list of numbers.
# a = int(input("Enter the number of elemets: "))
# res = []
# for i in range(a):
#     b = int(input(f"Enter numbers {i+1}: "))
#     res.append(b)

# print(f"list :{res}")
#======================================================================================

#     42. Write a program to find the largest element in a list.
# a = int(input("Enter the number of elemets: "))
# res = []
# for i in range(a):
#     b = int(input(f"Enter numbers {i+1}: "))
#     res.append(b)

# print(f"list :{res}")
# lg = res[0]
# for j in res:
#     if j > lg:
#         lg = j

# print(f"largest in list: {lg}")


#======================================================================================

#     43. Write a program to find the smallest element in a list.
# a = int(input("Enter the number of elemets: "))
# res = []
# for i in range(a):
#     b = int(input(f"Enter number {i+1}: "))
#     res.append(b)

# print(f"list :{res}")
# sm = res[0]
# for j in res:
#     if j < sm:
#         sm = j

# print(f"smallest in list: {sm}")

#======================================================================================

#     44. Write a program to calculate the sum of all elements in a list.
# a = int(input("Enter the number of elemets: "))
# res = []
# for i in range(a):
#     b = int(input(f"Enter number {i+1}: "))
#     res.append(b)

# print(f"list :{res}")
# add = 0
# for j in res:
#     add = add + j

# print(f"addtion: {add}")
#======================================================================================

#     45. Write a program to count occurrences of an element in a list.
# a = int(input("Enter the number of elemets: "))
# res = []
# for i in range(a):
#     b = int(input(f"Enter number {i+1}: "))
#     res.append(b)

# print(f"list :{res}")
# c = int(input("Enter the occurrence number : "))

# count = 0
# for j in res:
#     if c == j:
#         count = count + 1

# print(f"number {c} appears:{count} times")
#======================================================================================

#     46. Write a program to remove duplicates from a list.
# a = int(input("Enter the number of elemets: "))
# res = []
# for i in range(a):
#     b = int(input(f"Enter number {i+1}: "))
#     res.append(b)
# arr = []
# print(f"list :{res}")
# for j in res:
#     if j not in arr:
#         arr.append(j)
# print(f"List with no dupplicates: {arr}")
#======================================================================================

#     47. Write a program to sort a list in ascending and descending order.
# a = int(input("Enter the number of elements: "))
# res = []

# # Collecting the elements from the user
# for i in range(a):
#     b = int(input(f"Enter number {i+1}: "))
#     res.append(b)

# print(f"List: {res}")

# # Bubble Sort Algorithm to sort the list in ascending order
# for j in range(len(res)):
#     for k in range(len(res) - 1 - j):
#         if res[k] > res[k + 1]:
#             res[k], res[k + 1] = res[k + 1], res[k]

# print(f"Ascending: {res}")

# # Bubble Sort Algorithm to sort the list in descending order
# for j in range(len(res)):
#     for k in range(len(res) - 1 - j):
#         if res[k] < res[k + 1]:
#             res[k], res[k + 1] = res[k + 1], res[k]

# print(f"Descending: {res}")

#======================================================================================

#     48. Write a program to find the second largest element in a list.
# a = int(input("Enter the number of elements: "))
# res = []

# for i in range(a):
#     b = int(input(f"Enter number {i+1}: "))
#     res.append(b)

# print(f"List: {res}")
# large = res[0]
# secLarge = res[0]
# for j in res:
#     if j > large:
#         secLarge = large
#         large = j
#     elif j > secLarge and j != large:
#         secLarge = j

# print(f"Second largest : {secLarge}")

#======================================================================================

#     49. Write a program to merge two lists.
# a = [1,2,3,4,5]
# b = [6,7,8,9,10]
# c = a + b 
# print(f"merged lists:{c}")
#======================================================================================

#     50. Write a program to find the common elements between two lists.
# a = [1,2,3,4,5,7,5,7]
# b = [6,7,8,9,3,2,4]
# res = []
# for i in a:
#     if i in b and i not in res:
#         res.append(i)

# print(f"comman item: {res}")

#======================================================================================
