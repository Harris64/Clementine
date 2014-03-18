import pyglet

from pyglet.event import *
from pyglet.gl import *
from pyglet.graphics import *
from pyglet.window import *

try:
	config = Config(sample_buffers = 1, samples = 4, depth_size = 16, double_buffer = True)
	window = Window(config = config)
except NoSuchConfigException:
	window = Window()

@window.event
def on_resize(width, height):
	glViewport(0, 0, width, height)
	glMatrixMode(GL_PROJECTION)
	glLoadIdentity()
	glMatrixMode(GL_MODELVIEW)

	return EVENT_HANDLED

@window.event
def on_draw():
	batch.draw()

batch = Batch()

for i in range(0, 20):
	for j in range(0, 15):
		xOffset = (2.0 / 20)
		yOffset = (2.0 / 15)

		x = (i * xOffset) - 1
		y = (j * yOffset) - 1

		batch.add(
			3, GL_TRIANGLES, None,
			('v2f', (x, y, x + xOffset, y, x + xOffset, y + yOffset)),
			('c3B', (0, 0, 255, 0, 255, 0, 0, 0, 255)))
		batch.add(
			3, GL_TRIANGLES, None,
			('v2f', (x, y, x, y + yOffset, x + xOffset, y + yOffset)),
			('c3B', (0, 0, 255, 0, 255, 0, 0, 0, 255)))

pyglet.app.run()