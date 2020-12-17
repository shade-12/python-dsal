import math

def integer_square_root_math(k):
    """
    Returns the largest integer whose square is less than or equal to k.
    k is a non-negative integer.
    """
    return math.floor(math.sqrt(k))


def integer_square_root_bin(k):
    """
    Returns the largest integer whose square is less than or equal to k.
    k is a non-negative integer.
    """
    low, high = 0, k
    while low <= high:
        mid = low + (high - low) // 2
        mid_squared = mid * mid

        if mid_squared <= k:
            low = mid + 1
        else:
            high = mid - 1
    return low - 1

k = 300
print(integer_square_root_bin(k))