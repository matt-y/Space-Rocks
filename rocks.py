import pyglet
from vector import Vector
from resources import Resources, center_image
from ship import Ship
from gameobject import GameObject
import random


class Rock_List(object):
    def __init__(self, number, player_pos):
        self.number = number 
        self.rock_list = []
        for i in range(self.number):
            self.rock_list.append(Rock.create_rock_from_player_pos(player_pos))

class Rock(GameObject):
    def __init__(self, vector): 
        self.sprite = center_image(pyglet.sprite.Sprite(img=Resources.rock_image,
                                                             x=vector.x, y=vector.y))

        self.position = vector
        self.acceleration = Vector(random.uniform(-1,1), random.uniform(-1,1))
        self.rotation_speed = random.uniform(0, 1)

    @classmethod
    def create_rock_from_player_pos(klass, player_pos):
        #attempt this until the rock position is 100 away from the player 
        random_pos = player_pos
        #check with player position
        while(random_pos.v_distance_between(player_pos) < 100):
            random_pos = Vector(random.randint(0,800),
                                random.randint(0,600))

        rock_final = Rock(random_pos)
        rock_final.rotate(random.randint(0,360))
        return rock_final


    def draw(self):
        self.set_position_with_acceleration()
        self.rotate(self.rotation_speed)
        self.sprite.draw()
        if(self.is_out_of_bounds()):
          self.position = Vector(400, 300)
    
    def set_position_with_acceleration(self):
        self.position += self.acceleration
        self.sprite.set_position(self.position.x, self.position.y)

    def rotate(self, angle):
        self.sprite.rotation += angle
        
