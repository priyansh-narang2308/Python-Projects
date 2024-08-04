import random

def roll_dice():
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    return die1, die2

def play_game():

    print("Welcome to the Dice Game!")
    input("Press Enter to roll the dice...")

    # Player 1's roll
    player1_die1, player1_die2 = roll_dice()
    player1_total = player1_die1 + player1_die2
    print(f"Player 1 rolled: {player1_die1} and {player1_die2} (Total: {player1_total})")

    # Player 2's roll
    player2_die1, player2_die2 = roll_dice()
    player2_total = player2_die1 + player2_die2
    print(f"Player 2 rolled: {player2_die1} and {player2_die2} (Total: {player2_total})")

    # Determine the winner
    if player1_total > player2_total:
        print("Player 1 wins!")
    elif player2_total > player1_total:
        print("Player 2 wins!")
    else:
        print("It's a tie!")

if __name__ == "__main__":
    play_game()
