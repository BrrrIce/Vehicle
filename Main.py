from pygame.locals import *
import pygame
import Resources as r
import Vehicle as v
import random as ra

vehicles = []

width = 600	
height = 800

pygame.init()
pygame.display.set_caption('Evolution')
screen = pygame.display.set_mode([width, height])
screen.fill(r.white)

def update_screen():
	pygame.display.update()

def spawn(num):
	for i in range(0,num):
		vehicles.append(v.Vehicle(screen, i+1, 40, (ra.randint(100,300),200), r.red))
	
spawn(1)
	
running = True
while running:
	screen.fill(r.white)
	
	for vehicle in vehicles:
		vehicle.update()
	update_screen()
	for i in pygame.event.get():
		if i.type == pygame.QUIT:
			running = False
			pygame.quit()
		if i.type == KEYDOWN:
			if i.key == 102: # <f>
				spawn(1)