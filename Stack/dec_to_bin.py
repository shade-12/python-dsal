from stack import Stack

'''
Convert decimal integer to binary
'''

def dec_to_bin(dec_num):
    if dec_num == 0:
        return 0
        
    s = Stack()
    num = dec_num

    while num > 0:
        s.push(num % 2)
        num = num // 2

    bin = ''
    while not s.is_empty():
        bin += str(s.pop())

    return bin

print(dec_to_bin(8))