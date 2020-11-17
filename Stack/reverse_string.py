from stack import Stack

'''
Reverse a string

Python built-in function:
input_str = 'hello'
reversed = input_str[::-1]
'''

def reverse_string(str):
    if str == '':
        return ''

    s = Stack()
    for c in str:
        s.push(c)

    reversed = ''
    while not s.is_empty():
        reversed += s.pop()
    
    return reversed