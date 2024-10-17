import random

# def play():
#     computer_choice = random.choice(['r', 'p', 's'])
#     print(computer_choice)

#     user_input = input("'r' for rock, 's' for scissors and 'p' for paper")


#     if user_input == 'r' and computer_choice == 's':
#         print("User has won the game.")
#     elif user_input == 's' and computer_choice == 'p':
#         print("User has won the game.")
#     elif user_input == 'p' and computer_choice == 'r':
#         print("User has won the game.")
#     elif user_input == computer_choice:
#         print("The game has tied.")
#     else:
#         print("Computer wins the game.")



# play()

def khelam():
    user = input("'r' for rock, 's' for scissors and 'p' for paper")
    computer = random.choice(['r','p','s'])

    if user == computer:
        return "It's a tie."
    
    if is_winner(user, computer):
        return 'You Won.'

    return "You Lost."
    

def is_winner(player, opponent):
    if(player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True


print(khelam())

# Rock beats Scissors.
# Scissors beat Paper.
# Paper beats Rock.