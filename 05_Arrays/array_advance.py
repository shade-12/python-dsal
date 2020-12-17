def array_advance(arr):
    i, furthest_reached = 0, 0
    last_idx = len(arr) - 1
    while i <= furthest_reached and furthest_reached <= last_idx:
        furthest_reached = max(furthest_reached, arr[i] + i)
        i += 1
    return furthest_reached >= last_idx

# True: Possible to navigate to last index in A:
# Moves: 1,3,2
A = [3, 3, 1, 0, 2, 0, 1]
print(array_advance(A))

# False: Not possible to navigate to last index in A:
A = [3, 2, 0, 0, 2, 0, 1]
print(array_advance(A))