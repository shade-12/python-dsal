import math

def find_cyclically_shifted_min(arr):
    """
    Returns index of the smallest element in a cyclically shifted array
    """
    low, high = 0, len(arr) - 1
    while low < high:
        mid = (low + high) // 2
    
        if arr[mid] > arr[high]:
            low = mid + 1
        elif arr[mid] <= arr[high]:
            high = mid

    return low