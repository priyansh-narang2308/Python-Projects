import random

# Define the board with snakes and ladders
snakes = {16: 6, 47: 26, 49: 11, 56: 53, 62: 19, 64: 60, 87: 24, 93: 73, 95: 75, 98: 78}
ladders = {1: 38, 4: 14, 9: 31, 21: 42, 28: 84, 36: 44, 51: 67, 71: 91, 80: 100}

def roll_dice():
    return random.randint(1, 6)

def move_player(player_position):
    roll = roll_dice()
    player_position += roll
    print(f"Rolled a {roll}")

    if player_position > 100:
        player_position -= roll
        print(f"Roll exceeds 100, staying at {player_position}")
    
    # Check for snakes or ladders
    if player_position in snakes:
        player_position = snakes[player_position]
        print(f"Bitten by a snake! Move down to {player_position}")
    elif player_position in ladders:
        player_position = ladders[player_position]
        print(f"Climb up a ladder! Move up to {player_position}")

    return player_position

def play_game():
    player1_position = 0
    player2_position = 0
    turn = 1
    
    while True:
        if turn == 1:
            input("Player 1, press Enter to roll the dice")
            player1_position = move_player(player1_position)
            print(f"Player 1 is now on position {player1_position}")
            if player1_position == 100:
                print("Player 1 wins!")
                break
            turn = 2
        else:
            input("Player 2, press Enter to roll the dice")
            player2_position = move_player(player2_position)
            print(f"Player 2 is now on position {player2_position}")
            if player2_position == 100:
                print("Player 2 wins!")
                break
            turn = 1

# Start the game
play_game()
