import pyglet

class Map():
	def __init__(self, width, height):
		self.width = width
		self.height = height

		self.image = pyglet.image.load("../res/graphics/tilesets/001-Grassland01.png")
		self.imageGrid = pyglet.image.ImageGrid(self.image, 18, 8)

	def render(self):
		for x in range(self.width):
			for y in range(self.height):
				tile = self.imageGrid[136]
				tile.blit(x * 32, y * 32)