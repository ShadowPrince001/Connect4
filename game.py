import pygame
import numpy
pygame.init()
size = [700, 600]
screen = pygame.display.set_mode(size)
bg = (0, 128, 255)
Text_color=(0,255,255)

screen.fill(bg)
pygame.display.set_caption("This is Connect4.")

for a in range(0,7):
    for b in range(0,6):
        h, k = 50+(a*100),90+(b*90)
        pygame.draw.circle(screen, (0, 0, 0), (h,k), 30)        
        screen_array= pygame.surfarray.pixels2d(screen)
    
Column1 = pygame.draw.rect(screen, [0, 0, 0], [5, 50, 90, 540], 1)
Column2 = pygame.draw.rect(screen, [0, 0, 0], [105, 50, 90, 540], 1)
Column3 = pygame.draw.rect(screen, [0, 0, 0], [205, 50, 90, 540], 1)
Column4 = pygame.draw.rect(screen, [0, 0, 0], [305, 50, 90, 540], 1)
Column5 = pygame.draw.rect(screen, [0, 0, 0], [405, 50, 90, 540], 1)
Column6 = pygame.draw.rect(screen, [0, 0, 0], [505, 50, 90, 540], 1)
Column7 = pygame.draw.rect(screen, [0, 0, 0], [605, 50, 90, 540], 1)

run=True
C1=0
C2=0
C3=0
C4=0
C5=0
C6=0
C7=0
Turn=1
pygame.display.flip()
while Turn < 43:
    if Turn%2==1:
        Color=(0,255,0)
        pygame.display.set_caption("This is Connect4.Player 1 Turn")
    else:
        Color=(255,0,0)
        pygame.display.set_caption("This is Connect4.Player 2 Turn")
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONUP and  event.button == 1:
            if Column1.collidepoint(event.pos) and C1 < 6 :
                pygame.draw.circle(screen, (Color), (50,540-(C1*90)), 30)
                C1+=1
                Turn+=1
                pygame.display.flip()
            elif Column2.collidepoint(event.pos) and C2 < 6:
                pygame.draw.circle(screen, (Color), (150,540-(C2*90)), 30)
                C2+=1
                Turn+=1
                pygame.display.flip()
            elif Column3.collidepoint(event.pos) and C3 < 6:
                pygame.draw.circle(screen, (Color), (250,540-(C3*90)), 30)
                C3+=1
                Turn+=1
                pygame.display.flip()
            elif Column4.collidepoint(event.pos) and C4 < 6:
                pygame.draw.circle(screen, (Color), (350,540-(C4*90)), 30)
                C4+=1
                Turn+=1
                pygame.display.flip()
            elif Column5.collidepoint(event.pos) and C5 < 6:
                pygame.draw.circle(screen, (Color), (450,540-(C5*90)), 30)
                C5+=1
                Turn+=1
                pygame.display.flip()
            elif Column6.collidepoint(event.pos) and C6 < 6 :
                pygame.draw.circle(screen, (Color), (550,540-(C6*90)), 30)
                C6+=1
                Turn+=1
                pygame.display.flip()
            elif Column7.collidepoint(event.pos) and C7 < 6:
                pygame.draw.circle(screen, (Color), (650,540-(C7*90)), 30)
                C7+=1
                Turn+=1
                pygame.display.flip()
            elif Turn==42:
                break
                pygame.quit()
                exit()
            elif event.type == pygame.QUIT:
                break
                pygame.quit()
                exit()           
            
