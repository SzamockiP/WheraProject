import pygame

pygame.init()

canvas = pygame.display.set_mode((720, 480))

pygame.display.set_caption("Testy")
clock = pygame.time.Clock()

exit = False

while not exit:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			exit = True
	pygame.display.update()
	clock.tick(60)
