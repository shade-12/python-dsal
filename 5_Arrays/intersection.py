def intersection(a1, a2):
    """
    Find intersection of two arrays.
    """
    p1, p2 = 0, 0
    intersection = []
    
    while p1 < len(a1) and p2 < len(a2):
        if a1[p1] == a2[p2]:
            # No need to check previous value if p1 is 0
            if p1 == 0 or a1[p1] != a1[p1 - 1]:
                intersection.append(a1[p1])
            p1 += 1
            p2 += 1
        elif a1[p1] < a2[p2]:
            p1 += 1
        else:
            p2 += 1

    return intersection


A = [2, 3, 3, 5, 7, 11]
B = [3, 3, 7, 15, 31]

print(intersection(A, B))
