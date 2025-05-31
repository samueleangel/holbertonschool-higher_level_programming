#!/usr/bin/env python3

class SwimMixin:
    """Mixin providing swimming capability."""

    def swim(self):
        """Print swimming behavior."""
        print("The creature swims!")


class FlyMixin:
    """Mixin providing flying capability."""

    def fly(self):
        """Print flying behavior."""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """Dragon class that can both swim and fly."""

    def roar(self):
        """Print roaring behavior."""
        print("The dragon roars!")
