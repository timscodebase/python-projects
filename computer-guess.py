import random

print('Welcome to the Guessing Game!')
print('Here is the computer guessing your number!')

x = int(input('Pick a number between 10 and 30 (the guessing range): '))

while x < 10 or x > 30:
    x = int(input('Pick a number between 10 and 500: '))


def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low
        feedback = input(
            f'Is {guess} too high (H), too low (L), or correct (C)? ').lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
    print(f'Yay! The computer guessed your number, {guess}, correctly!')


computer_guess(x)
