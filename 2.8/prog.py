import math
class Vector_base:
    pass
def make_ndim_vector_class(n):    
    class Vector(Vector_base):
        dims = 0
        def __init__(self, *coords):
            if(len(coords) != Vector.dims):
                raise TypeError(f'Вектор размерности {Vector.dims}, но координат указано {len(coords)}')
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
                raise TypeError(f'Вектор можно сложить только с вектором, но второе слагаемое имеет тип {type(b)}')
            if Vector.dims != type(b).dims:
                raise TypeError(f'Попытка сложить вектора разной размерности. Размерность первого {self.dims}; размерность второго {b.dims}')
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