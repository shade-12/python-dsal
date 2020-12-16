def find_first_entry(arr, target):
    """
    Find the index of the first element in array where its value == target.
    Array is sorted and can contain duplicates.
    """
    low, high = 0, len(arr) - 1
    while low <= high:
        middle = low + (high - low) // 2
        if arr[middle] < target:
            low = middle + 1
        elif arr[middle] > target:
            high = middle - 1
        else:
            if middle == 0 or arr[middle - 1] != target:
                return middle
            high = middle - 1

    return None

A = [-14, -10, 2, 108, 108, 243, 285, 285, 285, 401]
target = 108
x = find_first_entry(A, target)
print(x)