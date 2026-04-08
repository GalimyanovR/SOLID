from abc import ABC, abstractmethod
from dataclasses import dataclass

# Абстрактный  класс для фигур
class Shape(ABC):
    @abstractmethod
    def area(self) -> int:
        pass

# Прямоугольник с независимыми шириной и высотой
@dataclass
class Rectangle(Shape):
    width: int
    height: int

    def area(self) -> int:
        return self.width * self.height

# Квадрат с одной стороной
@dataclass
class Square(Shape):
    side: int

    def area(self) -> int:
        return self.side * self.side

# Работает только с Rectangle, ожидая независимые width и height
def resize_and_get_area(rectangle: Rectangle) -> int:
    rectangle.width = 10
    rectangle.height = 5
    return rectangle.area()

# Работает фигурой, наследующей Shape
def get_area(shape: Shape) -> int:
    return shape.area()