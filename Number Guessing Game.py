import random

num = random.randint(1, 100)
guess = None

while guess != num:
    guess = input("Guess a number between 1 and 10: ")
    guess = int(guess)

    if guess == num:
        print("Congratulations! You won!")
        print("The number was",num)
        break
    else:
        print("Nope, sorry.")
        print("Wrong guess.")
        print("Try again!")
