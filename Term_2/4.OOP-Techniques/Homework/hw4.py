import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def is_on_x_axis(self):
        if self.y == 0:
            return True
        return False
    
    def is_same_coord(self, other_point):
        if self.x == other_point.x and self.y == other_point.y:
            return True
        return False

    def distance_from_other_point(self, other_point):
        dist = math.sqrt((self.x - other_point.x)**2 + (self.y - other_point.y)**2)
        return dist

    def in_unit_circle(self):
        if self.x**2 + self.y**2 <= 1:
            return True
        return False
    
    def midpoint_of_line(self, other_point):
        avg_x = (self.x + other_point.x) / 2
        avg_y = (self.y + other_point.y) / 2

        return avg_x, avg_y
    

p1 = Point(0, 0)
p2 = Point(1, 1)
p3 = Point(0, 5)
p4 = Point(0, 0) 

# Test is_on_x_axis
print(p1.is_on_x_axis())  # True, y=0
print(p2.is_on_x_axis())  # False, y=1
print(p3.is_on_x_axis())  # False, y=5

# Test is_same_coord
print(p1.is_same_coord(p2))  # False
print(p1.is_same_coord(p4))  # True

# Test distance_from_other_point
print(p1.distance_from_other_point(p2))  # sqrt(2)
print(p2.distance_from_other_point(p3))  # ~4.123

# Test in_unit_circle
print(p1.in_unit_circle())  # True, at origin
print(p2.in_unit_circle())  # False, distance from origin > 1
print(Point(0.5, 0.5).in_unit_circle())  # True, sqrt(0.5^2 + 0.5^2) <=1

# Test midpoint_of_line
print(p1.midpoint_of_line(p2))  # (0.5, 0.5)
print(p2.midpoint_of_line(p3))  # (0.5, 3.0)

