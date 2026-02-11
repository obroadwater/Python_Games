alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m', 'n', 'o','p','q','r','s','t','u','v','w','x','y','z']

class Square(object):
    piece = None
    coordinates = ""
    
    def __init__(self, piece, coordinates):
        self.piece = piece
        self.coordinates = coordinates
        
    def get_piece(self):
        return self.piece
    
    def get_coords(self):
        return self.coordinates
    
    def is_empty(self):
        return self.get_piece() == None
    
    def add_piece(self, piece):
        self.piece = piece
        
    def remove_piece(self):
        self.piece = None

        
class Piece(object):
    color = ""
    king = False
    
    def __init__(self, color, king = False):
        self.color = color
        self.king = king
    
    def get_color(self):
        return self.color
    
    def is_king(self):
        return self.king
    
    def promote(self):
        self.king = True
        self.color = self.color.upper()
        
class Player(object):
    name = ""
    color = ""
    pieces_left = 0
    
    def __init__(self, name, color, dimension):
        self.name = name
        self.color = color
        self.pieces_left = int((dimension-2)/2) * int(dimension/2)
        
    def get_name(self):
        return self.name
    
    def get_color(self):
        return self.color
    
    def get_pieces_left(self):
        return self.pieces_left
    
    def lost_piece(self):
        self.pieces_left -= 1
    
    
class Board(object):
    board = []
    dimensions = 0
    
    def __init__(self, length):
        self.dimensions = length
        rows_deep = int((length-2)/2)
        red_rows = range(rows_deep)
        black_rows = range(rows_deep + 2, length)
        
        # Number to be switched between 0 and 1 to reflect if pieces should be placed at odd or even indices
        desired_remainder = 1 
        for i in range(length):
            row = []
            for j in range(length):
                if(i in red_rows and j%2 == desired_remainder):
                    row.append(Square(Piece("r"), alphabet[i].upper()+str(j+1)))
                elif(i in black_rows and j%2 == desired_remainder):
                    row.append(Square(Piece("b"), alphabet[i].upper()+str(j+1)))
                else:
                    row.append(Square(None, alphabet[i].upper()+str(j+1)))
            desired_remainder = (desired_remainder + 1) % 2
            self.board.append(row)
    
    def get_square_at(self, alphanum):
        row = alphabet.index(alphanum[0].lower())
        col = int(alphanum[1])-1
        try:
            return self.board[row][col]
        except:
            return None
            
    def board_as_string(self):
        def color(square):
            color_to_return = " "
            if type(square.get_piece()) == Piece:
                color_to_return = square.get_piece().get_color()
            return color_to_return
        
        printout = ""
        row_borders = "  " + "-" * (self.dimensions * 2 + 1)
        for num in range(1, self.dimensions +1):
            if num != 1:
                printout += str(num) + " "
            else:
                printout += "   " + str(num) + " "
        printout += "\n" + row_borders

        printout += "\n"
        for i in range(self.dimensions):
            for j in range(self.dimensions):
                if j == 0:
                    printout += alphabet[i].upper() + " |"
                printout += color(self.board[i][j]) + "|"
            printout += "\n"
        printout += row_borders + "\n"
        return printout
        
class Manager(object):
    players = []
    board = None
    dimension = 0
    turn = 0
    
    def __init__(self, player_name1 = False,player_name2 = False, dimension = False):
        if player_name1 == False or player_name2 == False or dimension == False:
            if input("Hello, would you like to play a game of checkers?(y/n) ").lower() == "n":
                exit()
            print("")
            player_name1 = input("What is the name of the first player(black pieces)? ")
            player_name2 = input("What is the name of the second player(red pieces)? ")
            print("")
            conditions_met = False
            dimension = ""
            while(not conditions_met):
                try:
                    dimension = int(input("Which size of board would you like to play with? Please select 4 for a 4x4 grid, 6 for a 6x6 grid, or 8 for a 8x8 grid: "))
                except:
                    print("Please enter a numeric value")
                else:
                    if dimension % 2 == 0 and dimension in range(4, 9):
                        conditions_met = True
                    else:
                        print("Please enter an even number between 4 and 8")
            print("")
        self.players = [Player(player_name1, "B",  dimension), Player(player_name2, "R", dimension)]
        self.board = Board(dimension)
        self.turn = 0
        self.dimension = dimension
        
    def print_board(self):
        print(self.board.board_as_string())
        
        
    # Function for use in move(), to force the user to only select a valid piece
    def get_valid_start (self):
            conditions_met = False
            while(not conditions_met):
                starting_coords = input("Which piece do you want to move? Answer using the grid labels(e.g. A1, B3, etc.): ")
                if alphabet.index(starting_coords[0].lower()) < self.dimension and int(starting_coords[1]) <= self.dimension:
                    start = self.board.get_square_at(starting_coords)
                    if not start.is_empty() and start.get_piece().get_color().lower() == self.players[self.turn].get_color().lower():
                        conditions_met = True
                    else:
                        print("Invalid input, try again")
            return start
        
    # Function for use in move(), to only let the user move a piece to a square that it can move to within the rules of checkers
    def get_valid_end (self, valid_spaces_dict):
            conditions_met = False
            while(not conditions_met):
                ending_coords = input("Where should your piece end up? Answer using the grid labels(e.g. A1, B3, etc.): ")
                if ending_coords.lower() == "exit":
                    return False
                elif alphabet.index(ending_coords[0].lower()) < self.dimension and int(ending_coords[1]) <= self.dimension:
                    if ending_coords.upper() in valid_spaces_dict.keys():
                        conditions_met = True
                    else:
                        print("Invalid selection, select again. To change the piece you're moving, type exit in the next prompt.")
            return ending_coords.upper()
        
    def move(self, starting_coords = "", ending_coords = ""):
        squares_to_capture = []
        
        if starting_coords == "":
            start = self.get_valid_start()
            valid_spaces_dict = self.valid_squares_to_move_to(start, start.get_piece())
            print("")
            ending_coords = self.get_valid_end(valid_spaces_dict)
            
            while(ending_coords == False):
                start = self.get_valid_start()
                valid_spaces_dict = self.valid_squares_to_move_to(start, start.get_piece())
                ending_coords = self.get_valid_end(valid_spaces_dict)
                
            end = self.board.get_square_at(ending_coords)
            squares_to_capture = valid_spaces_dict[ending_coords]
        
        else:
            start = self.board.get_square_at(starting_coords)
            end = self.board.get_square_at(ending_coords)
            
        end.add_piece(start.get_piece())
        start.remove_piece()
        self.capture(squares_to_capture)
        
    def valid_squares_to_move_to(self, square, piece, is_secondaryaction = False):
        # is_secondaryaction is used when evaluating multi-jump moves, as once a piece jumps another it can only keep going through jumps
        square_options = {}
        # square options will have keys of square coordinates(e.g. A1) and values of a list of Squares
        # the coordinate will represent a valid endpoint for a move and the list of Squares will be represent the squares with captured pieces if the player chooses the given endpoint
        
        coords = square.get_coords()
        row = alphabet.index(coords[0].lower())
        col = int(coords[1])
        
        # Helper function for the recursion included later
        def append_to_dict(lst, former):
            return lst + former
        
        # Assumes that the square has already been checked to make sure it has a piece of the correct color on it
        square_color = piece.get_color().lower()
        target_color = ""
        if square_color == "r":
            target_color = "b"
        else:
            target_color = "r"
            
        # If a red piece or king
        if (square_color == "r" or piece.is_king()) and row + 1 < self.dimension:
            # Checking if the piece can move to its left
            if col-1 > 0:
                coord = alphabet[row+1].upper() + str(col-1)
                sq = self.board.get_square_at(coord)
                # Case if the square down and to the left is empty
                if sq.is_empty():
                    if not is_secondaryaction:
                        square_options[coord] = []
                
                # if its not empty, check if a capture can occur -- the square is of the opposite color and next diagonal square is still on the board and the next square is empty
                elif sq.get_piece().get_color().lower() == target_color and row + 2 < self.dimension and col - 2 > 0:
                    next_coord = alphabet[row+2].upper() + str(col-2)
                    next_sq = self.board.get_square_at(next_coord)
                    
                    # If meets all criteria, calls the function again from the spot the piece would move to, allowing for multiple captures where possible
                    if next_sq.is_empty():
                        sq_value = [sq]
                        possible_addon = self.valid_squares_to_move_to(next_sq, piece, True)
                        
                        # base case for the recursion, checks if there are no more moves that can be made
                        if len(possible_addon) == 0:
                            square_options[next_coord] = sq_value
                        else:
                            possible_addon = {key: append_to_dict(value, sq_value) for key, value in possible_addon.items()}
                            square_options.update(possible_addon)
                            square_options[next_coord] = sq_value
                    # If doesn't meet criteria, no action is needed
                    
            # same process as above but for other direction(down and to the right)
            if col+1 <= self.dimension:
                coord = alphabet[row+1].upper() + str(col+1)
                sq = self.board.get_square_at(coord)
                
                # Case if the square down and to the right is empty
                if sq.is_empty():
                    if not is_secondaryaction:
                        square_options[coord] = []
                        
                # if its not empty, check if a capture can occur -- the square is of the opposite color and next diagonal square is still on the board and the next square is empty
                elif sq.get_piece().get_color().lower() == target_color and row + 2 < self.dimension and col + 2 <= self.dimension:
                    next_coord = alphabet[row+2].upper() + str(col+2)
                    next_sq = self.board.get_square_at(next_coord)
                   
                   # Same recursion as above
                    if next_sq.is_empty():
                        sq_value = [sq]
                        possible_addon = self.valid_squares_to_move_to(next_sq, piece, True)
                        if len(possible_addon) == 0:
                            square_options[next_coord] = sq_value
                        else:
                            possible_addon = {key: append_to_dict(value, sq_value) for key, value in possible_addon.items()}
                            square_options.update(possible_addon)
                            square_options[next_coord] = sq_value
                            
        # if a king or black piece
        if (square_color == "b" or piece.is_king()) and row - 1 >= 0:
            # Checking if the piece can move to its left
            if col-1 > 0:
                coord = alphabet[row-1].upper() + str(col-1)
                sq = self.board.get_square_at(coord)
                
                # Case if the square up and to the left is empty
                if sq.is_empty():
                    if not is_secondaryaction:
                        square_options[coord] = []
                        
                # if its not empty, check if a capture can occur -- the square is of the opposite color and next diagonal square is still on the board and the next square is empty
                elif sq.get_piece().get_color().lower() == target_color and row - 2 >= 0 and col - 2 > 0:
                    next_coord = alphabet[row-2].upper() + str(col-2)
                    next_sq = self.board.get_square_at(next_coord)
                    
                    # If meets all criteria, calls the function again from the spot the piece would move to, allowing for multiple captures where possible
                    if next_sq.is_empty():
                        sq_value = [sq]
                        possible_addon = self.valid_squares_to_move_to(next_sq, piece, True)
                        if len(possible_addon) == 0:
                            square_options[next_coord] = sq_value
                        else:
                            possible_addon = {key: append_to_dict(value, sq_value) for key, value in possible_addon.items()}
                            square_options.update(possible_addon)
                            square_options[next_coord] = sq_value
                    # If doesn't meet criteria, no action is needed
                    
            # same process as above but for other direction(up and to the right)
            if col+1 <= self.dimension:
                coord = alphabet[row-1].upper() + str(col+1)
                sq = self.board.get_square_at(coord)
                
                # Case if the square up and to the right is empty
                if sq.is_empty():
                    if not is_secondaryaction:
                        square_options[coord] = []
                        
                # if its not empty, check if a capture can occur -- the square is of the opposite color and next diagonal square is still on the board and the next square is empty
                elif sq.get_piece().get_color().lower() == target_color and row - 2 >= 0 and col + 2 <= self.dimension:
                    next_coord = alphabet[row-2].upper() + str(col+2)
                    next_sq = self.board.get_square_at(next_coord)
                    
                    if next_sq.is_empty():
                        sq_value = [sq]
                        possible_addon = self.valid_squares_to_move_to(next_sq, piece, True)
                        if len(possible_addon) == 0:
                            square_options[next_coord] = sq_value
                        else:
                            possible_addon = {key: append_to_dict(value, sq_value) for key, value in possible_addon.items()}
                            square_options.update(possible_addon)
                            square_options[next_coord] = sq_value
        return square_options
    
    # Takes a list of squares with pieces to capture and removes the piece from the square, decrementing the player's number of remaining pieces
    def capture(self, to_capture):
        other_player = self.players[(self.turn + 1) % 2]
        for sq in to_capture:
            sq.remove_piece()
            other_player.lost_piece()
    
    # Checks the bottom and top rows to see if any pieces have reached far enough to be promoted
    def check_promotion(self):
        for i in range(1, self.dimension+1):
            sq = self.board.get_square_at("A"+str(i))
            if not sq.is_empty() and sq.get_piece().get_color() == "b":
                sq.get_piece().promote()
            sq = self.board.get_square_at(alphabet[self.dimension-1].upper()+str(i))
            if not sq.is_empty() and sq.get_piece().get_color() == "r":
                sq.get_piece().promote()
        
    # Checks the number of remaining pieces of each player to see if they have lost and the other player won
    def check_win_condition(self):
        if self.players[0].get_pieces_left() == 0:
            return self.players[1]
        elif self.players[1].get_pieces_left() == 0:
            return self.players[0]
        else:
            return False
        
    # Runs all of the functions included above in a game flow, modulating turn and checking for both promotion and win condition at the end of each turn
    def main(self):
        player_won = self.check_win_condition()
        while(player_won == False):
            current_player = self.players[self.turn]
            if current_player.get_color() == "B":
                color = "black"
            else:
                color = "red"
            print("\nIt is", current_player.get_name(), "'s move (",color, "pieces).\n")
            self.print_board()
            print("")
            self.move()
            self.check_promotion()
            player_won = self.check_win_condition()
            self.turn = (self.turn + 1) % 2
        print("\n","------------------------------------------", "\n")
        print(player_won.get_name(), " won! Congratulations!")
            
            
#test = Manager("owen","yohannes",4)
#test.print_board()
test = Manager()
test.main()      
         
  
#to check in test cases  

# board set up
"""test = Manager("john","yohannes",4)
test.board.board_as_string() == #the grid

test = Manager("john","yohannes",6)
test.board.board_as_string() == #the grid"""

# piece movement
"""test = Manager("john","yohannes",4)
test.move("D1","C2")
test.board.board_as_string() == #the grid

test = Manager("john","yohannes",4)
test.move("A4","B3")
test.board.board_as_string() == #the grid
"""

# piece capture
"""test = Manager("john","yohannes",4)
test.move("D1","C2")
test.move("A4","B3")
test.move("C2","A4")
test.board.board_as_string() == #the grid

test = Manager("john","yohannes",4)
test.move("D3","C2")
test.move("A4","B1")
test.move("C2","B3")
test.move("A4","C2")
test.board.board_as_string() == #the grid"""

# promotion
"""test = Manager("john","yohannes",4)
test.move("D1","C2")
test.move("A4","B3")
test.move("C2","A4")
test.check_promotion()
test.move("A4","B3")
test.board.board_as_string() == #the grid

test = Manager("john","yohannes",4)
test.move("D1","C2")
test.move("A4","B3")
test.move("C2","B1")
test.move("B3","C2")
test.move("D3","C4")
test.move("C2","D1")
test.check_promotion()
test.move("D1","B2")
test.board.board_as_string() == #the grid"""





# Print statement manual testing
"""test.print_board()
test.move("D1","C2")
test.move("A4","B3")
test.move("C2","A4")
test.check_promotion()
test.move("A2","B3")
test.print_board()
output = test.valid_squares_to_move_to(test.board.get_square_at("a4"), Piece("b", True))
for key, value in output.items():
    print(f"{key}: {value}")
    
for value in output.values():
    for v in value:
        print(v.get_coords())
        
if len(output) == 0:
    print("empty")"""
"""tst = Manager()
tst.print_board()
tst.move("C8","D7")
tst.move("D7","E6")
tst.move("B7","C8")
tst.move("F1", "E2")
#tst.move()
tst.print_board()
tst.move("E2","D3")
tst.print_board()
tst.move("G2","F1")
tst.print_board()
tst.move()
tst.print_board()
tst.move()
tst.print_board()
tst.move()
tst.print_board()
tst.move()
tst.print_board()
tst.move()
tst.print_board()
tst.move()
tst.print_board()
tst.move()
tst.print_board()
tst.move()
tst.check_promotion()
tst.print_board()
tst.move()
tst.print_board()"""

"""output = tst.valid_squares_to_move_to(tst.board.get_square_at("C2"), Piece("r"))
output = tst.valid_squares_to_move_to(tst.board.get_square_at("f7"), Piece("b"))

for key, value in output.items():
    print(f"{key}: {value}")
    
for value in output.values():
    for v in value:
        print(v.get_coords())
    
if len(output) == 0:
    print("empty")"""
    
    
    
    
    











