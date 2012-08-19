class GameObject(object):
    def width(self):
        return self.sprite.width

    def height(self):
        return self.sprite.height

    def rotate(self, angle):
        self.sprite.rotation += angle
    
    def is_out_of_bounds(self):
        return (self.position.x < -self.width() or self.position.x > 800+self.width()) or (self.position.y < -self.height() or self.position.y > 600+self.height())
