def look_say_sequence(s):
    """
    Return look and say sequence of a string.
    Eg. s = 1112 will return 3112 (Three 1, one 2)
    """
    result = ""
    i = 0
    while i < len(s):
        count = 1
        while i + 1 < len(s) and s[i] == s[i + 1]:
            i += 1
            count += 1
        result += str(count) + s[i]
        i += 1
    return result


s = "1"
print(s)
n = 4
for i in range(n-1):
    s = look_say_sequence(s)
    print(s)