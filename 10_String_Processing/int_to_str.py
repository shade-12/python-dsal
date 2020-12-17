def int_to_str(num):
    """
    Convert an integer to a string without using python built-in str() function.
    """
    result = ""
    stack = []

    # Check negative sign
    if num < 0:
        result += "-"
        num *= -1   # convert num to positive integer

    while num > 0:
        remainder = num % 10
        stack.append(chr(ord('0') + remainder))
        num //= 10

    while len(stack) > 0:
        result += stack.pop()

    return result

input_int = 123
print(input_int)
print(type(input_int))

output_str = int_to_str(input_int)
print(output_str)
print(type(output_str))
    
