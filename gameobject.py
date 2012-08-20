import constants 

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


