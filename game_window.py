import pygame

# initialize pygame
pygame.init()

# add game window
screen = pygame.display.set_mode((500,500))
screen.fill((255,255,255))
pygame.display.set_caption("TIC TAC TOE")
gameicon = pygame.image.load(r"C:\Users\rachi\2year_vac\pygame\ttt\tic-tac-toe.png")
pygame.display.set_icon(gameicon)

board = pygame.image.load(r"C:\Users\rachi\2year_vac\pygame\ttt\grid.png")
screen.blit(board,(122,122))


def startgame(mode:int):
    filled = []
    if mode ==1:
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
            cords = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEMOTION:
                    for i,j in gridmap.items():
                        if i not in filled and j[0] <= cords[0] <= j[0]+j[2] and j[1]<= cords[1] <= j[1]+j[3]:
                            # print(i)
                            pygame.draw.rect(screen,(255,160,160),j)
                        else:
                            if i not in filled:
                                pygame.draw.rect(screen,(255,255,255),j)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    for i,j in gridmap.items():
                        if event.button == 1 and i not in filled and j[0] <= cords[0] <= j[0]+j[2] and j[1]<= cords[1] <= j[1]+j[3]:
                            filled.append(i)
                            play = "X" if len(filled)%2==1 else "O"
                            move = pygame.font.SysFont("Times New Roman",36)
                            move_surf = move.render(play,True,(0,0,0))
                            screen.blit(move_surf,(j[0],j[1]))
        
            pygame.display.update()

startgame(2)
