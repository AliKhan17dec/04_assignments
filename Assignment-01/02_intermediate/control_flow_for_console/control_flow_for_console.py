import random

NUM_ROUNDS = 5

def main():
    print("Welcome to the High-Low Game!")
    print('--------------------------------')

    # Milestone 5: Keep track of score
    your_score = 0

    # Milestone 4: Play multiple rounds
    for round_num in range(1, NUM_ROUNDS + 1):
        print(f"Round {round_num}")
        
        # Milestone 1: Generate random numbers
        computer_num = random.randint(1, 100)
        your_num = random.randint(1, 100)
        print("Your number is", your_num)

        # Milestone 2: Get user guess
        choice = input("Do you think your number is higher or lower than the computer's?: ").lower()

        # Extension 1: Validate user input
        while choice != "higher" and choice != "lower":
            choice = input("Please enter either higher or lower: ").lower()

        # Milestone 3: Game logic
        if (choice == "higher" and your_num > computer_num) or (choice == "lower" and your_num < computer_num):
            print("You were right! The computer's number was", computer_num)
            your_score += 1
        else:
            print("Aww, that's incorrect. The computer's number was", computer_num)

        print("Your score is now", your_score)
        print()

    # Game over
    print("Thanks for playing!")
    print("Your final score is", your_score)

    # Extension 2: Ending message
    if your_score == NUM_ROUNDS:
        print("Wow! You played perfectly!")
    elif your_score > NUM_ROUNDS // 2:
        print("Good job, you played really well!")
    else:
        print("Better luck next time!")

if __name__ == "__main__":
    main()
