def recursive_multiply(x, y):
    """
    Return product of two positive integers x and y
    Requirement: Calculate product without using multiplication operator
    """
    if x < y:
        return recursive_multiply(y, x)
    if y == 0:
        return 0
    return x + recursive_multiply(x, y - 1)