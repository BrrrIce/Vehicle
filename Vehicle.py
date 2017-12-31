from pygame.locals import *
import pygame
import math as m
import Resources as r


class Vehicle():
	def __init__(self, screen, id, size, start_pos, color):
		self.screen = screen
		self.id = id
		self.size = size
		self.pos = [start_pos[0],start_pos[1]]
		self.color = color
		self.speed = 3
		self.dir = 0
		
		self.offs = 0
		self.steer = 0

	def get_angle(self, p1, p2):
		a = m.atan2(p2[1]-p1[1],p2[0]-p1[0])
		return ((a + m.pi) % (2 * m.pi)) - m.pi

	def update(self):
		mouse_pos = pygame.mouse.get_pos()
		self.update_vehicle(self.pos, self.get_angle(self.pos, mouse_pos), r.black)

	def update_vehicle(self, pos, dir, color):
		self.dir += (dir - self.dir) /50

		self.a = pos
		self.b = (m.cos(self.dir)*self.size+self.a[0], m.sin(self.dir)*self.size+self.a[1])
		self.c = (m.cos(m.radians(90)+self.dir)*self.size/3+self.a[0], m.sin(m.radians(90)+self.dir)*self.size/3+self.a[1])
		self.d = (m.cos(m.radians(-90)+self.dir)*self.size/3+self.a[0], m.sin(m.radians(-90)+self.dir)*self.size/3+self.a[1])
		pygame.draw.line(self.screen, color, self.a, self.c, 4)
		pygame.draw.line(self.screen, color, self.a, self.d, 4)
		pygame.draw.line(self.screen, color, self.b, self.c, 4)
		pygame.draw.line(self.screen, color, self.b, self.d, 4)