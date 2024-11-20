def tuples_to_dict(*tuples):
    """build a dictionary where teh keys are the first component of each
    tuple from the input, and the values will be the second components of
    the referred input tuples

    tuples (list): a variable argument list, made up of tuples (str, str)

    Outpot (dict): record of key-value pairs, matching the input tuples
    """
    result = dict()
    for my_tuple in tuples:
        key = my_tuple[0]
        value = my_tuple[1]
        if key not in result:
            result[key] = []
        result[key].append(value)
    return result
        
