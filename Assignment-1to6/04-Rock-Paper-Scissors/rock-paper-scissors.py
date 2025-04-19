import random

def play():
    user = input("Choose: 'r' for rock, 'p' for paper, 's' for scissors: ")
    computer = random.choice(['r', 'p', 's'])

    print(f"\nYou chose {user}, computer chose {computer}.")

    if user == computer:
        return "It's a tie!"

    if is_win(user, computer):
        return "You won!"

    return "You lost!"

def is_win(player, opponent):
    # return True if player beats opponent
    # winning conditions: r > s, s > p, p > r
    return (
        (player == 'r' and opponent == 's') or
        (player == 's' and opponent == 'p') or
        (player == 'p' and opponent == 'r')
    )

# Run the game
print(play())
