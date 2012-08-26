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
        self.rock_list = [Rock.create_rock_from_other_pos(player_pos)]
        for i in range(self.number):
         
            #create a rock. If the rock is in range of the player OR any rock in the rock list - try again 
            is_rock_valid = False 
           
            while(is_rock_valid == False):
                broken = False 
                #try to get a valid rock 
                rock = Rock.create_rock_from_other_pos(player_pos)
                for r in self.rock_list:
                    if(self.do_objects_overlap(r, rock)):
                        #conflict with current rock 
                        broken = True
                        break
                    else:
                        continue
                if(broken): 
                    continue
                else: 
                    is_rock_valid = True

            #outside while loop:
            self.rock_list.append(rock)

    def do_objects_overlap(self, one, other):
        if(one.position.v_distance_between(other.position) < 100):
            return True
        else:
            return False

    
class Rock(GameObject):
    def __init__(self, vector): 
        #pick rock sprite 
        
        self.sprite = pyglet.sprite.Sprite(img=self.choose_sprite_from_list(Resources.rock_sprites),
                                                             x=vector.x, y=vector.y)
        self.position = vector
        self.velocity = self.create_random_velocity()
        self.rotation_speed = random.uniform(0.1, 1.0)
        self.mass = 5.0
        self.ignore_collisions = False
        
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
    
    def reposition_rock3(self):
        '''
        This function will reposition a rock to the edge of the window, and will set its direction 
        towards the center of the window, while keeping its previous speed

        '''
        self.position = self.new_edge_point()
        self.velocity = self.create_velocity_to_center()
        self.set_position_with_velocity()
       

    def reposition_rock(self):
        #current position is already out of bounds 
        x_pos = self.position.x
        y_pos = self.position.y
        
        #Remember: Y axis grows downwards in the game window 
        
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
        #self.velocity = self.create_velocity_to_center()
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
        
