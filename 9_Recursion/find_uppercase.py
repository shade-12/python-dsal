def find_uppercase_iterative(sentence):
    """
    Return the first occurring uppercase letter in string
    """
    for i in range(len(sentence)):
        if sentence[i].isupper():
            return sentence[i]
    return None


def find_uppercase_recursive(sentence, i=0):
    """
    Return the first occurring uppercase letter in string
    """
    if i >= len(sentence):
        return None
    if sentence[i].isupper():
        return sentence[i]
    return find_uppercase_recursive(sentence, i + 1)
