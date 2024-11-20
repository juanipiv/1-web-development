def is_sorted(my_tuple):
    """checks if a given tuple is sorted in ascending order (or not)

    my_tuple (tuple): a sequence of elements
    output (boolean): True when all the elements in the tuple are sorted
    """
    previous = None
    for elem in my_tuple:
        if previous == None:  #if previous != None and elem < previous:
            previous = elem
        elif elem < previous:
            return False
        previous = elem
    return True

def is_sorted_v2(my_tuple):
    """checks if a given tuple is sorted in ascending order (or not)

    my_tuple (tuple): a sequence of elements
    output (boolean): True when all the elements in the tuple are sorted
    """
    i = 1
    while i < len(my_tuple):
        if my_list[i] < my_list[i-1]
            return False
        
        i = i + 1
    return True
        
