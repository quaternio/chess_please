from chess import Player, ChessGame
import time

def flirt_init_sequence():
    p1_name = input("Player 1, what's your name?\n")
    print("Wow...")
    time.sleep(1)
    print("That's a weird name...\n")
    time.sleep(0.75)
    p2_name = input("Player 2, what' your name?\n")
    print("Now that on the other hand...")
    time.sleep(1)
    print("is a beautiful name!\n")
    time.sleep(0.75)

    return p1_name, p2_name

def init_sequence():
    p1_name = input("\nPlayer 1, what's your name?\n")
    p2_name = input("\nPlayer 2, what' your name?\n")
    return p1_name, p2_name

def main():
    p1_name, p2_name = init_sequence()
    p1 = Player(p1_name, "white")
    p2 = Player(p2_name, "black")

    game = ChessGame(p1, p2)

    # Prompts player 1 (white) to move
    # and displays the updated board

    checkmate = False
    while not checkmate:
        checkmate, is_white_turn, end_game, concede = game.move()
        if end_game or concede:
            break
    
    if checkmate or concede:
        if is_white_turn:
            print(f"\nCongratulations, {p1_name}, you've won!\n")
        else:
            print(f"\nCongratulations, {p2_name}, you've won!\n")
    else:
        print("\nThanks for playing!\n")
        

if __name__ == "__main__":
    main()
