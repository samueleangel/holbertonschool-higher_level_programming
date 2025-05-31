#!/usr/bin/env python3
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """
    Abstract base class representing a geometric shape.

    Defines the blueprint for concrete shape classes,
    requiring implementation of area and perimeter methods.
    """

    @abstractmethod
    def area(self):
        """
        Calculate the area of the shape.

        Returns:
            float: The area of the shape.
        """
        raise NotImplementedError()

    @abstractmethod
    def perimeter(self):
        """
        Calculate the perimeter of the shape.

        Returns:
            float: The perimeter of the shape.
        """
        raise NotImplementedError()


class Circle(Shape):
    """
    Concrete implementation of Shape representing a circle.

    Attributes:
        radius (float): The radius of the circle.
    """

    def __init__(self, radius):
        """
        Initialize a Circle instance.

        Args:
            radius (float): The radius of the circle.
        """
        super().__init__()
        self.radius = radius

    def area(self):
        """
        Calculate the area of the circle.

        Returns:
            float: The area calculated as π * radius^2.
        """
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        """
        Calculate the perimeter (circumference) of the circle.

        Returns:
            float: The perimeter calculated as 2 * π * radius.
        """
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """
    Concrete implementation of Shape representing a rectangle.

    Attributes:
        width (float): The width of the rectangle.
        height (float): The height of the rectangle.
    """

    def __init__(self, width, height):
        """
        Initialize a Rectangle instance.

        Args:
            width (float): The width of the rectangle.
            height (float): The height of the rectangle.
        """
        super().__init__()
        self.width = width
        self.height = height

    def area(self):
        """
        Calculate the area of the rectangle.

        Returns:
            float: The area calculated as width * height.
        """
        return self.width * self.height

    def perimeter(self):
        """
        Calculate the perimeter of the rectangle.

        Returns:
            float: The perimeter calculated as 2 * (width + height).
        """
        return 2 * (self.width + self.height)


def shape_info(shape):
    """
    Print the area and perimeter of a shape object.

    This function uses duck typing: it calls the area() and perimeter()
    methods on the given object without explicit type checking.

    Args:
        shape (Shape): An object that implements area() and perimeter().
    """
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")
