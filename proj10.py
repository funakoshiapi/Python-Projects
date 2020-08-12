import tools
import gameai as ai
from checkers import Piece
from checkers import Board
from string import ascii_lowercase
import string


"""
    This programm allows the user to play checkers against a artificial intelligence sytem
    It features a board displayed on the screean and display the moves made, hints of moves and captures.  
"""

# =============================================================================
# Teacher Assistant helped me complething some of the functios in this project
# =============================================================================

def indexify(position):
    
    """
    This function will function converts the letter number 
    position to row-column indices
    Value: string
    Returns: tuple  
    
    """
    
    col = 0
    row = 0
    
    letters = string.ascii_lowercase
    row = letters.find(position[0])
    col = int (position[1:])-1
    my_tupple = (row,col)
    
    return  my_tupple
    
    




def deindexify(row, col):
    
    """
    This function will function converts row, col to a string
    Value: tuple
    Returns: string
    """

    letters= string.ascii_lowercase
    
    
    letter = str ( letters[row])
    
    n = str(col+1)
    
    position = letter+n
    
    return position
    
             

def initialize(board):
    """
    This function puts white and black pieces according to the checkers
    game positions. The black pieces will be on the top three rows and
    the white pieces will be on the bottom three rows (for an 8x8 board).
    The first row for the black pieces will be placed as a2, a4, a6, ...
    etc. and the next rows will be b1, b3, b5, ... etc. For the white
    rows, the placement patterns will be opposite of those of blacks.
    This must work for any even length board size.
    """
    row = col = board.get_length()
    initrows = (row // 2) - 1
    for r in range(row - 1, row - (initrows + 1), -1):
        for c in range(0 if r % 2 == 1 else 1, col, 2):
            board.place(r, c, Piece('white'))
    for r in range(0, initrows):
        for c in range(0 if r % 2 == 1 else 1, col, 2):
            board.place(r, c, Piece())

def count_pieces(board):
    """
    This function will count the pieces in the board
    Value: int
    Returns: tuple
    """
    w_count= 0
    b_count=0
    
    
    
    # Gets the dimentions of the board and 
    #the location of the pieces on the board
    # checks the  color of the piece relative to the position on the board 
    # and count the number of times it appears in the board
    
    b_length = board.get_length()

    for row in range(b_length):
        for col in range(b_length):
            
            p = board.get(row,col)
            
            if p == None:
                pass
          
            elif p.color() == 'white':
        
                w_count +=1
    
            else:                # p.color == 'black':
                
                b_count += 1
    
    return (int(b_count),int(w_count))

def get_all_moves(board, color, is_sorted = False):
    
    """
    This function will give all the possible moves
    Values: int, string , boolean
    Returns: list
    """
    moves_c = []    
    
    
    # Gets the dimentions of the board and 
    #the location of the pieces on the board
    
    # checks the color of the piece, row and col
    # checks the type of the returnd piece, and 
    # if it is a allowed type the creates a tuple and appends it to a list.
    
    
    
    b_length = board.get_length()
    for row in range(b_length):
        for col in range(b_length):
            
            piece = board.get(row,col)
            
            if piece != None:
                if piece.color() == color :
                    moves = tools.get_moves(board,row,col,is_sorted)
                    position = deindexify(row, col)
                    if moves:
                        for p in moves:
                            m_availabel = (position,p)
                            moves_c.append(m_availabel)
                        
    if is_sorted:
        
        moves_c.sort()
        
                        
    return moves_c

                            
            
    

def sort_captures(all_captures,is_sorted=False):
    '''If is_sorted flag is True then the final list will be sorted by the length
    of each sub-list and the sub-lists with the same length will be sorted
    again with respect to the first item in corresponding the sub-list,
    alphabetically.'''
    
    return sorted(all_captures, key = lambda x: (-len(x), x[0])) if is_sorted \
            else all_captures

def get_all_captures(board, color, is_sorted = False):
    """
    This function will give all the possible captures
    Values: int, string , boolean
    Returns: list
    """
    capture_lst=[]
    board_length = board.get_length()
    for row in range(board_length):
        for col in range(board_length):
            
            piece = board.get(row,col)
            
            if piece != None:
               
                if piece.color() == color :
                    cap = tools.get_captures(board, row, col, is_sorted )
#                    position = deindexify(row, col)
                    
                    if cap:
                        
                        for p in cap:
                            
                            captures = p
                            
                            capture_lst.append(captures)
                    
    return capture_lst

def apply_move(board, move):
    """
    Write something about this function here.
    
    Raise this exception below:
        raise RuntimeError("Invalid move, please type" \
                         + " \'hints\' to get suggestions.")    
        
    If,
        a. there is no move from move[0], i.e. use tools.get_moves() function to
            get all the moves from move[0]
        b. the destination position move[1] is not in the moves list found
            from tools.get_moves() function.            
    """
    '''
        get all the moves using the get_moves -> list
        if this list is not empty 
        if moves and move[1] in moves:
            then you just do the t
        if not then raise an error
        raise RunTimeError("Invalid mcove, please type" \
                         + " \'hints\' to get suggestions.") 
    '''
    
    
    initial_position = indexify(move[0])
    
    my_move_lst = tools.get_moves(board,initial_position[0], initial_position[1])
    
    next_pos = indexify(move[1])
    
    piece = board.get(initial_position[0],initial_position[1])
    
    if my_move_lst and move[1] in my_move_lst:
        
        board.place(next_pos[0], next_pos[1],piece)
        
        if piece.color() == 'black' and next_pos[0] == board.get_length() - 1 or piece.color() == 'white' and next_pos[0] == 0:
            piece.turn_king()
           
            
        return board.remove(initial_position[0],initial_position[1])
        
        
        
    
    else:
        raise Exception("Invalid move, please type" \
                         + " \'hints\' to get suggestions.") 
    
    
    
   

def apply_capture(board, capture_path):
    """
    Write something about this function here.
        
    Raise this exception below:
        raise RuntimeError("Invalid jump/capture, please type" \
                         + " \'hints\' to get suggestions.") 
    If,
        a. there is no jump found from any position in capture_path, i.e. use 
            tools.get_jumps() function to get all the jumps from a certain
            position in capture_path
        b. the destination position from a jump is not in the jumps list found
            from tools.get_jumps() function.            
    """
    
   
    
    for index, move in enumerate (capture_path[:-1]):
        
        begins = indexify(move)
        
        previous_p = begins
        
        new_position = indexify(capture_path[index+1])
        board_length = board.get_length()
        
        jump= tools.get_jumps(board, begins[0], begins[1])
        
        
        if jump!=[]:
            
            
            if capture_path[index+1] in jump:
                
                piece = board.get(previous_p[0],previous_p[1])
                board.place(new_position[0], new_position[1],piece)
                
                if new_position[0]== 0 and piece.is_white() or new_position[0]==board_length-1 and piece.is_black():
                    
                    if piece.is_king()==False:
                        
                        piece.turn_king()
                        
                    else:
                        pass
                        
                take_2 = 0
                take_1 = 0
                
                if previous_p[0]>new_position[0]:
                    take_1 = previous_p[0]-1
                    
                if previous_p[0]<new_position[0]:
                    take_1 = new_position[0]-1
                    
                if previous_p[1]>new_position[1]:
                    take_2 = previous_p[1]-1
                    
                if previous_p[1]<new_position[1]:
                    take_2 = new_position[1]-1 
                
                board.remove(take_1,take_2)
                board.remove(previous_p[0],previous_p[1])
        else:
            raise Exception("Invalid jump/capture, please type" \
                         + " \'hints\' to get suggestions.") 
        
            
def get_hints(board, color, is_sorted = False):
    """
    This function will give all the possible hints
    Values: int, string , boolean
    Returns: list
    """
    
    my_moves = get_all_moves(board, color, is_sorted )
    captures_made= get_all_captures(board, color, is_sorted )
    
    if captures_made:
        
                my_moves=[]
                
                x = (my_moves , captures_made)
    else:
                x = (my_moves , captures_made)
                
        
        
    return x
        
def get_winner(board, is_sorted = False):
    """
    This function will return who wins
    Values: int, boolean
    Returns: string
    
    """
    
    

    empty=([],[])
    moves_b = get_hints(board, 'black', is_sorted)
    moves_w = get_hints(board, 'white', is_sorted)
    
    # make use of the get_hints functions to compare the 
    # if the list of moves for the black piece or white piece is empty
    # in order to define  the winner 
    
    if moves_b !=  empty  and moves_w ==  empty:
        return 'black'
    
    if moves_w !=  empty  and moves_b ==  empty:
        return 'white'
    
    # use count_piece function in order to check if the there is a white and black piece left in the board
    
    count_p=count_pieces(board)
    
    if count_p == (1,1):
        
        b_length = board.get_length()
        for row in range(b_length):
            for col in range(b_length):
            
                p = board.get(row,col)
            
                if p == None:
                    pass
                
                # check if the black and white piece in the board are kings
                # in order to define a draw
                
                elif ( p.color() == 'black' and p.is_king()==True) and (p.color() == 'white' and p.is_king()==True):
                    return 'draw'  
                
                
    # This is the same source code from count_piece function
    # I've modified the end so that I could add  statement of comaprison  between the calculated counts.
    
    w_count= 0
    b_count=0
    
    b_length = board.get_length()

    for row in range(b_length):
        for col in range(b_length):
            
            p = board.get(row,col)
            
            if p == None:
                pass
          
            elif p.color() == 'white':
        
                w_count +=1
    
            else:                # p.color == 'black':
                
                b_count += 1
    if b_count > w_count:
        return 'black'
    
    elif w_count < w_count:
        return 'white' 
    else:
        return 'draw'
    
                        
def is_game_finished(board, is_sorted = False):
    """
    This function will  define if the game is over
    Values: int, boolean
    Returns: boolean
    """
    # this is the definition of empty or Null  that will be used for the if statement
    
    empty=([],[])
    
    # calling the function for hints for both moves on black and white piece
    
    moves_b = get_hints(board, 'black', is_sorted)
    moves_w = get_hints(board, 'white', is_sorted)
    
    # checking if the list of movememnts is empty
    # in order to define  the end of the game
    
    if (moves_b == empty) or (moves_w == empty): 
        return True
    else:
        return False
    
    

# Some error messages to save lines.
move_error = "Invalid move, please type \'hints\' to get suggestions."
hasjump_error = "You have jumps, please type \'hints\' to get suggestions."
jump_error = "Invalid jump, please type \'hints\' to get suggestions."
hint_error = "Invalid hint number."
cmd_error = "Invalid command."

def game_play_human():
    
    """
    This is the main mechanism of the human vs. human game play.
    Use this function to write the game_play_ai() function.
    """    
    # UNCOMMENT THESE TWO LINES TO TEST ON MIMIR SUBMISSION
    Piece.symbols = ['b', 'w']
    Piece.symbols_king = ['B', 'W']
    
    prompt = "[{:s}'s turn] :> "
    print(tools.banner)
   
    # Choose the color here
    (my_color, opponent_color) = tools.choose_color()
    
    # Take a board of size 8x8
    board = Board(8)
    initialize(board)
    
    # Decide on whose turn, use a variable called 'turn'.
    turn = my_color if my_color == 'black' else opponent_color
    print("Black always plays first.\n")
    
    # loop until the game is finished
    while not is_game_finished(board):
        try:
            # Count the pieces and assign into piece_count
            piece_count = count_pieces(board)
            
            print("Current board:")
            board.display(piece_count)    
            
            # Get the command from user using input
            command = input(prompt.format(turn)).strip().lower()
            
            # Now decide on different commands
            if command == 'pass':
                break
            elif command == 'exit':
                break
            elif command == 'hints':
                (moves, captures) = get_hints(board, turn, True)
                if moves:
                    print("You have moves:")
                    for i, move in enumerate(moves):
                        print("\t{:d}: {:s} --> {:s}"\
                                  .format(i + 1, move[0], move[1]))
                if captures:
                    print("You have captures:")
                    for i, path in enumerate(captures):
                        print("\t{:d}: {:s}".format(i + 1, str(path)))
            else:
                command = [s.strip().lower() for s in command.split()]
                (moves, captures) = get_hints(board, turn, True)
                action = None
                if command and command[0] == 'move' and len(command) == 3:
                    if not captures:
                        action = (command[1], command[2])
                        if action in moves:
                            apply_move(board, action)
                        else:
                            raise RuntimeError(move_error)
                    else:
                        raise RuntimeError(hasjump_error)
                elif command and command[0] == 'jump' and len(command) >= 3:
                    action = command[1:]
                    if action in captures:
                        apply_capture(board, action)
                    else:
                        raise RuntimeError(jump_error)
                elif command and command[0] == 'apply' and len(command) == 2:
                    id_hint = int(command[1])
                    if moves and (1 <= id_hint <= len(moves)):
                        action = moves[id_hint - 1]
                        apply_move(board, action)
                    elif captures and (1 <= id_hint <= len(captures)):
                        action = captures[id_hint - 1]
                        apply_capture(board, action)
                    else:
                        raise ValueError(hint_error)
                else:
                    raise RuntimeError(cmd_error + tools.usage)
                print("\t{:s} played {:s}.".format(turn, str(action)))
                turn = my_color if turn == opponent_color else opponent_color
        except Exception as err:
            print("Error:", err)
    
    # The loop is over.
    piece_count = count_pieces(board)
    print("Current board:")
    board.display(piece_count)    
    if command != 'pass':
        winner = get_winner(board)
        if winner != 'draw':
            diff = abs(piece_count[0] - piece_count[1])
            print("\'{:s}\' wins by {:d}! yay!!".format(winner, diff))
        else:
            print("This game ends in a draw.")
    else:
        winner = opponent_color if turn == my_color else my_color
        print("{:s} gave up! {:s} is the winner!! yay!!!".format(turn, winner))
    # --- end of game play human ---

def game_play_ai():
    
    """
    
    This is the main mechanism of the human vs. ai game play. You need to
    implement this function by taking helps from the game_play_human() 
    function.
    
    For a given board situation/state, you can call the ai function to get
    the next best move, like this:
        
        move = ai.get_next_move(board, turn)
        
    where the turn variable is a color 'black' or 'white', also you need to 
    import ai module as 'import gameai as ai' at the beginning of the file.
    This function will be very similar to game_play_human().
    # UNCOMMENT THESE TWO LINES TO TEST ON MIMIR SUBMISSION
    This is the main mechanism of the human vs. human game play.
    Use this function to write the game_play_ai() function.
    
    """    
    
    # UNCOMMENT THESE TWO LINES TO TEST ON MIMIR SUBMISSION
    Piece.symbols = ['b', 'w']
    Piece.symbols_king = ['B', 'W']
    
    prompt = "[{:s}'s turn] :> "
    
    print(tools.banner)
   
    # Choose the color here
    (my_color, opponent_color) = tools.choose_color()
    
    # Take a board of size 8x8
    board = Board(8)
    initialize(board)
    
    # Decide on whose turn, use a variable called 'turn'.
    
    turn = my_color if my_color == 'black' else opponent_color
    print("Black always plays first.\n")
    
    # loop until the game is finished
    
    while not is_game_finished(board):
        
        try:
            # Count the pieces and assign into piece_count
            
            piece_count = count_pieces(board)
            
            print("Current board:")
            board.display(piece_count)    
        
            
# =============================================================================
#                        Modififications from the game_play_human 
#                                Changes starts HERE                       
# =============================================================================
            
            if turn == my_color:
                
                 command = input(prompt.format(turn)).strip().lower()
                 
            else:
                
                move = ai.get_next_move(board, turn)
                                
                if type(move) == tuple:
                    
                    command = "move {:s} {:s}".format(move[0], move[1])
                    
                else:
                    command = "jump {:s}".format(" ".join([b for b in move]))
                command = command.strip().lower()  
            
            # Now decide on different commands
            
            if command == 'pass':
                break
            elif command == 'exit':
                break
            elif command == 'hints':
                (moves, captures) = get_hints(board, turn, True)
                if moves:
                    print("You have moves:")
                    for i, move in enumerate(moves):
                        print("\t{:d}: {:s} --> {:s}"\
                                  .format(i + 1, move[0], move[1]))
                if captures:
                    print("You have captures:")
                    for i, path in enumerate(captures):
                        print("\t{:d}: {:s}".format(i + 1, str(path)))
            else:
                command = [s.strip().lower() for s in command.split()]
                (moves, captures) = get_hints(board, turn, True)

                action = None
                if command and command[0] == 'move' and len(command) == 3:
                    if not captures:
                        action = (command[1], command[2])
                        if action in moves:
                            apply_move(board, action)
                        else:
                            raise RuntimeError(move_error)
                    else:
                        raise RuntimeError(hasjump_error)
                elif command and command[0] == 'jump' and len(command) >= 3:
                    action = command[1:]
                    if action in captures:
                        apply_capture(board, action)
                    else:
                        raise RuntimeError(jump_error)
                elif command and command[0] == 'apply' and len(command) == 2:
                    id_hint = int(command[1])
                    if moves and (1 <= id_hint <= len(moves)):
                        action = moves[id_hint - 1]
                        apply_move(board, action)
                    elif captures and (1 <= id_hint <= len(captures)):
                        action = captures[id_hint - 1]
                        apply_capture(board, action)
                    else:
                        raise ValueError(hint_error)
                else:
                    raise RuntimeError(cmd_error + tools.usage)
                print("\t{:s} played {:s}.".format(turn, str(action)))
                turn = my_color if turn == opponent_color else opponent_color
        except Exception as err:
            print("Error:", err)
    
    # The loop is over.
    
    piece_count = count_pieces(board)
    print("Current board:")
    board.display(piece_count)    
    if command != 'pass':
        winner = get_winner(board)
        if winner != 'draw':
            diff = abs(piece_count[0] - piece_count[1])
            print("\'{:s}\' wins by {:d}! yay!!".format(winner, diff))
        else:
            print("This game ends in a draw.")
    else:
        winner = opponent_color if turn == my_color else my_color
        print("{:s} gave up! {:s} is the winner!! yay!!!".format(turn, winner))
    # --- end of game play human ---
 
def main():
    
    #game_play_human()
    game_play_ai()
    
# main function, the program's entry point
if __name__ == "__main__":
    main()
