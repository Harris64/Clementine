import pyglet

class Map():
	def __init__(self, parent, width, height):
		self.parent = parent

		self.width = width
		self.height = height

		self.image = pyglet.image.load("../res/graphics/tilesets/001-Grassland01.png")
		self.imageGrid = pyglet.image.ImageGrid(self.image, 18, 8)

		for x in range(self.width):
			for y in range(self.height):
				tileImage = self.imageGrid[136]
				tileSprite = pyglet.sprite.Sprite(tileImage, self.parent.batch)
				