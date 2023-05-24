#
#   This program generates a random number between 1 and 100 
#
#   You have to guess it
#

import random
import time

while True:

    tries = 7 # Set the trys to 7
    number = random.randint(1,100) # Generate the random number

    print("\n\n\nGuess the number between 1-100\n")

    while True:

        guess = int(input("Guess: ")) # Let the user take his guess

        # Check if the guess is right
        if guess == number:

            print("\nYou guessed the number!")
            break
        
        tries -= 1 # Decrease the trys by 1

        # Check if tries are 0
        if tries == 0:
            print(f"\nYou lost! The correct number was {number}")

        if guess > number: print(f"\nThe number is lower than your guess \nYou still have {tries} trys\n") # Check if the number is lower than the guess

        elif guess < number: print(f"\nThe number is higher than your guess \nYou still have {tries} trys\n") # Check if the number is higher than the guess

    time.sleep(3) # Delay the next round






