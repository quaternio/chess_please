import random
from pieces import UnicodePieces, Piece
from typing import Type
import pieces


class Player:
    def __init__(self, name: str, color: str) -> None:
        self._name = name
        self._move_list = []

        if color not in ['white', 'black']:
            raise ValueError("Color must be 'white' or 'black'")
        else:    
            self._color = color

    def specify_move(self):
        move = input("{}, it's your turn!\n".format(self.name))
        self.move_list.append(move)
        return move 


class ChessBoard:
    """Holds game state."""
    def __init__(self):
        self._board = self.initialize_board()

    def initialize_board(self) -> dict:
        """Initializes chess board.

        Returns:
            dict: The initialized chessboard representation
        """
        b_init_seq = [Piece.BROOK, Piece.BKNIGHT, Piece.BBISHOP, Piece.BQUEEN, 
                      Piece.BKING, Piece.BBISHOP, Piece.BKNIGHT, Piece.BROOK]
        w_init_seq = [Piece.WROOK, Piece.WKNIGHT, Piece.WBISHOP, Piece.WQUEEN, 
                      Piece.WKING, Piece.WBISHOP, Piece.WKNIGHT, Piece.WROOK]
        rows = ['1', '2', '3', '4', '5', '6', '7', '8']
        cols = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
        board = {}
        for i in rows:
            board[i] = {}
            for idx, j in enumerate(cols):
                if i == '8':
                    board[i][j] = b_init_seq[idx]
                elif i == '7':
                    board[i][j] = Piece.BPAWN
                elif i == '2':
                    board[i][j] = Piece.WPAWN
                elif i == '1':
                    board[i][j] = w_init_seq[idx]
                else:
                    board[i][j] = Piece.EMPTY
        
        return board

    @property
    def board(self):
        return self._board


class ChessEngine:
    """The backend of the chess game. Encodes all of the chess rules."""
    def __init__(self):
        self._chess_board = ChessBoard()

    def move_valid(self, p1: str, p2: str) -> bool:
        """Checks to see if move is valid

        Args:
            p1 (string): Position of piece to move
            p2 (string): Proposed movement position

        Returns:
            is_valid (bool): True if move is valid
        """
        pass

    def make_move(self, p1: str, p2: str) -> Type[Piece]:
        pass

    @property
    def game_state(self):
        return self._chess_board


class ChessGame:
    """The actual chess game. A game is comprised of players (policies) and an engine (rules, state)."""
    def __init__(self, player_1: Type[Player], player_2: Type[Player]) -> None:
        # Specify players
        self._player_1, self._player_2 = player_1, player_2

        # Initialize the engine... vroom vroom
        self._backend = ChessEngine()

        # Initialize the frontend
        self._frontend = ChessFEUnicode(self._backend.game_state)


class ChessFE:
    def __init__(self, state=None):
        self._state = state

    @property
    def state(self) -> ChessBoard:
        return self._state

    @state.setter
    def state(self, state: ChessBoard) -> None:
        self._state = state

    def display_state(self):
        raise NotImplementedError()


class ChessFEUnicode(ChessFE):
    def __init__(self, state: ChessBoard=None) -> None:
        super().__init__(state)
        pretty_pieces = UnicodePieces()
        self._piece_to_unicode = pretty_pieces.unicode_pieces

    def display_state(self):
        if self._state is not None:
            rows = ['1', '2', '3', '4', '5', '6', '7', '8']
            cols = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
            num_rows = len(rows)
            num_cols = len(cols)
            for idxi, i in enumerate(rows):
                if i == '1':
                    print("  " + " _" * num_cols)
                
                print(str(num_rows - idxi) + " ", end="")
                for idxj, j in enumerate(cols):
                    piece = self._piece_to_unicode[self._state.board[rows[-(idxi+1)]][j]]
                    stop = ""
                    if idxj == num_cols - 1:
                        stop = "|\n"
                    print("|" + piece + stop, end="")
            print("  ", end="")
            for i in range(ord('a'), ord('a') + num_cols):
                print(' ' + chr(i), end="")
            print("\n")
        else:
            print("No state to display")


class UnicodeChessBoard(ChessFE):
    """A command line frontend."""
    def __init__(self):
        self.NUM_ROWS = 8
        self.NUM_COLS = 8
        self._pieces = [["" for j in range(self.NUM_COLS)] for i in range(self.NUM_ROWS)]
        pretty_pieces = UnicodePieces()
        self._pretty_pieces = pretty_pieces.unicode_pieces
        for i in range(self.NUM_ROWS):
            for j in range(self.NUM_COLS):
                self.pieces[i][j] = self.get_initial_placement(i,j)
        self.chess_engine = ChessEngine(self.pieces)

    def get_initial_placement(self, i, j):
        piece = "_"
        piece_order = ['rook','knight','bishop','queen','king','bishop','knight','rook']
        if i == 0:
            piece = self._pretty_pieces['w'][piece_order[j]]
        elif i == 1:
            piece = self._pretty_pieces['w']['pawn']
        elif i == self.NUM_ROWS-2:
            piece = self._pretty_pieces['b']['pawn']
        elif i == self.NUM_ROWS-1:
            piece = self._pretty_pieces['b'][piece_order[j]]
        else:
            piece = self._pretty_pieces['w']['checker'] if (i + j) % 2 == 0 else self._pretty_pieces['b']['checker']

        return piece

    def make_move(self, move: str, player: int) -> bool:
        # TODO: build later
        row_dict = {"A": 0, "a": 0, "B": 1, "b": 1, "C": 2, "c": 2, \
                    "D": 3, "d": 3, "E": 4, "e": 4, "F": 5, "f": 5, \
                    "G": 6, "g": 6, "H": 7, "h": 7}
        move_list = move.split(",")
        from_loc = list(move_list[0])
        to_loc    = list(move_list[1].strip())
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