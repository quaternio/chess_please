from pieces import UnicodePieces, Piece


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