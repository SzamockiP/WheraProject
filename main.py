import pygame
import json

pygame.init()

surface = pygame.display.set_mode((720, 480))

pygame.display.set_caption("Testy")
clock = pygame.time.Clock()

with open("mainMap.json", "r") as json_file:
	data = json.load(json_file)
	TILES = [pygame.image.load(data['tiles_to_load'][x]) for x in data['tiles_to_load']]
	TILESET = data['tileset']
	
exit = False	

while not exit:
	surface.fill([0,0,0])
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			exit = True
	
	for tile in TILESET:
		pos_x = tile['pos_x']
		pos_y = tile['pos_y']
		surface.blit(TILES[tile['texture']], (pos_x*16 + pos_y*-16 + 320, pos_x*8 + pos_y*8 - tile['height'] * 10 + 150))
	
	pygame.display.update()

	clock.tick(30)
