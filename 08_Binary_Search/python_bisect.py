# Python built-in binary serach method
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right

# bisect_left: Returns the index of left-most occurrence of the target value
# bisect_right: Returns the index of right-most occurrence of the target value
# bisect: Equivalent to bisect_right
# insort_left, insort_right: Behave in a similar way to bisect_left and bisect_right, 
#                            only the insort functions insert at the index positions

A = [-14, -10, 2, 108, 108, 243, 285, 285, 285, 401]

# -10 is at index 1
print(bisect_left(A, -10))

# First occurrence of 285 is at index 6
print(bisect_left(A, 285))


# Index position to right of -10 is 2.
print(bisect_right(A, -10)) 

# Index position after last occurrence of 285 is 9.
print(bisect_right(A, 285))


# Index position to right of -10 is 2. (Same as bisect_right)
print(bisect(A, -10)) 

# Index position after last occurrence of 285 is 9. (Same as bisect_right).
print(bisect(A, 285))


print(A)
insort_left(A, 108)
print(A)

insort_right(A, 108)
print(A)