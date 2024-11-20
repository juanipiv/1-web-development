#a
def classify_with_reference(my_list, k):
    """takes a list of numbers and extracts greater values, lesser values and equal values separated.
    
    my_list (list): collection of given values
    k (int): reference to filter my_list

    Output (tuple): lesser values, greater values and equal values
    """
    lesser_values = []
    greater_values = []
    equal_values = []
    for elem in my_list:
        if elem < k:
            lesser_values.append(elem)
        elif elem > k:
            greater_values.append(elem)
        elif elem == k:
            equal_values.append(elem)
    return lesser_values, greater_values, equal_values
#b
def filter_multiples(my_list, k):
    """extract the multiples of a given number that are in a list

    my_list (list): collection of given values
    k (int): reference to filter my_list

    output (list): list of k's multiples in my_list
    """
    multiples_list = []
    for elem in my_list:
       remainder = elem % k
       if remainder == 0:
            multiples_list.append(elem)
    return multiples_list
