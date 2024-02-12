import math


class Point:
    def __init__(self, x=0.0, y=0.0):
        self.__x = x
        self.__y = y

    def getx(self):
        return self.__x

    def gety(self):
        return self.__y

    def distance_from_xy(self, x, y):
        b = math.fabs(self.__x - x)
        h = math.fabs(self.__y - y)
        return math.hypot(b, h)

    def distance_from_point(self, point):
        b = math.fabs(self.__x - point.getx())
        h = math.fabs(self.__y - point.gety())
        return math.hypot(b, h)

class Triangle:
    def __init__(self, vertice1, vertice2, vertice3):
        self.v1 = vertice1
        self.v2 = vertice2
        self.v3 = vertice3

    def perimeter(self):
        return self.v1.distance_from_point(self.v2) + self.v2.distance_from_point(self.v3) + self.v3.distance_from_point(self.v1) 

## Point class test
point1 = Point(0, 0)
point2 = Point(1, 1)
print(point1.distance_from_point(point2))
print(point2.distance_from_xy(2, 0))

## Triangle class test
triangle = Triangle(Point(0, 0), Point(1, 0), Point(0, 1))
print(triangle.perimeter())