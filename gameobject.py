import constants 
import math
from vector import Vector

class GameObject(object):
    def width(self):
        return self.sprite.width

    def height(self):
        return self.sprite.height
    
    def rotate(self, angle): 
        self.sprite.rotation += angle
    
    def get_velocity(self):
        return self.position.v_distance_between(self.acceleration)

    def set_position_with_acceleration(self):
        self.position += self.acceleration
        self.sprite.set_position(self.position.x, self.position.y)

    def is_out_of_bounds(self):
        return (self.position.x < -self.width() or self.position.x > constants.window_width+self.width()) or (self.position.y < -self.height() or self.position.y > constants.window_height+self.height())

    def __eq__(self, other):
        return self.position == other.position and self.acceleration == other.acceleration

    #sprites are centered when created (center_image)
    def center_x(self):
        return self.position.x
    def center_y(self):
        return self.position.y   
    
    def radius(self):
        #position is in the center of the image (center_image)
        left_hand_edge_point = Vector(self.position.x - self.sprite.width/2, self.position.y)
        return self.position.v_distance_between(left_hand_edge_point)

    def will_collide_with(self, other):
        '''
        Returns true or false if a collision will occur between two game objects 

        '''
        distance = math.sqrt((self.center_x() - other.center_x())**2 + 
                             (self.center_y() - other.center_y())**2)
        radii_sum = self.radius() + other.radius()

        if(distance <= radii_sum):
            return True
        else:
            return False
    
    @classmethod
    def handle_collision(self, one, other):
        #Below, we get a vector from self to other, and other to self.
        one_to_other = other.position - one.position
        other_to_one = one.position - other.position

        #unit vectors in the direction of the collision 
        normal_one_to_other = one_to_other.v_normalize()
        normal_other_to_one = other_to_one.v_normalize()

        #here we fiugre out how far along the velocity/acceleration vector is along the 
        #normalized vectors that point to the collision  
        proj_vel_one_to_other = normal_one_to_other.v_dot(one.acceleration)
        proj_vel_other_to_one = normal_other_to_one.v_dot(other.acceleration)

        #subtract the scaled collision vector from the acceleration vector
        #yielding our NEW acceleration vector 
        new_one_acceleration_vector = (one.acceleration - (normal_one_to_other * proj_vel_other_to_one))
        new_other_acceleration_vector = (other.acceleration - (normal_other_to_one * proj_vel_other_to_one))
        
        #done 
        one.acceleration = new_one_acceleration_vector 
        other.acceleration = new_other_acceleration_vector

        
                                                              
                                                          
