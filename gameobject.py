import constants 
import math
import random
from vector import Vector


class GameObject(object):
    def width(self):
        return self.sprite.width

    def height(self):
        return self.sprite.height
    
    def rotate(self, angle): 
        self.sprite.rotation += angle
    
    def get_velocity(self):
        return self.position.v_distance_between(self.velocity)

    def set_position_with_velocity(self):
        self.position += self.velocity * constants.clock_interval
        self.sprite.set_position(self.position.x, self.position.y)

    def is_out_of_bounds(self):
        return (self.position.x < -self.width() or self.position.x > constants.window_width+self.width()) or (self.position.y < -self.height() or self.position.y > constants.window_height+self.height())

    def __eq__(self, other):
        return self.position == other.position and self.velocity== other.velocity

    #sprites are centered when created (center_image)
    def center_x(self):
        return self.position.x
    def center_y(self):
        return self.position.y   
    
    def radius(self):
        # subtracting 10 is a decent adjustment for the empty 
        # space on the edge of the sprites 
        return math.sqrt(.5) * self.width() -10

    def in_same_direction(self, other):
        v_between = self.position - other.position
        if (v_between.v_dot(self.position + self.velocity) <= 0):
            return False
        else:
            return True

    def speed_scale(self):
        return random.uniform(10,50)

    def create_random_velocity(self):
        return Vector(random.uniform(-1,1), random.uniform(-1,1)) * self.speed_scale()
    
    def create_velocity_to_center(self):
        return (constants.v_window_center - self.position).v_normalize() * self.speed_scale()


    @classmethod
    def will_collide_with(self, one, other):
        '''
        Returns true or false if a collision will occur between two game objects 

        '''
        distance = math.sqrt((one.center_x() - other.center_x())**2 + 
                             (one.center_y() - other.center_y())**2)
        radii_sum = one.radius() + other.radius()
        
        if(distance <= radii_sum):
            #early escape check
            if one.in_same_direction(other):
                return True

        else:
            return False
    
    def handle_collision(self, other):
        #thank you kindly to a lovely gamasutra article
        # here: http://www.gamasutra.com/view/feature/131424/pool_hall_lessons_fast_accurate_.php?page=1
        n = self.position - other.position 
       
        n_norm = n.v_normalize()

        v1 = self.velocity 
        v2 = other.velocity 
        
        a1 = v1.v_dot(n)
        a2 = v2.v_dot(n)

        op_P = ((a1 - a2) * 2.0) / (self.mass + other.mass)

        temp = n * op_P
        v1_prime = v1 - (temp * other.mass)
        v2_prime = v2 + (temp * self.mass)

        #these get normalized because distance between pixels DNE 
        # distance in R/L
        self.velocity = v1_prime.v_normalize() * self.speed_scale()
        other.velocity = v2_prime.v_normalize() * self.speed_scale()
        
            
   
        
                                                              
                                                          
