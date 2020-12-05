from stack import Stack

def reverse_string(str):
    str_stack = Stack()

    for c in str:
        str_stack.push(c)

    res = ""
    while not str_stack.is_empty():
        res += str_stack.pop()

    return res

input_str = "!dlroW olleH"
print(reverse_string(input_str))