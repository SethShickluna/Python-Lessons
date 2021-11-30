##############################################
# basic battleship game using 2-d arrays     #
# lesson 8                                   #
#  types of ships: 2 aircraft carrier (6)    #
#                  3 battleship (5)          #
#                  4 submarine (3)           #
#                  5 destroyer (3)           #
#                  6 torpedo boat (2)        #
# not guessed:  0                            #
# hit:         -1                            #
# miss:         1                            #
##############################################

board = [[0 for _ in range(10)] for _ in range(10)]

def print_board(): 
    letters = [" ","A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
    for c in letters: 
        print(c, end=" ")
    print()
    
    for num, row in enumerate(board): 
        print(num, end= ". ")
        for col in row:
            print(col, end= " ")
        print()

# this function sets up the entire game 
# makes the boards and puts the ships on the board 
def make_game():
    # aircraft carrier
    board[0][0] = 2
    board[0][1] = 2
    board[0][2] = 2
    board[0][3] = 2
    board[0][4] = 2
    board[0][5] = 2
    #battleship 
    board[3][2] = 3
    board[4][2] = 3
    board[5][2] = 3
    board[6][2] = 3
    board[7][2] = 3
    #submarine
    board[5][8] = 4
    board[6][8] = 4
    board[7][8] = 4
    board[8][8] = 4
    #destroyer
    board[9][0] = 5
    board[9][1] = 5
    board[9][2] = 5
    #torpedo boat
    board[7][1] = 6
    board[7][2] = 6


# the move parameter is a string like "a4"
def make_move(x, y): 
    #check if the square is valid 
    #if the square is valid, check to see if it hit anything 
    #replace that square with either an X for hit or an O for miss
    
    if board[x][y] == "X" or board[x][y] == "O" : 
        print("Invalid square, guess again.")
    else: 
        if board[x][y] == 0: 
            print("You missed!")
            board[x][y] = "O"
            return 0
        else: 
            print("HIT!!!!")
            board[x][y] = "X"
            return 1
    
    return 0 


#idea of this is to have the computer randomly guess a square 
# good news is that for this we dont have worry about using the letters cause everything is a number to the computer 
# hint try to use the make_move function 
def cpu_guess(): 
    pass 
    

def main(): 
    
    def get_num_from_letter(key): 
        lttr_dict = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F":6, "G":7, "H":8, "I":9, "J":10}
        
        return lttr_dict[key]
    
    make_game()
    total_hits = 0
    
    playing = True 
    while playing: 
        print_board()
        move = input("Choose a square: ")
        
        x = get_num_from_letter(move[0]) - 1
        y = int(move[1])
        
        total_hits += make_move(x, y)
        
        if total_hits >= 19: 
            break 
    
    print("You won!!")
        
main() 