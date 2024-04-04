# Import the required libraries.
import random
import time

# Function to get the user's choice of Rock, Paper, or Scissors.
def User_Choice():
    selection = input("Rock/Paper/Scissors: ")
    # Ensure the user input is valid.
    while selection.lower() != "scissors" and selection.lower() != "rock" and selection.lower() != "paper":
        selection = input("Rock/Paper/Scissors: ")
    # Map the user input to integer values: 0 for Rock, 1 for Paper, 2 for Scissors.
    if selection.lower() == "rock":
        selection = 0
    elif selection.lower() == "paper":
        selection = 1
    else:
        selection = 2
    return selection

# Function to generate the computer's choice of Rock, Paper, or Scissors.
def PC_Choice():
    choices = ["rock", "paper", "scissors"]
    selection = random.choice(choices)
    # Map the computer's choice to integer values: 0 for Rock, 1 for Paper, 2 for Scissors.
    if selection.lower() == "rock":
        selection = 0
    elif selection.lower() == "paper":
        selection = 1
    else:
        selection = 2
    # Print the computer's choice.
    print(selection)
    return selection

# Function to conduct the Rock, Paper, Scissors match.
def match():
    # Initialize variables to track game history and scores.
    History = []
    user_wins = 0
    pc_wins = 0
    round = 0
    # Continue the game until either the user or the computer wins 3 rounds.
    while user_wins != 3 and pc_wins != 3:
        round += 1
        # Get the user's choice.
        user = User_Choice()
        # Get the computer's choice.
        pc = PC_Choice()
        
        # Print the user's choice.
        if user == 0:
            print("You chose Rock!")
        elif user == 1:
            print("You chose Paper!")
        else:
            print("You chose Scissors!")

        time.sleep(1)

        # Print the computer's choice.
        if pc == 0:
            print("PC chose Rock!")
        elif pc == 1:
            print("PC chose Paper!")
        else:
            print("PC chose Scissors!")

        # Determine the winner of the round and update scores accordingly.
        if user - pc > 0 or user - pc == -2:
            print("YOU WIN!",end="\n")
            user_wins += 1
            Current_Score(user_wins, pc_wins)
        elif user - pc < 0 or user - pc == 2:
            print("YOU LOSE!")
            pc_wins += 1
            Current_Score(user_wins, pc_wins)
        else:
            print("TIE!!")
            Current_Score(user_wins, pc_wins)
        
        # Convert user and pc choices from integers to their corresponding strings.
        if user == 0:
            user = "Rock"
        elif user == 1:
            user = "Paper"
        else:
            user = "Scissors"

        if pc == 0:
            pc = "Rock"
        elif pc == 1:
            pc = "Paper"
        else:
            pc = "Scissors"
        
        # Log the game data for this round.
        Game_Data(History, user, pc, round, user_wins, pc_wins)

# Function to print the current score.
def Current_Score(user_wins, pc_wins):
    print(f"Current Score-->\tYou - {user_wins} \tPC - {pc_wins}")

# Function to log game data for each round.
def Game_Data(History, user, pc, round, user_wins, pc_wins):
    History.append(f"-----Round {round}-----")
    History.append(f"| Player: {user}|")
    History.append(f"| Computer: {pc}|")
    History.append(f"| Score: {user_wins}-{pc_wins}|")
    # Check if either the user or the PC has won 3 rounds to end the game.
    if user_wins == 3 or pc_wins == 3:
        End_Game(History)

# Function to display the final game results.
def End_Game(History):
    print("-----!GAME OVER!-----")
    time.sleep(0.5)
    print("Loading your stats...")
    time.sleep(1.5)
    # Print the game history.
    for i in History:
        time.sleep(0.2)
        print(i)

# Main program
match()
