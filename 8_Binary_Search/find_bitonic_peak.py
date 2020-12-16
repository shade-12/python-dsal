import math

def find_bitonic_peak(arr):
    """
    arr does not contain any duplicates.
    """
    if len(arr) == 0:
        return None
    if len(arr) == 1:
        return arr[0]

    low, high = 0, len(arr) - 1
    while low <= high:
        middle = low + (high - low) // 2
        left_val = arr[middle - 1] if middle - 1 > 0 else -math.inf
        right_val = arr[middle + 1] if middle + 1 < len(arr) else math.inf

        if left_val < arr[middle] and right_val < arr[middle]:
            return arr[middle]
        if right_val > arr[middle] and left_val < arr[middle]:
            low = middle + 1
        elif left_val > arr[middle] and right_val < arr[middle]:
            high = middle - 1
    return None

# Peak element is "5".
A = [1, 2, 3, 4, 5, 4, 3, 2, 1]
print(find_bitonic_peak(A))
A = [1, 6, 5, 4, 3, 2, 1]
print(find_bitonic_peak(A))
A = [1, 2, 3, 4, 5]
print(find_bitonic_peak(A))
A = [5, 4, 3, 2, 1]
print(find_bitonic_peak(A))