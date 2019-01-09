# import sys
# # This program says hello and asks for my name.
# print('Hello world!')
# print('What is your name?') # asks name
# myName = input()
# print('It is good to meet you, ' + myName)
# print('The length of your name is:')
# print(len(myName))
# print('What is your age?') # asks age
# myAge = input()
# print('You will be ' + str(int(myAge) + 1) + ' in a year.')


def least_difference(a, b, c):
    """Return the smallest difference between any two numbers
    among a, b and c.
    
    >>> least_difference(1, 5, -5)
    4
    """
    diff1 = abs(a - b)
    diff2 = abs(b - c)
    diff3 = abs(a - c)
    return min(diff1, diff2, diff3)

print(least_difference(1,10,20))
help(least_difference)