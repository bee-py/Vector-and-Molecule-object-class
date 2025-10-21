class Vector:
    'Implements 3D vectors and their behaviour'

    def __init__(self, i1,i2,i3):
         '''Initializes new vector objects by setting the values
            of their of their 3 components'''
         self.x = i1
         self.y = i2
         self.z = i3
        
    def scale(self,a): #<---scale method
        'Multiplies the vector by a scalar a'
        return Vector(self.x*a, self.y*a, self.z*a)
            
    def dot(self,other_v):
        "Computes the dot product of this vector with another"
        dot_prod = self.x*other_v.x+self.y*other_v.y+self.z*other_v.z
        return dot_prod

    def norm(self):
        "Computes the norm/length of the given vector"
        return (self.x**2+self.y**2+self.z**2)**0.5

    def __add__(self,other_v):
        "Sum of vectors"
        return Vector(self.x+other_v.x, self.y+other_v.y, self.z+other_v.z)

    def __sub__(self,other_v):
        "The difference between two vectors"
        return Vector(self.x-other_v.x, self.y-other_v.y, self.z-other_v.z)

    def __truediv__(self, scalar):
        "Divide the vector by a scalar value"
        return Vector(self.x / scalar, self.y / scalar, self.z / scalar)
                      
    def copy(self):
        'Create a copy of the vector object'
        return Vector(self.x,self.y,self.z)

    def __repr__(self):
        "Coords of our vector"
        return (f"{self.x,self.y,self.z}")