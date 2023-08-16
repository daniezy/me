"""Set 3, Exercise 3.

Steps on the way to making your own guessing game.
"""

import random


def advancedGuessingGame():
    """Play a guessing game with a user.

    The exercise here is to rewrite the exampleGuessingGame() function
    from exercise 3, but to allow for:
    * a lower bound to be entered, e.g. guess numbers between 10 and 20
    * ask for a better input if the user gives a non integer value anywhere.
      I.e. throw away inputs like "ten" or "8!" but instead of crashing
      ask for another value.
    * chastise them if they pick a number outside the bounds.
    * see if you can find the other failure modes.
      There are three that I can think of. (They are tested for.)

    NOTE: whilst you CAN write this from scratch, and it'd be good for you to
    be able to eventually, it'd be better to take the code from exercise 2 and
    merge it with code from excercise 1.
    You can refactor a bit, you should refactor a bit! Don't put the code all
    inside this function, think about reusable chunks of code that you can call
    in several places.
    Remember to think modular. Try to keep your functions small and single
    purpose if you can!
    """


import random


<<<<<<< HEAD
def super_asker(prompt):
=======
def get_integer_input(prompt):
>>>>>>> d013b9ec628b1d0ad04438740682cb5cf5ebe20b
while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
<<<<<<< HEAD
print("Please enter a valid number.")


def main():
    print("\nThis is the guessing game")
    lowerbound = super_asker("Enter a lowerbound: ")
    upperbound = super_asker("Enter an upperbound: ")
    print(f"Guess a number between {lowerbound} and {upperbound}.")
    actualNumber = random.randint(lowerbound, upperbound)
    guessed = False
    while not guessed:
        guessedNumber = super_asker("Guess a number: ")

        if guessedNumber == actualNumber:
            print("Congratulations! You guessed it!")
            guessed = True
        elif guessedNumber < actualNumber:
            print("Too small. Try again.")
        else:
            print("Too large. Try again.")


if __name__ == "__main__":
    main()

    # the tests are looking for the exact string "You got it!". Don't modify that!
=======print("Please enter a valid integer.")


def super_asker(lowerbound, upperbound):
    print("\nThis is the guessing game")

    actualNumber = random.randint(lowerbound, upperbound)
    while True:
        guessedNumber = get_integer_input(
            f"Guess a number between {lowerbound} and {upperbound}: "
        )

        if guessedNumber == actualNumber:
            print("You got it!")
            break
        elif guessedNumber < actualNumber:
            print("Too small, try again.")
        else:
            print("Too large, try again.")


def advancedGuessingGame():
    print("Welcome to the Advanced Guessing Game!")

    while True:
        lowerbound = get_integer_input("Enter the lowerbound: ")
        upperbound = get_integer_input("Enter the upperbound: ")

        if upperbound <= lowerbound:
            print("Upper bound must be greater than lower bound.")
        else:
            super_asker(lowerbound, upperbound)
            break


# Call the function to start the game
advancedGuessingGame()

# the tests are looking for the exact string "You got it!". Don't modify that!
>>>>>>> d013b9ec628b1d0ad04438740682cb5cf5ebe20b


if __name__ == "__main__":
    print(advancedGuessingGame())
