import pyglet

class Pedometer(object):

	# Initialisation method.
	def __init__(self):

		# Create game window.
		self.window = pyglet.window.Window()

		# Load resources.
		self.characterImage = pyglet.image.load("../res/graphics/characters/001-Fighter01.png")
		self.characterImageGrid = pyglet.image.ImageGrid(self.characterImage, 4, 4)
		self.characterAnimation = pyglet.image.Animation(self.characterImageGrid)

		# Create game objects.
		self.character = pyglet.sprite.Sprite(self.characterAnimation)

		# Assign game window event handlers.
		self.window.on_draw = self.draw

		# Run application.
		pyglet.app.run()

	def draw(self):

		# Draw character.
		self.character.draw()

pedometer = Pedometer()