def calculate_str_len_iterative(input):
    """
    Return the length of a string
    """
    l = 0
    for i in range(len(input)):
        l += 1
    return l

def calculate_str_len_recursive(input):
    """
    Return the length of a string
    """
    if input == '':
        return 0
    return 1 + calculate_str_len_recursive(input[1:])