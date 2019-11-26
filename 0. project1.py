import pygame

screen = pygame.display.set_mode((600, 600))
screen.fill((0, 0, 255))
running = True
x = 0
v = 20
fps = 60
clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONUP:
            screen.fill((0, 0, 255))
            pygame.draw.circle(screen, pygame.Color('yellow'), event.pos, 20)
    pygame.display.flip()
    clock.tick(50)
pygame.quit()
