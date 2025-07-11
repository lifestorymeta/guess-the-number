from random import randint
import os

# Generate a random number
number_to_guess = randint(1, 100)
user_guess = -1
attempts = 0

print("🎯 Welcome to the Guess the Number Game!")
print("I'm thinking of a number between 1 and 100.\n")

# Game loop
while user_guess != number_to_guess:
    try:
        user_guess = int(input("Enter your guess: "))
        attempts += 1

        if user_guess > number_to_guess:
            print("🔻 Lower number please!\n")
        elif user_guess < number_to_guess:
            print("🔺 Higher number please!\n")
        else:
            print(f"✅ Congratulations! You guessed the number {number_to_guess} in {attempts} attempts!\n")
    except ValueError:
        print("❗ Please enter a valid number.")

# Check or create high score
high_score_file = "High_score.txt"

# If file doesn't exist, create it with a high score of 0
if not os.path.exists(high_score_file):
    with open(high_score_file, "w") as f:
        f.write("0")

# Read high score from file
with open(high_score_file, "r") as f:
    try:
        high_score = int(f.read())
    except ValueError:
        high_score = 0

# Update high score if beaten
if high_score == 0 or attempts < high_score:
    print("🏆 New High Score! Well done!")
    with open(high_score_file, "w") as f:
        f.write(str(attempts))
else:
    print(f"📊 Current High Score: {high_score} attempts. Try again to beat it!")


