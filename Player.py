class Player:
	def __init__(self,x, y, name):
		self.__weight = 20
		self.__height = 60
		self.__x = x
		self.reset_y(y)
		self.__score 	= 0
		self.__name = name

	def move_up(self):
		if self.__y > 0 : self.__y -= 5

	def move_down(self):
		if self.__y < 540 : self.__y += 5

	def get_y(self):
		return self.__y

	def get_x(self):
		return self.__x

	def get_height(self):
		return self.__height

	def get_weight(self):
		return self.__weight

	def get_score(self):
		return self.__score

	def inc_score(self):
		self.__score += 1

	def reset_y(self, y):
		self.__y = y - self.__height / 2
	
	def get_name(self):
		return self.__name