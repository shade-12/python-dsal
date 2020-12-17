def is_anagram_xor(str1, str2):
    if len(str1) != len(str2):
        return False

    l1 = list(str1)
    l2 = list(str2)
    res1, res2 = 1, 1
    for i in range(len(str1)):
        res1 = res1 ^ ord(l1[i])
        res2 = res2 ^ ord(l2[i])
        
    return not (res1 ^ res2)

# This algorithmn will take O(N) time complexity and O(N) space complexity (create extra char array)
print(is_anagram_xor("iceman", "cinema"))
print(is_anagram_xor("icemaa", "cinema"))


def is_anagram_sort(str1, str2):
    if len(str1) != len(str2):
        return False

    res1 = sorted(str1)
    res2 = sorted(str2)

    return res1 == res2

# This algorithm will have O(Nlogn) time complexity and O(N) space complexity (create sorted string)
print(is_anagram_sort("iceman", "cinema"))
print(is_anagram_sort("icemaa", "cinema"))


def is_anagram_dict(str1, str2):
    if len(str1) != len(str2):
        return False

    store = dict()

    for i in range(len(str1)):
        if str1[i] in store:
            del store[str1[i]]
        else:
            store[str1[i]] = 1

        if str2[i] in store:
            del store[str2[i]]
        else:
            store[str2[i]] = 1

    return len(store) == 0

# This algorithm will have O(N) time complexity and O(N) space complexity (create dict)
print(is_anagram_dict("iceman", "cinema"))
print(is_anagram_dict("icemaa", "cinema"))