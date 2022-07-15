import math
import pygame
import json
import numpy
import time

pygame.init()

surface = pygame.display.set_mode((720, 480))

pygame.display.set_caption("Testy")
clock = pygame.time.Clock()

class Player():
	def __init__(self, pos_x, pos_y):
		self.pos_x = pos_x
		self.pos_y = pos_y

	def move():
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				exit = True

with open("mainMap.json", "r") as json_file:
	data = json.load(json_file)
	TILES = [pygame.image.load(data['tiles_to_load'][x]) for x in data['tiles_to_load']]
	TILESET = data['tileset']
	
exit = False	

while not exit:
	surface.fill([180,180,180])
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			exit = True

	mouse_pos = pygame.mouse.get_pos()
	old_time = time.time()
	for tile in TILESET:
		pos_x = tile['pos_x']
		pos_y = tile['pos_y']
		
		mouse_pos_tiled = numpy.dot([mouse_pos[0]-320, mouse_pos[1]-150+tile['height']*10], numpy.linalg.inv([[16,8],[-16,8]]))
		if math.floor(mouse_pos_tiled[0]-0.5) == pos_x and math.floor(mouse_pos_tiled[1]+0.5) == pos_y:
			surface.blit(TILES[tile['texture']], numpy.add(numpy.dot([pos_x,pos_y],[[16,8],[-16,8]]), [320,150-tile['height']*10-5]))
		else:
			surface.blit(TILES[tile['texture']], numpy.add(numpy.dot([pos_x,pos_y],[[16,8],[-16,8]]), [320,150-tile['height']*10]))
	print(time.time()-old_time)

	
	pygame.display.update()

	clock.tick(30)
