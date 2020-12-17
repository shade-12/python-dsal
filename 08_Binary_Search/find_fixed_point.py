def find_fixed_point(arr):
    """
    Find an element in array where arr[i] = i.
    Pre-condition: Array is sorted in ascending order. All elements are unique.
    """
    low, high = 0, len(arr) - 1
    while low <= high:
        middle = low + (high - low) // 2
        if arr[middle] == middle:
            return middle
        if arr[middle] < middle:
            low = middle + 1
        else:
            high = middle - 1

    return None


# Fixed point is 3:
A1 = [-10, -5, 0, 3, 7]

# Fixed point is 0:
A2 = [0, 2, 5, 8, 17]

# No fixed point. Return "None":
A3 = [-10, -5, 3, 4, 7, 9]
print("Binary Search Approach")
print(A1)
print(find_fixed_point(A1))
print(A2)
print(find_fixed_point(A2))
print(A3)
print(find_fixed_point(A3))