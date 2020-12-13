def increment_by_one(arr):
    arr[-1] += 1

    for i in reversed(range(1, len(arr))):
        if arr[i] != 10:
            break
        arr[i] = 0
        arr[i-1] += 1
    if arr[0] == 10:
        arr[0] = 1
        arr.append(0)
    return arr

A1 = [1, 4, 9]
A2 = [9, 9, 9]
print(increment_by_one(A1))
print(increment_by_one(A2))
