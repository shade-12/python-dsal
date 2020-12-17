def is_palindrome(s):
    """
    Check if a string is a palindrome.
    """
    i, end = 0, len(s) // 2
    while i < end:
        if s[i] != s[len(s) - i - 1]:
            return False
        i += 1
    return True

print(is_palindrome('live on time emit no evil'))