import pyglet
from vector import Vector
from resources import Resources
from gameobject import GameObject


class Ship(GameObject):
    def __init__(self, vector): 
        self.sprite = pyglet.sprite.Sprite(img=Resources.ship_image, 
                                                x=vector.x, y=vector.y)
        self.position = vector
        self.acceleration = self.position
    
    def rotate_left(self):
        self.rotate(-5)
    
    def rotate_right(self):
        self.rotate(5)

    def draw(self):
        self.sprite.draw()
        if(self.is_out_of_bounds()):
            #todo: reposition ship on the opposite edge 
            pass
        
    
