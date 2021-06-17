""" 
Number Guessing Game ---- Console Game
"""

#Step 1:
# Generate a random number between 0 and N.

""" 
random.randrange(start, stop[, step])
random.randint(start, stop, [,step])
"""

print("Welcome to Number Guessing Game")
import random
randomNumGen = random.randint(1,10)
print(randomNumGen)
#Step 2
# Then iterate from 1 to 10 and check if the input number is equal to the assumed number or not.
chances = 0

attempt = 1
while chances<6:
	number = int(input("Select a number between 1 to 10: "))
	print("You chose: ", number)

	if number==randomNumGen:
		print("You guessed it right, the number is ", randomNumGen)
		print("you guess in ",attempt,"attempts")
		break
	elif number<randomNumGen:
		print("The number is slightly Greater than you guess")
	elif number>randomNumGen:
		print("The number is slightly Smaller than you guess")
	else:
		print("Opps, Wrong Guess!!")

	chances+=1
	attempt +=1

