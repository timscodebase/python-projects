import random

print("Rock Paper Scissors")
print()


def play():
    user = input(
        "What's your choice? (R) for rock, (P) for paper, (S) for scissors: ").lower()
    computer = random.choice(['r', 'p', 's'])
    print("Rock... ")
    print("Paper... ")
    print("Scissors... ")
    print("SHOOT!")
    print()

    if user == computer:
        print("It's a tie")
        return

    if is_win(user, computer):
        print('You won!')
    else:
        print('You lost!')


def is_win(player, opponent):
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True


play()
