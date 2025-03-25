''' 
    Cheat Sheet:
'''


import math
#! F strings (less arguments and cleaner syntax, with automatic casting):
Name = "Nathan"
age = 21
#* instead of:
print("Hello, my name is " + Name + " and I am " + str(age) + " years old.") 
#* You can use f-strings:
print(f"Hello, my name is {Name} and I am {age} years old.")


#! Variable information:

#*  how to get data type of a variable:
name = "Nathan"
print(type(name))

#* short hand addition:
age = 21
age += 1
print(age)

#* Variable length:
name = "Nathan"
print(len(name))

#* find letter position in a string:
name = "Nathan"
print(name.find("a"))
#* find last position of a character in a string
print(f"{name.rfind("a")}th is the final position of letter a")

#* Capatalize + uppercase + lowercase + isdigit + isalpha + count letters + replace characters + displace multiple times:
name = "nathan"
print(name.capitalize()) #-> Nathan
print(name.upper())      #-> NATHAN
print(name.lower())      #-> nathan
print(name.isdigit())    #-> False
print(name.isalpha())    #-> True
print(name.count("a"))   #-> 2
print(name.replace("a", "o")) #-> Nothon
print(name * 3)         #-> NathanNathanNathan
print(name.title)

#! Multiple assignment: 

# * define multiple variables at once:
name, age, rizz = "Nathan", 21, True

#* define multiple variables the same:
Spongebob = Patrick = Sandy = Squidward = 30


#! Division (+ extras):

#* integer division:
number = 10
number //= 3 #(This is same as number = number // 3)
print(number) #-> 3

#* division with decimal numbers:
number = 10
number /= 3 #(This is same as number = number / 3)
print(number) #-> 3.333333333333

#* get remainder(MOD) (can be used to find if even or odd):
number = 10
number %= 3 #(This is same as number = number % 3)
print(number) #-> 1

#* round a number to nearest integer:
x = 3.145
result = round(x)
print(result) #-> 3

#* absolute value (distance from zero):
y = -5
result = abs(y)
print(result) #-> 5

#* power function:
result = pow(2, 3)
print(result) #-> 8

#* find largest number:
x = 5
y = 10
z = 15
result = max(x, y, z)
print(result) #-> 15

#* find smallest number:
result = min(x, y, z)
print(result) #-> 5

#* amount of decimal places after the decimal point:
circumference = 2 * 5 * math.pi
print(f"The circumference of the circle is {circumference:.2f}") #-> The circumference of the circle is 31.42
# can also be done like this:
print(f"The circumference of the circle is {round(circumference, 2)}") #-> The circumference of the circle is 31.42
#! Math functions (using import math):

#* Get value of pi:
pi = math.pi
print(pi)

#* get value of e:
e = math.e
print(e)

#* get square root of a number:
result = math.sqrt(25)
print(result) #-> 5.0

#* ceiling function (round up to nearest integer):
result = math.ceil(3.145)
print(result) #-> 4

#* floor function (round down to nearest integer):
result = math.floor(3.95)
print(result) #-> 3


#! one line else if shortcut ( Doesn't work with elif)

#* odd or even program
num = 10
result = "Even" if num % 2 == 0 else "Odd"
print(result)

#* second example
a = 4
b = 5
maxnum = a if a > b else b
minnum = a if a < b else b

#* final example
user = "Guest"
access_level = "Full Access" if user == "admin" else "Limited Access"
print(access_level)


#! help command

#* print help
#print(help(print))
#* str help
#print(help(print))


#! elif not command
#* without elif not:
username = "bob man"
if len(username) > 12:
    print("Your username cannot be longer that 12 characters")
elif username.find(" ") > -1:
    print("Your username cannot contain spaces")
else:
    print(f"Welcome {username}")

username = "bob man"
if len(username) > 12:
    print("Your username cannot be longer that 12 characters")
elif not username.find(" ") == -1:
    print("Your username cannot contain spaces")
else:
    print(f"Welcome {username}")


#! String indexing
credit_number = "1234-5678-9012-3456"
#                  [start:end:step]
#               step is amount go up by
print(credit_number[0]) #-> "1"
print(credit_number[5]) #-> "5"
print(credit_number[0:4]) #-> "1234" 
#* Same as 
print(credit_number[:4]) #-> "1234"
print(credit_number[5:]) #-> "5678-9012-3456"
print(credit_number[5:9]) #-> "5678"
print(credit_number[-1]) #-> "6"
print(credit_number[::5]) #-> "1293"
print(f"XXXX-XXXX-XXXX-{credit_number[-4:]}")


#! Extra f-string formatting:
#* format specifiers = {value:flags} format a value based on what are inserted
#* decimal rounding:
price1 = 3.14959
price2 = 3.1
print(f"The price is {price1:.2f}") #-> "The price is 3.15"
print(f"Price2 is {price2:.3f}") #-> "Price 2 is 3.100"
#* allocating space to show number
print(f"Price 1 is £{price1:10}") #-> "Price 1 is £   3.14959"
print(f"Price 2 is £{price2:10}") #-> "Price 2 is £       3.1"
#* "0" pad number
print(f"Price 1 is £{price1:010}") #-> "Price 1 is £0003.14959"
print(f"Price 2 is £{price2:010}") #-> "Price 2 is £00000003.1"
#* Left justify value
print(f"Price 1 is £{price1:<10}:") #-> "Price 1 is £3.14959   :"
print(f"Price 2 is £{price2:<10}:") #-> "Price 2 is £3.1       :"
#* centre aline
print(f"Price 1 is £{price1:^25}:") #-> "Price 1 is £         3.14959         :"
print(f"Price 2 is £{price2:^25}:") #-> "Price 2 is £           3.1           :"
#* show if value is positive
price3 = -4.968
print(f"Price 1 is £{price1:+}:") #-> Price 1 is £+3.14959:
print(f"Price 2 is £{price2: }:") #-> Price 2 is £ 3.1:
print(f"Price 3 is £{price3:+}:") #-> Price 3 is £-4.968:
#* thousands separator
price4 = 30789.56234
print(f"Price4 is £{price4:,} .") #-> Price4 is £30,789.56234 .
#* mixing flags
print(f"Price 4 is £{price4:+015,.2f} .") #-> Price 4 is £+0,000,030,789.56 .


#! For loops
for x in range(1,11):
    print(x) #-> "1 2 3 4 5 6 7 8 9 10" (all on new lines)
#* reversed
for x in reversed(range(1,11)):
    print(x) #-> "10, 9, 8, 7, 6, 5, 4, 3, 2, 1" (all on new lines)
#* Change increment
for x in range(1,11,2):
    print(x) #-> "1, 3, 5, 7, 9" (all on new lines)
#* for x in variable
num = "12345"
for x in num:
    print(x) #-> "12345" (all on new lines)
#* Skip number:
for x in range(1,21):
    if x == 13:
        continue
    else:
        print(x) #-> shows 1 to 20 without 13
#* break command
for x in range(1,21):
    if x == 13:
        break
    else:
        print(x) #-> prints up to 12
#* no new line
for x in range(1,11):
    print(x, end=" ") #-> "1 2 3 4 5 6 7 8 9"
print("")
print(name.title())
print("Hello world"[7:10])


#! List, Set, Tuple, Collection:
#* collection = single "variable" used to store multiple value
#*    list = [] ordered and changeable. Duplicated OK
#*     set = {} unordered and immutable, but ADD/REMOVE OK. NO duplicates
#*   Tuple = () ordered and NOT changeable. Duplicated OK. FASTER  
#*      2D = all arrays in a two Dimension array must be the same length.  


fruits = ["Apple", "banana", "orange"]
print(fruits) #-> ['Apple', 'banana', 'orange']
print(fruits[0]) #-> Apple
print(fruits[0:2]) #-> ['Apple', 'banana']
for x in fruits:
    print(x) #-> prints the fruit on different lines

print(len(fruits)) #-> 3
print("Apple" in fruits) #-> True

fruits[0] = "pineapple"
print(fruits) #-> ['pineapple', 'banana', 'orange']
fruits.append("apple")
print(fruits) #-> ['pineapple', 'banana', 'orange', 'apple']
fruits.sort()
print(fruits) #-> ['pineapple', 'banana', 'orange', 'apple']
fruits.remove("banana")
print(fruits) #-> ['apple', 'orange', 'pineapple']
fruits.insert(0,"banana")
print(fruits) #-> ['banana', 'apple', 'orange', 'pineapple']
fruits.reverse()
print(fruits) #-> ['pineapple', 'orange', 'apple', 'banana']
fruits.clear()
print(fruits) #-> []
fruits = ["Apple", "banana", "orange"]
print(fruits.index("Apple")) #-> 0
print(fruits.count("banana")) #-> 1

#* Sets
vegs = {"carrot", "spinach", "brocoli", "peas"}
print(vegs) #-> {'carrot', 'spinach', 'peas', 'brocoli'} (gives different order each time)


#!Two dimensional lists:
#* examples of one dimensional lists:
fruits = ["apple", "banana", "pear", "coconut"]
vegetables = ["carrot", "brocoli", "peas"]
meats = ["chicken", "beef", "Dog"]
print(fruits)
print(vegetables)
print(meats)
#* 2D list:
groceries = [fruits, vegetables, meats]
print(groceries) #-> [['apple', 'banana', 'pear', 'coconut'], ['carrot', 'brocoli', 'peas'], ['chicken', 'beef', 'Dog']]
print(groceries[0]) #-> ['apple', 'banana', 'pear', 'coconut']
print(groceries[2][2]) #-> Dog

#* can be written as:
groceries = [{"apple", "banana", "pear", "coconut"},
             {"carrot", "brocoli", "peas"},
             {"chicken", "beef", "dog"}]
for collection in groceries:
    for food in collection:
        print(food, end=" ")
    print()
    pass

#! Dictionaries
#* dictionary = a collection of {key:value} pairs
#*              ordered and changeable, no duplicates

capitals = {"UK": "London",
            "USA": "Washington D.C",
            "India": "New Delhi",
            "China": "Beijing",
            "Russia": "Moscow"}

print(capitals.get("UK")) #-> London
print(capitals.get("Japan")) #-> None

#* Check if a key is in the dictionary
if capitals.get("Japan"):
    print("That capital exists.")
else:
    print("That capital doesn't exist")

#* Update dictionary
capitals.update({"Germany": "Frankfurt"})
print(capitals.get("Germany"))
capitals.update({"Germany": "Berlin"})
capitals.pop("China")
print(capitals) #-> {'UK': 'London', 'USA': 'Washington D.C', 'India': 'New Delhi', 'Russia': 'Moscow', 'Germany': 'Berlin'}

keys = capitals.keys()
print(keys) #-> dict_keys(['UK', 'USA', 'India', 'Russia', 'Germany'])

for key in capitals.keys():
    print(key, end= " ") #-> UK USA India Russia Germany

print()
#! functions
#* function = block of reusable code
#*            place () after the function name to invoke it

def happyBday(name, age):
    print(f"Happy birthday to {name}!")
    print(f"You are {age} years old!")

happyBday("Nathan", 16)

def getPword(attempt):
    while attempt == 1:
        password = input("Please enter a password: ")
        if len(password) >= 6 and len(password) <= 8:
            attempt = 2
        else:
            print("Please try again, the password needs to be between 6-8 characters")
    if attempt == 2:
        password2 = input("Please re-enter the password again: ")
        if password2 == password:
            print("password change successful")
        else:
            print("Password change failed.")
            attempt = 1
            getPword(1)
    else:
        print("Error code: 001, please try again.")
        attempt = 1
        getPword(1)

    return password

password = getPword(1)
print(f"Password changed to {password}")


#! lambda function
#* Lambda is an anonymous , one line, function

#* Multiply argument wiith lambda:
x = lambda a, b : a * b
print(x(5, 6)) #-> 30

#* Addition:
x = lambda a, b, c : a + b + c
print(x(5, 6, 2)) #-> 13

#* Lambda becomes more powerful when utilised within other fuctions:
def myfunc(n):
  return lambda a : a * n #the number in the lmda function will be multiplied by n(this case 2)
mydoubler = myfunc(2) #2 = n (making this a doubler)
print(mydoubler(11)) #-> 22

#* comparing 1 line lambda function with classical function at adding x and y
def add_1(x,y): #classical way of doing this sam function
    return x + y

add_1 = lambda x, y: x+ y #does the same as above but in one line



#! Map function:
#* The map() function executes a specified function for each item in an iterable. The item is sent to the function as a parameter.
#  the syntax: map(function, iterables) 
def myfunc(a, b, c):
  return a + b + c

x = map(myfunc, ('apple', 'banana', 'cherry'), (",", " ", " "), ('orange', 'lemon', 'pineapple')) 
print()
print(x) #--> <map object at 0x0000012EA9516230>
print(list(x)) #--> ['apple orange', 'banana lemon', 'cherry pineapple']

#* Changing variable type of every item in a list:
list0 = [1,2,3,4,5,6]
typechange = map(str, list0) #doing string function to list 0
print(list(typechange)) #-> ['1', '2', '3', '4', '5', '6']

#* combining map with lambda function as seen below:
add1 = lambda a: a+1 #creating the function
list2 = [1, 2, 3, 4, 5, 6] #creating the list, don't name the list list as that willl break the list function
add = map(add1, list2) #creating function to add 1 to each item of the list
print(list(add)) #-> [2, 3, 4, 5, 6, 7]

#* lambda function inside map function
list3 = [1,2,3,4,5,6,7]
squarelist = list(map(lambda a: a**2, list3)) #can only be done once, turns square list into list before printing
print(squarelist) #-> [1, 4, 9, 16, 25, 36, 49]


#! Filter function
#*The filter() function returns an iterator where the items are filtered through a function to test if the item is accepted or not.
#The syntax: filter(function, iterable) 
#for more info read through map function, properties are very similar
numbers = [1,2,3,4,5,6,7,8,9]
evens = list(filter(lambda x: x % 2 == 0, numbers)) #prints all values where item in list is even
print(evens) #-> [2,4,6,8]


#! Sort Function:
#* The sort() method sorts the list ascending by default.
#* You can also make a function to decide the sorting criteria(s).
#syntax: list.sort(reverse=True/False, key=myFunc) 
# both parameters are optional

unsorted = [1,3,2,5,4,7,6,9,8]
unsorted.sort(reverse = True)
print(unsorted) #--> [9, 8, 7, 6, 5, 4, 3, 2, 1]

#* Sorting a list by length using Lambda
cars = ['Ford', 'Mitsubishi', 'BMW', 'VW']
cars.sort(reverse = True, key= lambda a: len(a)) #sorts the items by length and then reverse so that longesgt at front
print(cars) #-> ['Mitsubishi', 'Ford', 'BMW', 'VW']

#* Sorting a dictionary by the year using Lambda
cars = [
  {'car': 'Ford', 'year': 2005},
  {'car': 'Mitsubishi', 'year': 2000},
  {'car': 'BMW', 'year': 2019},
  {'car': 'VW', 'year': 2011}]
cars.sort(key= lambda a: a["year"]) #sorting by year start to end
print(cars) #-> [{'car': 'BMW', 'year': 2019}, {'car': 'VW', 'year': 2011}, {'car': 'Ford', 'year': 2005}, {'car': 'Mitsubishi', 'year': 2000}]

#* SORTED() VS SORT():
# sorted() creates a new list where as sort()
# syntax: sorted(iterable, key=key, reverse=reverse)  
values = [(1, 'b', "hello"), (2, 'a', "world"), (3, "c", "ok")]
sorted_values = sorted(values, key = lambda x: x[1]) #orders list by index 1 into a seperate list
print(list(sorted_values)) #-> [(2, 'a', 'world'), (1, 'b', 'hello'), (3, 'c', 'ok')]


#! Date module

#* allows you to accsess dat and format it

import datetime 
x= datetime.datetime.now()
print(x.year) #currently would result in 2025 (current year)
print(x.strftime("%A")) #prints day of the week
print(x) #prints in the following format: 2025-03-18 14:30:41.583721
y = datetime.datetime(2025, 5, 17) #datetime can also take in parameters
print(y) #2025-05-17 00:00:00

#* date formatting 
#go to this website for more formatting options: https://www.w3schools.com/python/python_datetime.asp
print(x.strftime("%a"))#shortened day (Mon, Tue, Wed etc.)
print(x.strftime("%w"))#gives day as number (0 is sunday, saturday is 6)
print(x.strftime("%V"))#gives week number (1-53)


#! Math module (extended functions)
#(first two are built in)
#* Min and Max()
x = min(1,5,10); print(x) #1
y = max(1,5,10); print(y) #10

#* absolute value
#turns any value to positive form
z = abs(-7.5); print(z) #7.5

import math
#* Square root
x = 64; print(math.sqrt(x)) #8.0
x = 64; print(x**0.5) #8.0

#* rounding
x = math.ceil(1.4); print(x) #2
y = math.floor(1.4); print(y) #1


#! JSON File Handling
import json

#* converting JSON to python dictionary
# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y["age"]) 

#! Exception Handling
#* try except block

try:
    print(x)
except:
    print("An exception occurred")

#* specific exception
try:
    print(x)
except NameError:
    print("Variable x is not defined")
except:
    print("Something else went wrong")


#! Enumerate function
#* returns both index and value of an iterable
#* syntax: enumerate(iterable, start=0)
#* start is optional

#* Most basic example:
x = ('apple', 'banana', 'cherry')
y = enumerate(x)
print(list(y)) #-> [(0, 'apple'), (1, 'banana'), (2, 'cherry')]


#* Enumerate within a for loop:
fruits = ["apple", "banana", "cherry"]
for i, fruit in enumerate(fruits):
    print(i, fruit) #-> 0 apple, 1 banana, 2 cherry

#* Enumerate with a start value:
fruits = ["apple", "banana", "cherry"]
for i, fruit in enumerate(fruits, start=1):
    print(i, fruit) #-> 1 apple, 2 banana, 3 cherry

#* Enumerate with a dictionary:
fruits = {"apple": 1, "banana": 2, "cherry": 3}
for i, fruit in enumerate(fruits):
    print(i, fruit) #-> 0 apple, 1 banana, 2 cherry


#! Zip function
#* The zip() function returns a zip object, which is an iterator of tuples where the first item in each passed iterator is paired together, and then the second item in each passed iterator are paired together etc.

#* Basic example:
x = [1, 2, 3]
y = ['a', 'b', 'c']
z = zip(x, y) #-> <zip object at 0x0000012EA9516230> (would output this if printed without list function)
print(list(z)) #-> [(1, 'a'), (2, 'b'), (3, 'c')]

#* Zip with different length lists:
x = [1, 2, 3]
y = ['a', 'b']
z = zip(x, y)
print(list(z)) #-> [(1, 'a'), (2, 'b')]

#* Zip with dictionaries:
x = {"apple": 1, "banana": 2, "cherry": 3}
y = {"apple": "red", "banana": "yellow", "cherry": "pink"}
z = zip(x, y)
print(list(z)) #-> [('apple', 'apple'), ('banana', 'banana'), ('cherry', 'cherry')]


#! Good habits:

#* only automatically run in same file else use main function
#so that functions aren't automatically run when imported
def main():
    print("Hello world")
if __name__ == "__main__":
    main() #only outputs if in current file

#* label variable types
#this is used so at a quick glance you can see what type of variable it is (espeically when not obvious)
name: str = "Nathan"
age: int = 21
rizz: bool = True #no joke AI auto put this down, it fr just knows

#* list comprehension
# list comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.
people: list[str] = ["Nathan", "Barnabus", "Kai", "Harrison", "Ben"]
long_names: list[str] = [name for name in people if len(name) > 4] #-> ["Nathan", "Barnabus", "Harrison"]
#this can also be done directly into a print statement
print([name for name in ["Nathan", "Barnabus", "Kai", "Ben", "Harrison"] if len(name) > 4]) #-> ["Nathan", "Barnabus", "Harrison"]


#! Python OS module:
#* The OS module in python provides functions for interacting with the operating system.
# sauce: https://www.w3schools.com/python/module_os.asp?ref=escape.tech
import os

#* get list of all working attributes and methods (this works in all modules)
print(dir(os)) #-> ['DirEntry', 'F_OK', 'MutableMapping', 'O_APPEND', 'O_BINARY' ...] (you get the point)

#* get current working directory (cwd)
print(os.getcwd()) #-> C:\Users\natha\OneDrive - Wren Academy\6th form\Computer Science> (this is my current working directory)

#* change directory
#os.chdir("C:/Users/natha/OneDrive - Wren Academy/6th form/Computer Science") #changes directory to the one specified (as a string
print(os.getcwd()) #-> C:\Users\natha\OneDrive - Wren Academy\6th form\Computer Science
#about is commented out to help preserve this cheat sheet

#* list all files and directories in the current directory
print(os.listdir()) #-> ['.venv', 'cs lessons', 'favourites', 'object oriented revision'] (this is what is in my current directory)


#* make/remove a new directory
os.mkdir("newdir") #makes a new directory called newdir (within current directory) (can't create subdirectories)
os.makedirs("newdir2/subdir") #makes a new directory called newdir2 and a subdirectory called subdir (within current directory)
#?and remove
os.rmdir("newdir") #removes the directory called newdir (within current directory) (can't remove subdirectories)
os.removedirs("newdir2/subdir") #removes the directory called subdir and newdir2 (within current directory)

#* rename a file
os.mkdir("test.txt") #creates a file called test.txt
os.rename("test.txt", "new.txt") #renames test.txt to new.txt
os.rmdir("new.txt") #removes the file called new.txt

#* check stats of a file
print(os.stat("favourites")) #-> os.stat_result(st_mode=16895, st_ino=1125899906842677, st_dev=4195380, st_nlink=1, st_uid=0, st_gid=0, st_size=4096, st_atime=1647600000, st_mtime=1647600000, st_ctime=1647600000)
#? st_size: is file size in bytes, st_mtime: is last modified time, st_ctime: is creation time
print(os.stat("favourites").st_size) #-> 4096 (size of the file in bytes)
#? make that readable to us
os.system('cls') #clears the console

#*get the os name:
print(os.name) #->nt (stands for windows New Technology, on unix this would output: posix)
#* This module does contain much more, but this is just a basic overview, for more info: https://docs.python.org/3/library/os.html


#! The Python SYS module
import sys
#* Python's sys module provides functions and variables used to manipulate different parts of the Python runtime environment. It's a powerful tool for handling system-specific parameters and functions.

#* current python update
print(sys.version) #-> 3.12.5 (tags/v3.12.5:ff3bc82, Aug  6 2024, 20:45:27) [MSC v.1940 64 bit (AMD64)]

#* system exit messages:
age = 17
if age < 18: 
    #sys.exit("Age less than 18")  would output-> An exception has occurred, use %tb to see the full traceback.\n \n SystemExit: Age less than 18
    print()   
else: 
    print("Age is not less than 18") 


#* Get more info on SYS module here: https://www.geeksforgeeks.org/python-sys-module/

#!array in python (using different module):
import numpy as np
#use this module for scientific computing where you need to handle complex operations, esepcially multi dimension.

#* Creating NumPy array:
arr = np.array([1,2,3,4])
print(arr) #->[1 2 3 4]

#*Element-wise operations:
print(arr * 2) #-> [2 4 6 8]

#* Multi dimentional array:
arr2d = np.array([[1, 2], [3, 4]])
print(arr2d * 2) 
#-> [[2 4]
#->  [6 8]]

import array as arr
#use this module as a basic memory-efficient container. with large quantities of uniform data without need of capabilities of num py

#* creating array module array:
#sytax: array( data_type , value_list )

a = arr.array("i", [1, 2, 3])
print(a) #-> array('i', [1, 2, 3])

#* Accsessing first index of array:
print(a[0]) #-> 1

#* Adding elements to an array:
a.append(5)
print(a) #-> array('i', [1, 2, 3, 5])

#* Iterating and printing each item:
for i in range(0, 3):
    print(a[i], end=" ") #-> 1 2 3

#* Integer array example
a = arr.array('i', [1, 2, 3])
print("Integer Array before insertion:", *a) #-> Integer Array before insertion: 1 2 3

#* Insert 4 at index 1
a.insert(1, 4) 
print("Integer Array after insertion:", *a) #_> Integer Array before insertion: 1 4 2 3 (therefor these arrays are dynamic)

#* for more info use this link: https://www.geeksforgeeks.org/python-arrays/


#! Python Magic Methods:
# Magic methods is the same as Dunder methods (double underscodre) as seen above there is __init__ and __main__ and _str__ etc.
# these methods allow for behavoirs of objects to be defined/customised

#* Example of magic methods:
class student:
    def __init__(self, name, grade): #this is initialised as soon as class is used
        self.name = name
        self.grade = grade

    def __str__(self): #this is the string returned when the object is printed
        return f"{self.name} has a grade of {self.grade}"
    
    def __eq__(self, other): #returns a boolean result to whether the two objects are equal
        return self.name == other.name
    
    def __gt__(self, other): #gt (shorter for greater than) returns a boolean result to whether the first object is greater than the second
        return self.grade > other.grade #there is also __lt__ (short for less than) that can be used
    
    def __add__(self, other): #adding the grades of two students
        return f"added together their grade is: {self.grade + other.grade}"
    
    def __contains__(self, keyword): #checks if a keyword is in the name of the student (returns boolean)
        return keyword in self.name #this could also have "or keyword in self.school" if this file had that attribute
    
    def __getitems__(self, key): #allows for the object to be indexed and then the value of the key to be returned
        if key == "name":
            return self.name
        elif key == "grade":
            return self.grade
        else:
            return f"the key {key} is not valid"
    
student1 = student("Nathan", 9)
student2 = student("Ben", 8)
print(student1) #-> Nathan has a grade of 9
print(student1 == student2) #-> False
print(student1 > student2) #-> True
print(student1 + student2) #-> 17
print("Nathan" in student1) #-> True
print(student1["name"]) #-> Nathan
print(student2["grade"]) #-> 8

#* for more info on magic methods: https://www.geeksforgeeks.org/dunder-magic-methods-python/

#!@property decorator:
#This is a built in decorator in python that allows for a method to be accessed as an attribute. Gives a getter, setter and deleter method.
# this logic is added when you read or write or delete attributes of an object
#* Example of @property decorator:
class Rectangle:
    def __init__(self, length, width):
        self._length = length #people use the _ prefix to make it clear that this is meant to be private variable
        self._width = width #this is done because there is not way to actually malke a variable private in python

    @property #this is the getter method
    def width(self):
        return f"{self._width:.1f}cm"

    @property #without these properties these bits of code would never run
    def length(self):
        return f"{self._length:.1f}cm"
    
    @width.setter #this is the setter method
    def width(self, new_width):
        if new_width < 0:
            raise ValueError("Width must be positive") #raises an exception
        else:
            self._width = new_width

    @length.setter #without these properties these bits of code would never run
    def length(self, new_length):
        if new_length < 0:
            raise ValueError("Length must be positive")
        else:
            self._length = new_length

rectangle = Rectangle(10, 5)

print(rectangle._length) #-> 10.0cm
print(rectangle._width) #-> 5.0cm

#! Python decorators:
# a decorator is a design pattern in Python that allows a user to add new functionality to an existing object without modifying its structure
# Decorators are often used in scenarios such as logging, authentication and memorization, allowing us to add additional functionality to 
# existing functions or methods in a clean, reusable way.

#*A simple decorator function
def decorator(func):
    def wrapper():
        print("Before calling the function.")
        func()
        print("After calling the function.")
    return wrapper
#?Applying the decorator to a function
@decorator #short hand for greet = decorator(greet)
def greet():
    print("Hello, World!")
greet()
#-> Before calling the function.
#-> Hello, World!
#-> After calling the function.

#* Program to square numbers using higher order functions
def fun(f, x): #a higher order function that takes a function and a number as arguments
    return f(x)

def square(x): #a simple function to square a number
    return x * x

res = fun(square, 5)
print(res) #-> 25   

#* Functions as first class objects:
#? This means: functions can be assigned as variables, passed as arguments, returned from other functions, and stored in data structures.

#* Assigning a function to a variable
# Assigning a function to a variable
def greet(n):
    return f"Hello, {n}!"
say_hi = greet  # Assign the greet function to say_hi
print(say_hi("Alice"))  #-> Hello, Alice!

#* Passing a function as an argument: (uses program from above)
def apply(f, v):
    return f(v)

res = apply(say_hi, "Bob")
print(res)  #-> Hello, Bob!

#* Returning a function from another function
def make_mult(f):  # makes a multiplier function for each given factor
    def mult(x):
        return x * f
    return mult

dbl = make_mult(2)
print(dbl(5))  #-> : 10

#* Function Decorators (introducting Args and Kwargs):
def add_sprinkles(func):
    def wrapper(*args, **kwargs): #this is required so that this function is called everytime a decorated get)ice_cream is called not when the decorator appears
        print("*You add sprinkles*")
        func(*args, **kwargs) #this is the print statement "Here is your ice cream!"
    return wrapper

def add_sauce(func):
    def wrapper(*args, **kwargs): #args = arguments, kwargs = keyword arguments
        print("*You add a sauce*")
        func(*args, **kwargs) #this is done so any number of args and kwargs can be passed through
    return wrapper

@add_sprinkles #this becomes shorthand for get_ice_cream = add_sprinkles(get_ice_cream)
@add_sauce #more than one decorator can be applied
def get_ice_cream(flavour): #this is brought in as a paramer "func" 
    print(f"Here is your {flavour} ice cream!")

if __name__ == "__main__":
    get_ice_cream("vanilla")
#-> *You add sprinkles*
#-> *You add a sauce*
#-> Here is your ice cream! (This is only printed once not twice)

#* Method decorators:
def method_decorator(func):
    def wrapper(self, *args, **kwargs): #self is there because of the class
        print("Before method execution")
        res = func(self, *args, **kwargs) #"*kwargs" arent doing anything in this case but are placement holders "*args" is a required placement
        print("After method execution")
        return res
    return wrapper
#you can have as many as you like *args and **kwargs.
class MyClass:
    @method_decorator #this means the function below is ran through the decorator as a parameter
    def say_hello(self):
        print("Hello!")

obj = MyClass()
obj.say_hello()


#* sauce https://www.geeksforgeeks.org/decorators-in-python/


#* Function iterators:
# An iterator is an object that contains a countable number of values.
# An iterator is an object that can be iterated upon, meaning that you can go through all the values.
# in python this is done through "__iter__()" and "__next__()" methods

# lists, tuples, dictionaries and sets are iterable objects

#* Example 1
mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(next(myit)) #-> apple
print(next(myit)) #-> banana
print(next(myit)) #-> cherry



