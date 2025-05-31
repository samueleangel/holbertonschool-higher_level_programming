#!/usr/bin/env python3

class CountedIterator:
    """
    Iterator wrapper that counts how many items have been iterated over.

    Attributes:
        iterator: The underlying iterator object.
        count: Number of items iterated so far.
    """

    def __init__(self, iterable):
        """
        Initialize the CountedIterator with an iterable.

        Args:
            iterable: An iterable object to wrap.
        """
        self.iterator = iter(iterable)
        self.count = 0

    def __next__(self):
        """
        Return the next item from the iterator and increment the count.

        Raises:
            StopIteration: When the underlying iterator is exhausted.

        Returns:
            The next item from the iterator.
        """
        item = next(self.iterator)  # May raise StopIteration
        self.count += 1
        return item

    def get_count(self):
        """
        Return the number of items iterated so far.

        Returns:
            int: The count of iterated items.
        """
        return self.count
