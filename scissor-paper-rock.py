# Scissor Paper Rock
import random

scissor = "\\ /\n |\n/_\\"
paper = "_______\n|     |\n|PAPER|\n|_____|"
rock = "  ____\n /    \\\n| ROCK |\n \\____/"

userInput = input("Enter S for scissor, P for paper, and R for rock: ").lower()

if userInput == "s":
    userInput = scissor
elif userInput == "p":
    userInput = paper
elif userInput == "r":
    userInput = rock
else:
    userInput = None

if userInput == None:
    print("INVALID CHOICE: ")
    exit()

option = [rock, paper, scissor]
computerInput = random.choice(option)

print(f"you: \n{userInput}\n\n\nComputer: \n{computerInput}\n\n")

if (
    (userInput == scissor and computerInput == paper)
    or (userInput == paper and computerInput == rock)
    or (userInput == rock and computerInput == scissor)
):
    print("You won 😉")
elif userInput == computerInput:
    print("Game is draw")
else:
    print("you lose 😝")
