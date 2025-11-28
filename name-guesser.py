import random
import time


# Initialize default game settings
score = 0                                                               # default number of points
score_per_correct_answer = 5                                            # default number of points added after each correct guess
score_taken_away_per_wrong_answer = 1                                   # default number of points taken away after each wrong guess
first = 1                                                               # default number of the highest number in the guessing range
second = 10                                                             # default number of the lowest number in the guessing range


# Main menu function
def main():
    # Show menu options
    print("----Number Guesser Menu----")
    print("A. Play")
    print("B. Settings")
    print("C. Quit")

    choice = input("Enter the first letter: ")

    # Player chooses to play the game
    if choice.lower() == "a":
        while True:          # Keep playing until the player quits from inside play()
            play()

    # Player chooses to change settings
    elif choice.lower() == "b":
        settings()

    # Player chooses to quit
    elif choice.lower() == "c":
        print("Quitting.")
        time.sleep(1)
        print("Quitting..")
        time.sleep(1)
        print("Quitting...")
        return True


# Settings function to change game parameters
def settings():
    global score_per_correct_answer, score_taken_away_per_wrong_answer, first, second

    # Ask player to set points for correct/incorrect guesses and the lowest & highest numbers in the guessing range
    score_per_correct_answer = int(input("Enter how many points the player gets after each correct guess(default is 5): "))
    score_taken_away_per_wrong_answer = int(input("Enter how many points the player loses after each wrong guess(default is 0): "))
    first = int(input("Enter the lowest number in the guessing range(default is 1): "))
    second = int(input("Enter the highest number in the guessing range(default is 10): "))


# Function to add points when player guesses correctly
def points_adder():
    global score
    score = score + score_per_correct_answer


# Function to subtract points when player guesses incorrectly
def points_take_away():
    global score
    score = score - score_taken_away_per_wrong_answer


# Function to generate a random number in the current range
def num_gen():

    generated_number = random.randint(first, second)
    return generated_number


# Main gameplay function
def play():
    # Ask player to guess a number
    user_input = int(input(f"Guess the number between {first}-{second}: "))

    # Generate a random number
    rand_num = num_gen()

    # Check if the player's guess is correct
    if rand_num == user_input:
        print("You've got it!")
        points_adder()          # Add points for correct guess
        print(f"Total score is {score}")
    else:
        print("That wasn't right...")
        points_take_away()      # Subtract points for wrong guess
        print(f"Total score is {score}")


# Run the main menu repeatedly until the player quits
while True:
    if main():
        break
