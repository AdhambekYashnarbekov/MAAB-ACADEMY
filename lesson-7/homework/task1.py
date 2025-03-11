import math 

class Point:
    def __init__(self, x, y, z):
        self.x=x
        self.y=y
        self.z=z
    
    def __add__(self, other):
        return Point(self.x+other.x, self.y+other.y, self.z+other.z)
    
    def __sub__(self, other):
        return Point(self.x-other.x, self.y-other.y, self.z-other.z)
    
    def __mul__(self, other):
        return Point(self.x*other.y, self.y*other.y, self.z*other.z)

    def __truediv__(self, other):
        if Point(other.x!=0 and other.y!=0 and other.z!=0):
            return Point(self.x/other.x, self.y/other.y, self.z/other.z)
    
    def __mul__(self, other):
        return self.x*other.x+self.y+other.y+self.z+other.z

    def scalar_value(self):
        scalar_value=int(input("Enter the scalar value: "))
        return Point(self.x*scalar_value, self.y*scalar_value, self.z*scalar_value)

    def magnitude(self):
        return math.sqrt(self.x**2+self.y**2+self.z**2)

    def normilize(self):
        magnitude=math.sqrt(self.x**2+self.y**2+self.z**2)
        if magnitude==0:
            raise ValueError("Cannot Normalize a zero vector")
        return (
                f"{self.x / magnitude:.3f}",
                f"{self.y / magnitude:.3f}",
                f"{self.z / magnitude:.3f}"
            )


    def __str__(self):
        return f"({self.x},{self.y},{self.z})"

v1=Point(1,2,3)
print(v1)
v2=Point(4,5,6)
v3=v1+v2
print(v3)
v4=v2-v1
print(v4)
dot_product=v1*v2
print(dot_product)
v5=v1.scalar_value()
print(v5)
print(v1.magnitude())

v_unit=v1.normilize()
print(v_unit)



    
    
        