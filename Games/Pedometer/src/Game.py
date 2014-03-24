import pyglet

from Character import *

class Game():
	def __init__(self):
		self.window = pyglet.window.Window(640, 320)
		self.window.set_caption("Pedometer")
		self.window.set_icon(pyglet.image.load("../res/graphics/icons/020-Accessory05.png"))
		self.window.on_key_press = self.input
		self.window.on_draw = self.render

		self.background = pyglet.image.load("../res/graphics/battlebacks/001-Grassland01.jpg")

		self.character = Character(self, 0, 0)
		self.steps = 0

		self.label = pyglet.text.Label("Steps: 0", font_name = "Helvetica", font_size = 12, x = 10, y = self.window.height - 10, anchor_x = "left", anchor_y = "top", bold = True)

		pyglet.gl.glEnable(pyglet.gl.GL_BLEND)
		pyglet.gl.glBlendFunc(pyglet.gl.GL_SRC_ALPHA, pyglet.gl.GL_ONE_MINUS_SRC_ALPHA)

		pyglet.clock.schedule_interval(self.update, 0.5 / 32)
		pyglet.app.run()

	def input(self, symbol, modifiers):
		if symbol == pyglet.window.key.UP:
			self.character.move(0)
		elif symbol == pyglet.window.key.RIGHT:
			self.character.move(1)
		elif symbol == pyglet.window.key.DOWN:
			self.character.move(3)
		elif symbol == pyglet.window.key.LEFT:
			self.character.move(2)

	def update(self, dt):
		self.character.update()

	def render(self):
		self.window.clear()
		self.background.blit(0, 0)
		self.character.render()
		self.label.draw()

if __name__ == "__main__":
	game = Game()