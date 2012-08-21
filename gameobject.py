import constants 
from vector import Vector

class GameObject(object):
    def width(self):
        return self.sprite.width

    def height(self):
        return self.sprite.height
    
    def rotate(self, angle): 
        self.sprite.rotation += angle
    
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
