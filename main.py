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
    p1_name = input("Player 1, what's your name?\n")
    p2_name = input("Player 2, what' your name?\n")
    return p1_name, p2_name

def main():
    p1_name, p2_name = init_sequence()
    p1 = Player(p1_name, "white")
    p2 = Player(p2_name, "black")

    game = ChessGame(p1, p2)
    game._frontend.display_state()
        

if __name__ == "__main__":
    main()
