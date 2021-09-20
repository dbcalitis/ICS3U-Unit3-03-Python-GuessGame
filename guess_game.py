#!/usr/bin/env python3

# Created by: Daria Bernice Calitis
# Created on: Sept 2021
# This program is the number guessing game

import constants


def main():
    # This function is the number guessing game
    # input
    guess_number = int(input("Enter a number as your guess (0-9): "))

    # process & output
    if guess_number == constants.ANSWER:
        print("You guessed correctly!")
    else:
        print("You guessed incorrectly.")
    print("The correct answer is {0}.".format(constants.ANSWER))
    print("\nDone.")


if __name__ == "__main__":
    main()
