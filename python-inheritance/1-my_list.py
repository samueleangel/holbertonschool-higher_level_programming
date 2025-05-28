#!/usr/bin/python3
"""
This module defines the class MyList that inherits from list.
"""


class MyList(list):
    """
    MyList class that inherits from list.
    """

    def print_sorted(self):
        """
        Prints the list in ascending sorted order.
        """
        print(sorted(self))
