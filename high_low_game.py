
# High-Low Game

import random

def high_low_game():
    NUM_ROUNDS = 5  # Number of rounds
    score = 0  # Initialize score

    print("Welcome to the High-Low Game!")
    print("--------------------------------")

    for round_num in range(1, NUM_ROUNDS + 1):
        print(f"Round {round_num}")
        
        # Generate random numbers for the player and computer
        player_num = random.randint(1, 100)
        computer_num = random.randint(1, 100)

        # Display player's number
        print(f"Your number is {player_num}")

        # Get user input and validate
        while True:
            user_guess = input("Do you think your number is higher or lower than the computer's? (type 'higher' or 'lower'): ").lower()
            if user_guess in ['higher', 'lower']:
                break
            print("Invalid input. Please type 'higher' or 'lower'.")

        # Check the result
        if (user_guess == "higher" and player_num > computer_num) or (user_guess == "lower" and player_num < computer_num):
            print(f"You were right! The computer's number was {computer_num}.")
            score += 1
        elif player_num == computer_num:
            print(f"It's a tie! The computer's number was also {computer_num}. The computer wins this round.")
        else:
            print(f"Aww, that's incorrect. The computer's number was {computer_num}.")

        # Display the current score
        print(f"Your score is now {score}")
        print("--------------------------------")

    # Final message based on performance
    print("Thanks for playing!")
    if score == NUM_ROUNDS:
        print("Perfect score! You played amazingly well!")
    elif score > NUM_ROUNDS // 2:
        print("Good job, you played really well!")
    else:
        print("Better luck next time! Keep practicing!")

# Run the game
if __name__ == "__main__":
    high_low_game()
