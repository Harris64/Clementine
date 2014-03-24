import pyglet

class Character():
	def __init__(self, parent, x, y):
		self.parent = parent

		self.locationX = x
		self.locationY = y
		self.positionX = self.locationX * 32
		self.positionY = self.locationY * 32

		self.direction = 0
		self.step = 0
		self.isMoving = False

		self.image = pyglet.image.load("001-Fighter01.png")
		self.atlas = pyglet.image.ImageGrid(self.image, 4, 4)

	def move(self, direction):
		if self.isMoving == False:
			self.isMoving = True
			self.direction = direction

	def update(self):
		if self.isMoving == True:
			if self.step < 32:
				self.step += 1

				if (self.step % 8) == 0:
					self.parent.steps += 1
					self.parent.label.text = "Steps: " + str(self.parent.steps)
			else:
				if self.direction == 0:
					self.locationY += 1
				elif self.direction == 1:
					self.locationX += 1
				elif self.direction == 2:
					self.locationX -= 1
				elif self.direction == 3:
					self.locationY -= 1

				self.step = 0
				self.isMoving = False

			if self.direction == 0:
				self.positionY = (self.locationY * 32) + self.step
			elif self.direction == 1:
				self.positionX = (self.locationX * 32) + self.step
			elif self.direction == 2:
				self.positionX = (self.locationX * 32) - self.step
			elif self.direction == 3:
				self.positionY = (self.locationY * 32) - self.step

	def render(self):
		if self.step == 32:
			self.frame = self.atlas[(self.direction * 4) + 3]
		else:
			self.frame = self.atlas[(self.direction * 4) + (self.step / 8)]

		self.frame.blit(self.positionX, self.positionY)
