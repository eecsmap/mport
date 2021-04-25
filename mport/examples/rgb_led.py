import mport
import pygame

pygame.init()

r = mport.Port('rgb.dat')
g = mport.Port('rgb.dat', offset=1)
b = mport.Port('rgb.dat', offset=2)

screen = pygame.display.set_mode([100, 100])

run = True

while run:
    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    screen.fill('black')
    pygame.draw.circle(screen, (r.value, g.value, b.value), (50, 50), 20)
    pygame.display.flip()

pygame.quit()
