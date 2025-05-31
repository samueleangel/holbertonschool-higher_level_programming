#!/usr/bin/env python3

class Fish:
    """
    Represents a fish with swimming ability and aquatic habitat.
    """

    def swim(self):
        """
        Print the swimming behavior of the fish.
        """
        print("The fish is swimming")

    def habitat(self):
        """
        Print the natural habitat of the fish.
        """
        print("The fish lives in water")


class Bird:
    """
    Represents a bird with flying ability and aerial habitat.
    """

    def fly(self):
        """
        Print the flying behavior of the bird.
        """
        print("The bird is flying")

    def habitat(self):
        """
        Print the natural habitat of the bird.
        """
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """
    Represents a flying fish that inherits from Fish and Bird.

    Overrides methods to demonstrate multiple inheritance and MRO.
    """

    def fly(self):
        """
        Print the flying behavior of the flying fish.
        """
        print("The flying fish is soaring!")

    def swim(self):
        """
        Print the swimming behavior of the flying fish.
        """
        print("The flying fish is swimming!")

    def habitat(self):
        """
        Print the habitat of the flying fish, combining both parents.
        """
        print("The flying fish lives both in water and the sky!")
