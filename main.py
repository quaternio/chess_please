from lib.chess import Player, ChessGame
import time

def init_sequence():
    p1_name = input("\nPlayer 1, what's your name?\n")
    p2_name = input("\nPlayer 2, what' your name?\n")
    return p1_name, p2_name

def main():
    p1_name, p2_name = init_sequence()
    p1 = Player(p1_name, "white")
    p2 = Player(p2_name, "black")

    game = ChessGame(p1, p2)

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
