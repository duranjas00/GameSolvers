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
            
def check_word(word):
    word = word.upper()
    with open('dictionary.txt') as file:
          for line in file:
            words = line.split()
            if word in words:
                return True
    return False
 def helper(board, ved, row, col, word, wordlst):
    #add new letter to word
    ved[row][col] = True
    word = word + board[row][col]
    
    #check if word is in dic
    #boggle word must be three letters in length
    if len(word) > 2:
        valid = check_word(word)
        if valid == True:
            wordlst.append(word)
        
    #traverse
    
    #move up and to the left
    nexrow = row - 1
    while nexrow <= row + 1 and nexrow < 4: 
        nexcol = col -1
        while nexcol <= col +1 and nexcol <4:
            if (nexrow >= 0 and nexcol >=0 and not ved[nexrow][nexcol]):
                helper(board, ved, nexrow, nexcol, word, wordlst)
           
    #move down and to the right
            nexcol +=1
        nexrow +=1
    
    #move back to prev letter
    word = word[-1]
    ved[row][col] = False


def solver(board):
    wordlst = []
    valid = False
    boollst = [False for x in range(4)]
    ved = [boollst]*4
    
    #use all letters as a start. hard coding 5 boggle boards are 4x4. 
    for i in range(4):
        for j in range(4):
                word = ""
                helper(board, ved, i, j,word, wordlst)
                #clear visited list for the next start letter
                boollst = [False for x in range(4)]
                ved = [boollst]*4
    return wordlst
          
