def str_to_int(s):
    """
    Convert a string to an integer without using python built-in int() function.
    """
    # Check negative
    if s[0] == "-":
        is_negative = True
        s = s[1:]
    else:
        is_negative = False

    res = 0

    for c in s:
        num = ord(c) - ord('0')
        res = res * 10 + num

    if is_negative:
        return -1 * res
    return res


s = "554"
x = str_to_int(s)
print(type(x))

s = "123"
print(str_to_int(s))

s = "-123"
print(str_to_int(s))
