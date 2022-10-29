from operator import is_
from pieces import UnicodePieces, Piece
from typing import Tuple


class ChessBoard:
    """Holds game state."""
    def __init__(self):
        self._board = self.initialize_board()

    @property
    def board(self):
        return self._board

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

    def move_piece(self, pos1: str, pos2: str) -> None:
        """Change the board's state as specified.

        Args:
            pos1 (str): Position of piece to be moved
            pos2 (str): Destination of piece to be moved
        """
        p1c1, p1c2 = self.unpack_move_string(pos1)
        p2c1, p2c2 = self.unpack_move_string(pos2)
        self._board[p2c1][p2c2] = self._board[p1c1][p1c2]
        self._board[p1c1][p1c2] = Piece.EMPTY

    def unpack_move_string(self, pos: str) -> Tuple[str,str]:
        idxs = list(pos)
        return idxs[1], idxs[0]

    def pack_move_string(self, r_idx: str, c_idx: str) -> str:
        return ''.join((c_idx, r_idx))
    

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

    def player_turn(self, is_white_turn):
        player = "Player 1" if is_white_turn else "Player 2"
        move = input(f"{player}, it's your move.\n")
        positions = [pos.strip() for pos in move.split(',')]
        pos1 = positions[0]
        pos2 = positions[1]

        return pos1, pos2