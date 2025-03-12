#loads board
def load_board():
    with open('Problem1.txt', 'r') as file:
        content = []
        for line in file:
            for char in line.strip():
                num = int(char)
                content.append(num)
    return content 
            

def create_board():
    # create array of notations (A1,A2,A3,A4 etc...)
    rows = "ABCDEFGHI"
    cols = "123456789"
    notation = [a+b for a in rows for b in cols]
    content = load_board()
    notatedboard = list(zip(notation,content))
    return notatedboard
    
def rowisvalid(notation,notatedboard, num):
    letter = notation[0]
    row = []
    for tulp in notatedboard:
        if letter in tulp[0]:
            row.append(tulp[1])
        if len(row) == 9:
            break
    if num in row:
        return False
    else:
        return True
def colisvalid(notation,notatedboard, num):
    number = notation[1]
    col = []
    for tulp in notatedboard:
        if number in tulp:
            col.append(tulp[1])
        if len(col) == 9:
            break
    if num in col:
        return False
    else:
        return True
def squareisvalid(notation,notatedboard, num):
    S1 = ['A1','A2','A3','B1','B2','B3','C1','C2','C3']
    S2 = ['A4','A5','A6','B4','B5','B6','C4','C5','C6']
    S3 = ['A7','A8','A8','B7','B8','B9','C7','C8','C9']
    S4 = ['D1','D2','D3','E1','E2','E3','F1','F2','F3']
    S5 = ['D4','D5','D6','E4','E5','E6','F4','F5','F6']
    S6 = ['D7','D8','D9','E7','E8','E9','F7','F8','F9']
    S7 = ['G1','G2','G3','H1','H2','H3','I1','I2','I3']
    S8 = ['G4','G5','G6','H4','H5','H6','I4','I5','I6']
    S9 = ['G7','G8','G9','H7','H8,''H9','I7','I8','I9']
    SQ = [S1,S2,S3,S4,S5,S6,S7,S8,S8]
    box = []
    square = []
    for sqr in SQ:
        if notation in sqr:
            box = sqr
            break       
    for tulp in notatedboard:
        if tulp[0] in box:
            square.append(tulp[1])
        if len(square) == 9:
            break
    if num in square:
        return False
    else:
        return True 
def isvalid(notation,notatedboard, num):
    if not colisvalid(notation,notatedboard, num):
        return False
    if not rowisvalid(notation,notatedboard, num):
        return False
    if not squareisvalid(notation,notatedboard, num):
        return False
    return True

print(isvalid('B3',create_board(), 2))