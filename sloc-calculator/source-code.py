# python program for guess the number game

import random
           
random.seed()
number = random.randint(1, 100)

guess = 0

print("guess a number between 1 and 100")

while guess != number :
	guess = int(input("> "))

	if guess < number :
		print("too low!")
	elif guess > number :
		print("too high!")

print("that's right!")
