consonants = "bcdfghjklmnpqrstvwxyz"

def count_consonants_iterative(input):
    """
    Returns the number of consonants present
    """
    count = 0
    for char in input:
        if char.lower() in consonants:
            count += 1
    return count


def count_consonants_recursive(input):
    """
    Returns the number of consonants present
    """
    if len(input) == 0:
        return 0
    if input[0].lower() in consonants:
        return 1 + count_consonants_recursive(input[1:])
    else:
        return count_consonants_recursive(input[1:])

input_str = "abc de"
print(input_str)
print(count_consonants_iterative(input_str))
input_str = "LuCiDPrograMMiNG"
print(input_str)
print(count_consonants_recursive(input_str))