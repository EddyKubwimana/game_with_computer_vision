import pygame
pygame.init()
import time
height=600
width=1000
window=pygame.display.set_mode((width,height))
pygame.display.set_caption('Eddy game')
fps=30
pygame.time.Clock()
begin=True
while begin:
    for event in pygame.event.get():
        if event.type== pygame.QUIT:
            begin=False
            pygame.QUIT
    window.fill((255, 0, 0))
    pygame.display.update()
