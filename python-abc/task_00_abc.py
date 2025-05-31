#!/usr/bin/env python3
from abc import ABC, abstractmethod


class Animal(ABC):

    """
    Abstract base class representing an animal.

    This class defines a blueprint for animal subclasses,
    enforcing the implementation of the 'sound' method.
    """

    @abstractmethod
    def sound(self):
        """
        Produce the sound made by the animal.

        This is an abstract method that must be overridden
        by all subclasses.

        Raises:
            NotImplementedError: If the subclass does not implement this.

        Returns:
            str: The sound that the animal makes.
        """
        pass


class Dog(Animal):

    """
    Concrete implementation of Animal representing a dog.
    """

    def sound(self):
        """
        Return the characteristic sound of a dog.

        Returns:
            str: The string "Bark".
        """
        return "Bark"


class Cat(Animal):

    """
    Concrete implementation of Animal representing a cat.
    """

    def sound(self):
        """
        Return the characteristic sound of a cat.

        Returns:
            str: The string "Meow".
        """
        return "Meow"
