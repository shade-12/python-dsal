def binary_search_iterative(data, target):
    """
    Find target element within data array iteratively.
    Precondition: data is sorted
    """
    low, high = 0, len(data) - 1

    while low <= high:
        middle = low + (high - low) // 2
        if target == data[middle]:
            return True
        if target < data[middle]:
            high = middle - 1
        else:
            low = middle + 1
    return False


def binary_search_recursive(data, target, low, high):
    """
    Find target element within data array recursively.
    Precondition: data is sorted
    """



data = [2,4,5,7,8,9,12,14,17,19,22,25,27,28,33,37]
target = 7

# print(binary_search_recursive(data, target, 0, len(data)-1))
print(binary_search_iterative(data, target))