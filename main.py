# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# prompt the user to enter a value R P or S
# the program should convert this value into Rock, Paper or Scissors respectively
# ask computer to generate a random value between 0 and 2
# 0 becomes rock, 1 becomes paper, 2 becomes scissors
# compare the users choice with the computer's choice to display a message indicating whether user won, lost or drew
# use conditional statements and your own functions


# ask for rock paper or scissors
import random
playAgain = "Y"
userWins = 0
computerWins = 0
computerChoice = "Z"

while playAgain.upper() == "Y":
    userChoice = input("Choose Rock(R), Paper(P) or Scissors(S): ")

# error check that the right letters have been put in and ask again
    while userChoice.upper() != "R" and userChoice.upper() != "P" and userChoice.upper() != "S":
        print("That's not a correct input.")
        userChoice = input("Choose Rock(R), Paper(P) or Scissors(S): ")

# generate a randon number and turn into Rock, Paper or Scissors
    randomNum = random.randint(0,2)
# print(randomNum)
    if randomNum == 0:
        computerChoice = "R"
    elif randomNum == 1:
        computerChoice = "P"
    elif randomNum == 2:
        computerChoice = "S"

# compare user and computer choice if computer choice is R and return result
    if computerChoice == "R" and userChoice.upper() == "R":
        print("I chose Rock. It's a draw.")
    elif computerChoice == "R" and userChoice.upper() == "P":
        userWins +=1
        print("I chose Rock. You win")
    elif computerChoice == "R" and userChoice.upper() == "S":
        computerWins += 1
        print("I chose Rock. I win")

# compare user and computer choice if computer choice is P and return result
    if computerChoice == "P" and userChoice.upper() == "P":
        print("I chose paper. It's a draw.")
    elif computerChoice == "P" and userChoice.upper() == "S":
        userWins +=1
        print("I chose paper. You win")
    elif computerChoice == "P" and userChoice.upper() == "R":
        computerWins += 1
        print("I chose paper. I win")

# compare user and computer choice if computer choice is S and return result
    if computerChoice == "S" and userChoice.upper() == "S":
        print("I chose scissors. It's a draw. ")
    elif computerChoice == "S" and userChoice.upper() == "R":
        userWins +=1
        print("I chose scissors. You win. ")
    elif computerChoice == "S" and userChoice.upper() == "P":
        computerWins += 1
        print("I chose scissors. I win. ")
# ask if they want to see total wins
    seeTotal = input("Do you want to see total wins? press Y or N: ")
    if seeTotal.upper() == "Y":
        print("The computer has won " + str(computerWins) + " games.")
        print("You have won " + str(userWins) + " games.")
# do error handling on this statement

# ask if they want to play again
    playAgain = input("Do you want to play again? Press Y or N:")
# do error handling on this statement too





