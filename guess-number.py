import random

print('Welcome to the Guessing Game!')
x = int(input('Pick a number between 10 and 30: '))

while x < 10 or x > 30:
    x = int(input('Pick a number between 10 and 30: '))


def guess(x):
    guess = 0
    random_number = random.randint(1, x)

    if x > 30:
        print("Please enter a number less than 30")
        return
    while (guess != random_number):
        guess = int(input(f'Guess a number between 1 and {x}: '))
        if guess < random_number:
            print('Sorry, guess again. Too low.')
        elif guess > random_number:
            print('Sorry, guess again. Too high.')
    print(
        f'Yay, congrats. You have guessed the number {random_number} correctly!')


guess(x)
