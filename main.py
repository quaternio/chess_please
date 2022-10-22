from chess import UnicodeChessBoard, Player, ChessGame
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
    #chessboard = UnicodeChessBoard()
    p1_name, p2_name = init_sequence()
    p1 = Player(p1_name, "white")
    p2 = Player(p2_name, "black")

    game = ChessGame(p1, p2)
    game._frontend.display_state()

    #session_active = True
    #while session_active:
        #chessboard.render_board()
        #p1_move = p1.specify_move()
        #move_valid = chessboard.make_move(p1_move, 1) 
        


if __name__ == "__main__":
    main()
