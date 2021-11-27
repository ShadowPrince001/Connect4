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
        h, k = 45+(a*100),90+(b*90)
        pygame.draw.circle(screen, (0, 0, 0), (h,k), 30)        
        screen_array= pygame.surfarray.pixels2d(screen)
        for y in range(600):
            for x in range(90):
                screen_array[x,y]=0
     
print(screen_array)

pygame.display.flip()


