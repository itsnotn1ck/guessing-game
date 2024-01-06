# github.com/itsnotn1ck

from random import randint


def guessing():

	while True:
		try:

			modes = ['easy', 'normal', 'hard']
			mode = input("Pick a mode!\nEasy - Normal - Hard\n")
			if mode not in modes:
				print("Please enter easy, normal, or hard.")
			else:
				if mode == 'easy':
					number = randint(1, 10)
					guess = int(input(f"Guess the number!\n(1, 10)\n"))
					if guess == number:
						print(f"Correct! You guessed {guess}!")
					else:
						print(f"You were wrong! The number was {number}")
				elif mode == 'normal':
					number = randint(1, 50)
					guess = int(input(f"Guess the number!\n(1, 50)\n"))
					if guess == number:
						print(f"Correct! You guessed {guess}!")
					else:
						print(f"You were wrong! The number was {number}")
				elif mode == 'hard':
					number = randint(1, 100)
					guess = int(input(f"Guess the number!\n(1, 100)\n"))
					if guess == number:
						print(f"Correct! You guessed {guess}!")
					else:
						print(f"You were wrong! The number was {number}")
	
		except ValueError:
			print("Please enter a valid, whole number.")


if __name__ == '__main__':
	guessing()
