import pygame

pygame.init()

WIDTH=1000
HEIGHT=700

screen=pygame.display.set_mode((WIDTH,HEIGHT))

screen.fill("grey")

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()


    pygame.display.update()
