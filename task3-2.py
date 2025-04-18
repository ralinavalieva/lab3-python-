# task3.py

from abc import ABC, abstractmethod
import math

class Shape(ABC):
    
    @abstractmethod
    def area(self):
       pass
    
    @abstractmethod
    def perimeter(self):
       pass


class Rectangle(Shape):
    
    def __init__(self, width, height):
       self.width = width
       self.height = height
    
    def area(self):
       return self.width * self.height
    
    def perimeter(self):
       return 2 * (self.width + self.height)


class Circle(Shape):

   def __init__(self, radius):
       self.radius = radius
   
   def area(self):
       return math.pi * (self.radius ** 2)
   
   def perimeter(self):
       return 2 * math.pi * self.radius


class Triangle(Shape):

   def __init__(self, base, height):
       self.base = base
       self.height = height
   
   def area(self):
       return 0.5 * self.base * self.height
   
   def perimeter(self): 
       # для простоты считаем равнобедренный треугольник с двумя равными сторонами 
       side_length = math.sqrt((self.base / 2) ** 2 + (self.height ** 2))
       return side_length * 2 + self.base


def print_shape_info(shape):
   print(f"площадь: {shape.area()}, периметр: {shape.perimeter()}")


if __name__ == "__main__":
   rectangle = Rectangle(5, 10)
   circle = Circle(7)
   triangle = Triangle(6, 8)

   print("информация о фигурах:")
   print("прямоугольник:")
   print_shape_info(rectangle)
   
   print("\nкруг:")
   print_shape_info(circle)

   print("\nтреугольник:")
   print_shape_info(triangle)