import pyglet

class Map(object):

    # Initialisation method.
    def __init__(self):

        self.layer1 = []
        self.layer2 = []
        self.layer3 = []

        self.batch = pyglet.graphics.Batch()
        self.background = pyglet.graphics.OrderedGroup(0)
        self.foreground = pyglet.graphics.OrderedGroup(0)
        
        self.image = pyglet.image.load("../res/graphics/tilesets/001-Grassland01.png")
        self.imageGrid = pyglet.image.ImageGrid(self.image, 18, 8)

        for i in range(20):
            for j in range(15):
                self.layer1.append(pyglet.sprite.Sprite(self.imageGrid[self.layer1[i][j]], x = i * 32, y = j * 32, batch = self.batch, group = self.background))
                self.layer2.append(pyglet.sprite.Sprite(self.imageGrid[136], x = i * 32, y = j * 32, batch = self.batch, group = self.background))
                self.layer3.append(pyglet.sprite.Sprite(self.imageGrid[136], x = i * 32, y = j * 32, batch = self.batch, group = self.foreground))

    def draw(self):
        self.batch.draw()

        
