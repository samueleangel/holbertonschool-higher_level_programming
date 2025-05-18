#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    """
    Prints x elements of a list.
    
    Args:
        my_list: List containing any type of elements
        x: Number of elements to print
        
    Returns:
        The real number of elements printed
    """
    count = 0
    try:
        for i in range(x):
            print(my_list[i], end="")
            count += 1
    except IndexError:
        pass
    print()
    return count 