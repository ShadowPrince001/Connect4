import pygame
import numpy
pygame.init()
size = [700, 600]
screen = pygame.display.set_mode(size)
color=(255,255,255)
screen.fill(color)
for a in range(0,7):
    for b in range(0,6):
        h, k = 45+(a*100),105+(b*90)
        screen_array= pygame.surfarray.pixels2d(screen)
        for y in range(200):
            for x in range(100):
                for r in range(30):
                    if round(float((x-h)**2 + (y-k)**2 - r**2)) ==0:
                        screen_array[x,y]=0
print(screen_array)

pygame.display.flip()
