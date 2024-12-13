
ChessVar: A Chess Variant Game in Python

ChessVar is a Python class for playing an abstract board game that is a variant of chess. This project introduces new gameplay mechanics while keeping many elements of standard chess intact. It is designed for chess enthusiasts who want to explore creative rule variations in a familiar framework.

Rules of ChessVar

Starting Position
The game starts with the standard chess board and pieces in their usual arrangement.
White moves first, as in traditional chess.
Piece Movement
All standard chess pieces move and capture the same as in standard chess.
Key differences:
No check or checkmate: The game ends when a king is captured.
No castling, en passant, or pawn promotion.
Pawns may move two spaces forward on their first move.
Game Objective
The game ends when one player captures the other’s king. The player whose king is captured loses.
Falcon and Hunter Pieces
Each player has two special pieces: the Falcon and the Hunter, which start off the board.
Falcon: Moves forward like a bishop and backward like a rook.
Hunter: Moves forward like a rook and backward like a bishop.
Entering Falcon or Hunter:
When a player loses a queen, rook, bishop, or knight, they can enter their Falcon or Hunter on a subsequent turn.
The piece may be placed on any empty square in the player's two home ranks.
Losing a second major piece allows the remaining Falcon or Hunter to enter later.

Class Features

The ChessVar class provides functionality for managing and playing the game.

Methods
__init__()

Initializes the game state, board, and turn tracking.

get_game_state() -> str

Returns the current state of the game:
'UNFINISHED'
'WHITE_WON'
'BLACK_WON'
make_move(from_square: str, to_square: str) -> bool

Moves a piece from one square to another.
Returns:
True if the move is valid.
False if the move is invalid (e.g., moving an opponent's piece, illegal move, or game already won).
enter_fairy_piece(piece: str, square: str) -> bool

Places a Falcon or Hunter on the board.
Returns:
True if the placement is valid.
False otherwise (e.g., invalid square, piece not eligible to enter).


