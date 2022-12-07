import math

class Vector_base:
    pass

def make_ndim_vector_class(n):    
    class Vector(Vector_base):
        dims = 0
        def __init__(self, *coords):
            if(len(coords) != Vector.dims):
                raise TypeError(f'Number of coordinates must be equal to {Vector.dims}, but given {len(coords)}')
            self.coords = coords
        
        def get_length(self):
            s = 0
            for x in self.coords:
                s+=x*x
            return math.sqrt(s)
        
        def show(self):
            print(*self.coords)
        
        def __add__(self, b):
            if (not isinstance(b, Vector_base)) :
                raise TypeError(f'Second argument must be vector, but {type(b)}')
            if Vector.dims != type(b).dims:
                raise TypeError(f'Dimensions of the vectors must be equal ({Vector.dims} != {type(b).dims}). ')
            new_coords =map(lambda x,y: x+y, self.coords, b.coords)
            return Vector(*new_coords)
        
    Vector.dims = n
    return Vector

Vector3 = make_ndim_vector_class(3)
Vector2 = make_ndim_vector_class(2)
a = Vector3(1,0.1,1.5)
b = Vector3(-1,0, 10)
c = Vector2(-1, 1)
(a+b).show()
#a + 0.1
print(c.get_length())