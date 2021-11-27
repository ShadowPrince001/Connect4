import pygame
import numpy
pygame.init()
size = [700, 600]
screen = pygame.display.set_mode(size)
bg = (0, 128, 255)
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
pygame.display.flip()
run=True
while run:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                if Column1.collidepoint(event.pos):
                    print("hi")
                elif Column3.collidepoint(event.pos):                    
                    run= False
                    
print(screen_array)

pygame.display.flip()
