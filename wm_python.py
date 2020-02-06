# Copyright © 2020 Elephant. All rights reserved

Keeping main counter as i

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
# M2
print(2)
print(3)
print(5)
for i in range(2, 100):
    if i % 2 != 0 and i % 3 !=0 and i % 5 != 0:
        print(i)
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
#M3
user_string = input('Enter string')
input_string = list(user_string)

length = len(input_string)

i = 0
flag = 1
while i < length // 2:
    if input_string[i] != input_string[-1 -i]:
        flag =0
        break
    i += 1
        
if flag:
    print('{0} is a palindrome'.format(user_string))
else:
    print('{0} is not a palindrome'.format(user_string))

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
    print('{0} is a perfect square'.format(num))
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
length = len(alist)
flag = 0
i = 0
while i < length:
    if num == alist[i]:
        flag = 1
        break
    i += 1

if flag:
    print('{0} is at index {1}'.format(num,i + 1))
else:
    print('{0} is not present'.format(num))

#--------------------------------------------------------------------------------------
#10. Binary search

def binary_search(a_list, num):
    low = 0
    high = len(a_list) - 1

    while low <= high:
        mid = (low + high) // 2

        if num == a_list[mid]:
            return mid

        if num < alist[mid]:
            high = mid - 1
        else:
            low = mid + 1
        
    return -1

def main():
    print('Enter numbers in sorted fashion')
    a_list = [int(x) for x in input().split()]
    num = int(input('Enter number'))
    index = binary_search(a_list, num)

    if index == -1:
        print('{0} is not present in the list'.format(num))
    else:
        print('{0} is present at index {1}'.format(num, index))

if __name__ == '__main__':
    main()

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
num = input('Enter number to add')
num = int(num)
position = input('Enter position')
position = int(position)
 
a_list.append(None)

i = len(a_list) - 1
while i >= position - 1:
    alist[i + 1] = a_list[i]
    i -= 1

alist[position - 1] = num

print('New list is {0}'.format(alist))

#--------------------------------------------------------------------------------------
#14. Delete an integer from a list

a_list = [int(x) for x in input().split()]
num = input('Enter number')
num = int(num)
flag = 0
length = len(a_list)
i = 0
while i < length - 1:
    if num == a_list[i] or flag == 1:
        a_list[i] = a_list[i + 1]
        flag = 1
    
    i += 1

del a_list[-1]

print('New list is {0}'.format(alist))

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
with open('input.txt') as f_one:
    with open('output.txt', 'w') as f_two:
        for line in f_one:
            f_two.write(line)

#-----------------------------------------
#M2

file_one = open('input.txt','r')
file_two = open('output.txt','w')

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

out_dict = dict(zip(keys,values))

print(out_dict)
print(list(out_dict.keys()))
print(list(out_dict.values()))

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

#Example 1, Print square of all even numbers
#M1
nums = range(10)
square_evens = [x**2 for x in nums if x%2 == 0 and x > 4]
print(square_evens)

#M2
nums = range(4, 19, 2)
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
# Removing all elements greater than 5
a = [24 , 66 , 10, 2, 3, 44, 55, 6]
a = [i for i in a if i < 5]
print(a)

#--------------------------------------------------------------------------------------
32.
""" decorators """

"""
Decorators allow us to wrap another function in order to extend the behavior of wrapped function,
without modifying it.
"""

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
35.


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
39.
output = """
HMM Internal Global State

Start reason                   : configuration
Sup state                      : Active
Restart type                   : Stateless
Platform Cap                   : Fwd | Auto-config
All core components up         : Yes
      Comp            Uuid       Pss_idx    Up         Dynamic    Init
      clis            261        0          True       False      True
      ifmgr           318        1          True       False      True
      l3vm            445        6          True       False      True
      l2fm            410        9          True       False      True
      vpc             593        12         True       True       True
      nve             1251       17         True       True       True
HMM thread                     : 0xe04fdb40
Cli ready                      : Yes
Debug Flags                    : Off
Confcheck                      : CAP-AUTO-CFG-UHOST-V1 (Counters 1)
System Ready                   : Yes
      Item                       Is Ready  
      [001] HMM SDB READY        True      

HMM Forwarding Internal Global State

HA Recovery in Progress        : False
All core components up         : Yes
      Comp            Uuid       Pss_idx    Up         Dynamic    Init
      clis            261        0          True       False      True
      adjmgr          264        2          True       False      True
      arp             268        3          True       False      True
      icmpv6          270        4          True       False      True
      netstack        545        5          True       False      True
      urib            273        7          True       False      True
      u6rib           274        8          True       False      True
      rpm             305        10         True       False      True
      l2rib           1290       11         True       True       True
      bgp             283        13         True       True       True
      hsrp_engine     406        14         False      True       False
      vrrp-eng        68         15         False      True       False
      pktmgr          263        16         True       False      True
      nve             1251       17         True       True       True
Libraries registered           : IP IPv6
Mobility Mode                  : EVPN-Seq-id
Duplicate Host detection       : 5 moves in 180 secs

HMM Profile Internal Global State

HA Recovery in Progress        : False
All core components up         : Yes
      Comp            Uuid       Pss_idx    Up         Dynamic    Init
      clis            261        0          True       False      True
      ifmgr           318        1          True       False      True
      bgp             283        13         True       True       True
      nve             1251       17         True       True       True
      adbm            1210       18         True       True       True
      port-profile    704        19         True       True       True
      vnsegment_mgr   1174       20         True       True       True
Auto-config Mode               : MT-FULL
Mock Flags                     : 
[OPTION] auto-id               : Not supported
[OPTION] auto-id               : Not supported
    Mock Flags
[OPTION] auto-val              : system_auto_val_vrfSegmentId
[OPTION] static-host           : Supported
Mock Flags
[OPTION] static-dci            : Not supported
[OPTION] auto-pull-host        : Supported
[OPTION] auto-pull-dci         : Supported

"""

output = output.split("Mock Flags",3)[2]
print(output)

output = output.split("\n")

for content in output:
    if "static-host" in content:
       break

if "Supported" in content:
    print(content)
else:
    print(content)

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
45. """ Spiral """
# 1 2 3 4 8 12 16 15 14 13 9 5 6 7 11 10
a = [[1,2,3,4],
     [5,6,7,8],
     [9,10,11,12],
     [13,14,15,16]]

L = 0
T = 0
B = 3
R = 3
dir = 0

while L <= R and T <= B:
    
    if dir == 0:        
        k = L
        while k <= R:
            print(a[T][k],end = ' ')
            k += 1
        T += 1 
        
    if dir == 1:
        k = T
        while k <= B:
            print(a[k][R],end = ' ')
            k += 1
        R -= 1
        
    if dir == 2:
        k = R
        while k >= L:
            print(a[B][k],end = ' ')
            k -= 1
        B -= 1
        
    if dir == 3:
        k = B
        while k >= T:
            print(a[k][L],end = ' ')
            k -= 1
        L += 1    
    dir = (dir + 1) % 4

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
49. """ Binary search tree"""

class Node(object):
    def __init__(self,data):
        self.value = data
        self.left = None
        self.right = None

class Tree(object):
    def __init__(self):
        self.root = None

    def insert(self,data):
        if self.root == None:
            self.root = Node(data)
        else:
            self._insert(self.root, data)
                
    def _insert(self,node, data):
        if(data < node.value):
            if(node.left is not None):
                self._insert(node.left, data)
            else:
                node.left = Node(data)
        else:
            if(node.right is not None):
                self._insert(node.right, data)
            else:
                node.right = Node(data)

    def preorder(self):
        if (self.root != None):
            self._preorder(self.root)

    def _preorder(self,cur):
        print(cur.value,end = ' ')
        if cur.left is not None:
            self._preorder(cur.left)
        if cur.right is not None:
            self._preorder(cur.right)

    def postorder(self):
        if self.root is not None:
            self._postorder(self.root)

    def _postorder(self, cur):
        if cur.left is not None:
            self._postorder(cur.left)

        if cur.right is not None:
            self._postorder(cur.right)

        print (cur.value,end = ' ')

    def inorder(self):
        if self.root is not None:
            self._inorder(self.root)

    def _inorder(self, cur):
        if cur.left is not None:
            self._inorder(cur.left)
        print (cur.value,end = ' ')
        if cur.right is not None:
            self._inorder(cur.right)
            
    def search(self,item):
        q = self.root
        self.found = False
        self.parent = None
    
        while q is not None:
            if q.value == item:
                self.found = True
                self.x = q
                return
            
            self.parent = q
        
            if(item < q.value):
                q = q.left
            else:
                q = q.right
            
    def delete(self,item):
        #self.found = False
        self.xsucc = None
        
        if (self.root is None):
            print("Empty tree")
            return -1
        
        self.search(item)
    
        if (self.found is False):
            print("Data not found")
            return -2
    
        if(self.x.left is not None) and (self.x.right is not None):
            self.parent = self.x
            self.xsucc = self.xsucc.right
        
            while (self.xsucc.left is not None):
                self.parent = self.xsucc
                self.xsucc = self.xsucc.left
            
            self.x.value = self.xsucc.value
            self.x = self.xsucc
        
        if (self.x.left is None) and (self.x.right is None):
            if self.parent.left is self.x:
                self.parent.left = None
            else:
                self.parent.right = None
            
            del self.x
            return
        
        if (self.x.left is None) and (self.x.right is not None):
            if(self.parent.left is self.x):
                self.parent.left = self.x.right
            else:
                self.parent.right = self.x.right
            
            del self.x      
            return
          
        if (self.x.left is not None) and (self.x.right is None):
            if(self.parent.left is self.x):
                self.parent.left = self.x.left
            else:
                self.parent.right = self.x.left
            
            del self.x
            return
            
link = Tree()
link.insert(5)
link.insert(10)
link.insert(13)
link.insert(2)
link.insert(3)
##link.insert(44)
##link.insert(15)
##link.insert(100)
link.inorder()
print()
link.delete(10)
link.delete(14)
link.delete(8)
link.delete(13)
link.inorder()
print()
link.preorder()
print()
link.postorder()
print()

#--------------------------------------------------------------------------------------
50. """ Merge sort"""

def merge_sort(a_list):
    print('Splitting', a_list)

    if len(a_list) >  1:
        mid = len(a_list) // 2

        left_half = a_list[:mid]
        right_half = a_list[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = 0
        j = 0
        k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                a_list[k] = left_half[i]
                i += 1
            else:
                a_list[k] = right_half[j]
                j += 1

            k += 1

        while i < len(left_half):
            a_list[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            a_list[k] = right_half[j]
            j += 1
            k += 1
    print('Merging ',a_list)

a_list = [int(x) for x in input().split()]
merge_sort(a_list)
print(a_list)

#--------------------------------------------------------------------------------------
51. """ Bubble sort """

def bubble_sort(a_list):
    length = len(a_list)
    for i in range(length):
        for j in range(0, length-1-i):
            if a_list[j] > a_list[j + 1]:
                a_list[j], a_list[j + 1] = a_list[j+1], a_list[j]
                
a_list = [65,43,56,89,4,17]
bubble_sort(a_list)
print(a_list)

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
            
        return 1

            
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
 
temp = number
rev = 0
 
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
    print('arg_one {1}',format(arg_one))
    print('arg_two {1}',format(arg_two))
    
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
number = int(input('Enter number '))

factorial = 1
i = number
while i > 1:
    factorial = factorial * i
    i -= 1
    
print('Factorial of {0} is {1}'.format(number, factorial))
     
#M2
#---

def factorial(number):
    if number == 1:
        return number
    else:
        return number * factorial(number - 1)

number = int(input('Enter a number : '))
    
if number < 0:
   print('Sorry, factorial does not exist for negative numbers')
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
67. Extract ip address, validate the same and tell which class does it fall under

output ="""
hostname sr1
host address 10.0.2.8/23
processor
"""

#M1
#---
import re
from ipaddress import IPv4Address
from ipaddress import IPv4Network

class_A = IPv4Network(('10.0.0.0', '255.0.0.0'))  # or IPv4Network("10.0.0.0\8")
class_B = IPv4Network(('172.16.0.0', '255.240.0.0'))  # or IPv4Network("172.16.0.0\12")
class_C = IPv4Network(('192.168.0.0', '255.255.0.0'))  # or IPv4Network("192.168.0.0\16")

def ip_class(ip_address):
    if ip_address in class_A:
        print('{0} belongs to Class A family'.format(ip_address))
    elif ip_address in class_B:
        print('{0} belongs to Class B family'.format(ip_address))
    elif ip_address in class_C:
        print('{0} belongs to Class C family'.format(ip_address))

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

#M2
#---
output ="""
hostname sr1
host address 10.0.2.8/23
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
    
ip_address = []
output = output.split('\n')
output = list(filter(None, output))

pattern = re.compile('(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.'
           	     '(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.'
                     '(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.'
                     '(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)')

for each in output:
    ip = re.search(pattern, each)
    if ip:        
        ip_address.append(ip.group(0))
        identify_class_ip_address(ip.group(0), int(ip.group(1)))
        
print(ip_address)
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

74. # Segregatting 0 and 1

# M1
def segregate_0_and_1(arr, size): 
  
    type0 = 0
    type1 = size - 1
      
    while type0 < type1: 
        if arr[type0] == 1: 
            arr[type0],  arr[type1] = arr[type1], arr[type0]
            type1 -= 1
        else: 
            type0 += 1

arr = [0, 1, 0, 1, 1, 1, 0, 0, 0, 1, 1] 
arr_size = len(arr) 
segregate_0_and_1(arr, arr_size) 
print('Array after segregation is {0}'.format(arr), end = ' ')

# M2

a_list = [0, 1, 0, 1, 1, 1, 0, 0, 0, 1, 1]

length = len(a_list)
count = 0
for i in a_list:
    if i == 0:
        count += 1

for i in range(0, count):
    a_list[i] = 0

for i in range(count, length):
    a_list[i] = 1

print(a_list)
#--------------------------------------------------------------------------------------

74.# Removing all element from a list greater than 5

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

def insertionSort(arr): 
 
    for i in range(1, len(arr)): 
  
        key = arr[i] 

        j = i-1
        while j >=0 and key < arr[j] : 
                arr[j+1] = arr[j] 
                j -= 1
        arr[j+1] = key 

arr = [12, 11, 13, 5, 6] 
insertionSort(arr) 
print ("Sorted list after insertion sort is:") 
print(arr)

#--------------------------------------------------------------------------------------
85. # Quick sort

def partition(arr,low,high): 
    i = ( low-1 )   
    pivot = arr[high]
  
    for j in range(low , high): 
 
        if   arr[j] <= pivot: 

            i = i+1 
            arr[i],arr[j] = arr[j],arr[i] 
  
    arr[i+1],arr[high] = arr[high],arr[i+1] 
    return ( i+1 ) 

def quickSort(arr,low,high): 
    if low < high: 
        pi = partition(arr,low,high)  
        quickSort(arr, low, pi-1) 
        quickSort(arr, pi+1, high) 
 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array after quick sort is:") 
print(arr)

#--------------------------------------------------------------------------------------
86. # Heap sort

def heapify(arr, n, i): 
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[i] < arr[l]: 
        largest = l 
  
    if r < n and arr[largest] < arr[r]: 
        largest = r 

    if largest != i: 
        arr[i],arr[largest] = arr[largest],arr[i]
  
        heapify(arr, n, largest) 
  
def heapSort(arr): 
    n = len(arr) 
  
    for i in range(n, -1, -1): 
        heapify(arr, n, i) 
  
    for i in range(n-1, 0, -1): 
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0) 
  
arr = [ 12, 11, 13, 5, 6, 7] 
heapSort(arr) 
n = len(arr) 
print ("Sorted array is") 
print(arr)

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
import random 

a_list = list(range(2, 25, 4))
print(a_list) # [2, 6, 10, 14, 18, 22]
random.shuffle(a_list)
print(a_list) # [6, 14, 2, 18, 22, 10]

#--------------------------------------------------------------------------------------
90.
"""
i / p = [3, 5]
o / p = [[3, 5],[3, 5, 2], [3, 5, 2, 1], [3, 5, 2, 1, 4]]
"""


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

ip = '10.16.177.18'

import re
result = re.match('([0-9]+).([0-9]+).([0-9]+).([0-9]+)', ip)

first = int(result.group(1))
second = int(result.group(2))
third = int(result.group(3))
fourth = int(result.group(4))

if first <= 255 and first >= 0:
	print('first Octet {0} is valid'.format(first))
	
if second <= 255 and second >= 0:
	print('second Octet {0} is valid'.format(second))
	
if third <= 255 and third >= 0:
	print('third Octet {0} is valid'.format(third))
	
if fourth <= 255 and fourth >= 0:
	print('fourth Octet {0} is valid'.format(fourth))

#--------------------------------------------------------------------------------------
94. # Removing dupicate words

str_a = 'hello try hello no python programming'
list_a = str_a.split(' ')
list_b = []

i = 0
while i < len(list_a):
	if list_a[i] not in list_b:
		list_b.append(list_a[i])
	i += 1
str_b = ' '.join(list_b)
print(str_b)

#--------------------------------------------------------------------------------------
95. # Print from reverse

str_a = 'hello try hello no python programming'
list_a = str_a.split(' ')

list_c = []
i = len(list_a) - 1
while i >= 0:
	list_c.append(list_a[i])
	i -= 1
	
str_b = ' '.join(list_c)
print(str_b)

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

count = 0 
max_count = 0 

i = 0 
while i < len(number):
    if number[i] == '0':
        count = 1 
        j = i + 1
        while j < len(number):
            if number[j] == '0':
                count += 1 
                j += 1
            else:
                break
            
            
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
