
# # Description: My chessvar code is for a variation of chess that has the hunter and fairy pieces. It essentially plays just like normal chess except for a few exceptions like there isnt any castling en-passiant or checkmate. The winner is the first person that captures the others king
def move_conversion(position):
    return tuple([int(position[1]),ord(position[0])-97])

"""This function finalize_move takes a temporary game board (temp_board), the current position of a game piece (current_position), 
and the final position where the piece is to be moved (final_position). It then updates the temp_board by moving the piece from the current 
position to the final position and clears the current position. Finally, it returns the updated temp_board."""
def finalize_move(temp_board,current_position, final_position):
    temp_board[final_position[0]][final_position[1]] = temp_board[current_position[0]][
        current_position[1]]
    temp_board[current_position[0]][current_position[1]] = ''
    return temp_board

"""This function checks whether the given piece belongs to the player whose turn it currently is, and returns True if it does, False otherwise."""
def is_player_turn(piece,player):
    return piece[0] == player

class ValidateMove:
    """ this function checks whether a horizontal move on the game board from the current position to the final position is valid.
    It considers obstacles (other pieces) between the two positions and ensures that the final position is either empty or occupied
    by an opponent's piece. If the move is valid, it returns True; otherwise, it returns False."""
    def validate_horizontal_move(game_board, current_position,final_position):
        piece_in_final_position = game_board[final_position[0]][final_position[1]]
        direction = int((current_position[1] - final_position[1]) / abs(current_position[1] - final_position[1]))
        for i in range(int(current_position[1]+direction), final_position[1],direction):
            if game_board[current_position[0]][i] != '':
                return False
        else:
            if piece_in_final_position:
                if piece_in_final_position[0] == game_board[current_position[0]][current_position[1]][0]:
                    return False
                else:
                    return True
            else:
                return True

    def validate_vertical_move(game_board, current_position, final_position):
        piece_in_final_position = game_board[final_position[0]][final_position[1]]
        direction = (final_position[0]- current_position[0]) / abs(current_position[0] - final_position[0])
        for i in range(int(current_position[0] + direction), final_position[0], int(direction)):
            if game_board[i][current_position[1]] != '':
                return False
        else:
            if piece_in_final_position:
                if piece_in_final_position[0] == game_board[current_position[0]][current_position[1]][0]:
                    return False
                else:
                    return True
            else:
                return True
    """ this function checks whether a vertical move on the game board from the current position to the final position is valid. 
    It considers obstacles (other pieces) between the two positions and ensures that the final position is either empty or occupied 
    by an opponent's piece. If the move is valid, it returns True; otherwise, it returns False."""

    def validate_diagonal_move(game_board, current_position, final_position):
        piece_in_final_position = game_board[final_position[0]][final_position[1]]
        row_direction = (final_position[0] - current_position[0]) // abs(final_position[0] - current_position[0])
        col_direction = (final_position[1] - current_position[1]) // abs(final_position[1] - current_position[1])

        row, col = current_position
        while (row, col) != final_position:
            row += row_direction
            col += col_direction
            if (row, col) == final_position:
                break
            if game_board[row][col] != '':
                return False

        if piece_in_final_position:
            if piece_in_final_position[0] == game_board[current_position[0]][current_position[1]][0]:
                return False
            else:
                return True
        else:
            return True


class ChessVar:
    """ This initialization sets up the initial state of the game, including the game state, the current board configuration,
    the current player, and the availability of fairy pieces for each player."""
    def __init__(self):
        self.game_state = 'UNFINISHED'
        self.current_board = [
                ['WF', 'WH', 'BF', 'BH'],
                ['WR', 'Wk', 'WB', 'WQ', 'WK', 'WB', 'Wk', 'WR'],
                ['WP', 'WP', 'WP', 'WP', 'WP', 'WP', 'WP', 'WP'],
                ['', '', '', '', '', '', '', ''],
                ['', '', '', '', '', '', '', ''],
                ['', '', '', '', '', '', '', ''],
                ['', '', '', '', '', '', '', ''],
                ['BP', 'BP', 'BP', 'BP', 'BP', 'BP', 'BP', 'BP'],
                ['BR', 'Bk', 'BB', 'BQ', 'BK', 'BB', 'Bk', 'BR'],
            ]
        self.current_player = 'W'
        self.white_fairy_pieces_available = 0
        self.black_fairy_pieces_available = 0

    """provide access to the game_state attribute from outside the class. It allows other parts of the program to 
    retrieve the current state of the game by calling this method on an instance of the class."""
    def get_game_state(self):
        return self.game_state

    """this method handles making a move in the game. It checks if the game is ongoing, if the move is valid, 
    makes the move, and updates the game state accordingly. If the move is successful, it returns True; otherwise, it returns False."""
    def make_move(self, current_position, final_position):
        if self.game_state != 'UNFINISHED':
            return False
        current_position = move_conversion(current_position)
        final_position = move_conversion(final_position)
        if final_position[0] < 1 or final_position[0] >8 or final_position[1] < 0 or final_position[1] > 7:
            return False
        piece_to_move = self.current_board[current_position[0]][current_position[1]]
        if not is_player_turn(piece_to_move, self.current_player):
            return False
        royal_taken_on_valid_move = False
        piece_to_attack = self.current_board[final_position[0]][final_position[1]]
        if piece_to_attack and piece_to_attack[1] in 'kQRB':
            royal_taken_on_valid_move = True
        if piece_to_move[1] == 'K':
            successful_move = self.move_king(current_position, final_position)
        elif piece_to_move[1] == 'Q':
            successful_move = self.move_queen(current_position, final_position)
        elif piece_to_move[1] == 'B':
            successful_move = self.move_bishop(current_position, final_position)
        elif piece_to_move[1] == 'k':
            successful_move = self.move_knight(current_position, final_position)
        elif piece_to_move[1] == 'R':
            successful_move = self.move_rook(current_position, final_position)
        elif piece_to_move[1] == 'P':
            successful_move = self.move_pawn(current_position, final_position)
        elif piece_to_move[1] == 'F':
            successful_move = self.move_falcon(current_position, final_position)
        elif piece_to_move[1] == 'H':
            successful_move = self.move_hunter(current_position, final_position)
        else:
            print('Invalid move, try again.')
            return False
        if successful_move:
            self.current_player = 'B' if self.current_player == 'W' else 'W'
            if royal_taken_on_valid_move:
                if self.current_player == 'B':
                    self.black_fairy_pieces_available += 1
                else:
                    self.white_fairy_pieces_available += 1
        else:
            return False
        spaces = []
        for x in self.current_board:
            for y in x:
                spaces.append(y)
        if self.current_player + "K" not in spaces:
            self.game_state = 'BLACK_WON' if self.current_player == 'W' else 'WHITE_WON'
        return True

    """ This method handles the entry of a fairy piece into the game. It checks if the conditions for placing the fairy piece are met, 
    updates the game board accordingly, updates the current player, and returns True if the entry is successful; otherwise, it returns False."""
    def enter_fairy_piece(self,type_of_piece,position):
        position = move_conversion(position)
        fairy_dict = {'F':'WF','H':'WH','f':'BF','h':'BH'}
        if self.current_board[position[0]][position[1]] != '':
            return False
        else:
            can_move = False
            temp_board = self.current_board.copy()
            if self.current_player == 'B' and self.black_fairy_pieces_available:
                if temp_board[0][2] and temp_board[0][3] or self.black_fairy_pieces_available > 1:
                    if position[0] in [7,8]:
                        can_move = True
            if self.current_player == 'W' and self.white_fairy_pieces_available:
                if temp_board[0][0] and temp_board[0][1] or self.white_fairy_pieces_available > 1:
                    if position[0] in [1, 2]:
                        can_move = True
            if can_move:
                temp_board[position[0]][position[1]] = fairy_dict[type_of_piece]
                temp_board[0][temp_board[0].index(fairy_dict[type_of_piece])] = ''
                self.current_board = temp_board
                self.current_player = 'B' if self.current_player == 'W' else 'W'
                return True
            else:
                return False

    """This method handles the movement of the king piece. It first checks if the move is within one square in any direction.
     Then, depending on whether the move is diagonal, horizontal, or vertical, it validates the move using appropriate validation
      methods and updates the game board if the move is valid. If the move is invalid at any point, it returns False.
       If the move is successful, it returns True."""
    def move_king(self, current_position, final_position):
        if abs(current_position[1] - final_position[1]) > 1 or abs(current_position[0] - final_position[0]) > 1:
            return False
        if current_position[1] != final_position[1] and current_position[0] != final_position[0]:
            if ValidateMove.validate_diagonal_move(self.current_board, current_position, final_position):
                self.current_board = finalize_move(self.current_board, current_position, final_position)
                return True
        elif current_position[1] != final_position[1]:
            if ValidateMove.validate_horizontal_move(self.current_board, current_position, final_position):
                self.current_board = finalize_move(self.current_board, current_position, final_position)
                return True
        elif current_position[0] != final_position[0]:
            if ValidateMove.validate_vertical_move(self.current_board, current_position, final_position):
                self.current_board = finalize_move(self.current_board, current_position, final_position)
                return True
    """ This method handles the movement of the queen piece. It first checks if the move is diagonal,
     then if it is vertical, and finally if it is horizontal. Depending on the direction of the move,
      it validates the move using appropriate validation methods and updates the game board if the move is valid.
       If the move is invalid at any point, it returns False. If the move is successful, it returns True."""
    def move_queen(self, current_position, final_position):
        if abs(current_position[1] - final_position[1]) == abs(current_position[0] - final_position[0]):
            if ValidateMove.validate_diagonal_move(self.current_board, current_position, final_position):
                self.current_board = finalize_move(self.current_board, current_position, final_position)
                return True
        elif abs(current_position[1] - final_position[1]) == 0:
            if ValidateMove.validate_vertical_move(self.current_board, current_position, final_position):
                self.current_board = finalize_move(self.current_board, current_position, final_position)
                return True
        elif abs(current_position[0] - final_position[0]) == 0:
            if ValidateMove.validate_horizontal_move(self.current_board, current_position, final_position):
                self.current_board = finalize_move(self.current_board, current_position, final_position)
                return True

    """This method handles the movement of the bishop piece. It first checks if the move is invalid if the bishop does not move diagonally.
     Then, if the move is diagonal, it validates the move using appropriate validation methods and updates the game board if the move is valid.
      If the move is invalid, it returns False. If the move is successful, it returns True."""
    def move_bishop(self, current_position, final_position):
        if abs(current_position[1] - final_position[1]) == 0 or abs(current_position[0] - final_position[0]) == 0:
            return False
        if abs(current_position[1] - final_position[1]) == abs(current_position[0] - final_position[0]):
            if ValidateMove.validate_diagonal_move(self.current_board, current_position, final_position):
                self.current_board = finalize_move(self.current_board, current_position, final_position)
                return True

    """This method handles the movement of the knight piece. It checks if the move is valid for the knight (i.e., moving in an L-shape)
     and updates the game board if the move is valid. If the move is invalid, it returns False. If the move is successful, it returns True."""
    def move_knight(self, current_position, final_position):
        piece_in_final_position = self.current_board[final_position[0]][final_position[1]]
        if piece_in_final_position:
            if piece_in_final_position[0] == self.current_board[current_position[0]][current_position[1]][0]:
                return False
        if abs(current_position[0] - final_position[0]) == 1 and abs(current_position[1] - final_position[1]) == 2:
            self.current_board = finalize_move(self.current_board, current_position, final_position)
            return True
        if abs(current_position[1] - final_position[1]) == 1 and abs(current_position[0] - final_position[0]) == 2:
            self.current_board = finalize_move(self.current_board, current_position, final_position)
            return True

    """This method handles the movement of the rook piece. It first checks if the move is invalid if the rook does not move horizontally
     or vertically. Then, depending on whether the move is vertical or horizontal, it validates the move using appropriate validation methods
      and updates the game board if the move is valid. If the move is invalid, it returns False. If the move is successful, it returns True."""
    def move_rook(self, current_position, final_position):
        if abs(current_position[1] - final_position[1]) != 0 and abs(current_position[0] - final_position[0]) != 0:
            return False
        if abs(current_position[1] - final_position[1]) == 0:
            if ValidateMove.validate_vertical_move(self.current_board, current_position, final_position):
                self.current_board = finalize_move(self.current_board, current_position, final_position)
                return True
        elif abs(current_position[0] - final_position[0]) == 0:
            if ValidateMove.validate_horizontal_move(self.current_board, current_position, final_position):
                self.current_board = finalize_move(self.current_board, current_position, final_position)
                return True

    """This method handles the movement of pawn pieces, including special initial two-square moves and regular one-square moves,
     as well as capturing of opponent pieces diagonally. It checks various conditions to validate the move and updates the game board accordingly.
      If the move is invalid, it returns False. If the move is successful, it returns True."""
    def move_pawn(self, current_position, final_position):
        if self.current_player == 'W':
            if current_position[0] >= final_position[0]:
                return False
            if current_position[1] == final_position[1]:
                if current_position[0] == 2 and final_position[0] == 4 and \
                        self.current_board[3][final_position[1]] == '' and \
                        self.current_board[4][final_position[1]] == '':
                    self.current_board = finalize_move(self.current_board, current_position, final_position)
                    return True
                if current_position[0] - final_position[0] == -1:
                    if self.current_board[final_position[0]][final_position[1]] != '':
                        return False
                    else:
                        self.current_board = finalize_move(self.current_board.copy(), current_position, final_position)
                        return True
            elif abs(current_position[1] - final_position[1]) != 1:
                return False
            elif self.current_board[final_position[0]][final_position[1]] == '':
                return False
            elif self.current_board[final_position[0]][final_position[1]][0] == \
                    self.current_board[current_position[0]][current_position[1]][0]:
                return False
            else:
                self.current_board = finalize_move(self.current_board.copy(), current_position, final_position)
                return True
        else:
            if current_position[0] <= final_position[0]:
                return False
            if current_position[1] == final_position[1]:
                if current_position[0] == 7 and final_position[0] == 5 and \
                    self.current_board[6][final_position[1]] == '' and \
                        self.current_board[5][final_position[1]] == '':
                    self.current_board = finalize_move(self.current_board, current_position, final_position)
                    return True
                if current_position[0] - final_position[0] == 1:
                    if self.current_board[final_position[0]][final_position[1]] != '':
                        return False
                    else:
                        self.current_board = finalize_move(self.current_board.copy(), current_position, final_position)
                        return True
            elif abs(current_position[1] - final_position[1]) != 1:
                return False
            elif self.current_board[final_position[0]][final_position[1]] == '':
                return False
            elif self.current_board[final_position[0]][final_position[1]][0] == \
                    self.current_board[current_position[0]][current_position[1]][0]:
                return False
            else:
                self.current_board = finalize_move(self.current_board.copy(), current_position, final_position)
                return True

    """This method handles the movement of the falcon piece. For the white player, it can move forward diagonally like a bishop or
     backward vertically like a rook. For the black player, it can move forward diagonally like a bishop or backward vertically like a rook.
      The method checks various conditions to validate the move and updates the game board accordingly. If the move is invalid, it returns False.
       If the move is successful, it returns True."""
    def move_falcon(self, current_position, final_position):
        #     FORWARD AS BISHOP BACKWARD AS ROOK
        if self.current_player == 'W':
            if final_position[0] >= current_position[0]:
                if self.move_bishop(current_position, final_position):
                    return True
                else:
                    return False
            elif final_position[0] <= current_position[0] and current_position[1] == final_position[1]:
                if ValidateMove.validate_vertical_move(self.current_board, current_position, final_position):
                    self.current_board = finalize_move(self.current_board, current_position, final_position)
                    return True
            else:
                return False
        else:
            if current_position[0] >= final_position[0]:
                self.move_bishop(current_position, final_position)
            elif current_position[0] <= final_position[0] and current_position[1] == final_position[1]:
                if ValidateMove.validate_vertical_move(self.current_board, current_position, final_position):
                    self.current_board = finalize_move(self.current_board, current_position, final_position)
                    return True
            else:
                return False
    """The t code in the move_hunter method is very similar to the move_falcon method, but it handles the movement of the hunter piece instead.
     The hunter piece also moves forward as a bishop and backward as a rook, but the conditions for moving forward and backward are different based on the current player's turn.
     in both methods, if the movement conditions are not met, they return False. If the movement is successful, they return True."""
    def move_hunter(self, current_position, final_position):
        if self.current_player == 'B':
            if current_position[0] >= final_position[0]:
                self.move_bishop(current_position, final_position)
            elif current_position[0] <= final_position[0] and current_position[1] == final_position[1]:
                if ValidateMove.validate_vertical_move(self.current_board, current_position, final_position):
                    self.current_board = finalize_move(self.current_board, current_position, final_position)
                    return True
            else:
                return False
        else:
            if current_position[0] <= final_position[0]:
                self.move_bishop(current_position, final_position)
            elif current_position[0] >= final_position[0] and current_position[1] == final_position[1]:
                if ValidateMove.validate_vertical_move(self.current_board, current_position, final_position):
                    self.current_board = finalize_move(self.current_board, current_position, final_position)
                    return True
            else:
                return False
if __name__ == '__main__':
    game = ChessVar()
    game.make_move('a2', 'a4') # White
    game.make_move('b7', 'b5')
    game.make_move('a1', 'a3') # White
    game.make_move('c8', 'b7')
    game.make_move('b1', 'c3') # White
    game.make_move('d8', 'c8')
    game.make_move('e2', 'e3') # White
    game.make_move('b7', 'g2')
    game.make_move('e1', 'e2') # White
    game.make_move('g2', 'h1')
    game.make_move('b2', 'b3') # White
    game.make_move('c8', 'a6')
    game.enter_fairy_piece('F', 'a1') # White
    game.make_move('b5', 'b4')
    game.make_move('a1', 'b2') # White
    game.make_move('a6', 'b5')
    game.make_move('b2','b1') # White
    game.make_move('b5', 'e2')
    print(game.game_state)
    print(game.white_fairy_pieces_available)
    print(game.black_fairy_pieces_available)
    for row in game.current_board:
        print(str(row).replace("''","'__'"))

