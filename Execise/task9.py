# 1. Создайте класс "Фигура", который будет иметь методы для вычисления площади и периметра. От этого класса унаследуйте классы "Круг", "Прямоугольник"
# и "Треугольник", которые будут иметь свои специфические методы для вычисления площади и периметра.

from math import pi

class Figure:

    def squares():
        pass


    def perimeter():
        pass
        

class  Circle(Figure):
    

    def __init__(self,redius):
        self.radius = redius


    def squares(self):
        res = (self.radius**2)*pi
        return res

    def perimeter(self):
        res = (2*pi)*self.radius
        return res

class Rectangle(Figure):

    def __init__(self, a, b):
        self.a  = a
        self.b = b


    def squares(self):
        return self.a * self.b


    def perimeter(self):
        return (self.a + self.b)*2


class Triangle(Figure):

    def __init__(self, a, b, c):
        self.a  = a
        self.b = b
        self.c =c


    def squares(self):
        p = (self.a + self.b + self.c) / 2
        square = (p*(p - self.a)*(p - self.b)*(p - self.c)) ** 0.5
        return square


    def perimeter(self):
        return self.a + self.b +self.c




# figer_1 = Figure
# c = Circle(6)
# print(c.perimeter())
r = Rectangle(2, 3)
print(r.squares())
t= Triangle(3, 4, 5)
print(t.squares())