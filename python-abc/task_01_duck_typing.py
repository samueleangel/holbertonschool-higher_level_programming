#!/usr/bin/env python

from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """
    Abstract base class for any geometric shape.
    Enforces area() and perimeter() methods in subclasses.
    """

    @abstractmethod
    def area(self):
        """
        Return the area of the shape.

        Returns:
            float: Calculated area.
        """
        pass

    @abstractmethod
    def perimeter(self):
        """
        Return the perimeter of the shape.

        Returns:
            float: Calculated perimeter.
        """
        pass


class Circle(Shape):
    """
    Circle defined by its radius.
    """

    def __init__(self, radius):
        """
        Create a Circle.

        Args:
            radius (float): Radius of the circle.
        """
        self.radius = radius

    def area(self):
        """
        Compute area using π * r^2.

        Returns:
            float: Area of the circle.
        """
        return math.pi * self.radius ** 2

    def perimeter(self):
        """
        Compute perimeter using 2 * π * r.

        Returns:
            float: Perimeter of the circle.
        """
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """
    Rectangle defined by width and height.
    """

    def __init__(self, width, height):
        """
        Create a Rectangle.

        Args:
            width (float): Width of the rectangle.
            height (float): Height of the rectangle.
        """
        self.width = width
        self.height = height

    def area(self):
        """
        Compute area using width * height.

        Returns:
            float: Area of the rectangle.
        """
        return self.width * self.height

    def perimeter(self):
        """
        Compute perimeter using 2 * (width + height).

        Returns:
            float: Perimeter of the rectangle.
        """
        return 2 * (self.width + self.height)


def shape_info(shape):
    """
    Display area and perimeter of a shape object.

    Args:
        shape (Shape): Any object that implements area() and perimeter().
    """
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")


if __name__ == "__main__":
    circle = Circle(5)
    rectangle = Rectangle(4, 7)

    print("Circle:")
    shape_info(circle)

    print("\nRectangle:")
    shape_info(rectangle)
