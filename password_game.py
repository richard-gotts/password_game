"""
This program challenges the user to guess a password containing 5 unique digits.

The user gets a score on each attempt, based on how close they were:

    2 points for a correct digit in the correct place
    1 point for a correct digit in the wrong correct place

"""

import random

# Generate a list of the digits 0-9

digits = []

for i in range(10):
    digits.append(str(i))

# Generate a random password using the list of digits

password = []

for i in range(5):
    password_digit = random.choice(digits)
    password.append(password_digit)

    # This line ensures that the password has unique digits

    digits.remove(password_digit)

# Declare variables for the score and number of attempts

SCORE = 0
ATTEMPTS = 0

# Begin guessing loop

print()
print("=== GUESS THE PASSWORD! === \n\nGuess the 5 digit password. Every digit is different... "
      "\n\nYou will get a score after each guess: \n\n\t2 points for a correct digit in the "
      "correct place. \n\t1 point for a correct digit in the wrong place. \n\nGood luck! \n")

while SCORE < 10:

    # Keep track of number of attempts

    ATTEMPTS += 1

    # Request guess from the user. If it isn't 5 digits long, request again.

    guess = input("Enter password: ")

    while len(guess) != 5:
        print()
        guess = input("Password should be 5 digits long. Please try again: ")

    # Go through the password and compare digits with the guess to find score

    for i in range(5):

        if password[i] == guess[i]:
            SCORE += 2

        elif password[i] in guess:
            SCORE += 1

        else:
            pass

    # If the password is guessed, move straight on to congratulations message.

    if SCORE == 10:
        break

    # Show score and number of attempts so far. Reset score to 0.

    print(f"{SCORE}/10. Total attempts = {ATTEMPTS}")
    print()

    SCORE = 0

print()
print(f"Well done! You correctly guessed the password in {ATTEMPTS} attempts.")
print()
