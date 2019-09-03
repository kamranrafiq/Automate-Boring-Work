import random

name = input("What's your name? ")
print("Well! " + name + " I am thinking of a number between 1 and 20.\nYou have 6 tries to guess that number.")

secret_number = random.randint(1,20)

for guesstaken in range(1,7):
	guess = int(input("Take a guess: "))

	if guess < secret_number:
		print("Your guess is low. Try again")

	elif guess > secret_number:
		print("Your guess is high. Try again")

	else:
		break

if guess == secret_number:
	print("Your guess is correct! You guessed the correct number in " + str(guesstaken) + " guesses")

else:
	print("Sorry! You were not able to guess the correct number. The number i was thinking of was " + str(secret_number) + ".")
