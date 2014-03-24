import pyglet

class Character():
	def __init__(self, parent, x, y):
		self.parent = parent

		self.x = x
		self.y = y

		self.xOffset = 0
		self.yOffset = 0

		self.step = 0
		self.direction = 0

		self.isMoving = False
		self.isStopping = False

		self.image = pyglet.image.load("../res/graphics/characters/001-Fighter01.png")
		self.imageGrid = pyglet.image.ImageGrid(self.image, 4, 4)

	def startMoving(self, direction):
		if self.isMoving == False:
			self.direction = direction
			self.isMoving = True

	def keepMoving(self):
		if self.isMoving == True:
			self.x += self.xOffset
			self.y += self.yOffset

			self.xOffset = 0
			self.yOffset = 0

			self.step = 0

			if self.isStopping == True:
				self.isMoving = False
				self.isStopping = False

	def stopMoving(self):
		if self.isMoving == True:
			if self.isStopping == False:
				self.isStopping = True

	def update(self):
		if self.isMoving == True:
			if self.direction == 0:
				self.yOffset += 1

				if (self.yOffset % 32) != 0:
					if (self.yOffset % 8) == 0:
						self.step += 1
						self.parent.steps += 1

				else:
					self.keepMoving()

			elif self.direction == 1:
				self.xOffset += 1

				if (self.xOffset % 32) != 0:
					if (self.xOffset % 8) == 0:
						self.step += 1
						self.parent.steps += 1

				else:
					self.keepMoving()

			elif self.direction == 2:
				self.xOffset -= 1

				if (self.xOffset % 32) != 0:
					if (self.xOffset % 8) == 0:
						self.step += 1
						self.parent.steps += 1

				else:
					self.keepMoving()

			elif self.direction == 3:
				self.yOffset -= 1

				if (self.yOffset % 32) != 0:
					if (self.yOffset % 8) == 0:
						self.step += 1
						self.parent.steps += 1

				else:
					self.keepMoving()

	def render(self):
		frame = self.imageGrid[(self.direction * 4) + self.step]
		frame.blit(self.x + self.xOffset, self.y + self.yOffset)