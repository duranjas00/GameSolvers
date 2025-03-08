import random
import json

#dice configuration for boggle (scribd.com)
def boggledice():
    d1 =['a','a','g','g','e','n']
    d2 =['a','b','b','j','o','o']
    d3 =['a','c','h','o','p','s']
    d4 =['a','f','f','k','p','s']
    d5 = ['a','o','o','t','t','w']
    d6 = ['c','i','m','o','t','u']
    d7 = ['d','e','i','l','r','x']
    d8 = ['d','e','l','r','v','y']
    d9 =['d','i','s','t','t','y']
    d10 =['e','e','g','h','n','w']
    d11 = ['e','e','i','n','s','u']
    d12 = ['e','h','r','t','v','w']
    d13 = ['e','i','o','s','s','t']
    d14 = ['e','l','r','t','t','y']
    d15 = ['h','i','m','n','u','qu']
    d16 = ['h','l','n','n','r','z']
    
    di = [d1,d2,d3,d4,d5,d6,d7,d8,d9,d10,d11,d12,d13,d14,d15,d16]
    
    return di


#pop the boggle dome, each dice has one letter up. 
def roll_dice():
    dice = boggledice()
    roll = []
    
    for d in dice:
        roll.append(random.choice(d))
    return roll

#dice fall into spaces randomly letter represent row/column of space
def set_dice():
    roll = roll_dice()
    
    aa = roll.pop(random.randint(0,len(roll)-1))
    ab = roll.pop(random.randint(0,len(roll)-1))
    ac = roll.pop(random.randint(0,len(roll)-1))
    ad = roll.pop(random.randint(0,len(roll)-1))
    ba = roll.pop(random.randint(0,len(roll)-1))
    bb = roll.pop(random.randint(0,len(roll)-1))
    bc = roll.pop(random.randint(0,len(roll)-1))
    bd = roll.pop(random.randint(0,len(roll)-1))
    ca = roll.pop(random.randint(0,len(roll)-1))
    cb = roll.pop(random.randint(0,len(roll)-1))
    cc = roll.pop(random.randint(0,len(roll)-1))
    cd = roll.pop(random.randint(0,len(roll)-1))
    da = roll.pop(random.randint(0,len(roll)-1))
    db = roll.pop(random.randint(0,len(roll)-1))
    dc = roll.pop(random.randint(0,len(roll)-1))
    dd = roll.pop(random.randint(0,len(roll)-1))
    
    #(letter, height, width)
    Arow = [(aa),(ab),(ac),(ad)]
    Brow = [(ba),(bb),(bc),(bd)]
    Crow = [(ca),(cb),(cc),(cd)]
    Drow = [(da),(db),(dc),(dd)]
    
    board = [Arow, Brow, Crow, Drow]
    return board  

def print_board(board):
    row = []
    for rows in board:
        for letter in rows:
            row.append(letter)
        print(row)
        row.clear()
            
def check_word(word,dictionary):
    word = word.upper()
    return word in dictionary

#words sourced from REDBO's scrabble repository on github https://github.com/redbo/scrabble/blob/master/dictionary.txt

def load_dictionary():
    try:
        with open(r'C:\Users\duran\OneDrive\VSCODE\GameSolvers\Boggle\dictionary.txt') as file:
            content = file.read().splitlines()  # Split by lines
            dictionary = {word.upper() for word in content}
        return dictionary
    
    #issues getting to file, troubleshoot below
    except FileNotFoundError:
        print("Error: dictionary.txt not found")
    except Exception as e:
        print(f"Error loading dictionary: {e}")

def helper(board,  visited, row, col, word, wordlst,dictionary):
    #add new letter to word
    visited[row][col] = True
    word = word + board[row][col]
    
    #check if word is in dic
    #boggle word must be three letters in length
    if len(word) > 2 and check_word(word, dictionary):
        wordlst.append(word)
        
    #traverse
    
    #check all 8 directions
    for num_row in [-1, 0, 1]:
        for num_col in [-1, 0, 1]:
            if num_row == 0 and num_col ==0:
                continue #skip current letter
                
            nexrow, nexcol = row + num_row, col + num_col
            if nexrow > 3 or nexrow < 0 or  nexcol > 3 or nexcol < 0:
                continue #skip areas outside of board
          
            if not visited[nexrow][nexcol]:
                helper(board, visited, nexrow, nexcol, word, wordlst,dictionary)
            
            
            
    #move back to prev letter
    visited[row][col] = False


def solver(board,dictionary):
    wordlst = []
    
    visited = [[False for _ in range(4)] for _ in range(4)]

    
    #use all letters as a start. 4x4 grid. 
    for i in range(4):
        for j in range(4):
                word = ""
                helper(board, visited, i, j,word, wordlst,dictionary)
    return wordlst
          
def boggle():
    board = set_dice()
    print_board(board)
    dictionary = load_dictionary()
    wordlst = solver(board,dictionary)
    if len(wordlst) ==0:
        print( "Wow, not a single word found")
    else:
        print(wordlst)
    
if __name__ == "__main__":
    boggle()