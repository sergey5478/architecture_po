"""Реализация ISP.
Есть два класса и каждый реализует те методы,
которые ему нужны."""

from abc import ABC, abstractmethod


# Абстрактный класс для 2D фигур
class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass

    @abstractmethod
    def calculate_perimeter(self):
        pass


# Абстрактный класс для 3D фигур
class Shape3D(ABC):
    @abstractmethod
    def calculate_volume(self):
        pass


# Реализация класса Круг
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return 3.14 * self.radius ** 2

    def calculate_perimeter(self):
        return 2 * 3.14 * self.radius


# Реализация класса Куб
class Cube(Shape3D):
    def __init__(self, side_length):
        self.side_length = side_length

    def calculate_volume(self):
        return self.side_length ** 3


# Пример использования
if __name__ == "__main__":
    circle = Circle(5)
    print(f"Площадь круга: {circle.calculate_area()}")
    print(f"Периметр круга: {circle.calculate_perimeter()}")

    cube = Cube(3)
    print(f"Объем куба: {cube.calculate_volume()}")
