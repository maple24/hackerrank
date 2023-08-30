from __future__ import annotations
import math

class Points:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __sub__(self, no: Points) -> Points:
        return Points(self.x - no.x, self.y - no.y, self.z - no.z)

    def dot(self, no: Points):
        return self.x * no.x + self.y * no.y + self.z * no.z

    def cross(self, no: Points) -> Points:
        x = self.y * no.z - self.z * no.y
        y = self.z * no.x - self.x * no.z
        z = self.x * no.y - self.y * no.x
        return Points(x, y, z)
        
    def absolute(self):
        return pow((self.x ** 2 + self.y ** 2 + self.z ** 2), 0.5)

if __name__ == '__main__':
    a = Points(0, 4, 5)
    b = Points(1, 7, 6)
    c = Points(0, 5, 9)
    d = Points(1, 7, 2)
    x = (b - a).cross(c - b)
    y = (c - b).cross(d - c)
    angle = math.acos(x.dot(y) / (x.absolute() * y.absolute()))

    print("%.2f" % math.degrees(angle))