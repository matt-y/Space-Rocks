import pyglet
from vector import Vector
from resources import Resources
from ship import Ship
import random


class Rock_List(object):
    def __init__(self, number, player_pos):
        self.number = number 
        self.rock_list = []
        for i in range(self.number):
            self.rock_list.append(self.create_rock(player_pos))
        


    def create_rock(self, player_pos):
        #attempt this until the rock position is 100 away from the player 
        random_pos = player_pos
        #check with player position
        while(random_pos.v_distance_between(player_pos) < 100):
            random_pos = Vector(random.randint(0,800),
                                random.randint(0,600))

        rock_final = Rock(random_pos)
        rock_final.rotate(random.randint(0,360))
        return rock_final
            
            

class Rock(object):
    def __init__(self, vector): 
        self.rock_sprite = pyglet.sprite.Sprite(img=Resources.rock_image, 
                                                x=vector.x, y=vector.y)

    def draw(self):
        self.rock_sprite.draw()
    
    def rotate(self, angle):
        self.rock_sprite.rotation = angle
        
