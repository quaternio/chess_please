# -*- coding: utf-8 -*-
import random
import unicode_pieces

pieces = unicode_pieces.ELEMENTS

class Player:
    def __init__(self, name):
        self.name = name
        self.move_list = []

    def specify_move(self):
        move = input("{}, it's your turn!\n".format(self.name))
        self.move_list.append(move)
        return move


class ChessBoard:
    def __init__(self):
        self.NUM_ROWS = 8
        self.NUM_COLS = 8
        self.pieces = [["" for j in range(self.NUM_COLS)] for i in range(self.NUM_ROWS)] 
        for i in range(self.NUM_ROWS):
            for j in range(self.NUM_COLS):
                self.pieces[i][j] = self.get_initial_placement(i,j)

    def get_initial_placement(self, i, j):
        piece = "_"
        piece_order = ['rook','knight','bishop','queen','king','bishop','knight','rook']
        if i == 0:
            piece = pieces['w'][piece_order[j]]
        elif i == 1:
            piece = pieces['w']['pawn']
        elif i == self.NUM_ROWS-2:
            piece = pieces['b']['pawn']
        elif i == self.NUM_ROWS-1:
            piece = pieces['b'][piece_order[j]]
        else:
            piece = pieces['w']['checker'] if (i + j) % 2 == 0 else pieces['b']['checker']

        return piece

    def make_move(self, move: str, player: int) -> bool:
        # TODO: build later
        row_dict = {"A": 0, "a": 0, "B": 1, "b": 1, "C": 2, "c": 2, \
                    "D": 3, "d": 3, "E": 4, "e": 4, "F": 5, "f": 5, \
                    "G": 6, "g": 6, "H": 7, "h": 7}
        move_list = move.split(",")
        from_loc = list(move_list[0])
        to_loc    = list(move_list[1])
        from_pos = (int(from_loc[1])-1, row_dict[from_loc[0]])
        to_pos   = (int(to_loc[1])-1, row_dict[to_loc[0]])
        piece = self.pieces[from_pos[0]][from_pos[1]]
        self.pieces[to_pos[0]][to_pos[1]] = piece
        self.pieces[from_pos[0]][from_pos[1]] = pieces['w']['checker'] if (from_pos[0] + from_pos[1]) % 2 == 0 else pieces['b']['checker']
        # Later fix to return False if invalid move

        return True


    def render_board(self):
        """Print the current state of the chess board"""
        NUM_ROWS = 8
        NUM_COLS = 8
        for i in range(NUM_ROWS):
            if i == 0:
                print("  " + " _"*NUM_COLS)
            
            print(str(NUM_ROWS-i) + " ", end="")
            for j in range(NUM_COLS):
                #"_" # Call a function piece(i,j) that prints appropriate piece later
                piece = self.pieces[-(i+1)][j] 
                stop = ""
                if j == NUM_COLS-1:
                    stop = "|\n"
                print("|"+piece+stop, end="")
        print("  ", end="")
        for i in range(ord('a'), ord('a')+NUM_COLS):
            print(' ' + chr(i), end="")
        print("\n")    

