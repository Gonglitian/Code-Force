import math


class Round(): #圆形
    def __init__(self, R):
        self.R = R

    def area(self):
        return round(self.R * self.R * 3.14, 2)

    def girth(self):
        return round(self.R * 2 * 3.14, 2)


class Rectangle():#矩形
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def girth(self):
        return (self.length + self.width) * 2


class Triangle():#三角形
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def area(self):
        l = (self.a + self.b + self.c)/2
        return round(math.sqrt(l * (l - self.a) * (l - self.b) * (l - self.c)), 2)  #round保留2为小数

    def girth(self):
        return self.a + self.b + self.c


class Guadrilateral():#任意四边形
    def __init__(self, a, b, c, d, angle):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.angle = angle

    def area(self):
        l = (self.a + self.b + self.c + self.d)/2
        return round(math.sqrt((l - self.a) * (l - self.b) * (l - self.c) * (l - self.d) -
                               self.a * self.b * self.c * self.d
                               * math.pow(math.cos(math.radians(self.angle)), 2)), 2) #pow函数幂次方radians弧度转换为角度

    def girth(self):
        return self.a + self.b + self.c + self.d
