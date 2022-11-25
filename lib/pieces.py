from enum import Enum

class UnicodePieces:
    """Specifies Pretty Printing of Unicode Chess."""
    def __init__(self):
        self._unicode_pieces = self.construct_unicode_map()
    
    @property
    def unicode_pieces(self):
        return self._unicode_pieces

    def construct_unicode_map(self):
        unicode_map = {}
        unicode_map[Piece.WPAWN]   = u'\u265F'
        unicode_map[Piece.WROOK]   = u'\u265C'
        unicode_map[Piece.WKNIGHT] = u'\u265E'
        unicode_map[Piece.WBISHOP] = u'\u265D'
        unicode_map[Piece.WQUEEN]  = u'\u265B'
        unicode_map[Piece.WKING]   = u'\u265A'
        unicode_map[Piece.BPAWN]   = u'\u2659'
        unicode_map[Piece.BROOK]   = u'\u2656'
        unicode_map[Piece.BKNIGHT] = u'\u2658'
        unicode_map[Piece.BBISHOP] = u'\u2657'
        unicode_map[Piece.BQUEEN]  = u'\u2655'
        unicode_map[Piece.BKING]   = u'\u2654'
        unicode_map[Piece.EMPTY]   = '_'

        return unicode_map


class Piece(Enum):
    WPAWN = 0
    WROOK = 1
    WKNIGHT = 2
    WBISHOP = 3
    WQUEEN = 4
    WKING = 5
    BPAWN = 6
    BROOK = 7
    BKNIGHT = 8
    BBISHOP = 9
    BQUEEN = 10
    BKING = 11
    EMPTY = 12

    