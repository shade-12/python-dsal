def is_all_unique(s):
    """
    Determine if a string contains only unique characters.
    """
    lowercase_s = s.lower()
    store = dict()
    for c in lowercase_s:
        if c in store:
            return False
        else:
            store[c] = 1
    return True