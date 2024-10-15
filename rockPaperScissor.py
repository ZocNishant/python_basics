import random

def play():
    computer_choice = random.choice(['r', 'p', 's'])
    print(computer_choice)

    user_input = input("'r' for rock, 's' for scissors and 'p' for paper")


    if user_input == 'r' and computer_choice == 's':
        print("User has won the game.")
    elif user_input == 's' and computer_choice == 'p':
        print("User has won the game.")
    elif user_input == 'p' and computer_choice == 'r':
        print("User has won the game.")
    elif user_input == computer_choice:
        print("The game has tied.")
    else:
        print("Computer wins the game.")



play()



# Rock beats Scissors.
# Scissors beat Paper.
# Paper beats Rock.