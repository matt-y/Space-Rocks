import pyglet
from vector import Vector
from resources import Resources, center_image
from ship import Ship
from gameobject import GameObject
import constants
import random
import math

class Rock(GameObject):
    def __init__(self, vector): 
        #pick rock sprite 
        
        self.sprite = pyglet.sprite.Sprite(img=self.choose_sprite_from_list(Resources.rock_sprites),
                                           x=vector.x,
                                           y=vector.y)
        self.position = vector
        self.velocity = self.create_random_velocity()
        self.rotation_speed = random.uniform(0.1, 1.0)
        self.mass = 5.0
        self.hp = random.randint(2,5)
        self.ignore_breaks = False
        self.ignore_collisions = False
        
    def set_sprite(self, sprite_image):
        self.sprite = pyglet.sprite.Sprite(img=sprite_image, 
                                           x=self.position.x, 
                                           y=self.position.y)

    def choose_sprite_from_list(self, list):
        return list[random.randint(0, len(list) -1)]

    @classmethod
    def create_rock_from_other_pos(klass, other_pos):
        #attempt this until the rock position is 100 away from the player 
        random_pos = other_pos
        #check with player position
        while(random_pos.v_distance_between(other_pos) < 100):
            random_pos = Vector(random.uniform(0, constants.window_width),
                                random.uniform(0,constants.window_height))

        rock_final = Rock(random_pos)
        rock_final.rotate(random.randint(0,360))
        return rock_final

    def draw(self):
        self.set_position_with_velocity()
        next_post = (self.position + self.velocity)
        if constants.debug:
            pyglet.gl.glColor4f(1.0,0,0,1.0)
            pyglet.graphics.draw(2, pyglet.gl.GL_LINES,
                             ('v2i', (int(self.position.x), int(self.position.y), int(next_post.x), int(next_post.y))))
       
        self.rotate(self.rotation_speed)
        self.sprite.draw()
        if(self.is_out_of_bounds()):
            self.reposition_rock()
    
    def break_rock(self):
        '''
        This function breaks a large rock into four smaller rocks.

        To do this, the rock is partitioned into four quadrants - the center of these quadrants is a new 
        rock position. New rocks are created at the center of each quadrant, and added to the rock list.
        the new velocities go outward from the center of the orighttp://www.reddit.com/inal sprite 
        '''
        #remove current rock from list. 
        new_list = []
        for rock in constants.object_list:
            if self != rock: 
                new_list.append(rock)

        width = self.width()
        height = self.height()

        center_x = self.position.x
        center_y = self.position.y
        
        quadrant_horizontal_offset = width/4
        quadrant_vertical_offset = height/4

        upper_left = Vector(center_x - quadrant_horizontal_offset,
                            center_y + quadrant_vertical_offset)
        upper_right = Vector(center_x + quadrant_horizontal_offset, 
                             center_y + quadrant_vertical_offset)
        bottom_left = Vector(center_x - quadrant_horizontal_offset, 
                             center_y - quadrant_vertical_offset)
        bottom_right = Vector(center_x + quadrant_horizontal_offset, 
                              center_y - quadrant_vertical_offset)

        sprite = Resources.rock_image1_small
        
        #create vectors, and add to rock list
        rock_upper_left = self.create_small_rock(upper_left, Vector(-1,1), sprite)

        rock_upper_right = self.create_small_rock(upper_right, Vector(1,1), sprite)

        rock_bottom_left = self.create_small_rock(bottom_left, Vector(-1,-1), sprite)
        
        rock_bottom_right = self.create_small_rock(bottom_right, Vector(1,-1), sprite)

        #add to rock list:
        
        temp = [rock_upper_left, rock_upper_right, rock_bottom_left, rock_bottom_right]
        random.shuffle(temp) #in place
        new_list.extend(temp[:2])
        constants.object_list = new_list
        

    def create_small_rock(self, position, velocity, sprite):
        r = Rock(position)
        r.velocity = velocity * self.speed_scale()
        r.set_sprite(sprite)
        r.ignore_breaks = True 
        r.mass = 1.0
        return r

    def reposition_rock(self):
        #current position is already out of bounds 
        x_pos = self.position.x
        y_pos = self.position.y
        
        new_x = x_pos
        new_y = constants.window_height - y_pos
        if x_pos < 0: 
            #if we are OOB to the LEFT 
            new_x = constants.window_width + 50
            print "oob left"
        if x_pos > constants.window_width:
            #If we are OOB to the RIGHT 
            new_x = -50
            print "oob right"
        if y_pos > constants.window_height: 
            #if we are OOB to the top
            new_y = 0
            print "oob top"
        if y_pos < 0:
            #if we areOOB to the bottom
            new_y = constants.window_height + 50
            print "oob bottom"
        self.position = Vector(new_x, new_y)
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
        
