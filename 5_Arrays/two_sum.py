# Time complecity: O(N)
# Space complexity: O(N)
def two_sum_dict(arr, target_sum):
    """
    Find two values in an array that add up to target sum using dictionary(hash table).
    """
    store = dict()
    for num in arr:
        if num in store:
            return True
        else:
            store[target_sum - num] = 1
    return False


# Time complexity: O(N)
# Space complexity: O(1)
def two_sum_pointers(arr, target_sum):
    """
    Find two values in an array that add up to target sum using two pointers.
    Pre: arr is sorted in ascending order
    """
    low, high = 0, len(arr) - 1
    while low < high:
        curr_sum = arr[low] + arr[high]
        if curr_sum == target_sum:
            return True
        elif curr_sum > target_sum:
            high -= 1
        else:
            low += 1
    return False


A = [-2, 1, 2, 4, 7, 11]
target = 13
print(two_sum_pointers(A,target))
target = 20
print(two_sum_pointers(A,target))