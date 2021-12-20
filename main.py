import random

rpm = ["rock", "paper", "scissors"]

def player_move():
    """
    player_move(): Get the player choice.
    None ---> str
    """
    choice = input("rock, paper or scissors? --> ")
    while choice not in rpm:
        print("Please enter 'rock', 'paper' or 'scissors")
        choice = input("rock, paper or scissors? --> ")
    return choice

def computer_move():
    """
    computer_move(): Get the computer choice.
    None ---> str
    """
    choice = random.choice(rpm)
    return choice

def decide_winner(player, computer):
    """
    decide_winner(player, computer): decides who the winner is.
    str, str ---> None
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
    if player == "paper" and computer == "rock":
        return print(f"Computer played {computer}. YOU WON!")

def start_game():
    """
    start_game():Introduction to the game.
    None ---> None
    """
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
            decide_winner(player, computer)
            exit = input("Type 'exit' to exit the game, Enter to continute playing.")
            if exit == "exit":
                break
        elif flag == "quit":
            exit()
        else:
            print("Please enter a valid argument.")
            flag = input()

start_game()