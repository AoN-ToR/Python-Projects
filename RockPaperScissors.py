import random

print("Welcome to my rock/paper/scissors game !")

options = ["rock", "paper", "scissors"]

computer_wins = 0
user_wins = 0


while True:
    user_choice = input("Type Rock/Paper/Scissors to play. Press Q to quit.\n").lower()
    if user_choice == "q":
        print("You won %d times! \nThe computer won %d times!" %(user_wins, computer_wins))
        if user_wins <= computer_wins:
            print("You lost... Better luck next time!")
        elif computer_wins == user_wins:
            print("How unbelievable! It's a draw, well played!")
        else:
            print("You won, congrats!")
        quit()

    elif user_choice not in options:
        print("Please input one of the allowed choices:")
    
    else:
        computer_choice = options[random.randint(0,2)]
        if user_choice == computer_choice:
            print("Computer chose %s... it's a draw!" %computer_choice)
        elif (user_choice == "rock" and computer_choice == "scissors") or (user_choice == "paper" and computer_choice == "rock") or (user_choice == "scissors" and computer_choice == "paper"):
            print("Computer chose %s... You've won!" %computer_choice)
            user_wins += 1
        else:
            print("Computer chose %s... You've lost!" %computer_choice)
            computer_wins += 1
    
