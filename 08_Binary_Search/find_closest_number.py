import math

def find_closest_number(arr, target):
    if len(arr) == 0:
        return None
    if target >= arr[-1]:
        return arr[-1]
    if target <= arr[0]:
        return arr[0]

    closest_num = None
    low, high = 0, len(arr) - 1
    while low <= high:
        middle = low + (high - low) // 2

        if arr[middle] == target:
            return target
        
        left_diff = abs(arr[middle - 1] - target) if ((middle - 1) >= 0) else math.inf
        right_diff = abs(arr[middle + 1] - target) if ((middle + 1) <= len(arr) - 1) else math.inf

        if left_diff < right_diff:
            high = middle - 1
            if (middle - 1) >= 0:
                closest_num = arr[middle - 1]
        else:
            low = middle + 1
            if (middle + 1) <= len(arr) - 1:
                closest_num = arr[middle + 1]

    return closest_num

A1 = [1, 2, 4, 5, 6, 6, 8, 9]
A2 = [2, 5, 6, 7, 8, 8, 9]

print(find_closest_number(A1, 11))
print(find_closest_number(A2, 4))