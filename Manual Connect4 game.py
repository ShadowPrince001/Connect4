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
        pygame.draw.circle(screen, (0, 0, 0), (45+(a*100),105+(b*90)), 30)
        h, k = 45+(a*100),105+(b*90)
        screen_array= pygame.surfarray.pixels2d(screen)
        for y in range(700):
            for x in range(600):
                if abs((x-h)**2 + (y-k)**2 - 30**2) == 0:
                    screen_array[x,y]=255

pygame.display.flip()
