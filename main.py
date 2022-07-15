import pygame

pygame.init()

surface = pygame.display.set_mode((720, 480))

pygame.display.set_caption("Testy")
clock = pygame.time.Clock()
basicTile = pygame.image.load("BasicTile.png")


exit = False
height = 0
while not exit:
	surface.fill([0,0,0])
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			exit = True
	
	for x in range(20):
		for y in range(20):
			surface.blit(basicTile, (x*16 + y*-16 + 320, x*8 + y*8))  # martix (0.5x + -0.5y, 0.25x + 0.25y)
		
	pygame.display.update()

	clock.tick(30)
