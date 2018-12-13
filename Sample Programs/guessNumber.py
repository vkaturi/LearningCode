# This is a Guess the Number game.
import random, sys
guessesTaken = 0
print('Hello! What is your name?')
myName = input()
number = random.randint(1, 20)

print "Guess a number between 1 and 20: "

for guessesTaken in range(5):

	if 0 < guessesTaken < 4:
		print "You are left with "+ str(5-guessesTaken) + " chances. Guess again: "
	if guessesTaken == 4:
		print "!!!!!!!!!!!!!!!Enter your last guess!!!!!!!!!!!!!!"
	guess = input()
	guess = int(guess)
	if guess<number:
		print "Your guess is too low"
	if guess>number:
		print "Your guess is too high"
	if guess==number:
		break

if guess==number:
	guessesTaken = str(guessesTaken + 1)
	if guessesTaken == 1:
		print "WOW!!!! Great " + myName + " you have guessed the number in first guess!!!"	
	else:
		print "Hey " + myName + " you have guessed the number in " + guessesTaken + " guesses!!!"

if guess != number:
	number = str(number)
	print "Chances Over!!! the actual number is " + number
