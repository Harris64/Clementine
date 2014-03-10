import pyglet

window = pyglet.window.Window()
image = pyglet.resource.image("res/battlebacks/001-Grassland01.jpg")

@window.event
def on_draw():
    window.clear()
    image.blit(0, 0)

pyglet.app.run()