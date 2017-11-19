# Simple number guessing game
# Created by Patrick Dusenge
import random

print("Welcome to Number Guessing!")
print("This game has three modes: \n1 - easy, 2 - normal and 3 - hard \n")

# User picks game mod

game_mod = int(input("Game Mode: "))

# Validate user input
while game_mod <= 0 or game_mod >= 4:
    print("Invalid Entry....try again")
    game_mod = int(input("Game Mode: "))

# Easy Game Mode

if game_mod == 1:

    print("\nEasy Game Mode - 1 to 10\nYou have 5 attempts")
    compt = int(random.randint(1,10))  # Generate random number 1 between 10
    round = 1  # Game starts at round 1

    while round <= 5:  # Maximum of 5 tries

        guess = input("\n" + str(round) + " Guess: ")  # User inputs guess
        if int(guess) == int(compt):  # If guess is correct
            print("Good guess, " + str(compt) + " is correct")
            break  # end game
        elif int(guess) != int(compt):  # If guess is incorrect
            round += 1;  # Add 1 to to round
            print("Nice try, try again ")

    print("\nThe correct answer was " + str(compt))  # show the answer


# Normal Game Mode

if game_mod == 2:

    print("\nEasy Game Mode - 1 to 20\nYou have 10 attempts")
    compt = int(random.randint(1, 20))
    round = 1

    while round <= 10:

        guess = input("\n" + str(round) + " Guess: ")
        if int(guess) == int(compt):
            print("Good guess, " + str(compt) + " is correct")
            break
        elif int(guess) != int(compt):
            round += 1;
            print("Nice try, try again ")

    print("\nThe correct answer was " + str(compt))


# Hard Game Mode

if game_mod == 3:

    print("\nEasy Game Mode - 1 to 30\nYou have 15 attempts")
    compt = int(random.randint(1, 30))
    round = 1

    while round <= 5:

        guess = input("\n" + str(round) + " Guess: ")
        if int(guess) == int(compt):
            print("Good guess, " + str(compt) + " is correct")
            break
        elif int(guess) != int(compt):
            round += 1;
            print("Nice try, try again ")

    print("\nThe correct answer was " + str(compt))
