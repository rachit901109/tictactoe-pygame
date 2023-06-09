import pygame
import sys

# initialize pygame
pygame.init()

# add game window
screen = pygame.display.set_mode((500,500))
screen.fill((255,255,255))
pygame.display.set_caption("TIC TAC TOE")
gameicon = pygame.image.load(r"C:\Users\rachi\2year_vac\pygame\ttt\tic-tac-toe.png")
pygame.display.set_icon(gameicon)
style = pygame.font.SysFont("Times New Roman",24)

maxint = sys.maxsize
minint = ~sys.maxsize

# check for wining conditions
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

# check for empty board
def isempty(board):
    for i in board:
        for j in i:
            if j == " ":
                return True
    return False
# +1 for x wining -1 for o wining 0 for tie
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

# recursively call each player checkall possible states choose maximer or miniser
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

# find bestmove by calling minimax for each possible move from initial position
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

# begin game
def startgame(mode,players):
    # add  grid image
    board_img = pygame.image.load(r"C:\Users\rachi\2year_vac\pygame\ttt\grid.png")
    screen.blit(board_img,(122,122))

    # create board
    board = [[" "]*3 for i in range(3)]

    gridmap={
            0:[122,122,60,60],
            1:[195,122,110,60],
            2:[315,122,60,60],
            3:[122,195,60,105],
            4:[195,195,110,105],
            5:[318,195,60,105],
            6:[122,315,60,60],
            7:[195,315,110,60],
            8:[315,315,60,60]
        }
    
    filled = []
    if mode == 1:
        # Single player
        screen.blit(style.render(f"Player - {players[0]}",True,(0,0,0)),(0,0))
        screen.blit(style.render(f"Computer - {players[1]}",True,(0,0,0)),(0,40))
        move = "human"
        ismax = (players[1]=="X")
        running = True
        # main loop
        while running:
            cords = pygame.mouse.get_pos()
            for event in pygame.event.get():
                # exit
                if event.type == pygame.QUIT:
                    running = False
                # hover over grids
                if event.type == pygame.MOUSEMOTION:
                    for i,j in gridmap.items():
                        if i not in filled and j[0] <= cords[0] <= j[0]+j[2] and j[1]<= cords[1] <= j[1]+j[3]:
                            pygame.draw.rect(screen,(255,160,160),j)
                        else:
                            if i not in filled:
                                pygame.draw.rect(screen,(255,255,255),j)
                # player selects a cell
                if event.type == pygame.MOUSEBUTTONDOWN:
                    for i,j in gridmap.items():
                        if event.button == 1 and i not in filled and move == "human" and j[0] <= cords[0] <= j[0]+j[2] and j[1]<= cords[1] <= j[1]+j[3]:
                            filled.append(i)
                            move = "ai"
                            # update on screen
                            screen.blit(style.render(players[0],True,(0,0,0)),(j[0]+(j[2]//2),j[1]+(j[3]//2)))
                            # update on board
                            x_val = i//3
                            y_val = i%3
                            board[x_val][y_val] = players[0]
                            print(board)
                            # check for win/tie
                            t = checkwin(board)
                            if t[0]:
                                reset_window(running,"Human Wins")
                            elif len(filled)==9:
                                reset_window(running,"It's a tie")
                pygame.display.update()
            if move == "ai":
                move = "human"
                cpmove = find_best_move(board,players[1],ismax)
                print(cpmove)
                board[cpmove[0]][cpmove[1]]=players[1]
                cell_pos = (3*cpmove[0])+(cpmove[1]%3)
                filled.append(cell_pos)
                screen.blit(style.render(players[1],True,(0,0,0)),(gridmap[cell_pos][0]+(gridmap[cell_pos][2]//2),gridmap[cell_pos][1]+(gridmap[cell_pos][3]//2)))
                # print(board)
                t = checkwin(board)
                if t[0]:
                    reset_window(running,"AI wins")
                elif len(filled)==9:
                    reset_window(running,"It's a tie")

    else:
        # two player mode
        screen.blit(style.render(f"Player1 - {players[0]}",True,(0,0,0)),(0,0))
        screen.blit(style.render(f"Player2 - {players[1]}",True,(0,0,0)),(0,40))
        running = True
        while running:
            # get mouse cordinates
            cords = pygame.mouse.get_pos()
            for event in pygame.event.get():
                # exit
                if event.type == pygame.QUIT:
                    running = False
                # Highlight cell on hovering
                if event.type == pygame.MOUSEMOTION:
                    for i,j in gridmap.items():
                        if i not in filled and j[0] <= cords[0] <= j[0]+j[2] and j[1]<= cords[1] <= j[1]+j[3]:
                            pygame.draw.rect(screen,(255,160,160),j)
                        else:
                            if i not in filled:
                                pygame.draw.rect(screen,(255,255,255),j)
                # Update cell on clicking
                if event.type == pygame.MOUSEBUTTONDOWN:
                    for i,j in gridmap.items():
                        if event.button == 1 and i not in filled and j[0] <= cords[0] <= j[0]+j[2] and j[1]<= cords[1] <= j[1]+j[3]:
                            filled.append(i)
                            play = "X" if len(filled)%2==1 else "O"
                            move_surf = style.render(play,True,(0,0,0))
                            # update on screen
                            screen.blit(move_surf,(j[0]+(j[2]//2),j[1]+(j[3]//2)))
                            # update on board
                            x_val = i//3
                            y_val = i%3
                            board[x_val][y_val] = play
                            print(board)
                            t = checkwin(board)
                            if t[0]:
                                play+=" Wins"
                                reset_window(running,play)
                            elif len(filled)==9:
                                play = "It's a tie"
                                reset_window(running,play)
        
            pygame.display.update()

def reset_window(running,play):
    screen.fill((255,255,255))
    screen.blit(style.render(play,True,(0,0,0)),(200,200))
    screen.blit(style.render("Press y to play again",True,(0,0,0)),(160,250))
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_y:
                    screen.fill((255,255,255))
                    startgame(mode,players)
                else:
                    screen.fill((255,255,255))
                    exit()
                      
        pygame.display.update()

players = ['X','O']
mode = 1
startgame(mode,players)
