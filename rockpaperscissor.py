import random

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def get_winner(player, computer):
    if player == computer:
        return "It's a tie!"
    elif (player == 'rock' and computer == 'scissors') or \
         (player == 'scissors' and computer == 'paper') or \
         (player == 'paper' and computer == 'rock'):
        return "You win!"
    else:
        return "Computer wins!"

def play():
    print("Welcome to Rock, Paper, Scissors!")
    player = input("Enter your choice (rock, paper, or scissors): ").lower()

    if player not in ['rock', 'paper', 'scissors']:
        print("Invalid choice. Please choose rock, paper, or scissors.")
        return

    computer = get_computer_choice()
    print(f"Computer chose: {computer}")
    result = get_winner(player, computer)
    print(result)

# Run the game
play()
