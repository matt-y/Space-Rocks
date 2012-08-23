import pyglet
from vector import Vector
from resources import Resources, center_image
from ship import Ship
from gameobject import GameObject
import constants
import random
import math


class Rock_List(object):
    def __init__(self, number, player_pos):
        self.number = number 
        self.rock_list = []
        for i in range(self.number):
            self.rock_list.append(Rock.create_rock_from_player_pos(player_pos))

class Rock(GameObject):
    def __init__(self, vector): 
        #pick rock sprite 
        
        self.sprite = pyglet.sprite.Sprite(img=self.choose_sprite_from_list(Resources.rock_sprites),
                                                             x=vector.x, y=vector.y)
        self.position = vector
        self.velocity = Vector(random.uniform(-1.0, 1.0), random.uniform(-1.0,1.0))
        self.rotation_speed = random.uniform(0.1, 1.0)
        self.mass = 10

    def choose_sprite_from_list(self, list):
        return list[random.randint(0, len(list) -1)]

    @classmethod
    def create_rock_from_player_pos(klass, player_pos):
        #attempt this until the rock position is 100 away from the player 
        random_pos = player_pos
        #check with player position
        while(random_pos.v_distance_between(player_pos) < 100):
            random_pos = Vector(random.uniform(0, constants.window_width),
                                random.uniform(0,constants.window_height))

        rock_final = Rock(random_pos)
        rock_final.rotate(random.randint(0,360))
        return rock_final

    def draw(self):
        self.set_position_with_velocity()
        next_post = (self.position + self.velocity) * 1.1
        pyglet.gl.glColor4f(1.0,0,0,1.0)
        pyglet.graphics.draw(2, pyglet.gl.GL_LINES,
                             ('v2i', (int(self.position.x), int(self.position.y), int(next_post.x), int(next_post.y))))
        self.rotate(self.rotation_speed)
        self.sprite.draw()
        if(self.is_out_of_bounds()):
            self.reposition_rock()
    
    def reposition_rock(self):
        '''
        This function will reposition a rock to the edge of the window, and will set its direction 
        towards the center of the window, while keeping its previous speed

        '''
        self.position = self.new_edge_point()
        self.velocity = (constants.v_window_center - self.position).v_normalize() * random.uniform(.5,1.5)
        self.set_position_with_velocity()
        
    def new_edge_point(self):
        '''
        A random value from 1 to 4 is chosen to represent which "edge" of the window we will 
        place a point. From there, we are able to create specific points with appropriate y or x 
        values. 

        '''
        side = random.randint(1,4)
        if side == 1: 
            #left side 
            return Vector(0, random.randint(0, constants.window_height))
        elif side == 2:
            #right side 
            return Vector(constants.window_width, random.randint(0, constants.window_height))
        elif side == 3:
            #top
            return Vector(random.randint(0, constants.window_width), 0)
        else:
            #bottom
            return Vector(random.randint(0, constants.window_width), constants.window_height)
        
