from stack import Stack

'''
Example of Balanced Brackets:
{}, {}{}, (({[]}))

Example of Unbalanced Brackets:
((), {{{)}}], [][]]
'''

parentheses_dict = {
    ")": "(",
    "]": "[",
    "}": "{",
    ">": "<"
}

def is_parentheses_balanced(parentheses):
    if parentheses == []:
        return True
    
    s = Stack()
    index = 0
    
    while index < len(parentheses):
        prn = parentheses[index]
        if prn in parentheses_dict.values():
            s.push(prn)
        else:
            if s.is_empty():
                return False
            else:
                if s.pop() is not parentheses_dict[prn]:
                    return False
        index += 1

    return s.is_empty()



print("String : (((({})))) Balanced or not?")
print(is_parentheses_balanced("(((({}))))"))

print("String : [][]]] Balanced or not?")
print(is_parentheses_balanced("[][]]]"))

print("String : [][] Balanced or not?")
print(is_parentheses_balanced("[][]"))
