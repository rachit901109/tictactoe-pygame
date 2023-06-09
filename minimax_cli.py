import random
import sys

maxint = sys.maxsize
minint = ~sys.maxsize

x_win = ['X']*3
o_win = ['O']*3
def checkwin(board):
    for i in board:
        if i == x_win:
            return [True,1]
        if i == o_win:
            return [True,0]
    for i in range(3):
        if [row[i] for row in board] == x_win:
            return [True,1]
        if [row[i] for row in board] == o_win:
            return [True,0]
        
    diag1 = [board[0][0],board[1][1],board[2][2]]
    diag2 = [board[0][2],board[1][1],board[2][0]]

    if diag1 == x_win or diag2 == x_win:
        return [True,1]
    if diag1 == o_win or diag2 == o_win:
        return [True,0]
    
    return [False,-1]

def draw_board(board):
    print("-------------")
    for i in board:
        print("|",end=" ")
        for j in i:
            print(j," |",end="")
        print()
        print("-------------",end="")
        print()

def player_move(board,cell,plmove):
    position = -1
    position = int(input("Enter cell(0 - 8):"))
    if (board[position//3][position%3]!=" "):
        while board[position//3][position%3]!=" ":
            print("Invalid position")
            position = int(input("Enter cell(0 - 8):"))
    board[position//3][position%3]=plmove
    cell.remove(position)

def rand_ai_move(cell):
    position = random.choice(cell)
    print(f"Computer choice: -{position}")
    board[position//3][position%3]='O'
    cell.remove(position)


def isempty(board):
    for i in board:
        for j in i:
            if j == " ":
                return True
    return False

def get_score(board):
    t = checkwin(board)
    if t[0] and t[1]==1:
        return 1
    elif t[0] and t[1]==0:
        return -1
    elif not isempty(board):
        return 0
    else:
        return " "

def minimax(board,depth,ismax):
    score = get_score(board)

    if score!=" ":
        return score

    if ismax:
        best_score = minint 
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j]= "X"
                    best_score = max(best_score,minimax(board,depth+1,not ismax))
                    board[i][j] = ' '
        return best_score
    
    else:
        best_score = maxint 
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j]="O"
                    best_score = min(best_score,minimax(board,depth+1,not ismax))
                    board[i][j] = ' '
        return best_score

def find_best_move(board,aimove,ismax):
    best_move = []
    max_val = minint
    min_val = maxint
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = aimove
                val = minimax(board,0,not ismax)
                board[i][j] = ' '

                if aimove == 'X':
                    if val>max_val:
                        max_val = val
                        best_move = [i,j]
                else:
                    if val<min_val:
                        min_val = val
                        best_move = [i,j]

    return best_move

def smart_ai_move(board,aimove):
    # ismax = True if aimove =="X" else False
    ismax = (aimove=="X")
    move = find_best_move(board,aimove,ismax)
    board[move[0]][move[1]] = aimove

play = "y" 

while play=="y":
    # create board
    board = [[" "]*3 for i in range(3)]
    cell = [i for i in range(9)]

    # define moves
    plmove = 'X'
    aimove = 'O'
    print(f"Player:{plmove}\t Computer:{aimove}")
    draw_board(board)
    # start game
    while 1:
        player_move(board,cell,plmove)
        draw_board(board)
        t = checkwin(board)
        if t[0]:
            if t[1] == 1:
                print("X wins")
            else:
                print("O wins")
            break
        if not isempty(board):
            print("Tie")
            break
        # rand_ai_move(cell)
        smart_ai_move(board,aimove)
        draw_board(board)
        t = checkwin(board)
        if t[0]:
            if t[1] == 1:
                print("X wins")
            else:
                print("O wins")
            break
        # if len(cell)==0:
        #     print("Tie")
        #     break
        if not isempty(board):
            print("Tie")
            break

    play = input("Press 'y' to play again: ")

        

        
        
        

