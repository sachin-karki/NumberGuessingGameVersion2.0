# Sachin Karki
# Purpose: Assignment 10: Number Guessing Game Version 2.0 with new added features.

# Welcome Screen
print("Welcome to Number Guessing Game Version 2.0")
print()

# Prompting the user for their name
name = input("Please Enter Your Name:")
print()

# Setting up conditions
topPlayers = "topPlayers.txt"
correctNumber = 10

while True:
    try:
        numberInput = input("Choose a number between 1 to 100 (or Q/q to Quit):")

        if numberInput.lower() == 'q':
            print("Quitting the game.")
            break  # This stops the program

        numberInput = int(numberInput)
        numberGuess = 1  # Initializes the number of guesses for this game

        while numberInput != correctNumber:
            if numberInput > correctNumber:
                print("Wrong Guess, It's less than", numberInput, "Please Try Again")
            elif numberInput < correctNumber:
                print("Wrong Guess, It's more than", numberInput, "Please Try Again")

            numberInput = int(input("Try again:"))
            numberGuess += 1

        print("Good Job! Your Guess is Correct")
        print("It took you", numberGuess, "guesses to get the right answer")

        # Reads the contents of the topPlayers.txt file
        with open(topPlayers, "r") as file:
            lines = file.readlines()

        # Updates the list of players and their scores
        playerScores = [line.strip().split() for line in lines]

        # Appends the player name and the number of guesses to the topPlayers.txt
        playerScores.append([numberGuess, name])

        # Sorts the player scores by the number of guesses (lowest to highest)
        playerScores.sort(key=lambda x: int(x[0]))

        # Limits the file to 5 rows
        playerScores = playerScores[:5]

        # Write the updated list back to the topPlayers.txt file
        with open(topPlayers, "w") as file:
            for score, player_name in playerScores:
                file.write(f"{score} {player_name}\n")

        # Asks the user if they want to play the game again
        play = input("Do you want to play the game again? (Yes/No): ")
        if play.lower() != 'yes':
            break

        # Catches or alerts users of any non-numeric input
    except ValueError:
        print("Invalid input. Please enter a valid number between 1 and 100.")

        # Lets user quit with CTRL+D
    except EOFError:
        print("Terminating Game.")
        exit()

