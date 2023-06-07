import pygame

# initialize pygame
pygame.init()

# add game window
screen = pygame.display.set_mode((500,500))
screen.fill((255,255,255))
pygame.display.set_caption("TIC TAC TOE")
gameicon = pygame.image.load(r"C:\Users\rachi\2year_vac\pygame\ttt\tic-tac-toe.png")
pygame.display.set_icon(gameicon)



# check for wining conditions
x_win = [1]*3
o_win = [0]*3
def checkwin(board):
    for i in board:
        if i == x_win or i == o_win:
            return True
    for i in range(3):
        if [row[i] for row in board] == x_win or [row[i] for row in board] == o_win:
            return True
    diag1 = [board[0][0],board[1][1],board[2][2]]
    diag2 = [board[0][2],board[1][1],board[2][0]]

    if diag1 == x_win or diag1 == o_win or diag2 == x_win or diag2 == o_win:
        return True
    
    return False



def startgame(mode:int,player):
    # add grid
    board_img = pygame.image.load(r"C:\Users\rachi\2year_vac\pygame\ttt\grid.png")
    screen.blit(board_img,(122,122))

    # add player info
    style = pygame.font.SysFont("Times New Roman",24)
    screen.blit(style.render(f"Player{player['X']} - X",True,(0,0,0)),(0,0))
    screen.blit(style.render(f"Player{player['O']} - O",True,(0,0,0)),(0,40))

    # create board
    board = [[-1]*3 for i in range(3)]

    filled = []
    if mode == 1:
        pass
    else:
        running = True
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
        # sq0 = [122,122,60,60]
        # sq1 = [195,122,110,60]
        # sq2 = [315,122,60,60]
        # sq3 = [122,195,60,105]
        # sq4 = [195,195,110,105]
        # sq5 = [318,195,60,105]
        # sq6 = [122,315,60,60]
        # sq7 = [195,315,110,60]
        # sq8 = [315,315,60,60]
        # pygame.draw.rect(screen,(255,0,0),sq8)

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
                            # print(i)
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
                            screen.blit(move_surf,(j[0],j[1]))
                            # update on board
                            x_val = i//3
                            y_val = i%3
                            board[x_val][y_val] = 0 if play == "O" else 1
                            print(board)
                            if checkwin(board):
                                # print(f"Player {play} Wins!")
                                screen.blit(style.render(f"Player {play} Wins!",True,(0,0,0)),(180,90))
                                # running = False
                            elif len(filled)==9:
                                screen.blit(style.render("It's a tie",True,(0,0,0)),(200,90))
                                # running = False
        
            pygame.display.update()

startgame(2,{"X":1,"O":0})
