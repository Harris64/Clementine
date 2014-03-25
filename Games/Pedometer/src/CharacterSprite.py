import pyglet

class CharacterSprite(pyglet.sprite.Sprite):

	# Initialisation method.
	def __init__(self, image):
		super(CharacterSprite, self).__init__(image)