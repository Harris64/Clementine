import pyglet

class Game():
	def __init__(self):
		self.window = pyglet.window.Window()
		self.batch = pyglet.graphics.Batch()
		self.fps = pyglet.clock.ClockDisplay()
		self.image = pyglet.image.load("../res/graphics/tilesets/001-Grassland01.png")
		self.imageGrid = pyglet.image.ImageGrid(self.image, 18, 8)

		self.tile = self.imageGrid[136]
		self.texture = self.tile.get_texture()

		pyglet.gl.glBindTexture(self.texture.target, self.texture.id)

		self.window.on_draw = self.render

		for x in range(self.window.width / 32):
			for y in range(self.window.height / 32):
				self.vertexList = self.batch.add(3, pyglet.gl.GL_TRIANGLES, None, ('v2i', (x * 32, y * 32, x * 32, y * 32 + 32, x * 32 + 32, y * 32 + 32)), ('c3B', (0, 0, 0, 0, 0, 0, 0, 0, 0)), ("t2f", (0, 0, 0, 1, 1, 1)))
				self.vertexList = self.batch.add(3, pyglet.gl.GL_TRIANGLES, None, ('v2i', (x * 32, y * 32, x * 32 + 32, y * 32, x * 32 + 32, y * 32 + 32)), ('c3B', (0, 0, 0, 0, 0, 0, 0, 0, 0)), ("t2f", (0, 0, 1, 0, 1, 1)))

		pyglet.app.run()

	def render(self):
		self.window.clear()
		self.batch.draw()
		self.fps.draw()

if __name__ == "__main__":
	game = Game()