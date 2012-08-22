import math

class Vector(object):
    """ 
    This class represents a simple two dimmensional vector with 
    an eye towards  a practical application in a 2d raycaster. 

    Any functionality that was not needed was not included.
    
    """

    def __init__(self, x=0,y=0):
        self.x = x
        self.y = y

    def __add__(self, vector):
        return Vector(self.x + vector.x, self.y + vector.y)

    def __sub__(self, vector):
        return Vector(self.x - vector.x, self.y - vector.y)
    
    def __mul__(self, obj):
        if(type(obj) is float):
            #scalar 
            return Vector(self.x * obj, self.y * obj)
        else:
            #matrix multiply 
            raise NotImplementedError("Multiplication between two vectors is not yet implemented")

    def __eq__(self, other):
        if (self.x == other.x and self.y == other.y):
            return True
        else: 
            return False

    def __len__(self):
        return math.sqrt(self.x*self.x + self.y*self.y)
    
    def v_dot(self, vector):
        return self.x*vector.x + self.y*vector.y

    def v_normalize(self):
        #we should avoid dividing by zero!
        denom = float(len(self))
        if denom == 0.0:
            denom = 0.1
        return Vector(self.x / denom, self.y / denom)

    def v_rotate(self, angle):
        x_prime = math.cos(angle)*self.x - (-math.sin(angle)*self.y)
        y_prime = math.sin(angle)*self.x + math.cos(angle)*self.y
        return Vector(x_prime, y_prime)

    def v_distance_between(self, vector):
        return math.sqrt((self.x - vector.x)**2 + (self.y - vector.y)**2)

    
