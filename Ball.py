import random
from math import cos, sin, pi, log, sqrt, atan

class Ball:

	def __init__(self, center_pos, radius):
		self.__x = center_pos[0]
		self.__y = center_pos[1]
		self.__v = 0
		self.__ang = 0
		self.__radius = radius
	
	def move(self):
		self.__y = self.__y + 10*2*atan(self.__v/35)/pi * sin(self.__ang) 
		self.__x = self.__x + 10*2*atan(self.__v/35)/pi * cos(self.__ang)
		#Bounce off upper and lower walls
		if (self.__y - self.__radius) <= 0 or (self.__y + self.__radius) >= 600:
				self.__ang = -self.__ang

	def colide_player1(self, player):
		if (player.get_y()-5) <= self.__y and self.__y <= (player.get_y() + player.get_height() + 5):
			#Change ang according to player location
			diff = self.__y - (player.get_y() + player.get_height()/2)
			self.__ang = (diff / player.get_height() * pi* 0.65)
			# increase speed
			self.__v = self.__v  + 4
			return True
		return False

	def colide_player2(self, player):
		if (player.get_y()-5) <= self.__y and self.__y <= (player.get_y() + player.get_height() + 5):
			#Change ang according to player location
			diff = self.__y - (player.get_y() + player.get_height()/2)
			self.__ang = pi - (diff / player.get_height() * pi* 0.65) 
			# increase speed
			self.__v = self.__v  + 4
			return True
		return False

	def get_radius(self):
		return self.__radius

	def get_x(self): return self.__x

	def get_y(self): return self.__y

	def start(self):
		rand = random.Random()
		self.__v = rand.choice([15])
		self.__ang = 0 # TODO: random good angle
