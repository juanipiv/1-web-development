def inverse(my_list):
    """revert the given list quequence of elements.

    my_list(list): a sequence of elemnts.
    
    Output(list): 
    """
    size = len(my_list)
    for i in range(size):
        last_elem = my_list.pop()
        my_list.insert(i, last_elem)
    return my_list
