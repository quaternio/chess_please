from frontend import ChessBoard, ChessFEUnicode
from pieces import Piece
from agents import Player
from typing import Type

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