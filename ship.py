import pyglet
from vector import Vector
from resources import Resources


class Ship(object):
    def __init__(self, vector): 
        self.ship_sprite = pyglet.sprite.Sprite(img=Resources.ship_image, 
                                                x=vector.x, y=vector.y)
        self.ship_position = vector
        

    def draw(self):
        self.ship_sprite.draw()
