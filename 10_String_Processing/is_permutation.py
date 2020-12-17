def is_permutation_sort(a, b):
    """
    Determine if a given string is a permutation of another string.
    """
    # Time complexity: O(NlogN), space complexity: O(1)
    if len(a) != len(b):
        return False

    return sorted(a) == sorted(b)


def is_permutation_xor(a, b):
    # Time complexity: O(N), space complexity; O(N)
    if len(a) != len(b):
        return False

    l_a, l_b = list(a), list(b)
    res_a, res_b = 1, 1
    for i in range(len(l_a)):
        res_a = res_a ^ ord(l_a[i])
        res_b = res_b ^ ord(l_b[i])

    return not (res_a ^ res_b)

is_permutation_1 = "google"
is_permutation_2 = "ooggle"

not_permutation_1 = "not"
not_permutation_2 = "top"
print(is_permutation_sort(is_permutation_1, is_permutation_2))
print(is_permutation_sort(not_permutation_1, not_permutation_2))

print(is_permutation_xor(is_permutation_1, is_permutation_2))
print(is_permutation_xor(not_permutation_1, not_permutation_2))