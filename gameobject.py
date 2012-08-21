import constants 
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
        radii_sum = self.radius() + other.obj_radius()

        if(distance <= radii_sum):
            return True
        else:
            return False

    def handle_collision(self, other):
        #retrieve a vecotr that  points from self to other
        at = other.position - self.position
        
        #normalize this direction vector 
        normalized_at = at.v_normalize()
        
        pass
