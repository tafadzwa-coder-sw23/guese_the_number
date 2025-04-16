import random

def user_guess(max_number):
    """
    Plays a number guessing game where the user tries to guess a random number
    chosen by the computer.

    Args:
        max_number (int): The highest number the computer can choose.
    """
    secret_number = random.randint(1, max_number)
    guess = 0

    print(f"\nI'm thinking of a number between 1 and {max_number}.")

    while guess != secret_number:
        try:
            guess = int(input(f"Guess the number: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue  # Go back to the beginning of the while loop

        if guess < secret_number:
            print("Too low!")
        elif guess > secret_number:
            print("Too high!")

    print(f"Congratulations! You guessed the number {secret_number} correctly!")


def computer_guess(max_number):
    """
    Plays a number guessing game where the computer tries to guess a number
    chosen by the user. Uses a binary search approach for efficiency.

    Args:
        max_number (int): The highest number the user can choose.
    """
    low = 1
    high = max_number
    feedback = ""

    print(f"\nThink of a number between 1 and {max_number}, and I'll try to guess it!")

    while feedback != "c":
        if low != high:
            guess = (low + high) // 2  # Integer division for the midpoint
        else:
            guess = low  # or high, as they are equal
        
        print(f"Is your number {guess}?")
        feedback = input("Enter 'h' for Too high, 'l' for Too low, or 'c' for Correct: ").lower()

        if feedback == "h":
            high = guess - 1
        elif feedback == "l":
            low = guess + 1
        elif feedback == "c":
            break # Exit the loop
        else:
            print("Invalid input. Please enter 'h', 'l', or 'c'.")
            continue

    print(f"I guessed your number, {guess}, correctly!")



# Let the user choose which game to play.
while True:
    game_mode = input("Do you want to (u) guess or have the (c)omputer guess? (u/c): ").lower()
    if game_mode == "u":
        user_guess(10)
        break # Exit the loop after the game finishes
    elif game_mode == "c":
        computer_guess(10)
        break # Exit the loop
    else:
        print("Invalid input. Please enter 'u' or 'c'.")
