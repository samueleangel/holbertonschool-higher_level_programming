#!/usr/bin/env python3

class VerboseList(list):
    """
    Extension of the list class that prints notifications whenever an item
    is added or removed.
    """

    def append(self, item):
        """
        Append an item to the end of the list and print a notification.

        Args:
            item: The item to append.
        """
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, iterable):
        """
        Extend the list by appending elements from the iterable and print
        how many items were added.

        Args:
            iterable: An iterable with items to add.
        """
        super().extend(iterable)
        print(f"Extended the list with [{len(iterable)}] items.")

    def remove(self, item):
        """
        Remove the first occurrence of the item and print a notification
        before removal.

        Args:
            item: The item to remove.

        Raises:
            ValueError: If the item is not in the list.
        """
        print(f"Removed [{item}] from the list.")
        super().remove(item)

    def pop(self, index=-1):
        """
        Remove and return item at index (default last). Print a notification
        before removal.

        Args:
            index (int, optional): The index to pop. Defaults to -1.

        Returns:
            The popped item.

        Raises:
            IndexError: If the list is empty or index is invalid.
        """
        item = self[index]
        print(f"Popped [{item}] from the list.")
        return super().pop(index)
