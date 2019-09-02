# This is a guess game
import random

name = input("What is your name? ")

print("Well, " + name + "! I'm thinking of a number between 1 and 20. You will only get six chances to guess that number")
secretnumber = random.randint(1, 20)

for guesstaken in range (1, 7):
	guess = int(input("Take a guess: "))

	if guess < secretnumber:
		print("Your guess is too low")
	elif guess > secretnumber:
		print("Your guess is too high")
	else:
		break  # This condition is for the correct guess

if guess == secretnumber:
	print("Good Job " + name + "! You guessed the correct number in " + str(guesstaken) + " guesses!")
else:
	print("Nope! You got it wrong. The secret number i was thinking was " + str(secretnumber))
