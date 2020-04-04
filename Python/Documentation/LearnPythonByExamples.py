################################### Print Python Version ################################
import sys
print 'Python version is : '
print(sys.version)
print (sys.version_info)

import platform
print(platform.python_version())

################################### Math Operators from Highest to Lowest ###################################
print '--------------Math Operators from Highest to Lowest----------------'
print "1. ** Exponent"
print "2. % Modulus/remainder"
print "3. // integer division/floored quotient"
print "4. / Division"
print "5. * Multiplication"
print "6. - Subtraction"
print "7. + Addition"

################################### booleans ################################
true_boolean = True
flase_boolean = False

################################ strings ################################
my_name = "Venkat"+" K"
print("Today I had {0} cups of {1}", format(3, 'tea'))

################################# float ################################
version = 2.7

print("---------------Concatenate string and float variables---------------")
print(my_name+"_"+str(version))

################################ Ending a Program Early ############################
print "------------------Ending a Program Early-----------------------"

import sys # importing sys module
print "sys.exit() method will exit the program execution, We can use this for debugging purpose"
# sys.exit() # This method will exit the program execution, We can use this for debugging purpose

################################ control structures ################################
print("---------------Control Structures---------------")
a = 5
b = 50
if a>b:
	print(str(a)+" is greater than "+str(b))
elif b>a:
	print(str(b)+" is greater than "+str(a))
else:
	print(str(a)+" is equal to "+str(b))

################################# looping/iterator ################################

print("---------------while Loop---------------")    
num = 1

while num <= 10:
    print(num)
    num += 1

################################# For loop ################################
# The range starts with 1 and goes until the 11th element (10 is the 10th element).

print("---------------For Loop---------------")    
# Calling range(1,11) will count 1 to 10 by intervals of one
print "Calling range(1,11) will count 1 to 10 by intervals of one"
for i in range(1, 11):
  print(i)

# Calling range(0, 10, 2) will count from zero to eight by intervals of two.
print "Calling range(0, 10, 2) will count from zero to eight by intervals of two"
for i in range(0,10,2):
    print(i)

# a negative number for the step argument to make the for loop count down instead of up
print "Calling range(5, -1, -1) will count from 5 to 0 by intervals of -1"
for i in range(5,-1,-1):
        print(i)    

################################ List: Collection | Array | Data Structure ################################
# List is a collection that can be used to store a list of values

print("---------------List: Collection | Array | Data Structure---------------")
my_list_int = [1,2,3,4,5]
my_list_str = ['abc', 'def', 'ghi', 'jkl', 'mno']
print(my_list_int)
print "-------------------Getting Individual Values in a List with Indexes--------------------"
print(my_list_int[0])
print(my_list_str)

############################## Nagative Indexes ###################################### 
# While indexes start at 0 and go up, you can also use negative integers for the index
# The integer value -1 refers to the last index in a list, the value -2 refers to the second-to-last index in a list, and so on
print "-------------------Nagative Indexes------------------"
print(my_list_str[-1])

############################## Getting Sublists with Slices ###########################
# Just as an index can get a single value from a list, a slice can get several values from a list, in the form of a new list.
print "----------------Sublists with Slices-----------------"
animals = ['cat', 'bat', 'rat', 'elephant']
print(animals[0:3]) # ['cat', 'bat', 'rat']
print(animals[0:-1]) # ['cat', 'bat', 'rat']
print(animals[:2]) # ['cat', 'bat']
print(animals[2:]) # ['rat', 'elephant']

print "----------------Length Of List-----------------"
print(len(animals))

################################ add a new value to a List is "append" ################################
print "----------------add a new value to a List-----------------"
my_list_int.append(6)
print(my_list_int)
my_list_str.append("pqr")
print(my_list_str)

############################### List Concatenation ###############################
print "---------------------List Concatenation---------------------"
new_list = my_list_int + my_list_str
print(new_list)

################ Dynamic concatenation ################
# catNames = []
# while True:
#     print('Enter the name of cat ' + str(len(catNames) + 1) + ' (Or enter nothing to stop.):')
#     name = input()
#     if name == 'stop':
#         break
#     catNames = catNames + [name] # list concatenation
# print('The cat names are:')
# for name in catNames:
#     print(' ' + name)

################ The in and not in Operators ####################
print "----------------------The in and not in Operators----------------------"

# myPets = ['Cat', 'Dog', 'Parrot']
# print('Enter a pet name:')
# name = input()
# if name not in myPets:
#     print('I do not have a pet named ' + name)
# else:
#     print(name + ' is my pet.')

##################### The Multiple Assignment Trick #####################
print "-----------------------The Multiple Assignment Trick-----------------------"
cat = ['fat', 'black', 'loud']
size, color, disposition = cat
print(size)

#################### Finding a Value in a List with the index() Method ##################
print "----------------------Finding a Value in a List with the index() Method----------------------"
cat = ['fat', 'black', 'loud']
print(cat.index('fat'))

print "---------------Nested Lists----------------"
nested_list = [['cat', 'bat'], [10, 20, 30, 40, 50]]
print(nested_list[0])
print(nested_list[0][1])

print "---------------Sort Lists----------------"
sort_list = [2, 5, 3.14, 1, -7]
sort_list.sort()
print(sort_list) # [-7, 1, 2, 3.14, 5]
sort_list.sort(reverse=True)
print(sort_list) # [5, 3.14, 2, 1, -7]

################################ List-like Types: Strings and Tuples #################################
print "-----------------------------List-like Types: Strings and Tuples-----------------------------"

# List, Strings and Tuples are similar.
# Many of the things you can do with lists can also be done with strings: 
# indexing; slicing; and using them with for loops, with len(), and with the in and not in operators
# But lists and strings are different in an important way. 
# A list value is a mutable data type: It can have values added, removed, or changed. 
# However, a string is immutable: It cannot be changed

# The tuple data type is almost identical to the list data type, except in two ways. 
# First, tuples are typed with parentheses, ( and ), instead of square brackets, [ and ]
# The main way that tuples are different from lists is that tuples, like strings, are immutable. 
# Tuples cannot have their values modified, appended, or removed.


################################ Dictionary is a collection of key-value pairs ################################

# Unlike lists, items in dictionaries are unordered
# Because dictionaries are not ordered, they cant be sliced like lists

print("---------------Dictionary: Key-Value Data Structure---------------")
my_dict = {'name':'sachin', 'skill':'batsman', 'style':'right-hand'}
print(my_dict)
print(my_dict['name'])
print("Batsman name is "+my_dict['name'])
print("Batsman name is %s" %(my_dict["name"]))

################################ Adding new value to dictionary ################################
my_dict['strike_rate'] = 90.19
print(my_dict)
print("Batsman name is %s having strike rate %f" %(my_dict["name"], my_dict["strike_rate"]))

############################### The keys(), values(), and items() Methods #######################
print "-----------------------The keys(), values(), and items() Methods-----------------------"
dict1 = {'color':'red', 'age':42}

print "Using keys() method"
for k in dict1.keys():
    print(k)
# print color age    

print "Using values() method"
for v in dict1.values():
    print(v)
# print red 42  

print "Using items() method"
for i in dict1.items():
    print(i)
# print ('color', 'red') ('age', 42)


################################ Iteration: Looping Through Data Structures ################################
print("---------------Looping Through Data Structures---------------")
for list_int in my_list_int:
	print list_int

for list_str in my_list_str:
	print list_str

################################ Nested dictionaries ################################
my_multi_dict = {0:{'name':'sachin', 'skill':'All-rounder', 'style':'right-hand'},1:{'name':'rahul', 'skill':'batsman', 'style':'right-hand'}}
print(my_multi_dict)

for multi_id,multi_info in my_multi_dict.items():
	print(multi_info['name'])
	
for key, info in my_multi_dict.items():
	for attribute, value in info.items():
		print("Batsman %s is %s" %(attribute, value))

############### get method ######################
print "---------------------------get method---------------------------"
picnicItems = {'apples': 5, 'cups': 2}
print 'I am bringing ' + str(picnicItems.get('cups', 0)) + ' cups.'
print 'I am bringing ' + str(picnicItems.get('eggs', 0)) + ' eggs.'

############### Pretty Printing ######################
print "---------------------------Pretty Printing---------------------------"

# import pprint
# pprint.pprint(someDictionaryValue)
# print(pprint.pformat(someDictionaryValue))

################################ Class ################################
'''
	private variables, public methods: 		Accessible from anywhere
	private variables, private methods: 	Accessible only in their own class. starts with two underscores
	Python doesn't have protected class

'''
print "-------------------------OOPs in Python-------------------------"
class Vehicle:
    def __init__(self, number_of_wheels, type_of_tank, seating_capacity, maximum_velocity, noise):
        self.number_of_wheels = number_of_wheels
        self.type_of_tank = type_of_tank
        self.seating_capacity = seating_capacity
        self.maximum_velocity = maximum_velocity
        self.noise = noise

    def make_noise(self):
    	print(self.noise)

vehicle1 = Vehicle(4, 'electric', 5, 250, 'VRUMMmmm')        
print(vehicle1.number_of_wheels)
vehicle1.number_of_wheels = 8
print(vehicle1.number_of_wheels)
print(vehicle1.make_noise())

######################### Encapsulation ###############################
class Car:
    __maxspeed = 0
    __name = ""
    wheels = 4
 
    # def __init__(self):
    #     self.__maxspeed = 200
    #     self.__name = "Supercar"
 
    def drive(self):
        print 'car has '+ str(self.wheels)+' wheels'
        print 'driving. maxspeed ' + str(self.__maxspeed)

    # This is to set private variable
    def setMaxSpeed(self, speed):
    	self.__maxspeed = speed

 
redcar = Car()
redcar.drive()
print(redcar.wheels)
redcar.__maxspeed = 10  # will not change variable because its private
redcar.drive()
redcar.setMaxSpeed(100)
redcar.drive()

#################### Inheritance ########################
# parent class
class Bird:
    
    def __init__(self):
        print("Bird is ready")

    def whoisThis(self):
        print("Bird")

    def swim(self):
        print("Swim faster")

# child class
class Penguin(Bird): # this is the syntax to inherit parent class

    def __init__(self):
        # call super() function
        # super().__init__()
        Bird.__init__(self) # Calling Base class constructor
        print("Penguin is ready")

    def whoisThis(self):
        print("Penguin")

    def run(self):
        print("Run faster")

peggy = Penguin()
peggy.whoisThis()
peggy.swim()
peggy.run()

########### Multilevel Inheritance ###########
class Animal:   
    def eat(self):  
      print 'Eating...'  
class Dog(Animal):  
   def bark(self):  
      print 'Barking...'  
class BabyDog(Dog):  
    def weep(self):  
        print 'Weeping...'  
d=BabyDog()  
d.eat()  
d.bark()  
d.weep()  

############### Multiple Inheritance ###################

#definition of the class starts here  
class Person:  
    #defining constructor  
    def __init__(self, personName, personAge):  
        self.name = personName  
        self.age = personAge  
  
    #defining class methods  
    def showName(self):  
        print(self.name)  
  
    def showAge(self):  
        print(self.age)  
  
    #end of class definition  
  
# defining another class  
class Student: # Person is the  
    def __init__(self, studentId):  
        self.studentId = studentId  
  
    def getId(self):  
        return self.studentId  
  
  
class Resident(Person, Student): # extends both Person and Student class  
    def __init__(self, name, age, id):  
        Person.__init__(self, name, age)  
        Student.__init__(self, id)  
  
  
# Create an object of the subclass
resident1 = Resident('John', 30, '102')
resident1.showName()
resident1.showAge()
print resident1.getId()


class A:  
    def __init__(self):  
    
        self.name = 'John'  
        self.age = 23  
  
    def getName(self):  
        return self.name  
  
  
class B: 
    id = 32 
    def __init__(self):  
    
        self.name = 'Richard'  
        self.id = id  
  
    def getName(self):  
        return self.name  

    # def getId(self):  
    #     return self.id  
  
  
class C(A, B):  
    def __init__(self):  
        # A.__init__(self)  
        # B.__init__(self)
        self.name = 'c class name'
  
    def getName(self):  
        return self.name  

    def getId(self):
        return B.getName(B())

C1 = C()  
print(C1.getName())  
print(C1.getId())


##################### Functions ###################################
print "------------------------Functions-------------------------------"
def hello(name):
    print('Hello ' + name)

hello('Sachin')

print "---------------------Function with return---------------------------"
import random
def getAnswer(answerNumber):
    if answerNumber == 1:
        return 'It is certain'
    elif answerNumber == 2:
        return 'It is decidedly so'
    elif answerNumber == 3:
        return 'Yes'
    elif answerNumber == 4:
        return 'Reply hazy try again'
    elif answerNumber == 5:
        return 'Ask again later'
    elif answerNumber == 6:
        return 'Concentrate and ask again'
    elif answerNumber == 7:
        return 'My reply is no'
    elif answerNumber == 8:
        return 'Outlook not so good'
    elif answerNumber == 9:
        return 'Very doubtful'

r = random.randint(1, 9)
fortune = getAnswer(r)
print(r)
print(fortune)

print "---------------------Function without return---------------------------"
def least_difference(a, b, c):
    """Return the smallest difference between any two numbers
    among a, b and c.
    """
    diff1 = abs(a - b)
    diff2 = abs(b - c)
    diff3 = abs(a - c)
    min(diff1, diff2, diff3)

print(
    least_difference(1, 10, 100),
    least_difference(1, 10, 10),
    least_difference(5, 6, 7),
)

print "------------------------Print Function--------------------------"
# print(1, 2, 3)
# print(1, 2, 3, sep='-')


##################### Importing Modules ##############################
# Python comes with a set of modules called the standard library. 
# Each module is a Python program that contains a related group of functions that can be embedded in your programs.
# The import keyword, The name of the module, 
# Optionally, more module names, as long as they are separated by commas
# import random, sys, os, math - to import multiple modules

print "------------------------Importing Modules-------------------------"

import math
print("It's math! It has type {}".format(type(math)))
print(dir(math))
print math.pi
print math.log(32, 2)
# help(math)

import random 
for i in range(5):
    print(random.randint(1, 10))

import time
l = [0]*500000
t1 = time.time()*1000

for i in range(0,len(l)):
    l[i]+=2
t1 = time.time()*1000-t1
print("Time taken by list is ", t1 ,"ms")


################ Regular Expressions ##################
print "-----------------------Regular Expressions----------------------"

import re # this regular expression module
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
'''
r: raw string, which does not escape characters
d means a digit character
'''
mo = phoneNumRegex.search('My number is 415-555-4242.')
''' 
A Regex objects search() method searches the string it is passed for any matches to the regex. 
The search() method will return None if the regex pattern is not found in the string. 
If the pattern is found, the search() method returns a Match object. 
Match objects have a group() method that will return the actual matched text from the searched string
'''
print('Phone number found: ' + mo.group())

####################### Grouping with Parentheses ####################
print "----------------------------Grouping with Parentheses----------------------------"
phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('My number is 415-555-4242.')
print mo.group() # 415-555-4242
print mo.group(0) # 415-555-4242
print mo.group(1) # 415
print mo.group(2) # 555-4242
print mo.groups() # ('415', '555-4242')
areaCode, mainNumber = mo.groups() # Multiple assignment
print areaCode # 415
print mainNumber # 555-4242

print "---------------------------- findall and search ----------------------------"
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search('Cell: 415-555-9999 Work: 212-555-0000')
print mo.group() # 415-555-9999
mo1 = phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000')
print mo1 # ['415-555-9999', '212-555-0000']

########################## Using the logging Module ###############################
print "---------------------------- Using the logging Module ------------------------"

import logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
logging.debug('Start of program')

def factorial(n):
    logging.debug('Start of factorial(%s%%)' % (n))
    total = 1
    for i in range(n + 1):
        total *= i
        logging.debug('i is ' + str(i) + ', total is ' + str(total))
    logging.debug('End of factorial(%s%%)' % (n))
    return total
print(factorial(5))
logging.debug('End of program')




