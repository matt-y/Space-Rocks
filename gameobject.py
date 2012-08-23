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
        return self.position.v_distance_between(self.velocity)

    def set_position_with_velocity(self):
        self.position += self.velocity
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
        #our sprites are squares. We define the radius as the distance from the 
        #center of the sprite, to a corner. 
        #distance from center to corner in a "unit square" is sqrt(.50)
        width = self.width()
        height = self.height()
        if(width == height):
            return math.sqrt(.5) * width

        #radii do not exist for polygons and rectangles (ok fine, or squares)
        elif(width > height):
            return width 
        else: 
            return height 
        
    @classmethod
    def will_collide_with(self, one, other):
        '''
        Returns true or false if a collision will occur between two game objects 

        '''
        distance = math.sqrt((one.center_x() - other.center_x())**2 + 
                             (one.center_y() - other.center_y())**2)
        radii_sum = one.radius() + other.radius()

        if(distance <= radii_sum):
            return True
        else:
            return False
    
    def handle_collision(self, other):
        #Compute the normal between self and other
        normal = other.position - self.position
        #get a unit vector from the above 
        unit_normal = normal.v_normalize()

        #compute the tangent vector of the unit vector 
        #(make the x component the negative of the normal's y, 
        #    and the y component the normal's x component)
        unit_tangent = Vector(-unit_normal.y, unit_normal.x)

        #project the velocities of objects over the unit vector of the collision normal 
        #This breaks the velocity vectors into normal and tengental components

        #(compute the scalar velocity of the objects along the normals 
        self_normal_scalar_v = unit_normal.v_dot(self.velocity)
        self_tangent_scalar_v = unit_tangent.v_dot(self.velocity) #new tangent velocity 
        other_normal_scalar_v = unit_normal.v_dot(other.velocity)
        other_tangent_scalar_v = unit_tangent.v_dot(other.velocity) #new tangent velocity 
        
        #compute the wikipedia normal velocity formula 
        mass_difference = self.mass - other.mass
        mass_sum = self.mass + other.mass
        self_new_norm_velocity = ((self_normal_scalar_v * mass_difference) + 2 * (other.mass*other_normal_scalar_v)) / mass_sum
        other_new_norm_velocity = ((other_normal_scalar_v * mass_difference) + 2 * (self.mass*self_normal_scalar_v)) / mass_sum 
        
        #convert the normal and tangent velocities into vectors (by scaling the unit normal vector)
        self_norm_component = unit_normal * self_new_norm_velocity
        other_norm_component = unit_normal * other_new_norm_velocity
        
        self_tan_component = unit_normal * self_tangent_scalar_v
        other_tan_component = unit_normal * other_tangent_scalar_v

        #get the final new velocities by adding the tangental component
        self_v_final = self_norm_component + self_tan_component
        other_v_final = other_norm_component + other_tan_component

        #OMG DONE
        self.velocity = self_v_final 
        other.velocity = other_v_final
        
                                                              
                                                          
