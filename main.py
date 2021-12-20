import random

rpm = ["rock", "paper", "scissors"]

def player_move():
    """
    Get the player choice.
    None ---> str
    """
    choice = input("rock, paper or scissors? --> ")
    while choice not in rpm:
        print("Please enter 'rock', 'paper' or 'scissors")
        choice = input("rock, paper or scissors? --> ")
    return choice

def computer_move():
    """
    Get the computer choice.
    None ---> str
    """
    choice = random.choice(rpm)
    return choice

def decide_winner(player, computer):
    """
    Get the player choice.
    str, str ---> str
    """
    if player == computer:
         return print(f"Computer played {computer}. IT'S A DRAW!!!")
    if player == "rock" and computer == "paper":
        return print(f"Computer played {computer}. YOU LOST!")
    if player == "rock" and computer == "scissors":
        return print(f"Computer played {computer}. YOU WON!")
    if player == "scissors" and computer == "paper":
        return print(f"Computer played {computer}. YOU WON!")
    if player == "scissors" and computer == "rock":
        return print(f"Computer played {computer}. YOU LOST!")
    if player == "paper" and computer == "scissors":
        return print(f"Computer played {computer}. YOU LOST!")
    if player == "paper" and computer == "rock ":
        return print(f"Computer played {computer}. YOU WON!")

def start_game():
    """Introduction to the game."""
    print("########### ROCK PAPERS SCISSORS ###########")
    print("#                                          #")
    print("#            type 'start' to play          #")
    print("#               'quit' to quit             #")
    print("#                                          #")
    print("############################################")
    flag = input()
    while flag != "start" or flag != "quit":
        if flag == "start":
            player = player_move()
            computer = computer_move()
            print(type(decide_winner(player, computer)))
            exit = input("Type 'exit' to exit the game, Enter to continute playing.")
            if exit == "exit":
                break
        elif flag == "quit":
            exit()
        else:
            print("Please enter a valid argument.")
            flag = input()



start_game()