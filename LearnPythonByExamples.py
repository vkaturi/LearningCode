################################### Print Python Version ################################
import sys
print 'Python version is : '
print(sys.version)
print (sys.version_info)

import platform
print(platform.python_version())

################################### booleans ################################
true_boolean = True
flase_boolean = False

################################ strings ################################
my_name = "Venkat"+" K"

################################# float ################################
version = 2.7

print("---------------Concatenate string and float variables---------------")
print(my_name+"_"+str(version))

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

for i in range(1, 11):
  print(i)

################################ List: Collection | Array | Data Structure ################################
# List is a collection that can be used to store a list of values

print("---------------List: Collection | Array | Data Structure---------------")
my_list_int = [1,2,3,4,5]
my_list_str = ['abc', 'def', 'ghi', 'jkl', 'mno']
print(my_list_int)
print(my_list_int[0])
print(my_list_str)
print(my_list_str[-1])

################################ add a new value to a List is "append" ################################
my_list_int.append(6)
print(my_list_int)
my_list_str.append("pqr")
print(my_list_str)

################################ Dictionary is a collection of key-value pairs ################################

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

################################ Class ################################
'''
	private variables, public methods: 		Accessible from anywhere
	private variables, private methods: 	Accessible only in their own class. starts with two underscores
	Python doesn't have protected class

'''
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

