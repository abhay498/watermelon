# Copyright © 2020 Elephant. All rights reserved

# Rules
# Keep main counter as i, j, k, x, y.
# Solutions should be both without using built-in functions and using built-in functions.Start with solutions that does not use built-in functions.
# Specify source
# Use coding guidelines and tools like autopep8.

#--------------------------------------------------------------------------------------
# 1. """ Fibonacci series upto 100 """

# M1
a, b = 0, 1
while a <= 100:
    print(a, end = ' ')
    a, b = b, a + b

#------------------------------------------
# M2

a = 0
b = 1

print(a, end = ' ')
print(b, end = ' ')

c = a + b
while c <= 100:
    print(c, end = ' ')
    a = b
    b = c
    c = a + b

#--------------------------------------------------------------------------------------
#2. """ Prime numbers upto 100 """

# M1
import math
print(2, end=' ')
for num in range(3, 101, 2):
    if all(num % i != 0 for i in range(3, int(math.sqrt(num) + 1), 2)):
        print(num, end = ' ')

#------------------------------------------
# M3
print(2, end=' ')
i = 3
while i <= 100:
    k = 3
    flag = 1
    while i // 2 >= k:
        if i % k == 0:
            flag = 0
            break
        k += 2
        
    if flag:
        print(i, end = ' ')
        
    i += 2

#--------------------------------------------------------------------------------------
#3. """ Leap year or not """

year = input('Enter year')
year = int(year)

if year % 400 == 0:
    print('{0} is a leap year'.format(year))
elif year % 100 == 0:
    print('{0} is not a leap year'.format(year))
elif year % 4 == 0:
    print('{0} is a leap year'.format(year))
else:
    print('{0} is not a leap year'.format(year))

#--------------------------------------------------------------------------------------
#4. """ String is palindrome or not """

#M1
string = input('Enter string')
string_2 = string[::-1]
print(string_2)

if string == string_2:
    print('{0} is a palindrome'.format(string))
else:
    print('{0} is NOT a palindrome'.format(string))

#------------------------------------------
#M2
string = input('Enter string')      
string_2 = ''.join(reversed(string))

if string == string_2:
    print('{0} is a palindrome'.format(string))
else:
    print('{0} is NOT a palindrome'.format(string))
#------------------------------------------
# M3
string = input('Enter the string ')

flag = 1
i = 0
while i < len(string):
    if string[i] != string[-1 -i]:
        flag = 0
        break
    i += 1

if flag:
    print('{0} is a palindrome'.format(string))
else:
    print('{0} is not a palindrome'.format(string))

#--------------------------------------------------------------------------------------
#5. """ Sum of digits of a number """

num = int(input('Enter number'))
temp = num

total = 0
while num != 0:
    total = total + num % 10
    num = num // 10

print('Sum of digits of {0} is {1}'.format(temp, total))

#--------------------------------------------------------------------------------------
#6. Armstrong number

# The Armstrong numbers between 1 and 1000 are: 

 # 1   2   3   4   5   6   7   8   9   153   370   371   407  
#M1
#---------------------------------------
num = int(input('Enter number'))
length = len(str(num))

total = 0
temp = num
while temp != 0:
    total = total + (temp % 10) ** length
    temp = temp // 10

if num == total:
    print('{0} is an armstrong number'.format(num))
else:
    print('{0} is not an armstrong number'.format(num))

#M2
#---------------------------------------
num = int(input('Enter number'))

dup_num_one = dup_num_two = num
digits = 0
total = 0

while dup_num_two != 0: 
    digits += 1
    dup_num_two = dup_num_two // 10
	
while num != 0:
    rem = num % 10
    mul = 1
    i = 0
    while i < digits:
        mul = mul * rem        
        i += 1
        
    total = total + mul
    num = num // 10

if total == dup_num_one:
    print('{0} is an armstrong number'.format(dup_num_one))
else:
    print('{0} is NOT an armstrong number'.format(dup_num_one))

#--------------------------------------------------------------------------------------
#7. Number is perfect square or not

num = int(input('Enter number'))
flag = 0
if num == 1 or num == 4:
    flag = 1
else:
    i = 3
    while num // 2 > i:
        if num == i * i:
            flag = 1
            break
        i += 1

if flag:
    print("{0} is a perfect square".format(num))
else:
    print("{0} is NOT a perfect square".format(num))

#--------------------------------------------------------------------------------------
#8. Reverse every word in a sentence

#M1
#-----
sentence = input('Enter sentence')
words = sentence.split(' ') 
new_words = [word[::-1] for word in words]
new_sentence = ' '.join(new_words)
print(new_sentence)

#M2
#-----
user_string = input('Enter string')
string = list(user_string)
length = len(string)

i = 0
j = 0
while j < length:
    if string[j] == ' ' or j == length - 1:

        if j < length - 1:
            k = j - 1
        else:
            k = j 

        while i < k:
            string[i], string[k] = string[k], string[i]
            i += 1
            k -= 1
        
        i = j + 1

    j += 1

string = ''.join(string)
print('Reversed every word in the input sentence : {0}'.format(string))

#--------------------------------------------------------------------------------------
#9. Linear search

a_list = [int(x) for x in input().split()]
num = int(input("Enter number"))
length = len(a_list)
flag = 0
i = 0
while i < length:
    if num == a_list[i]:
        flag = 1
        break
    i += 1

if flag:
    print('{0} is at index {1}'.format(num, i))
else:
    print('{0} is not present'.format(num))

#--------------------------------------------------------------------------------------
#10. Binary search
# Source : https://www.geeksforgeeks.org/python-program-for-binary-search/
	
# Iterative Binary Search Function
# It returns index of x in given array arr if present,
# else returns -1
def binary_search(arr, x):
	low = 0
	high = len(arr) - 1
	mid = 0

	while low <= high:

		mid = (high + low) // 2

		if arr[mid] < x:
			low = mid + 1

		elif arr[mid] > x:
			high = mid - 1

		else:
			return mid

	return -1

arr = [2, 3, 4, 10, 40]
x = int(input('Enter the number to search '))

result = binary_search(arr, x)

if result != -1:
	print('Number is present at index {0}'.format(result))
else:
	print('Number is not present in the list')

# o/p
# >>> 
# =============== RESTART: C:\Users\Abhay\OneDrive\Desktop\rough.py ==============
# Enter the number to search 2
# Number is present at index 0
# >>> 

#--------------------------------------------------------------------------------------
#11. Decimal to binary

base = 1
binary = 0
no_of_ones = 0

num = input("Enter decimal integer")
num = int(num)

decimal_num = num

while num > 0:
    rem = num % 2

    if rem == 1:
        no_of_ones += 1

    binary = binary + rem * base
    num = num // 2
    base = base * 10

print("Binary equivalent :{0}".format(binary))
print("Number of ones :{0}".format(no_of_ones))

#--------------------------------------------------------------------------------------
#12. Binary to decimal

binary = input("Enter binary number")
binary = int(binary)
decimal = 0
base = 1

while(binary > 0):
    rem = binary % 10
    decimal = decimal + rem * base
    binary = binary // 10
    base = base * 2

print("Decimal equivalent {0}".format(decimal))

#--------------------------------------------------------------------------------------
#13. Insert a number at a specified position in a list

a_list = [int(x) for x in input().split()]
num = int(input('Enter number to add'))
position = int(input('Enter position'))

if position > len(a_list) + 1 or position == 0:
    raise Exception ('Position out of range')

i = len(a_list) - 1 
a_list.append(None)

while i >= position - 1:
    a_list[i + 1] = a_list[i]
    i -= 1

a_list[position - 1] = num

print('New list is {0}'.format(a_list))

#o/p

# >>> 
# =============== RESTART: C:\Users\Abhay\OneDrive\Desktop\rough.py ==============
# 1 2 3
# Enter number to add92
# Enter position2
# New list is [1, 92, 2, 3]
# >>> 

#--------------------------------------------------------------------------------------
#14. Delete first occurence of the integer from a list, without using pop or remove.

def delete_integer(a_list, num):

    if num not in a_list:
        return 0
    
    flag = 0
    length = len(a_list)
    
    i = 0
    while i < length - 1:
        if num == a_list[i] or flag == 1:
            a_list[i] = a_list[i + 1]
            flag = 1
        
        i += 1

    if flag == 0 and a_list[-1] == num:
        flag = 1

    if flag:
        del a_list[-1]
    return a_list

a_list = [int(x) for x in input().split()]
num = int(input('Enter number'))

result = delete_integer(a_list, num)

if result:
    print('List after deletion :', a_list)
else:
    print('Number not present in the list')

#--------------------------------------------------------------------------------------
#15.  inp = ' DJ on module     234  56, instance 0\r\n\r',extract 234

import re
inp = ' DJ on module     234  56, instance 0\r\n\r'

inp = inp.strip()
matc = re.match("DJ\s+on\s+module\s+(\d+)\s+",inp,re.I)

if matc:
    print(matc.group(1))

#--------------------------------------------------------------------------------------
#16. search city

import re

cities = """
         Bangalore
         Auckland
         Canberra
         Ottawa
         San Jose
         Las Vegas
         Bangkok
         Lucknow 
         """

user = input('Enter string')

cities = cities.split('\n')

for each in cities:
    each = each.strip()
    matc = re.match('^'+user, each, re.I)

    if matc:
        print(each)

#--------------------------------------------------------------------------------------
#17. even ,odd separation

even = []
odd = []

a_list = [int(x) for x in input().split()]

for each in a_list:
    if each % 2 == 0:
        even.append(each)
    else:
        odd.append(each)

print('Even numbers {0}'.format(even))
print('Odd numbers {0}'.format(odd))

#--------------------------------------------------------------------------------------
#18.
"""
    1
   12
  123
 1234
12345
"""
i = 1
while i <=5:
    k = 5 - i
    j = 1
    while k > 0:
        print(" ",end= '')
        k -= 1

    while j <= i:
        print(j,end = '')
        j += 1

    print()

    i += 1 

#--------------------------------------------------------------------------------------
#19. File operations

#-----------------------------------------
#M1
#----
with open(r'C:\Users\Abhay\OneDrive\Desktop\input.txt') as f_one:
    with open(r'C:\Users\Abhay\OneDrive\Desktop\output.txt', 'w') as f_two:
        for line in f_one:
            f_two.write(line)

#-----------------------------------------
#M2

file_one = open(r'C:\Users\Abhay\OneDrive\Desktop\input.txt', 'r')
file_two = open(r'C:\Users\Abhay\OneDrive\Desktop\output.txt', 'w')

for line in file_one:
    file_two.write(line)

file_one.close()
file_two.close()

#--------------------------------------------------------------------------------------
#20. Election problem

votes = ['Victor','Veronica','Ryan','Dave','Maria','Maria','Veronica','John']

name_votes = {}
highest_votes = []
length = len(votes)

i = 0
while i < length:
    name = votes[i]
    
    if name in name_votes.keys():
        name_votes[name] += 1
    else:
        name_votes[name] = 1

    i += 1

num = list(name_votes.values())

maximum = num[0]

for i in num:
    if i > maximum:
      maximum = i

for i in name_votes:
    if name_votes[i] == maximum:
        highest_votes.append(i)

highest_votes.sort()

print(highest_votes[-1])

#---------------------------------------
M2
#---------------------------------------
from collections import Counter
votes = ['Victor','Veronica','Ryan','Dave','Maria','Maria','Veronica','John']

name_votes = Counter(votes)
highest_votes = []

number = list(name_votes.values())

maximum = number[0]

for each in name_votes.values():
    if each > maximum:
        maximum = each

for each in name_votes:
    if maximum == name_votes[each]:
        highest_votes.append(each)

highest_votes.sort()
print(highest_votes[-1])

#--------------------------------------------------------------------------------------
21. 
"""
process id 
hmm_process = ['ps -ef | grep hmm', 'root     26441 15790  0 02:11 ?        00:00:00 /isan/bin/routing-sw/hmm']
 ,extract --> 26441
"""

import re
hmm_process = ['ps -ef | grep hmm', 'root     26441 15790  0 02:11 ?        00:00:00 /isan/bin/routing-sw/hmm']

for each in hmm_process:
    if 'root' in content:
        matc = re.match('root\s+(\d+)',process_id)
    
    if matc:
            process_id = matc.group(1)

print(process_id)

#--------------------------------------------------------------------------------------
22. """ Dictionary operations """

a_list = ["veronica","rashmi","tina","sharya","agni"]

dict_1 = dict.fromkeys(a_list, 1)
dict_2 = dict_1

dict_3 = {}
dict_3['killer'] = 4
dict_3['drama'] = 8

dict_1.update(dict_3)

print(dict_1)
print(dict_2) # Elements of dictionary 2 also got updated
print(dict_3)

print('############## Keys ###############')
for each in dict_1:
    print(each)

print('################ Keys #############')
for each in dict_1.keys():
    print(each)

print('############# Values ################')

for each in dict_1.values():
    print(each)

print('############## Keys and Values ###############')
for key, value in dict_1.items():
    print(key, value)

#Dictionaries are now ordered from version 3.7
#http://www.blog.pythonlibrary.org/2018/02/27/python-3-7-dictionaries-now-ordered/
#--------------------------------------------------------------------------------------
23.
import re
string = "phone -- number 9876-9344 is 7896     .mine"
findc = re.findall("(\d+)\-(\d+)",string)

if findc:
    number = findc[0][0] + findc[0][1]
    print(number)

#--------------------------------------------------------------------------------------
24.
import re
string = "phone -- number 9876-9344 is      .mine"
subc = re.sub("([^0-9])","",string)
print(subc)
#--------------------------------------------------------------------------------------
25.

M1
#--
import re
string = "phone -- number 9876-9344 is 657     .mine"

searchc = re.search("(\d+).(\d+)",string)

if searchc:
    num_1 = searchc.group(1)
    num_2 = searchc.group(2)
    number = num_1 + num_2
    print(number)

M2
#--
import re
string = "phone -- number 9876-9344 is      .mine"
searchc = re.search("(\d+.\d+)",string)

if searchc:
    num = searchc.group(1)

num = re.sub('(\-)','',num)
print(num)

#--------------------------------------------------------------------------------------
26.
import re
string = 'phone -- number 9876-9344 is 7896     .mine'

mat_c = re.match('phone.*number\s+(\d+)-(\d+)', string, re.I)

if mat_c:
    num_1 = mat_c.group(1)
    num_2 = mat_c.group(2)
    number = num_1 + num_2
    print(num_1 + num_2)

#--------------------------------------------------------------------------------------
27.

""" Find numbers starting with digits in a list """

M1
#--
import re
alist = ["abc123","dog","34qweq","cat","23"]

for content in alist:
   if re.match("^[0-9]",content):
       print(content)

M2
#--
import re

aList = ["abc123","dog","34qweq","cat","23"]

for content in aList:
    if re.match("^\d",content):
        print(content)

#--------------------------------------------------------------------------------------
28.

""" Find numbers ending with digits in a list"""

import re

aList = ["abc123","dog","cat","23"]

for content in aList:
    if re.match(".*\d$",content):
        print(content)

#--------------------------------------------------------------------------------------
29.

""" Making dictionary from 2 lists """

keys = ['a','b','c']
values = [1,2,3]

a_dict = dict(zip(keys,values))

print(a_dict)
print(list(a_dict.keys()))
print(list(a_dict.values()))

#--------------------------------------------------------------------------------------
30.

""" Slicing """

a_list = ['Ram','Lakshman','Hanuman',3,7,'Abhay',56,32]
b_list = ['Triage','resurrection']

slice_1 = a_list[1:5]
slice_2 = a_list[2:]

print(slice_1)
print(slice_2)
print(slice_1 + slice_2)

#--------------------------------------------------------------------------------------
31.
""" list comprehension """

#Print square of all even numbers that are greater than 4 and less than 10.
#M1
nums = range(10)
square_evens = [x**2 for x in nums if x%2 == 0 and x > 4]
print(square_evens)

#M2
nums = range(6, 10, 2)
square_evens = [x**2 for x in nums]
print(square_evens)

#Example 3, Append all the elements of a dictionary to a list that start with abhay
#M1

import re
dict_1 = {'Samar':'java','Kabir':'c','AbhaySingh':'java','abhayksi':'python','abhay':'Ranchi'}

a_list = []
for each in dict_1:
    if re.match('abhay.*', each, re.I):
        a_list.append(each)

print(a_list)

#M2
import re
dict_1 = {'Samar':'java','Kabir':'c','AbhaySingh':'java','abhayksi':'python','abhay':'Ranchi'}
a_list = [each for each in dict_1 if re.match('abhay.*', each, re.I)]
print(a_list)

# Example 4
# Remove all elements greater than 5
a = [24 , 66 , 10, 2, 3, 44, 55, 6]
a = [i for i in a if i <= 5]
print(a)

#--------------------------------------------------------------------------------------
32.
""" decorators """

"""
Decorators allow us to wrap another function in order to extend the behavior of wrapped function,
without modifying it.
"""

# https://www.oreilly.com/content/5-reasons-you-need-to-learn-to-write-python-decorators/
# https://www.quora.com/What-is-the-use-of-decorators-in-Python-and-when-do-you-use-them
# https://stackoverflow.com/questions/489720/what-are-some-common-uses-for-python-decorators
# https://www.geeksforgeeks.org/decorators-in-python/
	
# Example 1
def double(f):
    def g(a,b):
        return 2 * f(a,b)
    return g

@double
def adder(a,b):
    return a + b

print(adder(3,4))

@double
def subtractor(a,b):
    return a - b

print(subtractor(9,3))

# Example 2
import time
import math

def calculate_time(func):
    def g(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        print('Total time taken for {0} {1}'.format(func.__name__, end - start))
    return g

@calculate_time
def factorial_number(num):
    print(math.factorial(num))

factorial_number(5)

#--------------------------------------------------------------------------------------
33. """ lambda """
sum_1 = lambda x, y : x + y
print(sum_1(1,2))

#--------------------------------------------------------------------------------------
34. 
""" classmethod and staticmethod """

class Employee:

    num_of_emps = 0
    
    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.email = first + '_' + last + '@email.com'
        self.pay = pay
        Employee.num_of_emps += 1
    
    def full_name(self):
        print(self.first + ' ' + self.last)
    
    @classmethod
    def fromstring(cls, emp_str):
        first,last,pay = emp_str.split('-')
        return cls(first,last,pay)
    
    @staticmethod
    def work_day(day):
        if day is 6 or day is 7:
            print("Not a working day")
        elif day > 7:
            print("Not a valid day")
        else:
            print("Working day")
        
emp_str_1 = 'John-Doe-70000'
emp_str_2 = 'Adam-Gilchrist-40000'
emp_str_3 = 'Harley-Davidson-50000'

emp1 = Employee.fromstring(emp_str_1)
emp2 = Employee.fromstring(emp_str_2)
emp3 = Employee.fromstring(emp_str_3)

print(emp1.email)
emp1.full_name()
print("Total number of emplayees: {0}".format(Employee.num_of_emps))
print(emp3.email)
emp3.full_name()
Employee.work_day(5)

#Point_1 : A class method can access or modify class state while a static method can’t access or modify it.
#--------------------------------------------------------------------------------------
35. # Recursion questions

# Source https://towardsdatascience.com/10-popular-coding-interview-questions-on-recursion-2ddd8aa86039

# a. Write a recursive function that takes a number and returns the sum of all the numbers from zero to that number.

def cumulative(num):
    if num in [0, 1]:
        return num
    else:
        return num + cumulative(num-1)
		
print(cumulative(5))

# b. Write a recursive function that takes a number ‘n’ and returns the nth number of the Fibonacci number.

def fibonacci(n):
    if n <= 0:
        print("Incorrect input")
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)

print(fibonacci(5))

# >>> 
# =============== RESTART: C:\Users\Abhay\OneDrive\Desktop\rough.py ==============
# 3
# >>> 

# c. Write a recursive function that takes a list of numbers as an input and returns the product of all the
#    numbers in the list.

def productOfArray(arr):
    if len(arr) == 0:
        return 0
    if len(arr) == 1:
        return arr[0]
    else:
        return arr[len(arr)-1] * productOfArray(arr[:len(arr)-1])

print(productOfArray([5, 4, 3]))

# d. Write a function that takes a string and returns if the string is a palindrome.

def isPalindrom(strng):
    if len(strng) == 0:
        return True
    if strng[0] != strng[len(strng)-1]:
        return False
    return isPalindrome(strng[1:-1])
    
# e. Write a recursive function that takes a string and reverse the string.

def reverse(st):
    if len(st) in [0, 1]:
        return st
    else:
        return st[len(st)-1] + reverse(st[:len(st)-1])
        
# f. Write a recursive function that takes an array that may contain more arrays in it and
#    returns an array with all values flattened.

def flatten(arr):
    res = []
    for i in arr:
        if type(i) is list:
            res.extend(flatten(i))
        else:
            res.append(i)
    return res

print(flatten([1, [2, 3], [4, [5, 6]]]))

#o /p :
# >>> 
# =============== RESTART: C:\Users\Abhay\OneDrive\Desktop\rough.py ==============
# [1, 2, 3, 4, 5, 6]
# >>> 

# g. Write a recursive function that takes an array of words and returns an array that contains
#    all the words capitalized. 

def capitalizeWords(arr):
    if len(arr) == 0:
        return []
    else:
        return [arr[0].upper()]+capitalizeWords(arr[1:])

print(capitalizeWords(['Hello','How']))

#o/p :

# >>> 
# =============== RESTART: C:\Users\Abhay\OneDrive\Desktop\rough.py ==============
# ['HELLO', 'HOW']
# >>> 

# h. Write a recursive function that will return the sum of all the positive numbers which are even numbers in a dictionary
#    which may contain more dictionaries nested in it.

def evenSum(obj, sum=0):
    for k in obj.values():
        if type(k) == int and k%2 ==0:
            sum += k
        elif isinstance(k, dict):
            sum += evenSum(k, sum=0)
    return sum
    
obj = {
  "a": 2,
  "b": {"x": 2, "y": {"foo": 3, "z": {"bar": 2}}},
  "c": {"p": {"h": 2, "r": 5}, "q": 'ball', "r": 5},
  "d": 1,
  "e": {"nn": {"lil": 2}, "mm": 'car'}}


print(evenSum(obj))

# o/p:

# >>> 
# =============== RESTART: C:\Users\Abhay\OneDrive\Desktop\rough.py ==============
# 10
# >>> 
#--------------------------------------------------------------------------------------
36. """ importing module from a different location """

import sys
import sample
path_to_module = 'C://z_data'
sys.path.append(path_to_module)
k = sample.__file__
result = sample.sub(16, 2)
print('result : {0}'.format(result))
print(k)
#--------------------------------------------------------------------------------------
37. """ A class example """

class Employee:
    emp_count = 0

    def __init__(self,name,age):
        self.name = name
        self.age = age
        Employee.emp_count += 1
        
    def display(self):
        print("Name is {0}".format(self.name))
        print("Age is {0}".format(self.age))

emp1 = Employee('Arun', 23)
emp2 = Employee('Satish', 45)

emp2.display()
print(Employee.emp_count)

#--------------------------------------------------------------------------------------
38. """ Inheritance """

class Parent:
    def __init__(self):
        print("Parent contructor")

    def set_value(self,attr):
        self.attr = attr

    def get_value(self):
        return self.attr + 4
        
class Child(Parent):
    def __init__(self):
        print("Child constructor")


obj_child = Child()
obj_child.set_value(4)
result = obj_child.get_value()
print(result)

#--------------------------------------------------------------------------------------
# 39. https://www.geeksforgeeks.org/rotate-a-matrix-by-90-degree-in-clockwise-direction-without-using-any-extra-space/

# M1
# O(n*n) time | O(1) space
def display(arr):
    for i in range(N) :
        for j in range(N) :
            print(arr[i][j],end=" ")
        print()
            
# Function to rotate the matrix 90 degree clockwise
def rotate90Clockwise(arr) :
    global N
    
    # Transpose of matrix
    for i in range(N) :
        for j in range(i+1,N) :
            arr[i][j],arr[j][i]=arr[j][i],arr[i][j]
    
    # Reverse individual rows
    for i in range(N//2) :
        low = 0
        high = N-1
        while (low<high) :
            arr[i][low],arr[i][high]=arr[i][high],arr[i][low]
            low = low + 1
            high = high - 1
        
# Driver code   
arr = [ [ 1, 2, 3, 4 ],
        [ 5, 6, 7, 8 ],
        [ 9, 10, 11, 12 ],
        [ 13, 14, 15, 16 ] ]
rotate90Clockwise(arr)
display(arr)

# M2
# O(n*n) time | O(1) space
N = 4

# Function to rotate the matrix
# 90 degree clockwise
def rotate90Clockwise(A):
    N = len(A[0])
    for i in range(N // 2):
        for j in range(i, N - i - 1):
            temp = A[i][j]
            A[i][j] = A[N - 1 - j][i]
            A[N - 1 - j][i] = A[N - 1 - i][N - 1 - j]
            A[N - 1 - i][N - 1 - j] = A[j][N - 1 - i]
            A[j][N - 1 - i] = temp

# Function to print the matrix
def printMatrix(A):
    N = len(A[0])
    for i in range(N):
        print(A[i])

# Driver code
A = [[1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]]
rotate90Clockwise(A)
printMatrix(A)

#--------------------------------------------------------------------------------------
40. """ Threading """

from threading import Thread
from time import sleep

def execute_thread(name,delay,repeat):
    
    print('Starting ' + name + ' thread')

    while repeat > 0:
        sleep(delay)                
        print('Executing {0}'.format(name))
        repeat = repeat - 1
    print('Thread ' + name + ' Completed')

def Main():

   t1 = Thread(target = execute_thread, args = ('THREAD_1',5,2))
   t2 = Thread(target = execute_thread, args = ('THREAD_2',5,5))

   t1.start()
   t2.start()

   t2.join()
   t1.join()

if __name__ == '__main__':
    Main()

"""
when the join() is invoked from a main thread, the main thread 
waits till the child thread on which join is invoked exits.
"""
#--------------------------------------------------------------------------------------
41.

a = """saveChangesInTheEditor"""
count = 0
for content in a:
    if content.isupper():
        count += 1

print(count + 1)

#--------------------------------------------------------------------------------------
42. """ filter """
def f(x):
    return x % 3 == 0 or x % 5 == 0

three_or_five = list(filter(f, range(2,25)))

print(three_or_five)

"""
The filter() method constructs an iterator from elements of an iterable for which a function returns true.
"""
#--------------------------------------------------------------------------------------
43.""" map """

#Example 1
def add(x):
    return x + 10

result = list(map(add, range(4,10)))

#Example 2
items = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, items))

"""
Python map() function is used to apply a function on all the elements of specified iterable and return map object.
Python map object is an iterator, so we can iterate over its elements. We can also convert map object to sequence
objects such as list, tuple etc. using their factory functions.
"""
#--------------------------------------------------------------------------------------
44.""" reduce """

#Example 1
from functools import reduce

def sum(x, y):
    return x + y
    
result = reduce(sum, [1,2,3,4])
print(result)

#Example 2


#--------------------------------------------------------------------------------------
# 45. Spiral traverse of a matrix
# 1 2 3 4 8 12 16 15 14 13 9 5 6 7 11 10
a = [[1,2,3,4],
     [5,6,7,8],
     [9,10,11,12],
     [13,14,15,16]]

L = 0
T = 0
B = len(a) - 1
R = len(a[0]) - 1

direction = 0
spiral = []

while L <= R and T <= B:
    
    if direction == 0:        
        k = L
        while k <= R:
            spiral.append(a[T][k])
            k += 1
        T += 1 
        
    if direction == 1:
        k = T
        while k <= B:
            spiral.append(a[k][R])
            k += 1
        R -= 1
        
    if direction == 2:
        k = R
        while k >= L:
            spiral.append(a[B][k])
            k -= 1
        B -= 1
        
    if direction == 3:
        k = B
        while k >= T:
            spiral.append(a[k][L])
            k -= 1
        L += 1    
    direction = (direction + 1) % 4

print(spiral)
#--------------------------------------------------------------------------------------
46. # 1 2 3 4 8 7 6 5 9 10 11 12 16 15 14 13

a = [[1,2,3,4],
     [5,6,7,8],
     [9,10,11,12],
     [13,14,15,16]]

i = 0
flag = 1
while(i <= 3):
    j = 0
    while(j <= 3):
        print(a[i][j],end = " ")
        j += 1
                
    i += 1        

#--------------------------------------------------------------------------------------
47.

# 1 2 3 4 5 6 12 11 10 9 8 7 13 14 15 16 17 18 24 23 22 21 20 19 25 26 27 28 29 30 36 35 34 33 32 31

a = [[1,2,3,4,5,6],
     [7,8,9,10,11,12],
     [13,14,15,16,17,18],
     [19,20,21,22,23,24],
     [25,26,27,28,29,30],
     [31,32,33,34,35,36]]

i = 0
while(i <= 5):
    j = 0
    while(j <= 5):
        if(i % 2 == 0):
            print(a[i][j],end = ' ')
        else:
            print(a[i][5-j], end = ' ')

        j += 1

    i += 1       

#--------------------------------------------------------------------------------------
48. """ Reversing a Linked list """
class Node(object):
    def __init__(self,data):
        self.data = data
        self.next_node = None
    
class LinkedList(object):
    def __init__(self):
        self.head = None
        
    def insert_end(self,data):
        
        new = Node(data)
        
        if self.head is None:
            self.head = new
        else:
            p = self.head
            while p.next_node is not None:
                    p = p.next_node
            
            p.next_node = new

    def traverse(self):
        p = self.head
        while p is not None:
            print(" {0}".format(p.data))
            p = p.next_node
            
    def reverse_node(self):
        q = self.head
        r = None
        s = None
        
        while q is not None:
            s = r
            r = q
            q = q.next_node
            r.next_node = s

        self.head = r
        
link = LinkedList()
link.insert_end(20)
link.insert_end(30)
link.insert_end(40)
link.insert_end(50)
link.insert_end(60)

link.traverse()
print("-------")
link.reverse_node()
link.traverse()

#--------------------------------------------------------------------------------------
# 49. 

#--------------------------------------------------------------------------------------
# 50.

# M1
a_list = [5, 4, 3, 2 ,1]
b_list = [9, 8, 7, 6]

a_list = a_list + b_list
a_list.sort() # or use merge sort
print(a_list)

#####################################
# M2
a_list = [5, 4, 3, 2 ,1]
b_list = [9, 8, 7, 6]

a_list.extend(b_list)
a_list.sort()
print(a_list)

#####################################
# M3
a_list = [5, 4, 3, 2 ,1]
b_list = [9, 8, 7, 6]

for x in b_list:
    a_list.append(x)

a_list.sort()
print(a_list)

#####################################

#--------------------------------------------------------------------------------------
51. """ Bubble sort """

def bubble_sort(a_list):
    length = len(a_list)
    for i in range(length):
        for j in range(0, length - 1 - i):
            if a_list[j] > a_list[j + 1]:
                a_list[j], a_list[j + 1] = a_list[j + 1], a_list[j]


a_list = [65, 43, 56, 89, 4, 17]
bubble_sort(a_list)
print(a_list)

# o/p

#>>> 
#================ RESTART: C:\Users\Abhay\OneDrive\Desktop\two.py ===============
#[4, 17, 43, 56, 65, 89]
#>>> 

#--------------------------------------------------------------------------------------
52. """ Stack """

class Node(object):
    def __init__(self,data):
        self.data = data
        self.next_node = None

class Stack(object):
    def __init__(self):
        self.top = None
        
    def push_stack(self,data):
        new = Node(data)

        if self.top == None:
            new.next_node = None
        else:
            new.next_node = self.top

        self.top = new

    def pop_stack(self):
        p = None
        element = None

        if self.top == None:
            print("Stack underflow")
            exit(0)

        p = self.top

        self.top = p.next_node
        element = p.data
        del p

        return element

    def traverse(self):
        p = self.top

        while p != None:
            print(p.data,end = ' ')
            p = p.next_node

link = Stack()
link.push_stack(20)
link.push_stack(30)
link.push_stack(40)
link.push_stack(50)
link.push_stack(60)
link.traverse()
print()
print("-------")
element = link.pop_stack()
print("Popped element ",element)
element = link.pop_stack()
print("Popped element ",element)
link.traverse()

#--------------------------------------------------------------------------------------
53. """ Queue """

class Node(object):
    def __init__(self,data):
        self.data = data
        self.next_node = None

class Queue(object):
    def __init__(self):
        self.front = None
        self.rear = None

    def en_queue(self,data):
        new = Node(data)

##      if (self.front == None) and (self.rear == None):
        if None in (self.front,self.rear):
            self.front = self.rear = new
            return

        self.rear.next_node = new
        self.rear = new

    def de_queue(self):
        p = self.front

        if self.front == None:
            print("Empty queue")
            return

        if self.front == self.rear:
            self.front = self.rear = None
        else:
            self.front = self.front.next_node

        del p
        p = None

    def traverse(self):
        p = self.front

        while p != None:
            print(p.data,end = ' ')
            p = p.next_node
            
link = Queue()  
link.en_queue(2)
link.traverse()
print()
link.en_queue(3)
link.traverse()
print()
link.en_queue(4)
link.traverse()
print()
link.de_queue()
link.traverse()
print()
link.de_queue()
link.traverse()

#--------------------------------------------------------------------------------------
54. """ Remove odd numbers from a linked list """

class Node(object):
    def __init__(self,data):
        self.data = data
        self.next_node = None
    
class LinkedList(object):
    def __init__(self):
        self.head = None
        
    def insert_end(self,data):
        
        new = Node(data)
        
        if self.head is None:
            self.head = new
        else:
            p = self.head
            while p.next_node is not None:
                    p = p.next_node
            
            p.next_node = new

    def traverse(self):
        p = self.head
        while p is not None:
            print(" {0}".format(p.data))
            p = p.next_node
        
    def delete_node(self):
        q = None
        p = self.head
        chk = p.data

        while chk % 2 == 1:
            self.head = p.next_node
            p.next_node = None
            del p

            if self.head is None:
                return 1
        
            p = self.head
        
            chk = p.data
            
        q = p
        p = p.next_node
        while p is not None:
            chk = p.data

            if (chk % 2 == 1):
                q.next_node = p.next_node
                p.next_node = None
                del p
                p = q.next_node
            else:
                q = p
                p = p.next_node
            
        return

            
link = LinkedList()
link.insert_end(20)
link.insert_end(31)
link.insert_end(40)
link.insert_end(51)
link.insert_end(60)

link.traverse()
print("-------")
ret_delete = link.delete_node()
link.traverse()

#--------------------------------------------------------------------------------------
55.
""" some debugging """

class Node(object):
    def __init__(self,data):
        self.data = data
        self.next_node = None
    
class LinkedList(object):
    def __init__(self):
        self.head = None
        
    def insert_end(self,data):
        
        new = Node(data)
        
        if self.head is None:
            self.head = new
        else:
            p = self.head
            while p.next_node is not None:
                    p = p.next_node
            
            p.next_node = new

    def traverse(self):
        p = self.head
        while p is not None:
            print(" {0}".format(p.data),end = ' ')
            p = p.next_node
        
    def sample(self):
        self.sample_two(self.head)

    def sample_two(self,cur):
        self.found = 5
        q = self.head
        while cur is not None:            
            print(" {0}".format(cur.data),end = ' ')
            cur = cur.next_node
        print()
        for i  in range(0,2):
            q = q.next_node

        print("q.data :", q.data)
    def show(self):
        print("self.head.data :",self.head.data)
        print("self.found:",self.found)
    
link = LinkedList()
link.insert_end(20)
link.insert_end(31)
link.insert_end(40)
link.insert_end(51)
link.insert_end(60)

#link.traverse()
print()
link.sample()
#link.traverse()
link.show()

#--------------------------------------------------------------------------------------
56. Usage of decorator
def a_new_decorator(a_func):
    def wrapTheFunction():
        print("Entering def : {0}".format(a_func.__name__))
        a_func()
        print("Leaving def : {0}".format(a_func.__name__))
    return wrapTheFunction

@a_new_decorator
def a_function_requiring_decoration():
    a = 3
    b = 5
    add = a + b
    print(add)

a_function_requiring_decoration()

#--------------------------------------------------------------------------------------
57. """ Veryfying whether a number is a palindrome or not """

#M1
def is_palindrome(number):
    number = str(number)
    if number == number[::-1]:
        print('{0} is a palindrome'.format(number))
    else:
        print('{0} is not a palindrome'.format(number))

is_palindrome(101)
is_palindrome(105)

#M2
number = int(input("Enter number: "))
rev = 0

temp = number
while temp != 0:
    rev = rev * 10 + temp % 10
    temp = temp // 10
 
if number == rev:
    print("number is palindrome")
else:
    print("number is not palindrome")

#--------------------------------------------------------------------------------------
58. """ *args and **kwargs """

# *args and **kwargs allow to pass a variable number of arguments to a function.

def example_one(f_argv, *args, **kwargs):
    print('First argument {0}'.format(f_argv))
    print(args)
    
    for each in args:
        print(each)

example_one('Hunt','won','the','race')

#----------------------------------------------

def example_three(f_argv, arg_one, arg_two, **kwargs):
    print('First argument is {0}'.format(f_argv))
    print('arg_one {0}'.format(arg_one))
    print('arg_two {0}'.format(arg_two))
    
args = ('Hunt','was','F1')
example_three(*args)

#----------------------------------------------

def example_four(**kwargs):
    if kwargs is not None:
        for key, value in kwargs.items():
            print('{0} is {1}'.format(key, value))
    
example_four(name='Hunt')
kwargs = {'name':'Hunt','Races':10,'Country':'England'}

example_four(**kwargs)

#----------------------------------------------

def example_five(f_argv, arg_one, arg_two, **kwargs):
    print('f_argv is {0}'.format(f_argv))
    print('arg_one is {0}'.format(arg_one))
    print('arg_two is {0}'.format(arg_two))

    for key, value in kwargs.items():
        print('{0} is {1}'.format(key, value))

args = ('Hunt', 10)
kwargs = {'Racer':'Hunt','Year':1979}
example_five('England', *args, **kwargs)
#--------------------------------------------------------------------------------------
59. """ Delete Kth node from the end """

class Node(object):
    def __init__(self,data):
        self.data = data
        self.next_node = None
    
class LinkedList(object):
    def __init__(self):
        self.head = None
        self.total = 0
        
    def insert_end(self,data):
        
        new = Node(data)
        
        if self.head is None:
            self.head = new
        else:
            p = self.head
            while p.next_node is not None:
                    p = p.next_node
            
            p.next_node = new

    def traverse(self, display=1):
        self.total = 0
        p = self.head
        while p is not None:
            if display:
               print(p.data, end=' ')
            p = p.next_node
            self.total += 1
    
    def delete_node(self, position_from_end):
        print('\nDeleting {0}th node from end'.format(position_from_end))
        position_from_start = self.total - position_from_end + 1

        if position_from_start <= 0:
            print('\nNo node present at that position')
            return
            
        p = self.head

        if position_from_start == 1:
            self.head = p.next_node
            p.next_node = None
            del p
            return
        
        count = 1
        while count < position_from_start - 1:
                p = p.next_node
                count += 1
            
        q = p.next_node
        p.next_node = q.next_node
        q.next_node = None
        del q
        
        
link = LinkedList()
link.insert_end(20)
link.insert_end(30)
link.insert_end(40)
link.insert_end(50)
link.insert_end(60)

link.traverse()
link.delete_node(2)
link.traverse()
link.delete_node(4)
link.traverse()
link.delete_node(3)
link.traverse()
link.delete_node(1)
link.traverse()

#--------------------------------------------------------------------------------------
60. """ Monkey Patching """

# In Python, we can change the behavior of a code at run-time with the help of monkey patching.

class Test:
    def __init__(self):  
      self.a = 4
      
    def class_method(self):
        print('This is a class method')
        print(self.a)
        
def monkey_function(self):
    print('This is a monkey function')
    print(self.a + 2)
    
Test.class_method = monkey_function
Test().class_method()

#-----------------------------------------------------------------
# monk.py 
class A: 
     def func(self): 
          print("func() is being called")
     
#---------------------
import monk 
def monkey_f(self): 
    print("monkey_f() is being called")

monk.A.func = monkey_f 
obj = monk.A() 

obj.func()

#---------------------
# Output : monkey_f() is being called
#--------------------------------------------------------------------------------------
61. Timestamp 

from datetime import datetime
now = datetime.now()
timestamp = datetime.timestamp(now)
print('Timestamp is {0}'.format(timestamp))

#--------------------------------------------------------------------------------------
62.

user_number  = input("Enter your number")
if( user_number.isdigit()):
    print("User input is Number ")
else:
    print("User input is string ")

#--------------------------------------------------------------------------------------
63. # Why is Python slow ?

#1. High-level programming language: With Python, the code looks very close to how humans think. For this purpose, it must abstract the    details of the computer from you: memory management, pointers,… Hence, it is slower than “lower-level language” like C;

#2. Python is interpreted and not compiled: Sure, this statement is a gross simplification but it’s somehow correct. During the  execution, Python code is interpreted at runtime instead of being compiled to native code at compile time;

#3. Python is a dynamically typed language: Unlike “statically-typed” languages like C, C++ or Java, you don’t have to declare the  variable type like String, boolean or int. The less you do, the more your computer has to work. For each attribute access, tons of lookup is required. In addition, being very dynamic makes it incredibly hard to optimize Python;

#4. Global Interpreter Lock (GIL): This GIL basically prevents multi-threading by mandating the interpreter only execute a single thread within a single process (an instance of the Python interpreter) at a time.

#--------------------------------------------------------------------------------------
#64. Find the longest words


#--------------------------------------------------------------------------------------
#65. Factorial of a number

#M1
#---

def factorial(number):
    factorial = 1
    i = number
    while i > 1:
        factorial = factorial * i
        i -= 1
    return factorial

number = int(input('Enter number : '))

if number < 0:
    print('Factorial does not exist for negative numbers')
elif number == 0:
    print('Factorial of 0 is 1')
else:
    print('Factorial of {0} is {1}'.format(number, factorial(number)))
     
#M2
#---

def factorial(number):
    if number == 1:
        return number
    else:
        return number * factorial(number - 1)

number = int(input('Enter a number : '))
    
if number < 0:
   print('Factorial does not exist for negative numbers')
elif number == 0:
   print('Factorial of 0 is 1')
else:
   print('Factorial of {0} is {1}'.format(number, factorial(number)))

#--------------------------------------------------------------------------------------
66. """ Find number of occurrences of a word in a passage """

import re
file_one = open('input.txt', 'r')
passage = file_one.read()
words = re.findall('language', passage, re.I)
count = len(words)
print(count)
#--------------------------------------------------------------------------------------
67. # Extract ip address, validate the same and tell which class does it fall under

output ="""
hostname sr1
host address 10.0.2.8/23
processor
"""

#M1 -- Used to specify only private IP addresses
#---
import re
from ipaddress import IPv4Address
from ipaddress import IPv4Network

class_A = IPv4Network(('10.0.0.0', '255.0.0.0'))  # or IPv4Network("10.0.0.0\8")
class_B = IPv4Network(('172.16.0.0', '255.240.0.0'))  # or IPv4Network("172.16.0.0\12")
class_C = IPv4Network(('192.168.0.0', '255.255.0.0'))  # or IPv4Network("192.168.0.0\16")

def ip_class(ip_address):
    if ip_address in class_A:
        print('{0} belongs to Class A private family'.format(ip_address))
    elif ip_address in class_B:
        print('{0} belongs to Class B private family'.format(ip_address))
    elif ip_address in class_C:
        print('{0} belongs to Class C private family'.format(ip_address))
    else:
        print('Not a valid private IP address')

output = output.split('\n')
output = list(filter(None, output))

for each in output:
    if re.match('host\s+address\s+([0-9]+(?:\.[0-9]+){3})', each):
        ipv4_address = re.match('host\s+address\s+([0-9]+(?:\.[0-9]+){3})', each)
        break

ip_address = ipv4_address.group(1)
try:
    ip_address =  IPv4Address(ip_address)
    ip_class(ip_address)
except:
    print('Invalid ip address')


#M2 -- For all IP addresses
#---
output ="""
hostname sr1
host address 10.1.2.8/23
processor
"""

import re
def identify_class_ip_address(ip, ip_first_block):
    if ip_first_block >= 0 and ip_first_block <= 127:
        print('{0} is a Class A IP Address'.format(ip))
        return
    if ip_first_block >= 128 and ip_first_block <= 191:
        print('{0} is a Class B IP Address'.format(ip))
        return
    if ip_first_block >= 192 and ip_first_block <= 223:
        print('{0} is a Class C IP Address'.format(ip))
        return
    if ip_first_block >= 224 and ip_first_block <= 239:
        print('{0} is a Class D IP Address'.format(ip))
        return
    if ip_first_block >= 240:
        print('{0} is a Class E IP Address'.format(ip))
        return
    
output = output.split('\n')
output = list(filter(None, output))

pattern = ('(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.'
           '(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.'
           '(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.'
           '(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])')

flag = 0
for each in output:
    ip = re.search('\s+' + pattern + '/', each)
    if ip:
        flag = 1
        break

if flag:
    identify_class_ip_address(ip.group(0).strip()[:-1], int(ip.group(1)))
else:
    print('Not a valid IP address')

#--------------------------------------------------------------------------------------
68. Vlan problem

vlan = 1, 2, 3, 20-30, 'abc'-'def', 40, 4099, 5001, 34, -1, 41-51

import re

def verify_vlan(vlan_id):

    if not isinstance(vlan_id, str):
        vlan_id = str(vlan_id)
        
    result = re.match('([0-9]+)-?([0-9]+)?', vlan_id)

    if not result:
       return 0

    if int(result.group(1)) > 4096 and int(result.group(1)) < 0:
        print('Invalid vlan')
        return 0
    return 1

result = verify_vlan(6)
if result:
    print('Valid vlan 6')
else:
    print('Invalid vlan 6')
    
result = verify_vlan('abc')
if result:
    print('Valid vlan abc')
else:
    print('Invalid vlan abc')
    
result = verify_vlan('20')
if result:
    print('Valid vlan 20')
else:
    print('Invalid vlan 20')

result = verify_vlan('20-40')
if result:
    print('Valid vlan 20 and 40')
else:
    print('Invalid vlan 20 and 40')

#--------------------------------------------------------------------------------------
#https://stackoverflow.com/questions/12354515/what-is-the-difference-between-sets-and-lists-in-python

#--------------------------------------------------------------------------------------
69. Enum
"""
An enumeration is a set of symbolic names (members) bound to unique, constant values. Within an enumeration,
the members can be compared by identity, and the enumeration itself can be iterated over.
"""

#Example 1

import enum
class Days(enum.Enum):
   Sun = 1
   Mon = 2
   Tue = 1
if Days.Sun == Days.Tue:
   print('Match')
if Days.Mon != Days.Tue:
   print('No Match')

#Example 2
#The members in an Enumeration are hashable, hence they can be used in dictionaries and sets.

import enum
class Days(enum.Enum):
   Sun = 1
   Mon = 2

Daytype = {}
Daytype[Days.Sun] = 'Sun God'
Daytype[Days.Mon] = 'Moon God'

print(Daytype =={Days.Sun:'Sun God',Days.Mon:'Moon God'})
print(Daytype[Days.Sun])
print(Daytype[Days.Mon])

#--------------------------------------------------------------------------------------
70. Generators
"""
unlike functions, which return a whole array, a generator yields one value at a time which requires less memory.
Any python function with a keyword “yield” may be called as generator.
A normal python function starts execution from first line and continues until we got a return statement or
an exception or end of the function however, any of the local variables created during the function scope are destroyed and not accessible further. While in case of generator when it encounters a yield keyword the state of the function is frozen and all the variables are stored in memory until the generator is called again.

We can used generator in accordance with an iterator or can be explicitly called using the “next” keyword.

Generally generators in Python:

-Defined with the def keyword
-Use the yield keyword
-May contain several yield keywords.
-Returns an iterator.
"""

#Example 1
def generator_example():
   yield 'xyz'
   yield 246
   yield 40.50

g = generator_example()
print(g.__next__())
print(g.__next__())
print(g.__next__())

#Example 2
#M1 Not using generator

n= 200
number_list = range(1, n+1)
for i in number_list:
    print(i*i)

#M2 Using generator

def num_generator(n):
    num =1
    while True:
       yield num
       if num == n:
          return
       else:
          num += 1

for i in num_generator(200):
   print (i*i)

#--------------------------------------------------------------------------------------
71. itertools # Functions creating iterators for efficient looping

"""
Python itertools module is very useful in creating efficient iterators.
In almost every program you write with any programming language, one of the task which is usually always present is Iteration.
Traversing sequence of objects and manipulating them is very common.
Many times while doing these common operations, we miss out on managing memory usage of the variables,
size of the sequence being iterated and create a risk of inefficient code usage.
With itertools module in Python, this can be prevented from happening with its functions.
"""

from itertools import islice
from itertools import count

for num in islice(count(), 4):
    print(num)
    
print('I stopped at 4.')

for num in islice(count(), 15, 20):
    print(num)

print('I started at 15 and stopped at 20.')

for num in islice(count(), 5, 50, 10):
    print(num)

print('I started at 5 and leaped by 10 till 50.')
#--------------------------------------------------------------------------------------
72. """ Shallow copy and Deep copy """

# https://www.python-course.eu/python3_deep_copy.php
	
############################################

>>> a_list = ['a', 'b', 'c', [4,5]]
>>> a_list
['a', 'b', 'c', [4, 5]]
>>> b_list = a_list[:]
>>> b_list
['a', 'b', 'c', [4, 5]]
>>> b_list[0] = 6
>>> b_list
[6, 'b', 'c', [4, 5]]
>>> a_list
['a', 'b', 'c', [4, 5]]
>>> b_list[3][1] = 'j'
>>> b_list
[6, 'b', 'c', [4, 'j']]
>>> a_list
['a', 'b', 'c', [4, 'j']]
>>> 

############################################
>>> from copy import deepcopy
>>> a_list = ['a', 'b', 'c', ['ab', 'cd']]
>>> b_list = deepcopy(a_list)
>>> print(id(a_list))
65263736
>>> print(id(b_list))
65262856
>>> b_list[3][1] = 'xyz'
>>> b_list
['a', 'b', 'c', ['ab', 'xyz']]
>>> a_list
['a', 'b', 'c', ['ab', 'cd']]
>>> b_list[0] = 'j'
>>> b_list
['j', 'b', 'c', ['ab', 'xyz']]
>>> a_list
['a', 'b', 'c', ['ab', 'cd']]
>>> id(a_list[1])
24165760
>>> id(b_list[1])
24165760
>>> 

#--------------------------------------------------------------------------------------

73. # Nth armstrong number

def nth_armstrong_number(n):

    if n == 1:
        return 0
    
    count = 1
    for i in range (1, 1000):
        temp = i
        total = 0
        length = len(str(i))
        while temp != 0:
            total = total + ( temp % 10) ** length
            temp = temp // 10

        if total == i:
            count += 1

        if count == n:
            return i

n = int(input('th armstrong number '))
print('{0} armstrong number is {1}'.format(n, nth_armstrong_number(n)))

#--------------------------------------------------------------------------------------

74. # Segregating 0 and 1

# M1
def segregate_0_and_1(array): 
  
    i = 0
    j = len(array) - 1
      
    while i < j: 
        if array[i] == 1: 
            array[i],  array[j] = array[j], array[i]
            j -= 1
        else: 
            i += 1

array = [0, 1, 0, 1, 1, 1, 0, 0, 0, 1, 1] 
segregate_0_and_1(array) 
print(array)

# M2
def segregate_0_and_1(arr):
    length = len(arr)
    i = 0
    j = length - 1
    
    while i < j:
        if arr[i] != 0:

            while arr[j] != 0:
                j -= 1
                
            arr[i], arr[j] = arr[j], arr[i]
            j -= 1
        i += 1

arr = [0, 1, 0, 1, 1, 1, 0, 0, 0, 1, 1] 
segregate_0_and_1(arr)
print(arr)

# o / p
# >>> 
# =============== RESTART: C:\Users\Abhay\OneDrive\Desktop\rough.py ==============
# [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1]
# >>> 

#--------------------------------------------------------------------------------------

75. # """ Multiprocessing """

from multiprocessing import Process
from time import sleep

def execute_process(name, delay, repeat):
    print('Starting ' + name + ' process')

    while repeat > 0:
        sleep(delay)
        print('Executing {0}'.format(name))
        repeat -= 1
    print('Process ' + name +' Complete')
    
def Main():

    p1 = Process(target = execute_process, args = ('PROCESS_ONE', 5, 2))
    p2 = Process(target = execute_process, args = ('PROCESS_TWO', 4, 3))

    p1.start()
    p2.start()

    p1.join()
    p2.join()
    

if __name__ == '__main__':
    Main()

#--------------------------------------------------------------------------------------
76. # """ subprocess"""
import subprocess
cmd = 'rm -rf ' + location
result = subprocess.Popen([cmd], stdout=subprocess.PIPE, shell=True)
result.wait()
#--------------------------------------------------------------------------------------
77. 
x = 5
y = 5
z = 10
m = 10

print(id(x) == id(y)) # True
print(id(z) == id(m)) # True
#--------------------------------------------------------------------------------------
78. # """ Dictionary comprehension"""
dict_1 = {'key 1' : 2, 'key 2' : 3}

dict_1 = {key.replace(' ','_'):value for (key, value) in dict_1.items()}
print(dict_1)

#--------------------------------------------------------------------------------------
79. """ Class attributes and object attributes """

class Test:
    b = 3
    
    def __init__(self, a):
        self.b = a

obj_2 = Test(67)
print(Test.b)   # 3
print(obj_2.b)  # 67

#--------------------------------------------------------------------------------------
80. # Convert time into years, days, hours and minutes

def convert_minutes_to_time(n): 

    years  = n // (365 * 24 * 60)
    n = n % (365 * 24 * 60)
    day = n // (24 * 60) 
  
    n = n % (24 * 60) 
    hour = n // 60
  
    n %= 60
    minutes = n
    
    print ( years, "years", 
            day, "days",
            hour, "hours",
            minutes, "minutes" )

n = 645640
convert_minutes_to_time(n)

#--------------------------------------------------------------------------------------
81. 
"""
Oneliner if statements
"""
# Example 1
value_one = '-67'
value = 67
if '-' in value_one : value = -value
print(value)

# Example 2
a, b = 10, 20
minimum = a if a < b else b
print(minimum)

#--------------------------------------------------------------------------------------
82. # Set comprehension

nums = {n**2 for n in range(10)}
print(nums)

# A set is an unordered and mutable collection of unique elements
# The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and stops before a specified number.
## range(start, stop, step)

#--------------------------------------------------------------------------------------
83. # Selection sort

A = [64, 25, 12, 22, 11] 

for i in range(len(A)): 

	min_id = i 
	for j in range(i+1, len(A)): 
		if A[min_id] > A[j]: 
			min_id = j 	 
	A[i], A[min_id] = A[min_id], A[i] 

print ("After selection sort") 
print (A)
#--------------------------------------------------------------------------------------
84. # Insertion sort

def insertion_sort(arr):

    for i in range(1, len(arr)):

        key = arr[i]

        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


arr = [12, 11, 13, 5, 6]
insertion_sort(arr)
print('List after insertion sort : ', arr)

# o/p:

#>>> 
#================ RESTART: C:\Users\Abhay\OneDrive\Desktop\two.py ===============
#List after insertion sort :  [5, 6, 11, 12, 13]
#>>> 

#--------------------------------------------------------------------------------------
# 85.

#--------------------------------------------------------------------------------------
# 86. 

#--------------------------------------------------------------------------------------
87.

"""
Enter number7
7
      A 
     B B 
    C C C 
   D D D D 
  E E E E E 
 F F F F F F 
G G G G G G G 
"""

alphabets = ['A', 'B', 'C', 'D', 'E', 'F','G','H', 'I','J','K','L','M']

number = int(input('Enter number'))
print(number)

i = 0
while i < number:
    k = number - i
    for j in range(k - 1): print(' ', end = '')
    for j in range(i + 1): print(alphabets[i], end = ' ')
    print()
    i += 1

#--------------------------------------------------------------------------------------
88. # Converting -ve number to +ve number

a = -4
b = 6

a = abs(a)
b = abs(b)

print(a)
print(b)

#--------------------------------------------------------------------------------------
89. # Using random
import random 

a_list = list(range(2, 25, 4))
print(a_list)

# Example 1
print ("A random number from list is : ",end="") 
print (random.choice(a_list)) 

# Example 2
print ("A random number from range is : ",end="") 
print (random.randrange(20, 50, 3))

# Example 3
random.shuffle(a_list)
print(a_list)

#--------------------------------------------------------------------------------------
90.
"""
i / p = [3, 5]
o / p = [[3, 5],[3, 5, 2], [3, 5, 2, 1], [3, 5, 2, 1, 4]]
"""

from copy import deepcopy

def simple(a_list):
    b_list = []
    b_list.append(a_list)
    c_list_length = 1

    length = 0
    while len(a_list) != length:
        
        length = len(a_list)
        a_list = deepcopy(a_list)
        
        while c_list_length != 0:
            j = 0
            while j < length - c_list_length:
                difference = a_list[length - c_list_length] - a_list[j]

                if difference < 0:
                    difference = -difference

                if difference not in a_list:
                    a_list.append(difference)

                j += 1
            c_list_length -= 1
            
        if b_list[-1] != a_list:
            b_list.append(a_list)
            c_list = list(set(b_list[-1]) - set(b_list[-2]))
            c_list_length = len(c_list)
            
    return b_list

print(simple([10, 16]))

#print(simple([3, 5]))

# [[3, 5], [3, 5, 2], [3, 5, 2, 1], [3, 5, 2, 1, 4]]
# [[10, 16], [10, 16, 6], [10, 16, 6, 4], [10, 16, 6, 4, 12, 2], [10, 16, 6, 4, 12, 2, 8, 14]]

#--------------------------------------------------------------------------------------
91.
# List operations
# Itearation using only for loop

# Example 1
a_list = [6, 4, 2, 1, 8, 3]

length = len(a_list)

for i in range(length):
    print(a_list[i], end = ' ')

# Example 2
a_list = [6, 4, 2, 1, 8, 3, 67, 43, 65, 22, 32, 54]
length = len(a_list)

for i in range(0, length, 2):
    print(a_list[i], end = ' ')

# Example 3
a_list = [6, 4, 2, 1, 8, 3, 67, 43, 65, 22, 32, 54]

length = len(a_list)

for i in range(length-1, -1, -1):
    print(a_list[i], end = ' ')

# Example 4
my_list = ['apple', 'orange'] 
my_list.append('peech')
another_list = [6,0,4,1]
my_list.append(another_list)

print(my_list)

# Example 5
my_list = ['apple', 'orange'] 
my_list.append('peech')
another_list = [6,0,4,1]
my_list.extend(another_list)

print(my_list)

# Example 6
a_list = [2, 1, 3, 5, 3, 8]
a_list.sort()
print(a_list)

# Example 7
a_list = [2, 1, 3, 5, 3, 8]
a_list.reverse()
print(a_list)

# Example 8
language = ['French', 'English', 'German']
language_tuple = ('Spanish', 'Portuguese')
language_set = {'Chinese', 'Japanese'}

language.extend(language_tuple)

print('New Language List: ', language)

language.extend(language_set)

print('Newest Language List: ', language)

# Example 9

a = [1, 2]
b = [3, 4]
a += b

print('a = ', a)

# Example 10

vowel = ['a', 'e', 'i', 'u']

vowel.insert(3, 'o')

print('Updated List: ', vowel)

# Example 11

mixed_list = [{1, 2}, [5, 6, 7]]

number_tuple = (3, 4)

mixed_list.insert(1, number_tuple)

print('Updated List: ', mixed_list) # Updated List:  [{1, 2}, (3, 4), [5, 6, 7]]

# Example 12
# animal list
animal = ['cat', 'dog', 'rabbit', 'guinea pig']

animal.remove('rabbit')

print('Updated animal list: ', animal) # Updated animal list:  ['cat', 'dog', 'guinea pig']

# Example 13

# If a list contains duplicate elements
# the remove() method removes only the first instance

# animal list
animal = ['cat', 'dog', 'dog', 'guinea pig', 'dog']

# 'dog' element is removed
animal.remove('dog')

#Updated Animal List
print('Updated animal list: ', animal) # Updated animal list:  ['cat', 'dog', 'guinea pig', 'dog']

# Example 14

# vowels list
vowels = ['a', 'e', 'i', 'o', 'i', 'u']

# count element 'i'
count = vowels.count('i')

# print count
print('The count of i is:', count)

# count element 'p'
count = vowels.count('p')

# print count
print('The count of p is:', count)

# The count of i is: 2
# The count of p is: 0

# Example 15

# random list
random = ['a', ('a', 'b'), ('a', 'b'), [3, 4]]

# count element ('a', 'b')
count = random.count(('a', 'b'))

# print count
print("The count of ('a', 'b') is:", count)

# count element [3, 4]
count = random.count([3, 4])

# print count
print("The count of [3, 4] is:", count)

The count of ('a', 'b') is: 2
The count of [3, 4] is: 1

# Example 16

# programming language list
language = ['Python', 'Java', 'C++', 'French', 'C']

# Return value from pop()
# When 3 is passed
return_value = language.pop(3)
print('Return Value: ', return_value)

# Updated List
print('Updated List: ', language)

Return Value:  French
Updated List:  ['Python', 'Java', 'C++', 'C']

# Example 17
# programming language list
language = ['Python', 'Java', 'C++', 'Ruby', 'C']

# When index is not passed
print('When index is not passed:') 
print('Return Value: ', language.pop())
print('Updated List: ', language)

# When -1 is passed
# Pops Last Element
print('\nWhen -1 is passed:') 
print('Return Value: ', language.pop(-1))
print('Updated List: ', language)

# When -3 is passed
# Pops Third Last Element
print('\nWhen -3 is passed:') 
print('Return Value: ', language.pop(-3))
print('Updated List: ', language)

"""
When index is not passed:
Return Value:  C
Updated List:  ['Python', 'Java', 'C++', 'Ruby']

When -1 is passed:
Return Value:  Ruby
Updated List:  ['Python', 'Java', 'C++']

When -3 is passed:
Return Value:  Python
Updated List:  ['Java', 'C++']
"""

# Example 18

# Defining a list
a_list = [{1, 2}, ('a'), ['1.1', '2.2']]

# clearing the list
a_list.clear()

print('List:', a_list)

# Example 19
# Defining a list
list = [{1, 2}, ('a'), ['1.1', '2.2']]

# clearing the list
del list[:]

print('List:', list)


#--------------------------------------------------------------------------------------
92.
class BankAccount:
	names = ['Abhay', 'Vikas', 'Pratik']
	
	def __init__(self, name, deposit):
	    self.name = name
	    self.deposit = deposit
		
	def display(self, withdrawl = 0):
	    print('Name is {0}'.format(self.name))
	    print('Deposit is {0}'.format(self.deposit))

	    if withdrawl:
	        self.deposit = self.deposit - withdrawl
		
	    print('Total amount {0}'.format(self.deposit))

	def verify_name(self):
	    if self.name in BankAccount.names:
	        print('Username is valid')
	    else:
	        print('Username is invalid')

person_1 = BankAccount('Abhay', 50000)
person_1.verify_name()
person_1.display(withdrawl = 30000)
person_1.display()
person_1.display(withdrawl = 10000)
person_1.display()

#--------------------------------------------------------------------------------------

93.

# Source : https://www.geeksforgeeks.org/python-program-to-validate-an-ip-address/
import re

regex = "^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$"

def verify_ip_address(ip):

	if(re.search(regex, ip)):
		print("Valid ip address")
		
	else:
		print("Invalid ip address")

if __name__ == '__main__' :
	ip = input('Enter IP address : ')
	verify_ip_address(ip)

#--------------------------------------------------------------------------------------
94. # Removing dupicate words

input_string = 'hello try hello no python programming'
list_a = input_string.split(' ')
list_b = []

i = 0
while i < len(list_a):
	if list_a[i] not in list_b:
		list_b.append(list_a[i])
	i += 1
output_string = ' '.join(list_b)
print(output_String)

#--------------------------------------------------------------------------------------
95. # Print from reverse

a_string = 'hello try hello no python programming'
a_list = a_string.split()

start, end = 0, len(a_list) - 1
while start < end:
    a_list[start], a_list[end] = a_list[end], a_list[start]
    start += 1
    end -= 1

a_string = ' '.join(a_list)
print(a_string)

#o/p
# >>> 
# =============== RESTART: C:\Users\Abhay\OneDrive\Desktop\rough.py ==============
#programming python no hello try hello
# >>> 
#--------------------------------------------------------------------------------------
96. # Odd and even numbers via list comprehension

numbers = [4,5,6,7,8,9]
even = [i for i in numbers if i % 2 == 0]
odd = [i for i in numbers if i % 2 != 0]

print(even)
print(odd)

#--------------------------------------------------------------------------------------
97. #
>>> a = (0,1,2,3,4)
>>> b = slice(0,2)
>>> print(a[b])
(0, 1)
>>> 
#--------------------------------------------------------------------------------------
98. # maximum continuous zeros

k = 110001100001
number = str(k)
length = len(number)

count = 0
max_count = 0

i = 0
while i < length:
	if number[i] == '0':
		j = i + 1
		count = 1
		
		while number[j] == '0':
			count += 1
			j += 1
		
		if count > max_count:
			max_count = count

	i += 1

print(max_count)

# Time_complexity : N^2
#--------------------------------------------------------------------------------------
99.
#PART_1
a = [1,2,3,4,5,6,7,8,9,10]
print(a[-5:-1])
#O/P  : [6,7,8,9]

#PART_2
a = [1,2,3,4,5,6,7,8,9,10]
print(a[-1:-5])
#O/P  : []

#--------------------------------------------------------------------------------------
100. # Using reload module

#########################
import pdb
def sample(x = 50):
    b = 0
    b = b + 2 * x
    pdb.set_trace()
    print(b)

sample()

##
(Pdb) import a
50
(Pdb) import a
(Pdb) import importlib
(Pdb) importlib.reload(a)
100
<module 'a' from '/home/abhay/Desktop/a.py'>
(Pdb)

##

import pdb
def sample(x = 50):
    b = 0
    b = b + 2 * x
    pdb.set_trace()
    print(b)

sample()
#--------------------------------------------------------------------------------------
101. # enumerate()

# A lot of times when dealing with iterators, we also get a need to keep a count of iterations.
# Python eases the programmers’ task by providing a built-in function enumerate() for this task.

# Example_1
l1 = ["eat","sleep","repeat"] 
s1 = "geek"
  
# creating enumerate objects 
obj1 = enumerate(l1) 
obj2 = enumerate(s1) 
  
print ("Return type:",type(obj1) )
print (list(enumerate(l1)))
  
# changing start index to 2 from 0 
print (list(enumerate(s1,2)))
print((dict(enumerate(s1,2))))

# o/p:
# >>> 
# ============== RESTART: C:\Users\Abhay\OneDrive\Desktop\editor.py ==============
# Return type: <class 'enumerate'>
# [(0, 'eat'), (1, 'sleep'), (2, 'repeat')]
# [(2, 'g'), (3, 'e'), (4, 'e'), (5, 'k')]
# {2: 'g', 3: 'e', 4: 'e', 5: 'k'}
# >>> 

# Example_2
a_list = [[1, 1], [2, 2], [3, 3], [0, 4], [-2, 6], [4, 0], [2, 1]]

for x, y in enumerate(a_list):
    print (x, ':', y)
    
# o/p:
# >>> 
# ============== RESTART: C:\Users\Abhay\OneDrive\Desktop\editor.py ==============
# 0 : [1, 1]
# 1 : [2, 2]
# 2 : [3, 3]
# 3 : [0, 4]
# 4 : [-2, 6]
# 5 : [4, 0]
# 6 : [2, 1]
# >>> 
#--------------------------------------------------------------------------------------
102. # namedtuple()

# Python supports a type of container like dictionaries called “namedtuples()” present in module, “collection“.
# Like dictionaries they contain keys that are hashed to a particular value. But on contrary, it supports both
# access from key value and iteration, the functionality that dictionaries lack.

# Example 1

# importing "collections" for namedtuple() 
import collections 
  
# Declaring namedtuple() 
Student = collections.namedtuple('Student',['name','age','DOB']) 
  
# Adding values 
S = Student('Nandini','19','2541997') 
  
# Access using index 
print ("The Student age using index is : ",end ="") 
print (S[1]) 
  
# Access using name  
print ("The Student name using keyname is : ",end ="") 
print (S.name) 
  
# Access using getattr() 
print ("The Student DOB using getattr() is : ",end ="") 
print (getattr(S,'DOB'))

O/P:

>>> 
================ RESTART: C:\Users\abhsingh\Desktop\sample_45.py ===============
The Student age using index is : 19
The Student name using keyname is : Nandini
The Student DOB using getattr() is : 2541997
>>> 

#--------------------------------------------------------------------------------------
103. # any() Function

# a. any() function example with lists

# all values are true
lis1 = [10, 20, 30, 40]
print(any(lis1))

# all values are false
lis2 = [0, False]
print(any(lis2))

# one value is false, others are true
lis3 = [0, 10, 5, 15]
print(any(lis3))

# one value is true, others are false
lis4 = [10, 0, False]
print(any(lis4))

# empty iterable
lis5 = []
print(any(lis5))

================ RESTART: C:\Users\abhsingh\Desktop\sample_45.py ===============
True
False
True
True
False
>>>

#-----------------------------------------

# b. any() function example with Dictionaries

# all keys are true
dict1 = {1: 'False', 2: 'True'}
print(any(dict1))

# all keys are false
dict2 = {0: 'False', False: 'True'}
print(any(dict2))

# one key is false, other is true
dict3 = {0: 'False', 1: 0}
print(any(dict3))

# One key is true, '0' is not false its True
# because '0' is a string not a number
# if it is 0 without quotes then its false
dict4 = {'0': 'False'}
print(any(dict4))

# empty dictionary
dict5 = {}
print(any(dict5))

================ RESTART: C:\Users\abhsingh\Desktop\sample_45.py ===============
True
False
True
True
False
>>> 

#--------------------------------------------------------------------------------------
104.
x = 'a' * 8
y = 'b' * 5

if x > y:
    print(x)
elif x < y:
    print(y)
else:
    print('equal')

#OUTPUT
##>>> 
##=================== RESTART: C:\Users\abhsingh\Desktop\sam.py ==================
##bbbbb
##>>> 

#--------------------------------------------------------------------------------------
105. # Inverting Binary tree


#--------------------------------------------------------------------------------------
106.
file_output = open('name.txt', 'w')
months_days = {6: 30,7:31, 8:31, 9:30 ,10:31, 11:30 ,12:31 }

for key, value in months_days.items():
    i = 1
    for i in range(i, value + 1):
        file_output.write(str(i) + '_' + str(key) + '_2021\n')
        i += 1

file_output.close()

#o/p:
"""
10_6_2021
11_6_2021
12_6_2021
13_6_2021
14_6_2021
15_6_2021
16_6_2021
17_6_2021
18_6_2021
19_6_2021
"""
#--------------------------------------------------------------------------------------
107. # Removing all element from a list greater than 35

a_list = [10, 20, 30, 40, 50, 60, 70]
 
print('Original list')
print(a_list)

length = len(a_list)
i=0
while i < length:
	if a_list[i] > 35:
	    a_list.remove(a_list[i])
	    length = length - 1  
	    continue
	i = i + 1

print ('New list')
print (a_list)

#--------------------------------------------------------------------------------------
108.
#--------------------------------------------------------------------------------------
109.

#--------------------------------------------------------------------------------------
110.

#--------------------------------------------------------------------------------------
111. # Group of stars 

number_of_groups = int(input('Enter number of groups : '))

i = 1
while i <= 5:
    k = number_of_groups
    while k > 0:
        j = 1
        while j <= i:
            print('*', end='')
            j += 1

        print(' '*(6 - i), end='')
        k -= 1

    print()
    i += 1
	
# o/p :

# >>> 
# ============== RESTART: C:\Users\Abhay\OneDrive\Desktop\editor.py ==============
# Enter number of groups : 6
# *     *     *     *     *     *     
# **    **    **    **    **    **    
# ***   ***   ***   ***   ***   ***   
# ****  ****  ****  ****  ****  ****  
# ***** ***** ***** ***** ***** ***** 
# >>> 

#--------------------------------------------------------------------------------------
112. # Dynamic programming

# Links :
# https://medium.com/geekculture/how-to-solve-fibonacci-sequence-using-dynamic-programming-b7cd784ee10d
	
# Dynamic programming was introduced by American mathematician Richard Bellman. The name “dynamic” has nothing to do with the actual process.
# There is nothing dynamic in dynamic programming!.

#---------------------------------------------------------------------------------------

# Three steps :
# a. Recursion
# b. Store (Memoize)
# c. Bottom-up

#--------------------------------------------------------------------------------------
113. # Transposing a matrix

# Source : https://www.geeksforgeeks.org/python-transpose-elements-of-two-dimensional-list/

# M1

import numpy

a_list= [[4, 5, 3, 9],
         [7, 1, 8, 2],
         [5, 6, 4, 7]]

print(numpy.transpose(a_list))

# >>> 
# ============== RESTART: C:\Users\Abhay\OneDrive\Desktop\editor.py ==============
# [[4 7 5]
#  [5 1 6]
#  [3 8 4]
#  [9 2 7]]
# >>> 

# M2

def transpose(l1, l2):
	l2 = list(map(list, zip(*l1)))
	return l2

l1 = [[4, 5, 3, 9],
      [7, 1, 8, 2],
      [5, 6, 4, 7]]

l2 = []
print(transpose(l1, l2))

# o / p :
#  
# >>> 
# ============== RESTART: C:\Users\Abhay\OneDrive\Desktop\editor.py ==============
# [[4, 7, 5], [5, 1, 6], [3, 8, 4], [9, 2, 7]]
# >>> 

# M3 ## outdated

def transpose(a_list):
    number_of_columns = len(a_list[0])
    number_of_rows = len(a_list)
    
    b_list = [[None for x in range(number_of_rows)] for y in range(number_of_columns)]
    
    i = 0
    while i < number_of_columns:
        j = 0
        while j < number_of_rows:
            b_list[i][j] = a_list[j][i]
            j += 1
        i += 1
        
    return b_list

a_list = [[1, 2],
          [3, 4],
          [5, 6]]

print(transpose(a_list))

# o/p:
# >>> 
# ============== RESTART: C:\Users\Abhay\OneDrive\Desktop\editor.py ==============
# [[1, 3, 5], [2, 4, 6]]
# >>> 

# M4 
def transpose(a_list, b_list):
    for i in range(len(a_list[0])):
        row =[]
        for item in a_list:
            row.append(item[i])
        b_list.append(row)
    return b_list

a_list = [[4, 5, 3, 9], [7, 1, 8, 2], [5, 6, 4, 7]]
b_list = []
print(transpose(a_list, b_list))

# o/p :

# >>> 
# ============== RESTART: C:\Users\Abhay\OneDrive\Desktop\editor.py ==============
# [[4, 7, 5], [5, 1, 6], [3, 8, 4], [9, 2, 7]]
# >>> 
#--------------------------------------------------------------------------------------

114. # Tiles problem

a_list = ['a', 'b', 'c', '#', 'e', 'f', 'm', '#'] # // True
b_list = ['#', 'b', 'c', '#', 'e', 'f', 'm', '#'] # // False
c_list = ['1', 'b', 'c', '#', 'e', '#', '#', 'l'] # // False
d_list = ['#', 'b', 'c', 'j', '#', 'o', 'p', 'l', '#', '#'] # // True

def verify_tiles(a_list):
    length = len(a_list)
    count = 0

    j = 0
    while j < length:
        if a_list[j] != '#':
            count += 1
            j += 1
            continue

        if count < 3 and count != 0:
            return False
        else:
            j += 1
            count = 0

    if count < 3 and count != 0:
        return False
    
    return True
        
print((verify_tiles(d_list)))

115. # Wall problem

def verify_wall(a_list):

    length = len(a_list[0])
    i = 0
    
    while i < length:
        count = 0
        j = 0
        while j < length:
            if a_list[i][j] != '#':
                count += 1
                j += 1
                continue
                
            if count < 3 and count != 0:
                return False
            else:
                j += 1
                count = 0
        if count < 3 and count != 0:
            return False
        
        i += 1

    return True

a_list = [['a', 'b', 'c', 'd', 'e'],
          ['e', 'f', 'k', 'd', 'g'],
          ['#', '#', '#', '#', '#'],
          ['a', 'm', 'n', 'd', 'k'],
          ['1', '2', '#', 'n', '#']]

print(verify_wall(a_list))

"...##" #[if no element between 2 tiles then it is fine]

116. # Perfect wall problem

def verify_wall(a_list):

    length = len(a_list[0])
    i = 0
    
    while i < length:
        count = 0
        j = 0
        while j < length:
            if a_list[i][j] != '#':
                count += 1
                j += 1
                continue
                
            if count < 3 and count != 0:
                return False
            else:
                j += 1
                count = 0

        if count < 3 and count != 0:
            return False
        
        i += 1

    return True

def transpose(a_list):
    number_of_columns = len(a_list[0])
    number_of_rows = len(a_list)
    
    b_list = [[None for x in range(number_of_rows)] for y in range(number_of_columns)]
    
    i = 0
    while i < number_of_columns:
        j = 0
        while j < number_of_rows:
            b_list[i][j] = a_list[j][i]
            j += 1
        i += 1
        
    return b_list

####################################
####################################

a_list = [['#', '#', 'c', 'z', 'e'],
          ['g', 'y', 'k', 'd', 'g'],
          ['o', 'e', 'h', 'z', 't'],
          ['a', 'm', 'n', 'd', '#'],
          ['1', '2', '3', '#', '#']]

result = verify_wall(a_list)

if result is True:
    print('Proceed for column-wise verification')
else:
    print('Broken wall')
    
a_list = transpose(a_list)
result = verify_wall(a_list)

if result is True:
    print('Perfect wall')
else:
    print('Broken wall')

#--------------------------------------------------------------------------------------
117. # Tower of Hanoi
# Source : https://www.geeksforgeeks.org/python-program-for-tower-of-hanoi/

def tower_of_hanoi(n , source, destination, auxiliary):
    if n==1:
        print ("Move disk 1 from source",source,"to destination",destination)
        return
    tower_of_hanoi(n-1, source, auxiliary, destination)
    print ("Move disk",n,"from source",source,"to destination",destination)
    tower_of_hanoi(n-1, auxiliary, destination, source)

n = 4
tower_of_hanoi(n,'A','B','C')

# o/p :
# 
# >>> 
# ============== RESTART: C:\Users\Abhay\OneDrive\Desktop\editor.py ==============
# Move disk 1 from source A to destination C
# Move disk 2 from source A to destination B
# Move disk 1 from source C to destination B
# Move disk 3 from source A to destination C
# Move disk 1 from source B to destination A
# Move disk 2 from source B to destination C
# Move disk 1 from source A to destination C
# Move disk 4 from source A to destination B
# Move disk 1 from source C to destination B
# Move disk 2 from source C to destination A
# Move disk 1 from source B to destination A
# Move disk 3 from source C to destination B
# Move disk 1 from source A to destination C
# Move disk 2 from source A to destination B
# Move disk 1 from source C to destination B
# >>>

#--------------------------------------------------------------------------------------
118. 

# a. The modulo operator in Python behaves as follows when used with a negative first operand:
# -x % y == -(x % y) + y
#
# b. The modulo operator always yields a result with the same sign as its second operand (or zero).

m = -5
k = m % 3
print(k)

# o/p :
# 
# >>> 
# ============== RESTART: C:\Users\Abhay\OneDrive\Desktop\editor.py ==============
# 1
# >>> 

#--------------------------------------------------------------------------------------
# 119. GCD or HCF of 2 numbers using modulo operator in Euclidean algorithm.

# M1, Source : https://www.geeksforgeeks.org/c-program-find-gcd-hcf-two-numbers/
def gcd(a,b):
    if (b == 0):
        return a
    return gcd(b, a%b)

a = 98
b = 56
if(gcd(a, b)):
    print('GCD of', a, 'and', b, 'is', gcd(a, b))
else:
    print('not found')

# Time Complexity: O(log(max(a,b)) | Auxiliary Space: O(log(max(a,b))

# o/p:
# >>> 
# ============== RESTART: C:\Users\Abhay\OneDrive\Desktop\editor.py ==============
# GCD of 98 and 56 is 14
# >>> 

# M2
import math
print(math.gcd(98, 56))

# >>> 
# ============== RESTART: C:\Users\Abhay\OneDrive\Desktop\editor.py ==============
# 14
# >>> 

#--------------------------------------------------------------------------------------
# 120. Matrix multiplication

# Source : https://www.geeksforgeeks.org/python-program-multiply-two-matrices/
# Time Complexity: O(M*M*N), as we are using nested loop traversing, M*M*N.
# Space Complexity: O(M*N), as we are using a result matrix which is extra space.
	
A = [[12, 7, 3],
    [4, 5, 6],
    [7, 8, 9]]

B = [[5, 8, 1, 2],
    [6, 7, 3, 0],
    [4, 5, 9, 1]]
    
result = [[0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]]

for i in range(len(A)):
    for j in range(len(B[0])):
        for k in range(len(B)):
            result[i][j] += A[i][k] * B[k][j]

for r in result:
    print(r)

# o/p:

# >>> 
# ============== RESTART: C:\Users\Abhay\OneDrive\Desktop\simple.py ==============
# [114, 160, 60, 27]
# [74, 97, 73, 14]
# [119, 157, 112, 23]
# >>> 

#--------------------------------------------------------------------------------------
# 121. Boolean matrix

# O(row*column) time |  O(1) space
def modify_matrix(matrix):
    row_column_1 = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 1:
                row_column_1.append([i, j])
                
    for i in range(len(row_column_1)):
        matrix = convert_to_1(matrix, row_column_1[i])
        
    return matrix

def convert_to_1(matrix, row_column_1):
    a, b = row_column_1
    for i in range(len(matrix[a])):
        matrix[a][i] = 1
    for i in range(len(matrix)):
        matrix[i][b] = 1
    return matrix
        
                   
matrix = [[0, 0, 1, 0],
          [0, 1, 0, 0],
          [0, 0, 0, 0]]

result = modify_matrix(matrix)
print(result)

# o/p:
# >>> 
# ============== RESTART: C:\Users\Abhay\OneDrive\Desktop\simple.py ==============
# [[1, 1, 1, 1], [1, 1, 1, 1], [0, 1, 1, 0]]
# >>>

#--------------------------------------------------------------------------------------
# 122. Recursion explained
def sample(n):
    total = 0
    if n == 1:
        return 1
    else:
        total += 1
        print(total)
        return n + sample(n - 1)

result = sample(4)
print(result)

# >>> 
# ================== RESTART: C:\Users\Ankur\Desktop\back_up.py ==================
# 1
# 1
# 1
# 10
# >>> 

#--------------------------------------------------------------------------------------
