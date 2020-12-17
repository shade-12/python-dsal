from stack import Stack

def is_paren_balanced(str):
    other_paren = {
        ")": "(",
        "}": "{",
        "]": "["
    }

    paren_stack = Stack()

    for c in str:
        if c in other_paren.values():
            paren_stack.push(c)
        else:
            if paren_stack.is_empty():
                return False
            else:
                other_half = paren_stack.pop()
                if other_half != other_paren[c]:
                    return False

    if not paren_stack.is_empty():
        return False

    return True

print("String : (((({})))) Balanced or not?")
print(is_paren_balanced("(((({}))))"))

print("String : [][]]] Balanced or not?")
print(is_paren_balanced("[][]]]"))

print("String : [][] Balanced or not?")
print(is_paren_balanced("[][]"))
