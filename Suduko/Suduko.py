#loads board
def load_board():
    with open(r'C:\Users\duran\OneDrive\VSCODE\GameSolvers\Suduko\Problem1.txt') as file:
        content = []
        for line in file:
            for char in line.strip():
                num = int(char)
                content.append(num)
    return content 

def print_board(board):
    for i in range(9):
        print(' '.join(map(str, board[i*9:(i+1)*9])))
    

def create_board():
    # create array of notations (A1,A2,A3,A4 etc...)
    """rows = "ABCDEFGHI" ; cols = "123456789" ; notation = [a+b for a in rows for b in cols] ; content = load_board() ; notatedboard = list(zip(notation,content)); return notatedboard"""
            
    #the board will be indexed 0-80, can mentally imagine it in a 9x9 box incrementing right to left
    return load_board()

#the unicode or A is 65, B is 66 etc. so B-A = col 1 A-A = col 0 etc.
#leaving the notation as A1-9 bc it makes more sense than A0-8 for board games, the conversion is below.
def notation_to_index(notation):
    row = ord(notation[0]) - ord('A') #returns a number between 0 and 8
    col = int(notation[1]) - 1 #returns a number between 0 and 8
    return row * 9 +col
    
def index_to_notation(index):
    row = index // 9 #9 columns if divible by nine 0 times, first row if devisble 4 time then it is 4th row
    col = index % 9  #modluo instead of divide but same logic as above. 
    
    row_note = chr(row+ord('A'))
    col_note = str(col +1)
    
    return row_note+col_note
    
def rowisvalid(notation, board, num):
    index = notation_to_index(notation)
    row_start = (index//9)*9
    row = board[row_start:row_start+9]
    if num in row:
        return False
    else:
        return True
    
def colisvalid(notation, board, num):
            #example of mess before using indices
    """number = notation[1];col = [];for tulp in board:; if number == tulp[0][1]:;col.append(tulp[1]);if len(col) == 9:;break;if num in col:;return False;else:;return True"""
    
    index = notation_to_index(notation)
    col_start = (index%9) 
    col = [board[i]for i in range(col_start, 81, 9)]
    if num in col:
        return False
    else:
        return True
            
        
    
def squareisvalid(notation,board, num):
    index = notation_to_index(notation)
    row = index//9
    col = index % 9 
    
    row_start = (row // 3) * 3 #3 instead of 9 so that rows 7-9 // 3 = 2 4-6//3 = 2 etc..
    col_start = (col // 3) * 3 #3 instead of 9 so that rows 7-9 // 3 = 2 4-6//3 = 2 etc..
    
    square = []
    for r in range(row_start, row_start+3):
        for c in range(col_start, col_start+3):
            square.append(board[r*9 +c]) 
        
    if num in square:
        return False
    else:
        return True 
    
def isvalid(notation,board, num):
    if not colisvalid(notation,board, num):
        return False
    if not rowisvalid(notation,board, num):
        return False
    if not squareisvalid(notation,board, num):
        return False
    return True



def possible_nums(board):
   
    possibles = []
    for i,value in enumerate(board):
        if value == 0:
            notation = index_to_notation(i)
            potential = []
            for num in range(1,10):
                valid = isvalid(notation, board, num)
                if valid:
                    potential.append(num)
            possibles.append((notation,potential))
    return possibles
 
def fill(num,board,notation):
    index = notation_to_index(notation)
    board[index] = num
    
def sudukohelper(board):
    possibles = possible_nums(board)
    #basecase
    if not possibles:
        return board
    for tulp in possibles:
        if len(tulp[1]) == 1:
            fill(tulp[1][0], board, tulp[0])
        
    return sudukohelper(board)
    
def suduko():
    board = create_board()
    print("Inital  Board:")
    print_board(board)
    solved = sudukohelper(board)
    print("Solved  Board:")
    return print_board(solved)
        
if __name__ == "__main__":
    suduko()
